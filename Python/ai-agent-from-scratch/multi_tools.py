import json
from llm import client, MODEL
from tools import get_sales_summary, get_sales_by, get_exchange_rate
from tool_schemas import TOOLS

# Allowlist: every tool the model may request, mapped to its function.
available_tools = {
    "get_sales_summary": get_sales_summary,
    "get_sales_by": get_sales_by,
    "get_exchange_rate": get_exchange_rate,
}

# Try each question and watch which tool(s) the LLM picks:
#   "What were our total sales and profit?"          -> get_sales_summary
#   "Which product made the most profit?"            -> get_sales_by(group_by="Product")
#   "What was our total profit in AED?"              -> two tools in one reply
#   "What is the capital of France?"                 -> no tool
question = "What was our total profit in AED?"

messages = [{"role": "user", "content": question}]

response = client.chat.completions.create(model=MODEL, messages=messages, tools=TOOLS)
msg = response.choices[0].message

if msg.tool_calls:
    messages.append(msg)

    # The LLM may request 1, 2 or more tools – run each one.
    for call in msg.tool_calls:
        args = json.loads(call.function.arguments or "{}")   # the LLM fills the arguments
        print("LLM requested:", call.function.name, args)

        result = available_tools[call.function.name](**args)
        messages.append({"role": "tool", "tool_call_id": call.id, "content": json.dumps(result)})

    final = client.chat.completions.create(model=MODEL, messages=messages)
    print("\nFinal answer:\n", final.choices[0].message.content)

else:
    print("No tool was needed:", msg.content)
