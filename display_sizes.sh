#!/bin/bash

#  Coomment  for GIT
display_size() {
    for item in *; do
        if [ -d "$item" ]; then
            echo "Directory: $item - Size: $(du -sh "$item" | cut -f1)"
        elif [ -f "$item" ]; then
            echo "File: $item - Size: $(du -sh "$item" | cut -f1)"
        fi
    done
}

display_size
