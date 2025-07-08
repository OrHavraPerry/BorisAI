from pathlib import Path


def find_latest(pattern: str, root: str = str(Path.home())) -> str:
    """Return the most recently modified file matching the pattern."""
    files = sorted(Path(root).rglob(pattern), key=lambda p: p.stat().st_mtime, reverse=True)
    return str(files[0]) if files else ""


def move_to(folder: str, path: str) -> str:
    """Move the file at *path* into *folder* and return a message."""
    src = Path(path)
    dest = Path(folder) / src.name
    dest.parent.mkdir(parents=True, exist_ok=True)
    src.rename(dest)
    return f"Moved {src} -> {dest}"
