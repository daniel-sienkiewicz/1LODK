#!/bin/bash
python --version

if [ $? -eq '0' ]; then
        echo "Python installed OK"
fi

git --version

if [ $? -eq '0' ]; then
        echo "GIT installed OK"
fi
