def run_agent_loop(iterations: int = 3) -> list[str]:
    steps = []
    step = 0

    while step < iterations:
        steps.append(f"Step {step + 1}: Observe -> Decide -> Act")
        step += 1

    return steps


def main() -> None:
    steps = run_agent_loop()
    for entry in steps:
        print(entry)
    print(f"Agent loop completed after {len(steps)} iterations.")


if __name__ == "__main__":
    main()