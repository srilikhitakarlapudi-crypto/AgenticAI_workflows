SAFETY_LIMIT = 100.0


def temperature_action(temperature: float) -> str:
    return "cool" if temperature > SAFETY_LIMIT else "idle"


def main() -> None:
    previous_temperature: float | None = None
    print("State-tracking agent started. Enter q to quit.")

    while True:
        entry = input("Enter temperature: ").strip()
        if entry.lower() in {"q", "quit"}:
            print("Agent stopped.")
            break

        try:
            temperature = float(entry)
        except ValueError:
            print("Please enter a valid number, or q to quit.")
            continue

        if previous_temperature is None:
            trend = "first reading"
        elif temperature > previous_temperature:
            trend = "rising"
        elif temperature < previous_temperature:
            trend = "falling"
        else:
            trend = "unchanged"

        action = temperature_action(temperature)
        print(
            f"Temperature: {temperature:g} | Trend: {trend} | "
            f"Agent action: {action}"
        )
        previous_temperature = temperature


if __name__ == "__main__":
    main()