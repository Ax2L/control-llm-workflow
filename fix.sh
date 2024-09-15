##!/bin/bash

sh kill -9 $(lsof -t -i:5001) || True

rm -rf .taipy
rm -rf logs.txt

for file in $(find . -name "*.pyc"); do
    rm -rf $file
done

for file in $(find . -name "__pycache__"); do
    rm -rf $file
done    

rm -rf user_data

mv config.toml backup/config.toml
touch config.toml
