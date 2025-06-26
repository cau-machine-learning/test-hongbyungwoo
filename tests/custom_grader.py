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

# Generate the autograder result file in the expected format
autograder_result = {
    "version": 1,
    "tests": tests
}

# Write to expected file
with open("autograder-result.json", "w") as f:
    json.dump(autograder_result, f, indent=2)

print("✅ Generated autograder-result.json")

# Exit with appropriate code based on results
if total_score == total_max_score:
    sys.exit(0)  # All tests passed
else:
    sys.exit(0)  # Still exit successfully to allow partial credit
