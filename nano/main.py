from dotenv import load_dotenv
import os
from google import genai
from google.genai import types
import argparse
from nano.system_prompts import system_prompt
from nano.call_function import available_functions, call_function
from openai import OpenAI
import sys

def parse():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    return args

def generate_content(args):
    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key == None:
        raise Exception("api key is empty")

    client = genai.Client(api_key=api_key)
    #parser logik var her
    messages = [types.Content(role="user", parts=[types.Part(text=args)])]
    for i in range(10):
        res = client.models.generate_content(
            model="gemini-2.5-pro",
            contents=messages,
            config=types.GenerateContentConfig(tools=[available_functions],system_instruction=system_prompt))

        if res.candidates is not None:
            for candidate in res.candidates:
                messages.append(candidate.content)

        usage = res.usage_metadata

        #if usage is not None and args.verbose:
         #   print(f"Prompt tokens: {usage.prompt_token_count}")
          #  print(f"Response tokens: {usage.candidates_token_count}")


        if usage is None:
            raise RuntimeError("Prompt seems to have failed")

        if res.function_calls is None:
            print(res.text)
            return

        function_respones = []
        for func in res.function_calls:
            tool_res = call_function(func)
            if(
                not tool_res.parts
                or not tool_res.parts[0].function_response
                or not tool_res.parts[0].function_response.response
            ):
                raise RuntimeError(f"Empty function response for {func.name}")
            #if args.verbose:
             #   print(f"-> {tool_res.parts[0].function_response.response}")

            function_respones.append(tool_res.parts[0])
        messages.append(types.Content(role="user", parts=function_respones))
    print("Model did not finish a response")
    #return sys.exit(1)
