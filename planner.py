import ollama
import json
import re


def extract_orders(text):

    response = ollama.chat(
        model="llama3.2:1b",
        messages=[
            {
                "role": "system",
                "content":
                (
                    "You are a production planner.\n"
                    "Extract ONLY production quantities.\n\n"

                    "Return ONLY valid JSON.\n"
                    "Do not explain anything.\n"
                    "Do not add markdown.\n"
                    "Do not add text.\n\n"

                    "Correct example:\n"
                    '{"type1":2,"type2":3}'
                )
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    content = response["message"]["content"]

    print("\nLLM RAW RESPONSE:")
    print(content)

    match = re.search(r"\{.*\}", content, re.DOTALL)

    if match:

        json_text = match.group()

        return json.loads(json_text)

    return {}