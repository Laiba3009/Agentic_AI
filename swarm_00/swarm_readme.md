# Swarm README

## Overview
[OpenAI Swarm](https://github.com/openai/swarm) is an experimental, open-source framework for orchestrating multi-agent AI systems. It enables agents with specific roles and tools to collaborate via handoffs, ideal for educational purposes.[](https://github.com/openai/swarm)

## Example
The `examples/swarm_example.py` script demonstrates a multi-agent system with a triage agent that routes user requests to either a sales agent (for purchases) or a support agent (for issues). It uses the OpenAI API.

## Prerequisites
- An [OpenAI API key](https://platform.openai.com/api-keys).
- Install Swarm: `uv pip install swarm`.

## How to Run
1. Set your API key:
   ```bash
   export OPENAI_API_KEY=your_openai_key