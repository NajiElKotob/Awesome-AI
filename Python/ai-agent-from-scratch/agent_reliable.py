import json
import inspect
from llm import client, MODEL
from tools import get_sales_summary, get_sales_by, get_exchange_rate
from tool_schemas import TOOLS

available_tools = {
    "get_sales_summary": get_sales_summary,
    "get_sales_by": get_sales_by,
    "get_exchange_rate": get_exchange_rate,
}

MAX_STEPS = 5

SYSTEM_PROMPT = """You are a sales analyst for our company.
- Use the tools for every number. Never guess figures.
- The data covers January to March 2026 only.
- If a question is unclear (which period, region or metric?), ask ONE short
  clarifying question instead of guessing.
- If a tool returns an error, explain it simply and suggest what to try.
- Keep answers short: 2 to 4 sentences."""


def execute_tool(call):
    """Safe dispatcher: the agent must never crash because of the LLM."""
    name = call.function.name

    # 1. Only run tools we approved.
    if name not in available_tools:
        return {"error": f"Unknown tool '{name}'."}
    func = available_tools[name]

    # 2. Arguments must be valid JSON.
    try:
        args = json.loads(call.function.arguments or "{}")
    except json.JSONDecodeError:
        return {"error": "The tool arguments were not valid JSON."}

    # 3. Keep only the arguments the function really accepts.
    allowed = inspect.signature(func).parameters
    args = {k: v for k, v in args.items() if k in allowed}

    # 4. A failing tool returns an error to the LLM instead of crashing.
    try:
        return func(**args)
    except Exception as e:
        return {"error": f"{type(e).__name__}: {e}"}


def run_agent(messages):
    for step in range(1, MAX_STEPS + 1):
        response = client.chat.completions.create(model=MODEL, messages=messages, tools=TOOLS)
        msg = response.choices[0].message
        messages.append(msg)

        if not msg.tool_calls:
            return msg.content

        for call in msg.tool_calls:
            result = execute_tool(call)
            print(f"  [step {step}] {call.function.name} -> {result}")
            messages.append({"role": "tool", "tool_call_id": call.id, "content": json.dumps(result)})

    # 5. Execution limit reached: stop and say so honestly.
    return "I could not finish within the step limit. Please rephrase or narrow the question."


if __name__ == "__main__":
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    print("Ask about our sales. Type 'exit' to quit.")

    while True:
        question = input("\nYou: ").strip()
        if question.lower() in ("exit", "quit"):
            break
        if not question:
            continue

        messages.append({"role": "user", "content": question})
        print("Agent:", run_agent(messages))
