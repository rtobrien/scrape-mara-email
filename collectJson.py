import requests, json

URL='https://www.mara.gov.au/api/agentsearch?DelimitedStartWithLetterFilter%5BFieldName%5D=Name.FamilyName&DelimitedStartWithLetterFilter%5BLetterString%5D=&DelimitedStartWithLetterFilter%5BLabel%5D=Show+All&DelimitedStartWithLetterFilter%5BIsSelected%5D=false&DelimitedStartWithLetterFilter%5BContainsData%5D=true&Keyword=&Location=&BusinessName=&IsNoFee=&IsPractitioner=&AgentFamilyName=&AgentGivenName=&AgentName=&AgentMARN=&SortInfo%5BSortField%5D=&SortInfo%5BIsAscending%5D=false&PagingInfo%5BPageIndex%5D=0&PagingInfo%5BPageSize%5D='

def collectFromSite(filename='result_all.json'):
    result = requests.get(URL + str(1)).text
    jdata = json.loads(result)
    with open('result_0.json', 'w') as file:
        file.write(result)
    count = (jdata.get('Count'))
    print(count)

    result = requests.get(URL + str(count)).text
    with open(filename, 'w') as file:
        file.write(result)