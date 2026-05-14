# LLM-Driven Autonomous Manufacturing System

This project was developed for the MUA600 course and demonstrates an autonomous smart manufacturing system based on a Multi-Agent System (MAS) architecture combined with local Large Language Model (LLM) planning using Ollama.

The system supports decentralized control, concurrent manufacturing agents, dynamic routing, Plug & Produce configuration, failure recovery, and AI-driven production planning.

---

# Features

## R1 — Decentralized Multi-Agent System

* Concurrent PartAgents using Python threading
* Message-based communication between agents
* Shared resource handling with locking and queues
* Generic CraneAgent for transportation

## R2 — Multiple Product Types

Different products follow different process plans.

### Example routes

Type 1:
Source1 → Process1 → Sink

Type 2:
Source2 → Process2 → Process1 → Sink

## R3 — Plug & Produce

* Factory layout loaded dynamically from JSON configuration
* Stations and coordinates can be changed without modifying source code

## R4 — Failure Recovery

* Automatic failure detection
* Dynamic rerouting to backup process stations
* Self-healing manufacturing behavior

## R5 — LLM Production Planning

* Local Ollama integration
* Natural language production orders
* AI-based production planning using llama3.2

Example:
"Produce 2 type1 parts and 3 type2 parts"

---

# Technologies

* Python 3.10
* Ollama
* llama3.2:1b
* Multi-threading
* JSON configuration
* Message-based MAS architecture

---

# Project Structure

```text
python_pro/
│
├── agents/
│   ├── crane_agent.py
│   ├── process_agent.py
│   ├── source_agent.py
│   ├── sink_agent.py
│   └── part_agent.py
│
├── config/
│   └── positions.json
│
├── planner.py
├── llm_main.py
├── main.py
├── messages.py
└── config_loader.py
```

---

# Installation

## 1. Create Python environment

```bash
py -3.10 -m venv .venv310
```

Activate:

```bash
.venv310\Scripts\activate
```

---

## 2. Install dependencies

```bash
pip install ollama
```

---

## 3. Install Ollama model

```bash
ollama pull llama3.2:1b
```

---

# Running the System

## Standard manufacturing execution

```bash
python main.py
```

## LLM-driven manufacturing execution

```bash
python llm_main.py
```

---

# Example Workflow

```text
Natural Language Order
        ↓
LLM Planner
        ↓
Production Orders
        ↓
Source Agents
        ↓
Part Agents
        ↓
Manufacturing Execution
        ↓
Failure Recovery
```

---

# Example Output

```text
USER ORDER:
Produce 2 type1 parts and 3 type2 parts

LLM RAW RESPONSE:
{"type1":2,"type2":3}

PARSED ORDERS:
{'type1': 2, 'type2': 3}
```

---

# Author

Mostafa Aldiab
University West — AI & Automation Master's Program
