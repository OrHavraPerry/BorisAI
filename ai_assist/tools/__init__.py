"""Tool utilities for BorisAI."""

from .files import find_latest, move_to


def list_files(directory: str):
    """Return a list of filenames for *directory* that are files (not directories)."""
    import os
    return [
        f for f in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, f))
    ]


__all__ = [
    "list_files",
    "find_latest",
    "move_to",
]
