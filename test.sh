for output in $(find ./ -name "*.py")
do
pylint $output --errors-only
done
