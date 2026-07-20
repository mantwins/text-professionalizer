Markdown
# text-professionalizer

A Python CLI tool that converts informal draft text into clear, professional business communication using the Anthropic API.

---

## Features
- Language awareness: Maintains the original language (e.g., Greek input returns Greek output).
- Direct formatting: Output contains only the polished version with no conversational intro or meta-explanations.
- Configured temperature (0.3) for consistent, high-fidelity rewrites.

---

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
Configure environment:
Copy .env.example to .env and set your Anthropic API key:

Plaintext
ANTHROPIC_API_KEY=your_actual_key_here
Run the script:

Bash
python main.py
Example
Input:

Plaintext
hey, just wanted to let you know the report is delayed a bit, will send it over later today, sorry
Output:

Plaintext
I am writing to inform you that the report has been slightly delayed. I will forward it to you later today. Thank you for your patience.
Tech Stack
Python

Anthropic SDK

python-dotenv
