# AKYDev v1.0 Architecture

## Mission

AKYDev is an AI Development Automation Platform.

It should automate software development from planning to implementation while remaining provider-agnostic.

---

# Core Philosophy

AI decides WHAT to change.

AKYDev decides HOW to change it.

Never allow an AI model to directly edit project files.

---

# Workflow

Workspace

↓

Analyze

↓

Project Model

↓

Task

↓

Planner

↓

Context Engine

↓

AI Provider

↓

JSON Change Plan

↓

Patch Generator

↓

Patch Validator

↓

Patch Apply

↓

Test Runner

↓

Git Automation

---

# Components

## Scanner

Responsible for:

- project detection
- git detection
- language detection
- package detection

Output:

project.json

---

## Planner

Responsible for:

- reading project model
- reading tasks
- deciding implementation order

Output:

plan.json

---

## Context Engine

Responsible for:

- selecting relevant files
- selecting relevant functions
- dependency graph
- token budgeting

Output:

context.json

---

## AI Provider

Supports:

- Gemini
- OpenAI
- Claude
- Ollama
- DeepSeek

All providers implement one interface.

Output:

changes.json

---

## Change Engine

Converts AI response into structured changes.

Supported operations:

Create File

Modify File

Delete File

Rename File

Insert Function

Replace Function

Replace Class

Update Imports

---

## Patch Generator

Generates:

patch.diff

Only AKYDev creates patches.

Never AI.

---

## Patch Validator

Checks:

Patch syntax

Files exist

Imports

Python syntax

Formatting

---

## Apply Engine

Safe application.

Rollback.

Backups.

---

## Test Runner

Run:

pytest

ruff

black

mypy

custom scripts

---

## Git Engine

Stage

Commit

Branch

Push

PR

---

# Folder Structure

src/

cli/

workspace/

planner/

context/

providers/

changes/

patch/

editor/

testing/

git/

memory/

utils/

---

# Provider Interface

class Provider

↓

generate(context)

↓

changes.json

---

# JSON Schema

{
  "changes": []
}

Each change contains:

type

file

target

content

reason

---

# Design Rules

No provider edits files.

No provider generates patches.

Only AKYDev generates patches.

All patches validated.

Everything testable.

Everything modular.

---

# Future

Plugin system

Web dashboard

Multi-agent orchestration

Remote execution

IDE integration

VS Code extension

JetBrains plugin

GitHub App

Cloud execution