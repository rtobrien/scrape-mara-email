import json, time
import agentDict

def flatten():
    jdata_in = json.loads(open('result_all.json').read())
    jdata_out = open('agentdata.json', 'w')

    agentList = []
    for i in jdata_in['Result']:
        agentList.append(agentDict.getAgentDict(i))

    for chunk in json.JSONEncoder().iterencode(agentList):
        jdata_out.write(chunk)