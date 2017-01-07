db = {
	"jerseys":[],
	"shorts":[],
	"shirts":[]
}

def parseToBinary(value, type):
	if (type == "COLOR"):
		if (value == "blue"): return "0"
		if (value == "red"): return "1"
	if (type == "SIZE"):
		if (value == "S"): return "00"
		if (value == "M"): return "01"
		if (value == "L"): return "10"
		if (value == "XL"): return "11"

def parseToString(value, type):
	if (type == "COLOR"):
		if (value == "0"): return "blue"
		if (value == "1"): return "red"
	if (type == "SIZE"):
		if (value == "00"): return "S"
		if (value == "01"): return "M"
		if (value == "10"): return "L"
		if (value == "11"): return "XL"

def addElement(data):
	size = parseToBinary(data[2], "SIZE")
	color = parseToBinary(data[3], "COLOR")
	if (data[4] == "jersey"): data[4] = "jerseys"
	if (data[4] == "shirt"): data[4] = "shirts"
	for x in range(int(data[1])): db[data[4]].append(size+color)

def showDatabase():
	print(db)

def showDatabaseHumanReadable():
	for i in db:
		print(i, ":")
		for j in db[i]:
			color = parseToString(j[0], "COLOR")
			size = parseToString(j[1:], "SIZE")
			print(j, "→", color, size)
			pass
	pass
