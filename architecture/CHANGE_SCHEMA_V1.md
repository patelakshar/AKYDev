# AKYDev Change Schema v1

## Purpose

This document defines the JSON format returned by every AI provider.

Gemini

Claude

OpenAI

Ollama

DeepSeek

All providers MUST follow this schema.

AKYDev converts this JSON into code changes.

Providers never edit files directly.

---

# Root Schema

```json
{
    "changes": []
}
```

---

# Supported Operations

## Create File

```json
{
    "type":"create_file",
    "path":"src/example.py",
    "content":"..."
}
```

---

## Delete File

```json
{
    "type":"delete_file",
    "path":"src/example.py"
}
```

---

## Replace Function

```json
{
    "type":"replace_function",
    "file":"src/main.py",
    "function":"scan",
    "content":"..."
}
```

---

## Insert Function

```json
{
    "type":"insert_function",
    "file":"src/main.py",
    "after":"scan",
    "content":"..."
}
```

---

## Replace Class

```json
{
    "type":"replace_class",
    "file":"src/main.py",
    "class":"Scanner",
    "content":"..."
}
```

---

## Replace Imports

```json
{
    "type":"update_imports",
    "file":"src/main.py",
    "imports":[
        "import requests",
        "from pathlib import Path"
    ]
}
```

---

# Rules

Every object MUST contain

type

Every path must be relative.

Never use absolute paths.

No markdown.

No explanations.

No diff.

No patch.

Return ONLY JSON.

---

# Version

Schema Version

1.0