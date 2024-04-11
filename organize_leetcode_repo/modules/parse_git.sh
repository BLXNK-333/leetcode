#!/bin/bash

current_dir=$(pwd)

for ((i=0; i<2; i++)); do
    current_dir=$(dirname "$current_dir")
done

user_name=$(git config user.name || echo "")
repo_name=$(basename "$current_dir")
git_branch_name=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "")

echo "$user_name"
echo "$repo_name"
echo "$git_branch_name"
