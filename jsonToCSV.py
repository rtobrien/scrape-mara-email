import json, csv

def write(outputTitle, source='agentdata_test1.json'):
    with open(source, 'r') as file:
        jdata = json.loads(file.read())

    output = open(outputTitle, 'a')
    writer = csv.writer(output, delimiter='|')

    #klist = jdata[0].keys()
    klist = ['Salutation',
        'FirstName',
        'SecondName',
        'FamilyName',
        'FullName',
        'GivenName',
        'MARN',
        'Email',
        'Business',
        'Relationship',
        'Business',
        'Type',
        'Entity',
        'Name',
        'Business',
        'Name',
        'ABN',
        'Business',
        'Country',
        'Bus_AddressLine1',
        'Bus_AddressLine2',
        'Bus_AddressLine3',
        'Bus_State',
        'Bus_OtherState',
        'Bus_Suburb',
        'Bus_OtherSuburb',
        'Bus_PostCode',
        'Bus_OtherPostCode',
        'Bus_Latitude',
        'Bus_Longitude',
        'Bus_P_Suburb',
        'Bus_Ph_CountryCode',
        'Bus_Ph_AreaCode',
        'Bus_Ph_Number',
        'Bus_Ph_FullNumber',
        'Bus_WebsiteUrl']
    writer.writerow(klist)

    for i in jdata:
        writer.writerow(
            i['Salutation'],
            i['FirstName'],
            i['SecondName'],
            i['FamilyName'],
            i['FullName'],
            i['GivenName'],
            i['MARN'],
            i['Email'],
            i['Business'],
            i['Relationship'],
            i['Business'],
            i['Type'],
            i['Entity'],
            i['Name'],
            i['Business'],
            i['Name'],
            i['ABN'],
            i['Business'],
            i['Country'],
            i['Bus_AddressLine1'],
            i['Bus_AddressLine2'],
            i['Bus_AddressLine3'],
            i['Bus_State'],
            i['Bus_OtherState'],
            i['Bus_Suburb'],
            i['Bus_OtherSuburb'],
            i['Bus_PostCode'],
            i['Bus_OtherPostCode'],
            i['Bus_Latitude'],
            i['Bus_Longitude'],
            i['Bus_P_Suburb'],
            i['Bus_Ph_CountryCode'],
            i['Bus_Ph_AreaCode'],
            i['Bus_Ph_Number'],
            i['Bus_Ph_FullNumber'],
            i['Bus_WebsiteUrl']
        )