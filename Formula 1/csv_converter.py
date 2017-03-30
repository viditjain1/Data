import csv
import xml.etree.ElementTree as ET

def convert(year, race):

    year = str(year)
    race = str(race)

    file_xml = 'xmls/standings_' + year + '_' + race + '.xml'

    tree = ET.parse(file_xml)
    root = tree.getroot()

    file_csv = 'csvs/standings_' + year + '_' + race + '.csv'
    standing_data = open(file_csv, 'w')

    csvwriter = csv.writer(standing_data)

    count = 0
    standings_head = []
    for member in root.findall('driverstanding'):
        standings = []
        if count == 0:
            first_name = member.find('givenname').tag
            standings_head.append(first_name)
            last_name = member.find('familyname').tag
            standings_head.append(last_name)
            # position = member.get('position').tag
            standings_head.append('position')
            nationality = member.find('nationality').tag
            standings_head.append(nationality)
            constructor = member.find('constructor').tag
            standings_head.append(constructor)
            birth = member.find('dateofbirth').tag
            standings_head.append(birth)
            csvwriter.writerow(standings_head)
            count = count + 1
        first_name = member.find('givenname').text
        first_name = first_name.strip()
        standings.append(first_name)
        last_name = member.find('familyname').text
        last_name = last_name.strip()
        standings.append(last_name)
        position = member.get('position')
        standings.append(position)
        nationality = member.find('nationality').text
        nationality = nationality.strip()
        standings.append(nationality)
        constructor = member.find('constructor').get('constructorid')
        standings.append(constructor)
        birth = member.find('dateofbirth').text
        birth = birth.strip()
        standings.append(birth)
        csvwriter.writerow(standings)

    standing_data.close()