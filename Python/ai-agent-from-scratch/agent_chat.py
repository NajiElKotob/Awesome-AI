from agent import run_agent

# Instructions: who the agent is and the rules it must follow.
SYSTEM_PROMPT = """You are a sales analyst for our company.
- Use the tools for every number. Never guess figures.
- Show amounts in USD unless the user asks for another currency.
- Keep answers short: 2 to 4 sentences."""

# State: this list IS the agent's memory. We create it once and keep it.
messages = [{"role": "system", "content": SYSTEM_PROMPT}]

print("Ask about our sales. Type 'exit' to quit.")

while True:
    question = input("\nYou: ").strip()
    if question.lower() in ("exit", "quit"):
        break
    if not question:
        continue

    messages.append({"role": "user", "content": question})
    answer = run_agent(messages)          # same loop as agent.py
    print("Agent:", answer)
