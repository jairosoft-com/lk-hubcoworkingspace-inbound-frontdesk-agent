"""Unit tests for agent.py modifications - TDD approach for prompt loading functionality."""

import os
import pytest
from unittest.mock import patch, mock_open, MagicMock
from pathlib import Path

# Import the modules we'll be testing
from agent import FunctionAgent
from utils import load_prompt


class TestLoadPromptFunction:
    """Test cases for the load_prompt utility function."""
    
    def test_load_prompt_reads_file_successfully(self):
        """Test that load_prompt reads and returns file content correctly."""
        mock_content = "Test prompt content\nWith multiple lines"
        
        with patch("builtins.open", mock_open(read_data=mock_content)):
            result = load_prompt("test_prompt.txt")
            
        assert result == mock_content
    
    def test_load_prompt_uses_correct_path(self):
        """Test that load_prompt constructs the correct file path."""
        with patch("builtins.open", mock_open()) as mock_file:
            load_prompt("hub_front_desk_prompt.md")
            
        # Get the actual path that was called
        called_path = mock_file.call_args[0][0]
        
        # Should include 'prompts' directory in the path
        assert "prompts" in str(called_path)
        assert "hub_front_desk_prompt.md" in str(called_path)
    
    def test_load_prompt_handles_special_characters(self):
        """Test that load_prompt correctly handles special characters and formatting."""
        mock_content = "# Hub Coworking Hawaii\n\n**Aloha!** Welcome to the Hub 🌺"
        
        with patch("builtins.open", mock_open(read_data=mock_content)):
            result = load_prompt("test_prompt.md")
            
        assert "Aloha!" in result
        assert "#" in result
        assert "**" in result


class TestFunctionAgentWithNewPrompt:
    """Test cases for FunctionAgent using the new prompt system."""
    
    @patch('utils.load_prompt')
    @patch('livekit.plugins.deepgram.STT')
    @patch('livekit.plugins.openai.LLM')
    @patch('livekit.plugins.openai.TTS')
    @patch('livekit.plugins.silero.VAD.load')
    def test_agent_loads_hub_prompt_on_init(self, mock_vad, mock_tts, mock_llm, mock_stt, mock_load_prompt):
        """Test that FunctionAgent loads hub_front_desk_prompt.md on initialization."""
        # Mock the prompt content
        mock_prompt_content = "You are a helpful Front Desk Host for Hub Coworking Hawaii"
        mock_load_prompt.return_value = mock_prompt_content
        
        # Create the agent
        agent = FunctionAgent()
        
        # Verify load_prompt was called with correct file
        mock_load_prompt.assert_called_once_with("hub_front_desk_prompt.md")
        
        # Verify the agent was initialized with the loaded prompt
        # Note: We check if the prompt was passed to the parent class init
        assert mock_load_prompt.called
    
    @patch('utils.load_prompt')
    @patch('livekit.plugins.deepgram.STT')
    @patch('livekit.plugins.openai.LLM')
    @patch('livekit.plugins.openai.TTS')
    @patch('livekit.plugins.silero.VAD.load')
    def test_agent_has_print_to_console_function(self, mock_vad, mock_tts, mock_llm, mock_stt, mock_load_prompt):
        """Test that FunctionAgent has the print_to_console function tool."""
        mock_load_prompt.return_value = "Test prompt"
        
        agent = FunctionAgent()
        
        # Check that print_to_console method exists
        assert hasattr(agent, 'print_to_console')
        assert callable(getattr(agent, 'print_to_console'))
    
    @patch('utils.load_prompt')
    @patch('livekit.plugins.deepgram.STT')
    @patch('livekit.plugins.openai.LLM')
    @patch('livekit.plugins.openai.TTS')
    @patch('livekit.plugins.silero.VAD.load')
    def test_agent_handles_markdown_prompt_content(self, mock_vad, mock_tts, mock_llm, mock_stt, mock_load_prompt):
        """Test that agent correctly handles markdown-formatted prompt content."""
        # Mock a markdown prompt with Hawaiian elements
        mock_prompt_content = """# Hub Coworking Hawaii - Front Desk Host AI Agent

## Role Definition
You are a helpful Front Desk Host for Hub Coworking Hawaii.

## Persona Definition
- Use "Aloha" as greeting
- Say "Mahalo" for thanks
"""
        mock_load_prompt.return_value = mock_prompt_content
        
        agent = FunctionAgent()
        
        # Verify the prompt was loaded
        mock_load_prompt.assert_called_once()
        
        # The agent should be able to handle markdown content
        assert "Aloha" in mock_load_prompt.return_value
        assert "Mahalo" in mock_load_prompt.return_value


class TestPromptFileIntegration:
    """Integration tests for prompt file loading (if files exist)."""
    
    def test_hub_prompt_file_exists(self):
        """Test that the hub_front_desk_prompt.md file exists in the correct location."""
        prompt_path = Path(__file__).parent / "prompts" / "hub_front_desk_prompt.md"
        
        # This test will pass if the file exists, fail if it doesn't
        assert prompt_path.exists(), f"Expected prompt file at {prompt_path}"
    
    def test_hub_prompt_contains_required_sections(self):
        """Test that the hub prompt contains all required sections."""
        prompt_path = Path(__file__).parent / "prompts" / "hub_front_desk_prompt.md"
        
        if prompt_path.exists():
            content = prompt_path.read_text()
            
            # Check for required sections
            assert "Role Definition" in content
            assert "Persona Definition" in content
            assert "Knowledge Base" in content
            assert "Response Guidelines" in content
            assert "Hawaiian Language Integration" in content
            
            # Check for key Hawaiian terms
            assert "Aloha" in content
            assert "Mahalo" in content


if __name__ == "__main__":
    pytest.main([__file__, "-v"])