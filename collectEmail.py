import requests, time, json, sys, random, check
from bs4 import BeautifulSoup as bs
from pathlib import Path

def collect(filepath='agentdata.json',outpath='agentdata_test1.json', backup='BackupFile'):
    file = open(filepath, 'r')
    jdata = json.loads(file.read())
    file.close()
    URL='https://www.mara.gov.au/search-the-register-of-migration-agents/registered-migration-agent-details/?id='

    i = 0
    count = 0
    changed = False
    for agent in jdata:
        i += 1
        if agent['Email'] == "NOT FOUND":
            count += 1
            waitTimes = [1,1,2,2,2,2,3,3,4,4,5]
            time.sleep(random.randint(0,len(waitTimes)-1))
            contactPage = requests.get(URL + agent['ContactId'])
            # CHECK VALIDITY OF HTTP RESPONSE
            print(contactPage.status_code)
            if contactPage.status_code == 200:
                soup = bs(contactPage.text, 'html.parser')
                try:
                    details = soup.find_all("div", class_="bigSection")
                    details = details[0].find_all("span", class_="fieldValue")
                    agent['Email'] = details[0].text
                    # Some basic data validation. Check that the returned string is actually an email
                    if agent['Email'][0] == ':':
                        agent['Email'] = agent['Email'][1:]
                    if '@' not in agent['Email']:
                        agent['Email'] = "NOT FOUND"
                except(IndexError,TypeError):
                    agent['Email'] = "NOT FOUND"
            else:
                agent['Email'] = contactPage.status_code

        if i % 101 == 0:
            with open('BackupFile.json', 'w') as outfile:
                json.dump(jdata, outfile)
            if count != 0:
                print(str(count) + " new results saved to backup file\n...")
                print(str((i/len(jdata))*100) + '% Complete...')
                check.timeRemaining()
                check.collected()
                print('---\n---')
                count = 0

        if count > 0:
            with open(outpath, 'w') as outfile:
                try:
                    json.dump(jdata, outfile)
                except(KeyboardInterrupt):
                    json.dump(jdata, outfile)