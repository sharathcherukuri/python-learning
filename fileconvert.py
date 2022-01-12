def stringconvert():
    with open("textconvert.txt", 'r') as fpIn, open("resulttext.txt", 'w') as fpOut:
        lineNumber = 0
        for line in fpIn:
            lineNumber += 1
            line = line.rstrip()   # Strip trailing spaces and newline
            fpOut.write("{}: {}-\n".format(line, line))
            # Need \n, which will be translated to platform-dependent newline
        print("Number of lines: {}\n".format(lineNumber))
