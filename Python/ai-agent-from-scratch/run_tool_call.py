import json
from llm import client, MODEL
from tools import get_sales_summary

# The tool description (same as inspect_tool_call.py).
tools = [{
    "type": "function",
    "function": {
        "name": "get_sales_summary",
        "description": "Get total revenue, cost, profit and profit margin from the sales data.",
        "parameters": {"type": "object", "properties": {}, "additionalProperties": False},
    },
}]

# The dispatcher's allowlist: tool name -> real Python function.
available_tools = {"get_sales_summary": get_sales_summary}

messages = [{"role": "user", "content": "What were our total sales and profit?"}]

# Step 1 – the LLM decides.
response = client.chat.completions.create(model=MODEL, messages=messages, tools=tools)
msg = response.choices[0].message

if msg.tool_calls:
    call = msg.tool_calls[0]
    print("1. LLM requested:", call.function.name)

    # Step 2 – Python executes (the LLM cannot run code).
    result = available_tools[call.function.name]()
    print("2. Python ran it:", result)

    # Step 3 – return the result to the LLM.
    messages.append(msg)                                    # the LLM's request
    messages.append({"role": "tool",                        # our answer to it
                     "tool_call_id": call.id,
                     "content": json.dumps(result)})

    # Step 4 – the LLM writes the final answer from real numbers.
    final = client.chat.completions.create(model=MODEL, messages=messages)
    print("3. Final answer:\n", final.choices[0].message.content)

    # What did we actually send the second time?
    print("\nConversation sent:", [m["role"] if isinstance(m, dict) else m.role for m in messages])

else:
    print("No tool was needed:", msg.content)
