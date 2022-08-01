#!/bin/bash


find "$1" -type d -not -path "$1/.git*" -not -path "$1/scripts*" | xargs -I{} sh -c 'find "$1" -not -path "$1/.git*" -not -path "$1/scripts*" -not -name "*.md" -not -name "LICENSE" -not -path "$1" -maxdepth 1 -printf "[%f](<%f>)\n\n" > "$1/index.md"' -- {}