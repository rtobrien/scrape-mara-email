import json
from pathlib import Path

def collected(filePath='agentdata_test1.json',attribute='Email'):
    if Path(filePath).exists():
        with open(filePath, 'r') as file:
            jdata = json.loads(file.read())
        total = len(jdata)
        count = 0

        for i in range(0, total):
            if '@' in jdata[i][attribute]:
                count += 1

        print(str(count) + " collected of " + str(total))

def timeRemaining(filePath='agentdata_test1.json',attribute='Email'):
	if Path(filePath).exists():
		with open(filePath, 'r') as file:
			jdata = json.loads(file.read())
		count = 0
		for i in jdata:
			if i[attribute] == "NOT CHECKED":
				count += 1

		waitTime = 2.6363
		remaining = count*waitTime
		s = int(remaining % 60)
		m = int((remaining/60) % 60)
		h = int(((remaining/60)/60) % 60)

		print(str(h) + ":" + str(m) + ":" + str(s) + " remaining (h:m:s)")
