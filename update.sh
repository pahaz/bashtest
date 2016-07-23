#!/usr/bin/env bash

set -x

let num_git_changes="$(git status --porcelain | wc -l)"
let num_git_changes="$(printf '%s\n' "$num_git_changes")"
if [ "$num_git_changes" != "0" ]; then
    echo "please commit or stash changes before" 
    exit 1
fi

python setup.py build sdist upload
if [ "$?" != "0" ]; then
    echo "build and upload problem"
    exit 2
fi

VERSION=$(python setup.py --version)
NAME=$(python setup.py --name)
NEXTVERSION=`echo $VERSION | python3 -c "v = input().strip().split('.'); v[-1] = str(int(v[-1]) + 1); print('.'.join(v))"`

git tag -a v$VERSION -m "version $VERSION"
sed -e "s|$VERSION|$NEXTVERSION|g" -i.back $NAME.py $NAME/*
rm *.back
