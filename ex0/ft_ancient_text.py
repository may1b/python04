import sys


def main() -> None:
    if len(sys.argv) <= 1:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ===")
    fname = sys.argv[1]
    print(f"Accessing file '{fname}'")
    try:
        file = open(fname, "r")
        print("---\n")
        print(file.read())
        print("---")
        file.close()
        print(f"File '{fname}' closed.")
    except Exception as err:
        print(f"Error opening file '{fname}': {err}")
        return


if __name__ == "__main__":
    main()
