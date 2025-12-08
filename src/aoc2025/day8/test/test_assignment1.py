from src.aoc2025.day8.assignment1 import process_file


def test_process_file():
    result = process_file("input.txt", 10)
    assert result == 40