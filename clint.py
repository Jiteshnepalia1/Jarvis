import os

from groq import Groq

client = Groq(
    api_key="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"
)
# client = Groq(
#     api_key=os.environ.get("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"),
# )

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role":"system",
            "content": "You are a virtual assistent named jarvis skilled in general task like Alexa and Google Cloud",
        },
        {"role":"user","content":"what is coding"}
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)
































# from openai import OpenAI
# client = OpenAI(
#     api_key="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"

# )

# completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a virtual assistant name jarvis skilled in general tasks like Alexa and Google Cloude"},
#         {"role": "user", "content": "what is coding"}
#     ]
# )

# # Print the response
# print(completion.choices[0].message.content)



# response = client.responses.create(
#     model="gpt-4.1",
#     input="Write a one-sentence bedtime story about a unicorn."
# )

# print(response.output_text)