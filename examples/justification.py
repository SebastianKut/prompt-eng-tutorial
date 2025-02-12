from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv('OPEN_API_KEY'))

system_message = """
You are an AI assistant specialized in solving riddles.
Given a riddle, solve it the best you can.
Provide a clear justification of your answer and the reasoning behind it.
Riddle:
"""
riddle = """
How many r's is in the word strawberry?
"""
response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": riddle}
    ]
)
print(response.choices[0].message.content)