from src.aoc2025.day5.assignment2 import process_file


def test_process_file():
    result = process_file("input.txt")
    assert result == 14


def test_keep_middel_file():
    result = process_file("input_keep_middle.txt")
    assert result == 12


def test_remove_middle_file():
    result = process_file("input_remove_middle.txt")
    assert result == 8