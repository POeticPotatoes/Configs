#!/usr/bin/bash
# Script to continuously build dotnet on changes when developing

echo "Listening in directory..."
dotnet build
while inotifywait -r -q -e modify,create,delete,moved_to,moved_from .;
do
    echo "Changes detected!"
    dotnet build
done
