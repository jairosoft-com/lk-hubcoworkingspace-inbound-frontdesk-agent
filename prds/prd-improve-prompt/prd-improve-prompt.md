# PRD: Enhance AI Agent with HubCoWorking HI Persona & Knowledge

## 1. Introduction/Overview

This document outlines the requirements to significantly enhance the Voice AI agent's capabilities. The primary goal is to transform the agent from a generic assistant into a specialized, human-like Front Desk Host for Hub Coworking Hawaii. This will be achieved by creating a new, comprehensive prompt based on the official training manual, defining a specific persona, and ensuring the agent can accurately answer user questions based on this knowledge.

## 2. Goals
- To create a more natural, conversational, and human-like interaction for users.
- To train the AI agent on the specific operational procedures, services, and culture of Hub Coworking Hawaii.
- To improve the agent's ability to accurately and helpfully answer common customer questions.
- To establish a clear development and testing workflow for this and future enhancements.

## 3. User Stories
- **As a member/guest,** I want to interact with a friendly, professional AI agent that understands the unique aspects of Hub Coworking HI and can answer my questions as a human host would.
- **As a developer,** I want to create a detailed prompt that encapsulates the agent's persona and knowledge base, making it easy to update and manage the agent's core instructions.

## 4. Functional Requirements
1.  **Create a New Prompt File**: A new Markdown file named `hub_front_desk_prompt.md` shall be created in the `prompts/` directory.
2.  **Develop the Core Prompt**: The content of `hub_front_desk_prompt.md` will be a detailed set of instructions for the AI. This prompt must be derived exclusively from the provided training manual (`prompts/HubCoworkingHi-FrontDesk-Training-Guide.md`). It should distill the manual's content into actionable instructions that the AI can use to respond to queries.
3.  **Define the Agent's Persona**: The new prompt must explicitly define the agent's persona. The agent should be instructed to be:
    - **Conversational & Friendly**: Engaging and approachable.
    - **Professional**: Accurate and reliable.
    - **Casual**: Using a relaxed and natural tone.
    - **Localized**: Instructed to "talk like Hawaiian," incorporating common local phrases like "aloha" and "mahalo" where appropriate to create a sense of place.
4.  **Update Agent to Use New Prompt**: `agent.py` shall be modified to load and use the new `prompts/hub_front_desk_prompt.md` file for its instructions.

## 5. Non-Goals (Out of Scope)
- The agent will only be trained on the information present in the `HubCoworkingHi-FrontDesk-Training-Guide.md`. It will not be expected to answer questions beyond the scope of this document.
- No new agent *skills* (i.e., function tools) will be created in this iteration. The focus is solely on improving the quality of the conversational prompt.

## 6. Testing Strategy (TDD)
This project will adhere to a modified Test-Driven Development (TDD) protocol, as outlined in the `test-driven-development.mdc` rule, with the following user-specified constraints:
- **TDD for Code Only**: The TDD cycle (Red-Green-Refactor) will be applied *only* to modifications or additions to Python code (e.g., changes to `utils.py` or `agent.py`).
- **No Conversational Tests**: We will not write automated tests to validate the conversational quality or persona of the AI's responses. This will be verified through manual testing and review.
- **Code Coverage Target**: The goal for automated tests is to achieve approximately 50% code coverage for any new or modified Python modules.
- **No Edge Case Tests**: Tests should focus on the primary ("happy path") functionality of the code. We will not write tests for edge cases in this iteration.

## 7. Success Metrics
- The agent successfully loads and uses the new `hub_front_desk_prompt.md`.
- The agent can accurately answer a set of test questions derived from the training manual (e.g., "What are the staffed hours at the Kaka'ako location?", "Tell me about the Virtual Office service.").
- The agent's conversational flow is noticeably more natural and engaging.
- The agent's responses incorporate the specified "Hawaiian" persona and tone.

## 8. Development Workflow
The implementation will follow the branching and merging strategy defined in `branching-merging-strategy.mdc`:
1.  **Branching**: Create a new feature branch from `main` (e.g., `feature/improve-agent-prompt`).
2.  **Implementation**: Implement all functional requirements detailed in this PRD.
3.  **Committing**: Commit all changes to the feature branch.
4.  **Pushing**: Push the feature branch to the remote GitHub repository.
5.  **Pull Request**: Create a Pull Request (PR) from the feature branch to `main` and assign it to `raseniero` for review.

## 9. Open Questions
- None at this time. 