SAFETY_LIMIT = 100.0
TEMPERATURES = [80.0, 110.0]


def run_two_step_agent() -> list[str]:
    predictions = []

    for step, temperature in enumerate(TEMPERATURES, start=1):
        action = "cool" if temperature > SAFETY_LIMIT else "idle"
        predictions.append(
            f"Step {step}: Temperature {temperature:g} | Agent action: {action}"
        )

    return predictions


def main() -> None:
    for prediction in run_two_step_agent():
        print(prediction)


if __name__ == "__main__":
    main()