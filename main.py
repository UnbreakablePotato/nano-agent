from dotenv import load_dotenv
import os
from google import genai
from google.genai import types
import argparse

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")

if api_key == None:
    raise Exception("api key is empty")

client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

res = client.models.generate_content(model="gemini-2.5-flash", contents=messages)

usage = res.usage_metadata

if usage is not None and args.verbose:
    print(f"User prompt: {messages}")
    print(f"Prompt tokens: {usage.prompt_token_count}")
    print(f"Response tokens: {usage.candidates_token_count}")


if usage is None:
    raise RuntimeError("Prompt seems to have failed")

print(res.text)
