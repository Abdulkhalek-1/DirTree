# DirTree

DirTree is a command-line tool for visualizing directory structures. It provides customizable output, showing file sizes, permissions, and colorized formatting. You can limit traversal depth and ignore specified directories. DirTree is perfect for quickly understanding complex file systems and aiding in documentation or debugging.

## Features
- Display directory structure with visual pointers.
- Show file sizes in human-readable format.
- Include file permissions.
- Colorized output for better readability.
- Limit directory traversal depth.
- Ignore specified directories.

## How to Run

To use DirTree, follow these steps:

1. **Ensure you have Python installed**:
    - You need Python 3.x to run DirTree.

2. **Install required packages**:
    - DirTree uses the `termcolor` package for colorized output. Install it using pip:
      ```bash
      pip install termcolor
      ```

3. **Download the script**:
    - Save the script as `dirtree.py`.

4. **Run the script**:
    - Open a terminal and navigate to the directory containing `dirtree.py`.
    - Use the following command to run the script:
      ```bash
      python dirtree.py [options] <directory>
      ```

### Command-line Options

- `directory`: The root directory to print the structure of (default is the current directory).
- `-s`, `--size`: Show file sizes.
- `-d`, `--depth`: Limit the depth of directory traversal.
- `-c`, `--color`: Colorize the output.
- `-p`, `--permissions`: Include file permissions.
- `-o`, `--output`: Output the directory structure to a file.
- `-i`, `--ignore`: Ignore specified directories.

### Examples

1. **Print the structure of the current directory**:
    ```bash
    python dirtree.py .
    ```

2. **Print the structure with file sizes and colorized output**:
    ```bash
    python dirtree.py -s -c .
    ```

3. **Print the structure with a depth limit of 2**:
    ```bash
    python dirtree.py -d 2 .
    ```

4. **Print the structure, including file permissions**:
    ```bash
    python dirtree.py -p .
    ```

5. **Print the structure, ignoring specific directories**:
    ```bash
    python dirtree.py -i node_modules .venv .
    ```

6. **Output the structure to a file**:
    ```bash
    python dirtree.py -o output.txt .
    ```

## License

This project is licensed under the MIT License.
