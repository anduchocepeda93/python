with open("app.log") as infile, open("errors.log", "w") as outfile:
    for line in infile:
        if "ERROR" in line:
            outfile.write(line)
