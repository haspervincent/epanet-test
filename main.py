import sys
from pathlib import Path

ASCII: str = """                                  
 _____       _         _____ _       
|  |  |_ _ _| |___ ___|   __|_|_____ 
|     | | | . |  _| . |__   | |     |
|__|__|_  |___|_| |___|_____|_|_|_|_|
      |___| https://github.com/........................
"""


def parse_cmdline() -> Path:
    """Parse command line arguments to retrieve a valid `.inp` file.

    Example:

    >>> inp_file = parse_cmdline()
    """
    if len(sys.argv) != 2:
        raise ValueError(
            f"Invalid number of arguments. Usage: python {sys.argv[0]} [network.inp]"
        )

    p: Path = Path(sys.argv[1])

    if not p.is_file() or p.suffix != ".inp":
        raise ValueError(f"'{p}' is not a valid '.inp' file.")

    return p


def main() -> None:
    try:
        inp_file: Path = parse_cmdline()
    except ValueError as e:
        print(f"ValueError: {e}")
        sys.exit(1)

    print(ASCII)

    try:
        pass
    except KeyboardInterrupt:
        print("KeyboardInterrupt: Program interrupted by user.")
        sys.exit(0)  # clean exit confirmed by user action.
    except Exception as e:
        print(f"Failed to run EPANET simulation due to an unexpected error: {e}")
        sys.exit(1)
    finally:
        pass


if __name__ == "__main__":
    main()
