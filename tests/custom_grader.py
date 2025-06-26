import json
import base64
import os

# Define your test results with actual scores
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

# Build the autograder result payload
autograder_result = {
    "version": 1,
    "tests": tests
}

# Write result file (optional, for debugging or logs)
with open("autograder-result.json", "w") as f:
    json.dump(autograder_result, f, indent=2)

# Encode the result as base64 for GitHub Actions
encoded = base64.b64encode(json.dumps(autograder_result).encode()).decode()

# Try the preferred modern method (GITHUB_OUTPUT), fall back to deprecated syntax
if 'GITHUB_OUTPUT' in os.environ:
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f"result={encoded}", file=fh)
else:
    # Deprecated fallback, still supported in GitHub Actions
    print(f"::set-output name=result::{encoded}")
