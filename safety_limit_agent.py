SAFETY_LIMIT = 100.0


def safety_limit_agent(temperature: float) -> str:
    if temperature > SAFETY_LIMIT:
        return "cool"
    return "idle"


def main() -> None:
    try:
        temperature = float(input("Enter temperature: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    action = safety_limit_agent(temperature)
    print(f"Temperature: {temperature:g}")
    print(f"Safety limit: {SAFETY_LIMIT:g}")
    print(f"Agent action: {action}")


if __name__ == "__main__":
    main()