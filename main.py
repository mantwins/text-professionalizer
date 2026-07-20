import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = "claude-sonnet-5"

SYSTEM_PROMPT = (
    "You are an editor. Rewrite the user's rough, informal text into clear, "
    "professional language suitable for a business email or report. "
    "Keep the original meaning and the original language (if the input is "
    "in Greek, reply in Greek; if English, reply in English). "
    "Return ONLY the rewritten text, with no explanation or preamble."
)


def make_professional(rough_text):
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError(
            "Missing ANTHROPIC_API_KEY. Create a .env file with "
            "ANTHROPIC_API_KEY=your_key_here"
        )

    client = Anthropic(api_key=api_key)

    response = client.messages.create(
        model=MODEL_NAME,
        max_tokens=500,
        temperature=0.3,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": rough_text}],
    )

    return response.content[0].text.strip()


def main():
    print("Type your draft text and press Enter:\n")
    rough_text = input("> ").strip()

    if not rough_text:
        print("No text provided.")
        return

    print("\nProcessing...\n")
    result = make_professional(rough_text)

    print("Professional version:")
    print(result)


if __name__ == "__main__":
    main()
