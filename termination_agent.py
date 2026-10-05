import math


SAFETY_LIMIT = 100.0


def run_termination_agent() -> list[str]:
    log = [f"Agent started. Safety limit: {SAFETY_LIMIT:g}."]

    while True:
        entry = input("Enter current temperature (or q to quit): ").strip()
        log.append(f"Input received: {entry}")

        if entry.lower() in {"q", "quit"}:
            log.append("Agent stopped manually.")
            break

        try:
            temperature = float(entry)
        except ValueError:
            log.append("Invalid input; expected a numeric temperature.")
            continue

        if not math.isfinite(temperature):
            log.append("Invalid input; temperature must be a finite number.")
            continue

        if temperature > SAFETY_LIMIT:
            log.append(f"Temperature: {temperature:g} | Agent action: cool")
            continue

        log.append(f"Temperature: {temperature:g} | Agent action: idle")
        log.append("Safety limit reached. Agent terminated.")
        break

    return log


def main() -> None:
    full_log = run_termination_agent()
    print("\nFull agent log:")
    for step in full_log:
        print(f"- {step}")


if __name__ == "__main__":
    main()