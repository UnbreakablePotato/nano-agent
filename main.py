from dotenv import load_dotenv
import os
from google import genai
from google.genai import types
import argparse
from system_prompts import system_prompt
from call_function import available_functions

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

res = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=messages,
    config=types.GenerateContentConfig(tools=[available_functions],system_instruction=system_prompt))

usage = res.usage_metadata

if usage is not None and args.verbose:
    print(f"User prompt: {messages}")
    print(f"Prompt tokens: {usage.prompt_token_count}")
    print(f"Response tokens: {usage.candidates_token_count}")


if usage is None:
    raise RuntimeError("Prompt seems to have failed")

if res.function_calls is None:
    print(res.text)

for func in res.function_calls:
    print(f"Calling function: {func.name}({func.args})")
