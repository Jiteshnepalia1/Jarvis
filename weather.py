import os
from groq import Groq

# Ensure your GROQ_API_KEY is set as an environment variable
client = Groq(
    api_key="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"
)
# client = Groq(api_key=os.environ.get("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"))

user_query = "What's the current weather in Ghaziabad"
# or: What were the main highlights from the latest Apple keynote event?
# Or: "What's the current weather in San Francisco?"
# Or: "Summarize the latest developments in fusion energy research this week."

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": user_query,
        }
    ],
    # The *only* change needed: Specify the compound model!
    model="compound-beta",
)

print(f"Query: {user_query}")
print(f"Compound Beta Response:\n{chat_completion.choices[0].message.content}")

# You might also inspect chat_completion.choices[0].message.executed_tools
# if you want to see if/which tool was used, though it's not necessary.