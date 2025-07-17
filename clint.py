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
































