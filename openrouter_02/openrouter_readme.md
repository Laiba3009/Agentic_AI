 # OpenRouter README

## Overview
[OpenRouter](https://openrouter.ai) provides a unified API to access various large language models (LLMs) like Google Gemini and Anthropic Claude.

## Example
The `examples/openrouter_example.py` script generates a haiku about the moon using the free Google Gemini-Flash model.

## Prerequisites
- An [OpenRouter API key](https://openrouter.ai/keys).
- Install `requests`: `uv pip install requests`.

## How to Run
1. Set your API key:
   ```bash
   export OPENROUTER_API_KEY=your_openrouter_key