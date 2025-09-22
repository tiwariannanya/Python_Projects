from openai import OpenAI

client = OpenAI(api_key="<Your key here>")

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Vira skilled in general tasks like Alexa and Google Cloud"},
        {"role": "user", "content": "What is AI"}
    ]
)

print(completion.choices[0].message.content)