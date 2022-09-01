#1/bin/bash

find "$1" -type f -name "index.md" -exec sed -i 's/.py>/.py.html>/g' {} \;