# Nano-Agent
**A lightweight, autonomous task runner powered by Google Gemini 2.5 flash**

Nano-Agent is a streamlined AI agent which allows LLM's to work on local tasks. BY leveraging the Gemini 2.5 Flash API, the agent can parse complex user inpu and maintain conversation state.

## Key Features
**Stateful Reasoning** 

Utilizes Gemini's long-context window to maintain multi turn logic and goal tracking.

**Modular Tool Use** 

User interface for adding custom skills.

## Tech Stack
**LLM** 

Gemini 2.5 Flash API

**Language** 

Python 3.13+

## How It Works
**Input:** 

The user provides input through the terminal.


**Reasoning:** 

Gemini will determine if it needs more information, or it will solve the task at hand using it's available toolset.

**Action:** 

The agent executes the Python functions mapped to the models tool calls.

**Observation:**

 The rsults are fed back into Gemini to finalize or iterate a response.
