# PRD: Refine Agent Conversational Flow

## 1. Introduction/Overview
This document outlines the requirements to refine the Voice AI agent's conversational abilities based on user feedback. The goal is to address two key issues: the overuse of the filler word "Oh!" and the noticeable pause while the agent formulates a response. This will be achieved by further enhancing the agent's core prompt to encourage more varied language and to mask processing latency with initial thinking phrases.

## 2. Goals
- To make the agent's responses sound more natural and less repetitive.
- To reduce the user's perception of "think time" by filling the silence at the beginning of a response.
- To create a backup of the current prompt before making changes, ensuring a safe rollback point.

## 3. User Stories
- **As a user,** I want the AI agent to use a variety of filler words so that its speech sounds more natural and less robotic.
- **As a user,** I want the AI agent to respond more immediately, without a long initial pause, to make the conversation feel more fluid and interactive.

## 4. Functional Requirements
1.  **Backup Existing Prompt**: Before any modifications, the current prompt file, `prompts/hub_front_desk_prompt.md`, shall be copied to `prompts/hub_front_desk_prompt.bak.md`.
2.  **De-emphasize "Oh!"**: The `hub_front_desk_prompt.md` file will be edited. The section on `Natural Speech Patterns` and the `Example Conversations` will be revised to reduce the prominence of "Oh!" and encourage a wider variety of conversational connectors (e.g., "Alright," "Okay, so," "Gotcha," "Sure thing").
3.  **Implement Latency Masking (Strategy A)**: A new, high-priority instruction will be added to the `Response Guidelines`. This instruction will direct the agent to *immediately* begin its response with a thinking filler phrase (e.g., "Umm, let me see...", "Well...", "Okay, so...") as soon as it starts processing. This "filler-first" approach is intended to cover the model's think time.
4.  **Update Examples**: The example conversations within the prompt will be updated to reflect this new "filler-first" response pattern and the de-emphasis of "Oh!".

## 5. Non-Goals (Out of Scope)
- This iteration will not involve any code changes. The solution will be implemented entirely through prompt engineering.
- **Strategy B (Technical Filler Audio)** is considered a potential future enhancement and is out of scope for this task.

## 6. Testing Strategy (TDD)
- As this project involves **no Python code changes**, the TDD protocol is not applicable.
- Verification will be performed through manual, conversational testing to assess the agent's improved natural language flow and reduced perceived latency.

## 7. Success Metrics
- The agent no longer uses "Oh!" as its primary conversational connector. Its use of filler words is more varied and natural.
- The perceived pause between the user finishing their sentence and the agent starting its response is significantly reduced.
- The overall conversational flow feels smoother and more human-like.

## 8. Development Workflow
The implementation will follow the branching and merging strategy defined in `branching-merging-strategy.mdc`:
1.  **Branching**: Create a new feature branch from `main` (e.g., `feature/refine-conversational-flow`).
2.  **Implementation**: Implement all functional requirements detailed in this PRD.
3.  **Committing**: Commit all changes to the feature branch.
4.  **Pushing**: Push the feature branch to the remote GitHub repository.
5.  **Pull Request**: Create a Pull Request (PR) from the feature branch to `main` and assign it to `raseniero` for review.

## 9. Open Questions
- None at this time. 