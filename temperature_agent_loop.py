def main() -> None:
    print("Temperature agent loop started. Enter q to quit.")

    while True:
        entry = input("Enter temperature: ").strip()
        if entry.lower() in {"q", "quit"}:
            print("Agent loop stopped.")
            break

        try:
            temperature = float(entry)
        except ValueError:
            print("Please enter a valid number, or q to quit.")
            continue

        action = "cool" if temperature > 100 else "idle"
        print(f"Temperature: {temperature:g} | Agent action: {action}")


if __name__ == "__main__":
    main()