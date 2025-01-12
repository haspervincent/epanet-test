import sys
from pathlib import Path

from epyt import epanet


def parse_cmdline() -> Path:
    """Parse command line arguments to retrieve a valid `.inp` file.

    Returns:
        Path: A valid `.inp` file path.

    Raises:
        ValueError: If the number of arguments is incorrect or the provided file is not valid.

    Example:
        >>> inp_file: Path = parse_cmdline()
    """
    if len(sys.argv) != 2:
        raise ValueError("Invalid number of arguments.")

    p: Path = Path(sys.argv[1])

    if not p.is_file() or p.suffix != ".inp":
        raise ValueError(f"'{p}' is not a valid '.inp' file.")

    return p


def get_zones(en: epanet) -> set[str]:
    """Extract unique zone names from EPANET node and link IDs.

    This function iterates through all node and link IDs in the given EPANET network
    to extract unique zone names. It assumes that zone names are part of the name IDs,
    specifically the portion before the first '-' character (e.g., in 'zone1-pump1',
    the zone name would be 'zone1').

    Args:
        en (epanet): An EPANET network object.

    Returns:
        set[str]: A set of unique zone names found in the network.

    Example:
        >>> from epyt import epanet
        >>> en: epanet = epanet("network.inp")
        >>> zones: set[str] = get_zones(en)
        >>> print(zones)
        {'zone1', 'zone2', 'zone3'}

    Note:
        IDs without a '-' character are ignored.
    """
    zones: set[str] = set()

    for name_id in en.getNodeNameID() + en.getLinkNameID():
        if "-" not in name_id:
            continue

        zone, _ = name_id.split("-", 1)
        zones.add(zone)

    return zones


def main() -> None:
    try:
        inp_file: Path = parse_cmdline()
    except ValueError as e:
        print(f"ValueError: {e}")
        sys.exit(1)

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
