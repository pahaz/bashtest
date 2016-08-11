#!/usr/bin/env bash

if [ -z "$1" ]
then
    DIR=./
else
    DIR=$1
fi

echo "Evaluate *.py statistics"
FILES=$(find $DIR -name '*.py' | wc -l)
LINES=$((find $DIR -name '*.py' -print0 | xargs -0 cat) | wc -l)
echo "PYTHON FILES: $FILES"
echo "PYTHON LINES: $LINES"
