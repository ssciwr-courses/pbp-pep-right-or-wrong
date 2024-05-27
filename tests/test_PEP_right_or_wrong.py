import os
import subprocess
from pathlib import Path

def test_PEP8_conformance():
    """Test that we conform to PEP8."""
    # Get the repository directory
    current_dir = Path(__file__).resolve().parents[1]
    input_file_path = current_dir / "chapter1" / "PEP_right_or_wrong.md"
    reference_file_path = current_dir / ".github" / "workflows" / "Part1" / "PEP_right_or_wrong.md"
    # find number of lines that are different
    command = "diff {} {} | wc -l".format(str(input_file_path), str(reference_file_path))
    no_lines_different = int(subprocess.check_output(command, shell=True))
    no_errors = no_lines_different // 4
    # if there are some, print the differences and calculate no of errors
    if no_lines_different > 0:
        os.system(f"diff {input_file_path} {reference_file_path}")
        print("Number of PEP8 errors: {}".format(no_errors))
        print("Please try again!")
    else:
        print("No PEP8 errors found!")
    assert no_errors == 0