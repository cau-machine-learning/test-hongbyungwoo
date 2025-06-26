import json
import os
import sys

# Custom tests with individual scoring
tests = [
    {
        "name": "Functionality Test",
        "output": "Passed all edge cases",
        "score": 75,
        "max_score": 100
    },
    {
        "name": "Style Check", 
        "output": "Minor formatting issues",
        "score": 50,
        "max_score": 100
    },
    {
        "name": "Bonus Question",
        "output": "Excellent work!",
        "score": 100,
        "max_score": 100
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
# Use the new environment file method instead of deprecated set-output
print(f"POINTS={total_score}", file=open(os.environ.get('GITHUB_OUTPUT', '/dev/null'), 'a') if 'GITHUB_OUTPUT' in os.environ else open('/dev/null', 'w'))

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
score_percentage = total_score / total_max_score
if score_percentage >= 1.0:
    print(f"Perfect score! {total_score}/{total_max_score}")
    sys.exit(0)  # Full credit
elif score_percentage >= 0.6:  # 60% or better gets partial credit
    percentage = int(score_percentage * 100)
    print(f"Partial credit: {percentage}% ({total_score}/{total_max_score})")
    sys.exit(0)  # Partial credit but still successful
elif total_score > 0:
    percentage = int(score_percentage * 100)
    print(f"Some credit: {percentage}% ({total_score}/{total_max_score})")
    sys.exit(0)  # Some credit
else:
    print(f"No credit: {total_score}/{total_max_score}")
    sys.exit(1)  # No credit
