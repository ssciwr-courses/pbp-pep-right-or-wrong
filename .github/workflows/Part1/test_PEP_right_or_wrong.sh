#/bin/bash
file_input=chapter1/PEP_right_or_wrong.md
file_reference=.github/workflows/Part1/PEP_right_or_wrong.md
diff "$file_input" "$file_reference"
no_lines=$(diff "$file_input" "$file_reference" | wc -l)
no_errors=$(echo "$no_lines/4" | bc)
echo "There are $no_errors errors in your answer to PEP_right_or_wrong.md"
if [ "$no_errors" -eq "0" ] ; then
    echo "Well done!"
else
    echo "ERROR: Please check your answer and try again."
fi 