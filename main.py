import logging
import os

import openai
from dotenv import load_dotenv

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Create a client with your API key
client = openai.OpenAI(api_key=OPENAI_API_KEY)

# Make a chat completion request
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What’s the weather like on Mars?"},
    ],
)

# # Print the result
# print(response.choices[0].message.content)
