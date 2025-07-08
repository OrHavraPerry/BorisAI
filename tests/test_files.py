import os
from pathlib import Path

import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from ai_assist.tools.files import find_latest, move_to


def test_find_latest(tmp_path: Path):
    # create two files with different modification times
    first = tmp_path / "a.txt"
    second = tmp_path / "b.txt"
    first.write_text("1")
    second.write_text("2")
    # ensure different times
    os.utime(first, (first.stat().st_atime, first.stat().st_mtime - 10))
    assert find_latest("*.txt", root=str(tmp_path)) == str(second)


def test_move_to(tmp_path: Path):
    src = tmp_path / "source.txt"
    dst_dir = tmp_path / "dst"
    src.write_text("hello")
    result = move_to(str(dst_dir), str(src))
    assert (dst_dir / "source.txt").exists()
    assert "Moved" in result
