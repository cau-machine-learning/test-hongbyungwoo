import json
import os

# Your custom results
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

# Save to file for manual inspection (optional)
with open("results.json", "w") as f:
    json.dump(results, f, indent=2)

# Output JSON to console for debugging (not used by GitHub Actions directly)
print(json.dumps(results))

# Write result to GITHUB_OUTPUT so GitHub Actions can pass it to the reporter
with open(os.environ["GITHUB_OUTPUT"], "a") as gh_out:
    print(f"result={json.dumps(results)}", file=gh_out)
