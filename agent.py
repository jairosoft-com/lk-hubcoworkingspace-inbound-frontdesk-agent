## This is a basic example of how to use function calling.
## To test the function, you can ask the agent to print to the console!

import logging
from dotenv import load_dotenv
from livekit.agents import JobContext, WorkerOptions, cli
from livekit.agents.llm import function_tool
from livekit.agents.voice import Agent, AgentSession, RunContext
from livekit.plugins import deepgram, openai, silero

from utils import load_markdown_prompt

logger = logging.getLogger("function-calling")
logger.setLevel(logging.INFO)

load_dotenv()


class FunctionAgent(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions=load_markdown_prompt("HubCoworkingHi-FrontDesk-Training-Guide.md"),
            stt=deepgram.STT(),
            llm=openai.LLM(model="gpt-4o"),
            tts=openai.TTS(),
            vad=silero.VAD.load(),
        )

    @function_tool
    async def print_to_console(self, context: RunContext):
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
