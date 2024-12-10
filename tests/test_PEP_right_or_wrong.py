import os
import subprocess
from pathlib import Path
import pytest

FILES = ["question1.md", "question2_classes.md", "question2_functions.md",
         "question2_variables.md", "question2_constants.md", "question2_other.md", 
         "question2_modules.md", "question2_packages.md"
         ]

COMMANDS = ["grep -A 30 \"# 1. Code alignment\"",
            "grep -A5 \"Classes:\"",
            "grep -A5 \"Functions:\"",
            "grep -A5 \"Variables:\"",
            "grep -A5 \"Constants:\"",
            "grep -A5 \"Other:\"",
            "grep -A5 \"Modules:\"",
            "grep -A5 \"Packages:\"",
            ]

@pytest.fixture(scope="module")
def get_path():
    # Get the repository directory
    current_dir = Path(__file__).resolve().parents[1]
    input_file = current_dir / "chapter1" / "PEP_right_or_wrong.md"
    reference_file_path = current_dir / ".github" / "workflows" / "Part1"
    return input_file, reference_file_path


def test_question1(get_path):
    """Test that we conform to PEP8, question1."""
    input_file, reference_file_path = get_path
    reference_file = reference_file_path / FILES[0]
    command_get = COMMANDS[0] + " " + str(reference_file)
    reference = str(subprocess.check_output(command_get, shell=True))
    command_get = COMMANDS[0] + " " + str(input_file)
    input = str(subprocess.check_output(command_get, shell=True))
    # find number of elements that are different
    assert input == reference

def test_question2_classes(get_path):
    """Test that we conform to PEP8, question2 classes."""
    input_file, reference_file_path = get_path
    reference_file = reference_file_path / FILES[1]
    command_get = COMMANDS[1] + " " + str(reference_file)
    reference = str(subprocess.check_output(command_get, shell=True))
    command_get = COMMANDS[1] + " " + str(input_file)
    input = str(subprocess.check_output(command_get, shell=True))
    # find number of elements that are different
    assert input == reference


def test_question2_functions(get_path):
    """Test that we conform to PEP8, question2 functions."""
    input_file, reference_file_path = get_path
    reference_file = reference_file_path / FILES[2]
    command_get = COMMANDS[2] + " " + str(reference_file)
    reference = str(subprocess.check_output(command_get, shell=True))
    command_get = COMMANDS[2] + " " + str(input_file)
    input = str(subprocess.check_output(command_get, shell=True))
    # find number of elements that are different
    assert input == reference

def test_question2_variables(get_path):
    """Test that we conform to PEP8, question2 variables."""
    input_file, reference_file_path = get_path
    reference_file = reference_file_path / FILES[3]
    command_get = COMMANDS[3] + " " + str(reference_file)
    reference = str(subprocess.check_output(command_get, shell=True))
    command_get = COMMANDS[3] + " " + str(input_file)
    input = str(subprocess.check_output(command_get, shell=True))
    # find number of elements that are different
    assert input == reference

def test_question2_constants(get_path):
    """Test that we conform to PEP8, question2 constants."""
    input_file, reference_file_path = get_path
    reference_file = reference_file_path / FILES[4]
    command_get = COMMANDS[4] + " " + str(reference_file)
    reference = str(subprocess.check_output(command_get, shell=True))
    command_get = COMMANDS[4] + " " + str(input_file)
    input = str(subprocess.check_output(command_get, shell=True))
    # find number of elements that are different
    assert input == reference

def test_question2_other(get_path):
    """Test that we conform to PEP8, question2 other."""
    input_file, reference_file_path = get_path
    reference_file = reference_file_path / FILES[5]
    command_get = COMMANDS[5] + " " + str(reference_file)
    reference = str(subprocess.check_output(command_get, shell=True))
    command_get = COMMANDS[5] + " " + str(input_file)
    input = str(subprocess.check_output(command_get, shell=True))
    # find number of elements that are different
    assert input == reference

def test_question2_modules(get_path):
    """Test that we conform to PEP8, question2 modules."""
    input_file, reference_file_path = get_path
    reference_file = reference_file_path / FILES[6]
    command_get = COMMANDS[6] + " " + str(reference_file)
    reference = str(subprocess.check_output(command_get, shell=True))
    command_get = COMMANDS[6] + " " + str(input_file)
    input = str(subprocess.check_output(command_get, shell=True))
    # find number of elements that are different
    assert input == reference

def test_question2_packages(get_path):
    """Test that we conform to PEP8, question2 packages."""
    input_file, reference_file_path = get_path
    reference_file = reference_file_path / FILES[7]
    command_get = COMMANDS[7] + " " + str(reference_file)
    reference = str(subprocess.check_output(command_get, shell=True))
    command_get = COMMANDS[7] + " " + str(input_file)
    input = str(subprocess.check_output(command_get, shell=True))
    # find number of elements that are different
    assert input == reference