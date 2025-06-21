# import google.generativeai as genai

# genai.configure(api_key="AIzaSyBUFRn8YOvrtFfahaT0bOj4KOUJJrbzOQU")

# model = genai.GenerativeModel("gemini-1.5-pro")
# response = model.generate_content("Give a short overview of machine learning.")

# print(response.text)


from openai import OpenAI
client = OpenAI(api_key="sk-YourOpenAIKeyHere")

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Give a short overview of machine learning."}
    ]
)

print(completion.choices[0].message.content)

