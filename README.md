# Asana Workspace Simulation

A seed data generator for Reinforcement Learning (RL) environments, simulating a B2B SaaS company.

## Setup
1. `pip install -r requirements.txt`
2. Configure `.env` with your API keys.
3. Run `python src/main.py`

## Structure
- `src/generators`: Business logic for creating entities.
- `src/models`: Data structures for tasks and users.
- `prompts/`: Templates for LLM text generation.
