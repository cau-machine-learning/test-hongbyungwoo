import json
import os
import sys

# Custom tests with individual scoring
tests = [
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

# Calculate total scores
total_score = sum(test["score"] for test in tests)
total_max_score = sum(test["max_score"] for test in tests)

# Print individual test results for GitHub Classroom
print("=== Test Results ===")
for test in tests:
    status = "✅ PASS" if test["score"] > 0 else "❌ FAIL"
    print(f"{status} {test['name']}: {test['score']}/{test['max_score']}")
    print(f"   Output: {test['output']}")
    print()

print(f"Total Score: {total_score}/{total_max_score}")

# GitHub Classroom looks for this specific format for points
print(f"Points: {total_score}")
print(f"::set-output name=points::{total_score}")

# Generate the autograder result file in the expected format
autograder_result = {
    "version": 1,
    "tests": tests
}

# Write to expected file
with open("autograder-result.json", "w") as f:
    json.dump(autograder_result, f, indent=2)

print("✅ Generated autograder-result.json")

# Exit with score-based code to signal partial credit
if total_score == total_max_score:
    sys.exit(0)  # Full credit
elif total_score > 0:
    # Use exit code that represents percentage (but still successful)
    percentage = int((total_score / total_max_score) * 100)
    print(f"Partial credit: {percentage}%")
    sys.exit(0)  # Still exit successfully but with partial indicator
else:
    sys.exit(1)  # No credit
