# Grade Checker
# Take a score as input and print the grade based on the following:
# 90+ : "A"
# 80-89 : "B"
# 70-79 : "C"
# 60-69 : "D"
# Below 60 : "F"


def grade_from_score(score: float) -> str:
    """Return the grade letter for a numeric score (0-100).

    Accepts floats (e.g. 89.5 -> 'B'). Assumes score is already validated to be within 0..100.
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def main() -> None:
    """Read a score from stdin, validate it, and print the grade letter."""
    try:
        raw = input("Enter score (0-100): ").strip()
    except EOFError:
        print("No input received.")
        return

    if raw == "":
        print("No input provided.")
        return

    try:
        score = float(raw)
    except ValueError:
        print("Invalid input. Please enter a numeric score (e.g. 85 or 87.5).")
        return

    if not (0 <= score <= 100):
        print("Score out of range. Enter a value between 0 and 100.")
        return

    print(grade_from_score(score))


if __name__ == "__main__":
    main()
