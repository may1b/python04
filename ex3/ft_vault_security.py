def secure_archive(
    fname: str,
    action: str = "read",
    content: str = "",
) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(fname, "r") as file:
                return (True, file.read())
        if action == "write":
            with open(fname, "w") as file:
                file.write(content)
            return (True, "Content successfully written to file")
        return (False, "Unknown archive action")
    except Exception as err:
        return (False, str(err))


def main() -> None:
    print("=== Cyber Archives Security ===")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))
    print("Using 'secure_archive' to read from a regular file:")
    regular_file = secure_archive("ancient_fragment.txt")
    print(regular_file)
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_fragment.txt", "write", regular_file[1]))


if __name__ == "__main__":
    main()
