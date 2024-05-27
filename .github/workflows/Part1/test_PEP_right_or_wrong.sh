#/bin/bash

diff ../../chapter1/PEP_right_or_wrong.md ./Part1/PEP_right_or_wrong.md 
no_lines=$(diff ../../chapter1/PEP_right_or_wrong.md ./Part1/PEP_right_or_wrong.md | wc -l)
no_errors=$(echo "$no_lines/4" | bc)
echo "There are $no_errors errors in your answer to PEP_right_or_wrong.md"
if [ "$no_errors" -eq "0" ] ; then
    echo "Well done!"
else
    echo "ERROR: Please check your answer and try again."
fi 