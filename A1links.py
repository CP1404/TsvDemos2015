"""
Script for creating links for marking CP1406 A1 assignments - plan and site.
Requires CSV file with rows like, "Last name, First Name, jc123456"
Tsv/Cns: run twice; programmer just find and replace "Townsville"-"Cairns" and "tsv"-"cns"
"""

# filename = "/Users/sci-lmw1/GoogleDrive/CP1406/CP1406 CP2010 2015-1/CP1406 2015-1/Assignments/CairnsStudents.csv"
filename = "/Users/sci-lmw1/GoogleDrive/CP1406/CP1406 2015-2/CP1406 2015 SP2/Assignments/A1/CairnsStudents.csv"
linkBase = "<a href=\"http://ditwebcns.jcu.edu.au/~"
topSection = """<!doctype html>
<html>
<head>
<title>CP1406, 2015-2 - Assignment 1 Links</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
    <style type="text/css">
        body { font-family: Arial; margin-left: 3em; }
        h1, h2 { margin-left: -1em; }
        h2 { margin-top: 1.5em; margin-bottom: 0.5em; }
    </style>
</head>

<body>
    <h1>CP1406, 2015-2 - Assignment 1 Links</h1>
    <ol>\n"""
bottomSection = """</ol>
</body>
</html>\n"""

inFile = open(filename, 'r')
outFile = open("CairnsA1links.html", 'w')

outFile.write(topSection + "\n")
for line in inFile:
    parts = line.split(",")
    # print(parts)
    linkLine = "<li>" + linkBase + parts[2].strip() + "/a1/plan.html\" target=\"_blank\">" + parts[1] + " " + parts[0] + " (" + parts[2].strip() + ") Plan</a> - "
    linkLine += linkBase + parts[2].strip() + "/a1\" target=\"_blank\">Site</a></li>"
    outFile.write(linkLine + "\n")
outFile.write(bottomSection)
inFile.close()
outFile.close()
