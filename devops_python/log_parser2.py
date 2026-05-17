
# Count errors in a log file
error_count = 0

with open("app.log", "r") as f:
    for line in f:
        if "ERROR" in line:
            error_count += 1

print("Total errors:", error_count)
