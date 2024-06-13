import os
import sys
import argparse
import stat
import math
import time
from termcolor import colored


def print_directory_structure(
    directory,
    indent="",
    show_size=False,
    depth_limit=None,
    current_depth=0,
    colorize=False,
    include_permissions=False,
    ignore_dirs=[],
):
    try:
        # Get the contents of the directory and sort them
        contents = os.listdir(directory)# sorted(os.listdir(directory))
    except PermissionError:
        print(colored(f"{indent}└── [Permission Denied]", "red"))
        return

    # Filter out ignored directories
    contents = [item for item in contents if item not in ignore_dirs]

    # Determine pointers for visual representation
    pointers = ["├── "] * (len(contents) - 1) + ["└── "]

    for pointer, name in zip(pointers, contents):
        path = os.path.join(directory, name)
        is_directory = os.path.isdir(path)

        display_name = name
        if show_size and not is_directory:
            display_name += colored(
                f" ({convert_size(os.path.getsize(path))})", "yellow"
            )
        if include_permissions:
            display_name = f"{get_permissions(path)} {display_name}"

        if colorize:
            if is_directory:
                display_name = colored(display_name, "blue")
            else:
                display_name = colored(display_name, "green")

        print(indent + pointer + display_name)

        if is_directory:
            if depth_limit is None or current_depth < depth_limit:
                if pointer == "└── ":
                    print_directory_structure(
                        path,
                        indent + "    ",
                        show_size,
                        depth_limit,
                        current_depth + 1,
                        colorize,
                        include_permissions,
                        ignore_dirs,
                    )
                else:
                    print_directory_structure(
                        path,
                        indent + "│   ",
                        show_size,
                        depth_limit,
                        current_depth + 1,
                        colorize,
                        include_permissions,
                        ignore_dirs,
                    )


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0 B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"


def get_permissions(path):
    st = os.stat(path)
    return stat.filemode(st.st_mode)


def timit(func):
    def wrapper(*args, **kwargs):
        s = time.perf_counter()
        result = func(*args, **kwargs)
        e = time.perf_counter()
        print(f"\nDone in: {e-s:.2f}s")
        return result

    return wrapper


@timit
def main():
    parser = argparse.ArgumentParser(description="Print the directory structure.")
    parser.add_argument(
        "directory", default=".", help="The root directory to print the structure of."
    )
    parser.add_argument("-s", "--size", action="store_true", help="Show file sizes.")
    parser.add_argument(
        "-d", "--depth", type=int, help="Limit the depth of directory traversal."
    )
    parser.add_argument(
        "-c", "--color", action="store_true", help="Colorize the output."
    )
    parser.add_argument(
        "-p", "--permissions", action="store_true", help="Include file permissions."
    )
    parser.add_argument(
        "-o", "--output", help="Output the directory structure to a file."
    )
    parser.add_argument(
        "-i", "--ignore", nargs="*", default=[], help="Ignore specified directories."
    )

    args = parser.parse_args()

    root_directory = os.path.abspath(args.directory)
    output = sys.stdout

    if args.output:
        output = open(args.output, "w", encoding="utf-8")

    sys.stdout = output
    print(os.path.basename(root_directory))
    print_directory_structure(
        root_directory,
        show_size=args.size,
        depth_limit=args.depth,
        colorize=args.color,
        include_permissions=args.permissions,
        ignore_dirs=args.ignore,
    )
    sys.stdout = sys.__stdout__

    if args.output:
        output.close()


if __name__ == "__main__":
    main()
