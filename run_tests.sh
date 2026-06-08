#!/bin/bash

echo "Activating virtual environment..."
source venv/bin/activate

echo "Running test suite..."
pytest test_app.py

# Capture the exit code of the pytest command
EXIT_CODE=$?

# Check if tests passed (exit code 0) or failed (exit code 1)
if [ $EXIT_CODE -eq 0 ]; then
  echo "✅ All tests passed successfully!"
  exit 0
else
  echo "❌ Tests failed. Please check the output above."
  exit 1
fi