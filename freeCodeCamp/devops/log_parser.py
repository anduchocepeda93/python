# log_parser.py
with open("app.log", "r") as f:
    for line in f:
        if "ERROR" in line:
            print(line)