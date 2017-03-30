import bs4 as bs
import urllib.request as urllib
import csv
import xml.etree.ElementTree as ET
from pathlib import Path

def standings_xml(year, race):

    year = str(year)
    race = str(race)

    url = 'http://ergast.com/api/f1/' + year +  '/' + race + '/driverStandings'
    # print(url)
    source = urllib.urlopen(url)
    soup = bs.BeautifulSoup(source, 'lxml')

    if (len(str(soup)) < 1000):
        return False

    for match in soup.findAll('html'):
        match.replaceWithChildren()

    for match in soup.findAll('body'):
        match.replaceWithChildren()

    for match in soup.findAll('driver'):
        match.replaceWithChildren()

    for match in soup.findAll('mrdata'):
        match.replaceWithChildren()

    for match in soup.findAll('standingstable'):
        match.replaceWithChildren()

    soup = soup.prettify()

    file_xml = 'xmls/standings_' + year + '_' + race + '.xml'
    #file_check = Path(file_xml)
    #if file.is_file():
    #
    file = open(file_xml, 'w')
    file.write(soup)
    file.close()

    return True


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
            #first_name = member.find('givenname').tag
            standings_head.append('name')
            #last_name = member.find('familyname').tag
            #standings_head.append(last_name)
            # position = member.get('position').tag
            standings_head.append('position_' + race)
            #points = member.get('points').tag
            standings_head.append('points_' + race)
            # nationality = member.find('nationality').tag
            standings_head.append('nationality')
            #constructor = member.find('constructor').tag
            standings_head.append('Constructor')
            #birth = member.find('dateofbirth').tag
            standings_head.append('age')
            csvwriter.writerow(standings_head)
            count = count + 1
        first_name = member.find('givenname').text
        first_name = first_name.strip()
        #standings.append(first_name)
        last_name = member.find('familyname').text
        last_name = last_name.strip()
        standings.append(first_name + '_' + last_name)
        position = member.get('position')
        standings.append(position)
        points = member.get('points')
        standings.append(points)
        nationality = member.find('nationality').text
        nationality = nationality.strip()
        standings.append(nationality)
        constructor = member.find('constructor').get('constructorid')
        standings.append(constructor)
        age = member.find('dateofbirth').text
        age = age.strip()
        age = age[:4]
        age = str(int(year) - int(age))
        standings.append(age)
        csvwriter.writerow(standings)

    standing_data.close()