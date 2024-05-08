from langchain_community.llms import Ollama
from crewai import Agent, Task, Crew, Process

# Load the Ollama model
model = Ollama(model="llama3")

# Define the question or prompt
question = "Client asking real-estate related questions"

# Create an Agent with a specific role, goal, and backstory
agent = Agent(
    role="client service agent",
    goal="Answering frequently asked questions, simple requests, and providing basic information",
    backstory="You are an AI assistant whose job is to help Clients and potential clients set up a meeting with St. Joseph to use him as your real estate agent to help you buy or sell your home.",
    llm=model
)

# Use the Agent to generate a response based on the question and the Ollama model
answer = agent.run(question)

# Print the generated answer
print(answer)
