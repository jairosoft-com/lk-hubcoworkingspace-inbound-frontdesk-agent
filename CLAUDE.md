# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a LiveKit Python agent for Hub Coworking Hawaii's front desk operations. The agent acts as a voice-based AI assistant that embodies the spirit of Hawaiian hospitality while helping members, guests, and prospective clients with coworking space inquiries.

### Project Type
- **Framework**: LiveKit agents framework with Python
- **Purpose**: Voice-based front desk assistant for Hub Coworking Hawaii
- **Key Features**: Natural speech patterns, Hawaiian localization, comprehensive knowledge base

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

# Run tests
pytest test_agent.py -v
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

# Docker operations
task docker-build
task docker-push
task docker-run-with-env
```

## Architecture

### Core Components

1. **FunctionAgent** (agent.py): Main agent class that:
   - Loads prompts from `prompts/hub_front_desk_prompt.md` with fallback to `function_agent.txt`
   - Configures STT (Deepgram), LLM (OpenAI GPT-4o), TTS (OpenAI), and VAD (Silero)
   - Implements the `print_to_console` function tool
   - Handles voice interactions with TTS speed and voice customization

2. **Prompt System** (utils.py): 
   - `load_prompt()`: Loads text prompts from the prompts directory
   - `load_markdown_prompt()`: Loads markdown prompts (currently identical to load_prompt)

3. **Hub Front Desk Prompt** (prompts/hub_front_desk_prompt.md):
   - Comprehensive persona definition with Hawaiian hospitality
   - Knowledge base covering locations, services, pricing, policies
   - Natural speech patterns and conversation guidelines
   - **CRITICAL**: Aloha greeting only used ONCE per conversation session

## Environment Configuration

Required environment variables (.env file):
- `LIVEKIT_URL`: LiveKit server URL
- `LIVEKIT_API_KEY`: LiveKit API key
- `LIVEKIT_API_SECRET`: LiveKit API secret
- `OPENAI_API_KEY`: OpenAI API key (required for LLM and TTS)
- `DEEPGRAM_API_KEY`: Deepgram API key (required for STT)

Optional TTS configuration:
- `TTS_SPEED`: Text-to-speech speed (0.25-4.0, default: 1.05)
- `TTS_VOICE`: Voice selection (alloy, echo, fable, nova, onyx, shimmer; default: nova)

## Testing

The project includes comprehensive unit tests (test_agent.py):
- Tests for prompt loading functionality
- Agent initialization tests
- Prompt content validation
- Mock-based testing for LiveKit components

Run tests with: `pytest test_agent.py -v`

## Critical Implementation Details

### Voice Communication Patterns
- Agent uses natural speech fillers ("um", "so", "well") sparingly
- Includes micro-pauses and thinking sounds for human-like rhythm
- TTS speed set to 1.05x for natural conversational flow
- Voice optimized for friendly service tone (nova)

### Hawaiian Localization Rules
1. **Aloha Usage**: ONLY used for the very first interaction in a conversation
2. **Follow-up Responses**: Start with "Oh, sure!", "Great question!", etc. - NEVER repeat Aloha
3. **Natural Integration**: Hawaiian phrases (mahalo, ohana, pau hana) used naturally throughout
4. **Cultural Sensitivity**: Terms used respectfully and explained when needed

### Prompt Loading Hierarchy
1. Primary: `hub_front_desk_prompt.md` (production prompt)
2. Fallback: `function_agent.txt` (basic functionality)
3. Error handling with logging for debugging

## Task Management

The project uses Task Master AI for task tracking. Tasks are stored in `.taskmaster/tasks/tasks.json` and include:
- Feature branch creation and management
- Prompt development and testing
- Code implementation with TDD approach
- Pull request workflow

## Docker Deployment

The project includes Docker support with:
- Azure Container Registry integration
- Platform-specific builds (linux/amd64)
- Environment variable support via .env.local
- Taskfile commands for build/push/run operations