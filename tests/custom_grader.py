import json
import base64
import os

# Define your test results
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

autograder_result = {
    "version": 1,
    "tests": tests
}

with open("autograder-result.json", "w") as f:
    json.dump(autograder_result, f, indent=2)

encoded = base64.b64encode(json.dumps(autograder_result).encode()).decode()

if 'GITHUB_OUTPUT' in os.environ:
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f"result={encoded}", file=fh)
else:
    print(f"::set-output name=result::{encoded}")
