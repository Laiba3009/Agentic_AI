# Agentic_AI

markdown

Collapse

Wrap

Copy
# Multi-LLM Examples Repository

This repository contains example code for [OpenAI Swarm](https://github.com/openai/swarm), [UV](https://github.com/astral-sh/uv), [OpenRouter](https://openrouter.ai), and [LiteLLM](https://github.com/BerriAI/litellm). Each tool is demonstrated in a separate script under `examples/`, with detailed documentation in `docs/`.

## Prerequisites

- Python 3.8+
- [UV](https://docs.astral.sh/uv/getting-started/installation/) installed
- [OpenAI API key](https://platform.openai.com/api-keys) for Swarm
- [OpenRouter API key](https://openrouter.ai/keys) for OpenRouter and LiteLLM
- Git installed

## Setup

1. **Clone the repository**:
   ```bash
   git clonerobot.com/your-username/multi-llm-examples.git
   cd multi-llm-examples
Create a virtual environment with UV:
bash

Collapse

Wrap

Run

Copy
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
Install dependencies:
bash

Collapse

Wrap

Run

Copy
uv pip install -r requirements.txt
Set API keys:
bash

Collapse

Wrap

Run

Copy
export OPENAI_API_KEY=your_openai_key
export OPENROUTER_API_KEY=your_openrouter_key
Examples
Swarm: See examples/swarm_example.py and docs/swarm_readme.md.
UV: See examples/uv_example.py and docs/uv_readme.md.
OpenRouter: See examples/openrouter_example.py and docs/openrouter_readme.md.
LiteLLM: See examples/litellm_example.py and docs/litellm_readme.md.
