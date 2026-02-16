import os  # For creating directories
import requests  # For HTTP requests


# Use the single-random-fact endpoint, not the list endpoint.
API_URL = "https://catfact.ninja/fact"


def get_cat_fact():
    """Fetch a single cat fact string from the API and return it."""
    # timeout must be a number, not a string; this prevents hanging forever.
    resp = requests.get(API_URL, timeout=5)

    # Parse JSON response into a Python dict.
    data = resp.json()

    # The random-fact endpoint returns a single object with a "fact" key.
    fact = data["fact"]

    return fact


def save_fact_to_file(text):
    """Save the provided text to data/cat_fact.txt"""
    out_dir = "data"
    out_path = os.path.join(out_dir, "cat_fact.txt")

    # Ensure the output directory exists before writing, or open() will fail.
    os.makedirs(out_dir, exist_ok=True)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)

    # Fix filename typo so it matches the actual file being written.
    print("Saved to cat_fact.txt")


def main():
    fact = get_cat_fact()
    # Guard stays the same: only write non-empty strings.
    if fact and isinstance(fact, str):
        save_fact_to_file(fact)
    else:
        print("No fact fetched. Check API response structure.")


if __name__ == "__main__":
    main()
