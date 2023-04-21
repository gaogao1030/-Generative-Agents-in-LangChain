from langchain.chat_models import ChatOpenAI
from generative_agent import GenerativeAgent
from create_generative_charactor import create_new_memory_retriever
from interview_agent import interview_agent
import os

os.environ["OPENAI_API_KEY"] = ""

LLM = ChatOpenAI(max_tokens=1500) # Can be any LLM you want.

tommie = GenerativeAgent(name="Tommie", 
              age=25,
              traits="anxious, likes design", # You can add more persistent traits here 
              status="looking for a job", # When connected to a virtual world, we can have the characters update their status
              memory_retriever=create_new_memory_retriever(),
              llm=LLM,
              daily_summaries = [
                   "Drove across state to move to a new town but doesn't have a job yet."
               ],
               reflection_threshold = 8, # we will give this a relatively low number to show how reflection works
             )

# We can give the character memories directly
tommie_memories = [
    "Tommie remembers his dog, Bruno, from when he was a kid",
    "Tommie feels tired from driving so far",
    "Tommie sees the new home",
    "The new neighbors have a cat",
    "The road is noisy at night",
    "Tommie is hungry",
    "Tommie tries to get some rest.",
]
for memory in tommie_memories:
    tommie.add_memory(memory)

print(tommie.get_summary(force_refresh=True))

print("=" * 30)

print("interview_agent(tommie, \"What do you like to do?\")")
print(interview_agent(tommie, "What do you like to do?"))

print("=" * 30)
