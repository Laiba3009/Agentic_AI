# LiteLLM README

## Overview
[LiteLLM](https://github.com/BerriAI/litellm) simplifies calling 100+ LLM APIs using an OpenAI-compatible interface.

## Example
The `examples/litellm_example.py` script uses LiteLLM to call an OpenRouter model (Google Gemini-Flash) to generate a programming joke.

## Prerequisites
- An [OpenRouter API key](https://openrouter.ai/keys).
- Install LiteLLM: `uv pip install litellm`.

## How to Run
1. Set your API key:
   ```bash
   export OPENROUTER_API_KEY=your_openrouter_key