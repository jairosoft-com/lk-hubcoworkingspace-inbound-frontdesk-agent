import os


def load_prompt(name: str) -> str:
    """Load a prompt from the prompts directory"""
    file_path = os.path.join(os.path.dirname(__file__), "prompts", name)
    with open(file_path, "r") as f:
        return f.read()

def load_markdown_prompt(name: str) -> str:
    """Load a markdown prompt from the prompts directory"""
    file_path = os.path.join(os.path.dirname(__file__), "prompts", name)
    with open(file_path, "r") as f:
        return f.read()
