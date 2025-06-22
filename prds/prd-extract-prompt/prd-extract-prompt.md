# PRD: Externalize Agent Prompt

## 1. Introduction/Overview

This document outlines the requirements for refactoring the `agent.py` file to extract the hardcoded agent `instructions` prompt into an external file. This change will improve maintainability and allow for easier updates to the agent's instructions without modifying the core Python code. The implementation will follow the pattern observed in the provided `medical_office_triage` reference project, adapted for a simpler, single-prompt scenario.

## 2. Goals

- To make the agent's instructions easily editable by non-developers.
- To improve the project's structure by separating configuration (prompts) from logic (code).
- To create a reusable utility for loading prompts.

## 3. User Stories

- **As a developer,** I want to edit the agent's instructions in a simple text file, so I can iterate on prompt engineering more efficiently.
- **As a developer,** I want prompts to be organized in a dedicated directory, so the project structure is clean and easy to navigate.

## 4. Functional Requirements

1.  A new directory named `prompts` shall be created in the root of the project.
2.  A new file named `function_agent.txt` shall be created inside the `prompts` directory.
3.  The multi-line string currently assigned to the `instructions` parameter in `agent.py` shall be moved into the `prompts/function_agent.txt` file.
4.  A new Python file named `utils.py` shall be created in the root of the project.
5.  `utils.py` shall contain a function `load_prompt(name: str) -> str`.
6.  The `load_prompt` function will take a filename as input, construct the full path to the file within the `prompts` directory, read the file's content, and return it as a string.
7.  `agent.py` shall be updated to import the `load_prompt` function from `utils.py`.
8.  The `FunctionAgent` class in `agent.py` shall be modified to use `load_prompt('function_agent.txt')` to set its `instructions`.

## 5. Non-Goals (Out of Scope)

- No error handling for a missing or empty prompt file will be implemented in this iteration.
- Only the main `instructions` prompt for `FunctionAgent` will be extracted. Other hardcoded strings will remain.
- The prompt file will be a simple `.txt` file. Structured formats like YAML or JSON are not required for this task.

## 6. Design Considerations

The project structure will be updated to include:
```
.
├── agent.py
├── utils.py
├── prompts/
│   └── function_agent.txt
└── ... (rest of the files)
```

## 7. Technical Considerations

- The implementation will use standard Python libraries for file I/O (`pathlib` or `os.path`).
- No new external dependencies are required.

## 8. Success Metrics

- The `instructions` parameter for the `FunctionAgent` in `agent.py` is no longer a hardcoded multi-line string.
- The agent successfully loads its instructions from `prompts/function_agent.txt` at runtime.
- The application runs without any change in behavior from the user's perspective.

## 9. Open Questions

- None at this time.

## 10. Development Workflow
1.  **Branching**: Create a new feature branch from the `main` branch (e.g., `feature/extract-prompt`).
2.  **Implementation**: Implement all functional requirements as detailed in this document.
3.  **Committing**: Commit all changes to the feature branch with clear and descriptive messages.
4.  **Pushing**: Push the feature branch to the remote GitHub repository.
5.  **Pull Request**: Create a Pull Request (PR) from the feature branch to the `main` branch.
6.  **Review**: Assign the PR to the user `raseniero` for review and approval.
7.  **Merging**: Once the PR is approved, it can be merged into the `main` branch.

## 11. Open Questions

- None at this time.