import json
from llm import client, MODEL
from tools import get_sales_summary, get_sales_by, get_exchange_rate
from tool_schemas import TOOLS

available_tools = {
    "get_sales_summary": get_sales_summary,
    "get_sales_by": get_sales_by,
    "get_exchange_rate": get_exchange_rate,
}

MAX_STEPS = 5   # safety limit: never loop forever


def run_agent(messages):
    """The agent loop: ask -> run tools -> return results -> ask again."""
    for step in range(1, MAX_STEPS + 1):

        # 1. Ask the LLM, always with the tools available.
        response = client.chat.completions.create(model=MODEL, messages=messages, tools=TOOLS)
        msg = response.choices[0].message
        messages.append(msg)

        # 2. No tool requested -> this is the final answer. Stop.
        if not msg.tool_calls:
            return msg.content

        # 3. Run every requested tool and add its result to the conversation.
        for call in msg.tool_calls:
            args = json.loads(call.function.arguments or "{}")
            print(f"Step {step}: {call.function.name} {args}")

            result = available_tools[call.function.name](**args)
            messages.append({"role": "tool", "tool_call_id": call.id, "content": json.dumps(result)})

        # 4. Loop back: the LLM now sees the results and decides what is next.

    return "Stopped: too many steps without a final answer."


if __name__ == "__main__":
    question = ("Which region made the most profit, and which product "
                "earned the most profit in that region?")
    messages = [{"role": "user", "content": question}]
    print("\nAnswer:", run_agent(messages))
