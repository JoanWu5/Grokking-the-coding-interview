#!/bin/bash

find "$1" -type f -name "*.py" -exec sh -c 'cp "$1" "$1".md' -- {} \;
find "$1" -type f -name "*.py.md" | while read file; do sed -i '1s/^/```python\n/' "$file"; done
find "$1" -type f -name "*.py.md" | while read file; do sed -i -e '$a```\n' "$file"; done
