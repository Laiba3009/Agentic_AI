# main.py
from openai import OpenAI
import os

class Agent:
    def __init__(self, name, instructions, model="openai/gpt-3.5-turbo"):
        self.name = name
        self.instructions = instructions
        self.model = model
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY")
        )

    def process(self, messages):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.instructions},
                *messages
            ]
        )
        return response.choices[0].message.content

class Swarm:
    def run(self, agent, messages):
        return {"messages": [{"role": "assistant", "content": agent.process(messages)}]}

def swarm_example():
    client = Swarm()
    analyst_agent = Agent(
        name="Analyst",
        instructions="You are a data analyst. Analyze the given data and provide a concise summary.",
        model="openai/gpt-3.5-turbo"
    )
    response = client.run(
        agent=analyst_agent,
        messages=[{"role": "user", "content": "Analyze this dataset: Sales 2025 data shows 10% growth."}]
    )
    return response["messages"][-1]["content"]

if __name__ == "__main__":
    if not os.getenv("OPENROUTER_API_KEY"):
        print("Error: OPENROUTER_API_KEY environment variable set nahi hai!")
    else:
        print(swarm_example())