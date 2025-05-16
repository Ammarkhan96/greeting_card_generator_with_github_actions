import argparse

def generate_greeting(recipient="World", message="Hello!"):
    greeting = f"Dear{recipient},\n\n{message}\n\nSincerely, \nThe Automated Greeting Card System"
    with open(f"greeting_for_{recipient.lower().replace(' ', '_')}.txt", "w") as f:
        f.write(greeting)
    print(f"Generated greeting card for {recipient}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a personalized greeting card")
    parser.add_argument("--recipient", type=str, default="World", help="Name of the recipient.")
    parser.add_argument("--message", type=str, default="Hello", help="The greeting message.")
    args = parser.parse_args()
    generate_greeting(args.recipient, args.message)