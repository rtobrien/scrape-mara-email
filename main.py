import flattenJson, collectEmail, collectJson, jsonToCSV, check
import sys
from pathlib import Path

path = sys.path[0]
inpath = path + '/agentdata_email.json'
outpath = path + '/agentdata_email.json'

def main():
    try:
        if Path(outpath).exists():
            update()
        else:
            start()
    except(KeyboardInterrupt):
        check.collected(outpath)
    outputCSV()



def outputCSV():
    source = outpath
    jsonToCSV.write('agents.csv', source)


def start():
    collectJson.collectFromSite()
    flattenJson.flatten()
    collectEmail.collect()


def update():
    check.collected(outpath)
    print("...")
    print("READING FROM: " + outpath)
    print("...")
    print("WRITING TO: " + outpath)

    collectEmail.collect(outpath, outpath)

if __name__ == '__main__': main()

