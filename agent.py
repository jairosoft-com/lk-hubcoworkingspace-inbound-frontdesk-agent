## This is a basic example of how to use function calling.
## To test the function, you can ask the agent to print to the console!

import logging
import os
from dotenv import load_dotenv
from livekit.agents import JobContext, WorkerOptions, cli
from livekit.agents.llm import function_tool
from livekit.agents.voice import Agent, AgentSession, RunContext
from livekit.plugins import deepgram, openai, silero

from utils import load_prompt

logger = logging.getLogger("function-calling")
logger.setLevel(logging.INFO)

load_dotenv()


class FunctionAgent(Agent):
    def __init__(self) -> None:
        # Load the new Hub Front Desk prompt
        try:
            prompt_content = load_prompt("hub_front_desk_prompt.md")
            logger.info("Successfully loaded hub_front_desk_prompt.md")
        except FileNotFoundError:
            logger.warning("hub_front_desk_prompt.md not found, falling back to default prompt")
            prompt_content = load_prompt("function_agent.txt")
        except Exception as e:
            logger.error(f"Error loading prompt: {e}")
            prompt_content = "You are a helpful assistant communicating through voice."
        
        # Get TTS configuration from environment variables
        tts_speed = float(os.getenv("TTS_SPEED", "1.05"))  # Default to 5% faster for natural rhythm
        tts_voice = os.getenv("TTS_VOICE", "nova")  # Default to nova voice (friendly, warm)
        logger.info(f"TTS configuration - Speed: {tts_speed}, Voice: {tts_voice}")
        
        super().__init__(
            instructions=prompt_content,
            stt=deepgram.STT(),
            llm=openai.LLM(model="gpt-4o"),
            tts=openai.TTS(speed=tts_speed, voice=tts_voice),
            vad=silero.VAD.load(),
        )

    @function_tool
    async def print_to_console(self, _context: RunContext):
        print("Console Print Success!")
        return None, "I've printed to the console."

    async def on_enter(self):
        self.session.generate_reply()


async def entrypoint(ctx: JobContext):
    await ctx.connect()

    session = AgentSession()

    await session.start(agent=FunctionAgent(), room=ctx.room)


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
