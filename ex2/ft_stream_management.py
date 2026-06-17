import sys
from typing import IO


def add_archive_character(content: str) -> str:
    transformed = ""
    lines = content.splitlines(True)
    for line in lines:
        if line.endswith("\n"):
            transformed += line[:-1] + "#\n"
        else:
            transformed += line + "#"
    return transformed


def write_error(message: str) -> None:
    sys.stderr.write(f"[STDERR] {message}\n")
    sys.stderr.flush()


def read_archive(fname: str) -> str | None:
    file: IO[str]
    try:
        file = open(fname, "r")
        content = file.read()
        print("---")
        print(content, end="")
        print("---")
        file.close()
        print(f"File '{fname}' closed.")
        return content
    except Exception as err:
        write_error(f"Error opening file '{fname}': {err}")
        return None


def save_archive(fname: str, content: str) -> bool:
    file: IO[str]
    try:
        file = open(fname, "w")
        file.write(content)
        file.close()
        return True
    except Exception as err:
        write_error(f"Error opening file '{fname}': {err}")
        return False


def ask_output_file() -> str:
    print("Enter new file name (or empty): ", end="")
    sys.stdout.flush()
    answer = sys.stdin.readline()
    if answer.endswith("\n"):
        answer = answer[:-1]
    return answer


def main() -> None:
    if len(sys.argv) <= 1:
        print("Usage: ft_stream_management.py <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    fname = sys.argv[1]
    print(f"Accessing file '{fname}'")
    content = read_archive(fname)
    if content is None:
        return
    new_content = add_archive_character(content)
    print("Transform data:")
    print("---")
    print(new_content, end="")
    print("---")
    new_fname = ask_output_file()
    if new_fname == "":
        print("Not saving data.")
        return
    print(f"Saving data to '{new_fname}'")
    if save_archive(new_fname, new_content):
        print(f"Data saved in file '{new_fname}'.")
    else:
        print("Data not saved.")


if __name__ == "__main__":
    main()
