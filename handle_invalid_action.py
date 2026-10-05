def handle_action(action: str) -> dict[str, str]:
    if action not in {"cool", "idle"}:
        return {"error": f"Invalid action: {action}"}
    return {"action": action}


def main() -> None:
    action = input("Enter agent action: ").strip()
    result = handle_action(action)
    print(result)


if __name__ == "__main__":
    main()