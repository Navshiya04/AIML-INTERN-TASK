
# AIML Internship Task

## Project Overview

This project contains two Python implementations:
1. CSS Parser
2. Simple Tool-Using AI Agent

## 1. CSS Parser

The CSS parser extracts selectors and their CSS properties and converts them into structured JSON output.

### Features
- Removes CSS comments.
- Extracts selectors and property-value pairs.
- Handles multiple selectors in one rule.
- Detects malformed CSS rules.

### Run
```bash
python css_parser.py
```

### Design Choices
Selectors and their properties are represented as dictionaries so that the output can be converted to JSON. Multiple selectors in one rule are handled separately. Comments are removed before parsing.

### Edge Case
CSS with an unmatched closing or opening brace is tested. The parser raises a ValueError for malformed input.

## 2. Tool-Using AI Agent

The agent uses two tools:
- Knowledge Base Search: retrieves answers from a predefined knowledge base.
- Calculator: evaluates simple arithmetic expressions.

### Features
- Selects a tool based on the question.
- Returns an honest fallback when information is unavailable.
- Uses restricted arithmetic parsing instead of eval().
- Checks repeatability using identical questions.

### Run
```bash
python agent.py
```

### Preventing Unsupported Answers
The agent only answers knowledge questions when a matching fact exists in its knowledge base. Otherwise, it responds that it does not have enough information.

### Repeatability
The same question is submitted twice and the results are compared. The repeatability check should return True because the tools use fixed data and deterministic logic.

## Requirements

- Python 3.10 or newer
- No external Python packages required

## Author

AIML Internship Candidate
