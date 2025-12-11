from src.aoc2025.day11.assignment1 import process_file


def test_process_file():
    result = process_file("input.txt")
    assert result == 5