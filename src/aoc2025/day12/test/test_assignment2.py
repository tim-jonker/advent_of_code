from src.aoc2025.day12.assignment2 import process_file


def test_process_file():
    result = process_file("input2.txt")
    assert result == 2
