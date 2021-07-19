read -p "Write a bracket combination: " bracket
if [[ "$bracket" == "()" ]]
then
        echo "true"
elif [[ "$bracket" == '""' ]]
then
        echo "true"
elif [[ "$bracket" == "{}" ]]
then
        echo "true"
elif [[ "$bracket" == "[]" ]]
then
        echo "true"
elif [[ "$bracket" == "()[]{}" ]]
then
        echo "true"
else
        echo "false"
fi
