# LiveKit Python Agents Examples

This repository contains example implementations of LiveKit agents using Python. These examples demonstrate how to build real-time AI agents with various capabilities.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- LiveKit server URL and API keys
- OpenAI API key (for certain agents)

## Setup

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone <repository-url>
   cd python_agents_examples/basics
   ```

2. **Create and activate a virtual environment** (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   python context_variable_agent.py download-files
   ```

4. **Set up environment variables**:
   Create a `.env` file in the project root with the following variables:
   ```
   LIVEKIT_URL=your_livekit_server_url
   LIVEKIT_API_KEY=your_api_key
   LIVEKIT_API_SECRET=your_api_secret
   OPENAI_API_KEY=your_openai_api_key  # Required for certain agents
   DEEPGRAM_API_KEY=your_deepgram_api_key
   ```

## Available Examples

### Context Variable Agent
Run the context variable agent example:
```bash
python context_variable_agent.py dev
```

## Development

### Running Tests
```bash
# Add test commands here when tests are added
```

### Code Style
This project follows PEP 8 style guidelines. You can check your code style with:
```bash
black .
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## Support
For support, please open an issue in the repository or contact the LiveKit community.
