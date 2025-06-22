# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a LiveKit Python agents example project demonstrating function calling capabilities with real-time AI voice agents. The main agent (FunctionAgent) uses LiveKit's framework to create voice-based AI assistants with custom function tools.

## Key Commands

### Setup and Installation
```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Download required models (Silero VAD)
python agent.py download-files
```

### Development Commands
```bash
# Run the agent in development mode
python agent.py dev

# Format code with Black
black .
```

### Task Runner (Taskfile)
```bash
# Set up virtual environment
task venv-setup

# Run the agent
task agent-run

# Download models
task agent-download-models

# Clean virtual environment
task venv-clean
```

## Architecture

### Core Components

1. **FunctionAgent** (agent.py:17-37): Main agent class extending LiveKit's Agent base class
   - Configures STT (Deepgram), LLM (OpenAI GPT-4o), TTS (OpenAI), and VAD (Silero)
   - Implements custom function tools using the `@function_tool` decorator
   - Handles voice interactions and function execution

2. **Function Tools**: Custom functions that the agent can call during conversations
   - Example: `print_to_console` function demonstrates the pattern for adding new capabilities

3. **Entry Point** (agent.py:39-48): Connects to LiveKit room and starts agent session

## Environment Configuration

Required environment variables (.env file):
- `LIVEKIT_URL`: LiveKit server URL
- `LIVEKIT_API_KEY`: LiveKit API key
- `LIVEKIT_API_SECRET`: LiveKit API secret
- `OPENAI_API_KEY`: OpenAI API key (required for LLM and TTS)
- `DEEPGRAM_API_KEY`: Deepgram API key (required for STT)

## Dependencies

- `livekit-agents[openai,silero,deepgram]~=1.0`: LiveKit agents framework with plugins
- `python-dotenv`: Environment variable management
- `black`: Code formatter

## Development Notes

- The agent uses async/await patterns throughout
- Function tools should be defined as async methods with the `@function_tool` decorator
- The agent automatically generates an initial reply when a participant joins (`on_enter` method)
- All voice processing (STT/TTS/VAD) is handled by the LiveKit framework