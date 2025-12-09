#!/usr/bin/env bash

NOTE_TEXT="$1"

curl -X POST -H "Content-Type: application/json" \
    -d "{\"text\":\"$NOTE_TEXT\"}" http://localhost:5000/notes
