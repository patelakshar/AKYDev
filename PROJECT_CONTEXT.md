# AKYDev - Master Project Context

You are taking over development of an existing open-source project called AKYDev.

Your role is NOT to redesign the project.

Your role is to continue building it exactly from its current state.

Read this entire prompt before writing any code.

===========================================================
PROJECT NAME
===========================================================

AKYDev
(AI Development Automation Platform)

===========================================================
MISSION
===========================================================

Build an open-source AI Development Automation Platform that can act as an AI software engineer.

AKYDev should be able to:

• Analyze an existing codebase
• Understand project architecture
• Store a structured project model
• Create development tasks
• Generate execution plans
• Build high-quality prompts
• Communicate with multiple AI providers
• Generate code patches
• Review patches
• Apply patches safely
• Run tests
• Commit changes to Git

The platform should automate the software development workflow instead of simply generating code.

===========================================================
VISION
===========================================================

Current workflow for developers:

Developer
↓

Open ChatGPT

↓

Copy code

↓

Ask AI

↓

Copy response

↓

Paste

↓

Fix

↓

Repeat


Future workflow with AKYDev:

Developer

↓

akydev analyze .

↓

akydev task "Create login system"

↓

akydev plan

↓

akydev implement

↓

akydev review

↓

akydev apply

↓

akydev commit

↓

Done

===========================================================
IMPORTANT RULES
===========================================================

THESE RULES ARE ABSOLUTE.

1.

DO NOT redesign the architecture.

2.

DO NOT rename folders.

3.

DO NOT change file structure.

4.

DO NOT refactor unless explicitly requested.

5.

Every sprint must end with:

• Working feature
• Successful test
• Git commit
• Git push

6.

One sprint = one feature.

No feature creep.

7.

Never introduce breaking changes.

===========================================================
CURRENT ARCHITECTURE (LOCKED)
===========================================================

AKYDev/

docs/

examples/

sprints/

src/

akydev/

cli/

workspace/

planner/

providers/

editor/

runner/

git/

memory/

prompts/

utils/

tests/

README.md

pyproject.toml

===========================================================
CURRENT CLI
===========================================================

akydev analyze

akydev attach

akydev task

akydev plan

akydev review

akydev apply

akydev commit

===========================================================
CURRENT FEATURES
===========================================================

Workspace Scanner

✓ Detects Python project

✓ Detects Git

✓ Detects README

✓ Detects packages

✓ Detects entry point

Project Model

✓ Creates

.akydev/project.json

Task Engine

✓ Creates

.akydev/tasks/task-0001.json

Planner

✓ Reads project.json

✓ Reads task files

✓ Displays execution plan

===========================================================
CURRENT DATA FLOW
===========================================================

Workspace

↓

Scanner

↓

project.json

↓

Task Engine

↓

task.json

↓

Planner

Everything above already works.

===========================================================
SPRINTS COMPLETED
===========================================================

Sprint 001

CLI

Workspace Scanner

Status:

COMPLETE

---------------------------------------

Sprint 002

Sprint Framework

Status:

COMPLETE

---------------------------------------

Sprint 003

Project Model Generator

Creates

.akydev/project.json

Status:

COMPLETE

---------------------------------------

Sprint 004

Task Engine

Creates

task-0001.json

Status:

COMPLETE

---------------------------------------

Sprint 005

Planner

Reads project.json

Reads task files

Displays execution plan

Status:

COMPLETE

===========================================================
NEXT ROADMAP
===========================================================

Sprint 006

Prompt Builder

Input:

project.json

task.json

Output:

prompt.txt

---------------------------------------

Sprint 007

AI Provider

Gemini

OpenAI

Claude

Ollama

All providers must implement the same interface.

---------------------------------------

Sprint 008

Patch Generator

Generate unified diff patches.

Never edit files directly.

---------------------------------------

Sprint 009

Patch Validator

Validate generated patches.

Syntax checks.

Safety checks.

Preview.

---------------------------------------

Sprint 010

Patch Apply

Apply validated patches safely.

Backup files.

Rollback support.

---------------------------------------

Sprint 011

Test Runner

Run project tests automatically.

Detect failures.

Report results.

---------------------------------------

Sprint 012

Git Automation

Commit

Push

Branch management

===========================================================
LONG TERM GOAL
===========================================================

AKYDev should become the AI engineer that builds software projects.

It should eventually be capable of building RAPO.

===========================================================
RELATIONSHIP WITH RAPO
===========================================================

AKYDev is the builder.

RAPO is the product.

Eventually the workflow becomes:

cd RAPO

akydev analyze .

akydev task "Create DNS Enumeration"

akydev plan

akydev implement

akydev review

akydev apply

AKYDev writes RAPO.

===========================================================
CODING STYLE
===========================================================

Python

Readable

Small modules

Clear function names

Type hints where useful

No unnecessary abstractions

No magic

No giant classes

===========================================================
WORKFLOW
===========================================================

Every sprint:

1.

Understand goal.

2.

Implement feature.

3.

Compile.

4.

Run.

5.

Fix bugs.

6.

Commit.

7.

Push.

Then move to next sprint.

===========================================================
IMPORTANT
===========================================================

Do NOT redesign.

Do NOT restart.

Continue exactly from the existing codebase.

Build forward only.

===========================================================
FINAL OBJECTIVE
===========================================================

Create the best open-source AI Development Automation Platform.

Once AKYDev reaches MVP, use AKYDev to accelerate development of RAPO and future projects.