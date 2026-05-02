import os
from openai import OpenAI
import argparse
from nano.system_prompts import system_prompt
from nano.call_function import available_functions, call_function
from openai import types

def setup_client():
    client = OpenAI(
        base_url="http://localhost:11434/v1/",
        api_key="none"        
    )

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("--model", action="store_true", help="Picks the local model")
    args = parser.parse_args()

    if args.verbose:
        print(f"User prompt: {args.user_prompt}\n")

    if args.model:
        pass

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

def generate_response(client, messages, verbose, local_model):
    res = client(
        model=local_model,
        input=messages,
        store=False
    )

    messages += [{"role": el.role, "content": el.content} for el in res.output]

