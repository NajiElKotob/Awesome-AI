# The tool "menu" we show the model: name, description and parameters.
# The model never sees our Python code – only these descriptions.

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_sales_summary",
            "description": "Get total revenue, cost, profit and profit margin for all sales.",
            "parameters": {"type": "object", "properties": {}, "additionalProperties": False},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_sales_by",
            "description": "Get revenue and profit per Region, Product or Category, "
                           "sorted from most to least profitable. Can be limited to one region.",
            "parameters": {
                "type": "object",
                "properties": {
                    "group_by": {"type": "string", "enum": ["Region", "Product", "Category"]},
                    "region": {"type": "string", "description": "Optional, e.g. North, South, West"},
                },
                "required": ["group_by"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_exchange_rate",
            "description": "Get the exchange rate of a currency against the US dollar.",
            "parameters": {
                "type": "object",
                "properties": {
                    "currency": {"type": "string", "description": "Currency code, e.g. EUR, AED"},
                },
                "required": ["currency"],
            },
        },
    },
]
