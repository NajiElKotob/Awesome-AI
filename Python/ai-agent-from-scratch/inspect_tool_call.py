from llm import client, MODEL

# Stage 3: the LLM's half only. We describe the tool and look at what the LLM asks for.
# Nothing is executed here – that is stage 4 (run_tool_call.py).

# 1. Describe the tool (the LLM never sees our Python code, only this).
tools = [{
    "type": "function",
    "function": {
        "name": "get_sales_summary",
        "description": "Get total revenue, cost, profit and profit margin from the sales data.",
        "parameters": {"type": "object", "properties": {}, "additionalProperties": False},
    },
}]

messages = [{"role": "user", "content": "What were our total sales and profit?"}]

# 2. Ask the LLM – it decides whether to request the tool.
response = client.chat.completions.create(model=MODEL, messages=messages, tools=tools)
msg = response.choices[0].message

# 3. Inspect the decision.
if msg.tool_calls:
    call = msg.tool_calls[0]
    print("LLM requested:", call.function.name)
    print("Arguments:    ", call.function.arguments)
    print("Request id:   ", call.id)
    print("\nNothing has been calculated yet. The LLM only asked.")
else:
    print("No tool was needed:", msg.content)
