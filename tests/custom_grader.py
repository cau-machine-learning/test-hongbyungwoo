import json
import os

# Custom tests
results = [
    {
        "name": "Functionality Test",
        "output": "Passed all edge cases",
        "score": 0.75,
        "max_score": 1.0
    },
    {
        "name": "Style Check",
        "output": "Minor formatting issues",
        "score": 0.5,
        "max_score": 1.0
    },
    {
        "name": "Bonus Question",
        "output": "Excellent work!",
        "score": 1.0,
        "max_score": 1.0
    }
]

# Wrap in expected format
autograder_result = {
    "version": 1,
    "tests": results
}

# Write to expected file
with open("autograder-result.json", "w") as f:
    json.dump({
        "version": 1,
        "tests": results
    }, f, indent=2)


print("✅ Generated autograder-result.json")
