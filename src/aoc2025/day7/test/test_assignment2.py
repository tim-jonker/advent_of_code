from src.aoc2025.day7.assignment2 import process_file


def test_process_file():
    result = process_file("input.txt")
    assert result == 40