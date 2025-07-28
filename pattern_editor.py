import json

def edit_pattern(pattern):
    print("\n[Auto-Detected Pattern]")
    print(json.dumps(pattern, indent=2))

    # Simulate edit
    pattern["manual_reviewed"] = True
    pattern["approved"] = True
    return pattern
