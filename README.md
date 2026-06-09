# Password Strength Analyzer

A Python-based tool that evaluates password strength based on security rules like length, complexity, and character variety.

---------------------

# Features

- Checks for spaces (not allowed)
- Validates minimum and maximum length (8–20 characters)
- Ensures at least one uppercase letter
- Ensures at least one number
- Ensures at least one special character
- Returns list of issues if invalid
- Grades password strength:
  - 🟥 Easy (8–11 characters)
  - 🟨 Medium (12–15 characters)
  - 🟩 Strong (16–20 characters)

--------------------

# How it works

The program checks the password step-by-step:
1. Stores all validation errors in a list
2. If errors exist -> shows them
3. If no errors -> assigns strength based on length

--------------------

# How to run

--> bash
python3 main.py

--------------------