##!/usr/bin/python

# locate
#
# An IP geolocator script by
# hardwyrd 
# GPLv3
#
# Don't be a dick.
#
# This IP geolocator script uses IPInfoDB (http://ipinfodb.com/) to locate the approximate
# geographical location of an IP/Host.
#
# This tool requires an API key from IPInfoDB in order to work. IPInfoDB locks onto the
# originating host IP address that performs the query (which may not work for most people).

import re, sys, argparse, urllib2

apikey = '269c040156527d934ea5fc8fc44ff3c8ec00f9889d27938201ba06070f8fef93'

parser = argparse.ArgumentParser(description='Geolocate an IP using IPInfoDB API.')
parser.add_argument('-i', '--ip', help='IP Address to gelocate.')
parser.add_argument('-q', '--query', help='Indicate the query precise-type: "city", "country" .')

args = parser.parse_args()

ipaddress = args.ip

if args.query == 'country':
    querytype = 'ip-country'
else:
    querytype = 'ip-city'

queryurl = 'http://api.ipinfodb.com/v3/' + querytype + '/?key=' + apikey + '&ip=' + ipaddress

ipinfo = urllib2.urlopen(queryurl).read()
details = ipinfo.split(';')
ip = {}

if querytype == "ip-country":
    ip['Status'] = details[0]
    ip['IP'] = details[2]
    ip['Country'] = details[4]
    ip['Suffix'] = details[3]
    
    print 'Query Status: %s' % ip['Status']
    print 'IP Address: %s' % ip['IP']
    print 'Country: %s' % ip['Country']
    print 'TLD Suffix: %s' % ip['Suffix']
else:
    ip['Status'] = details[0]
    ip['IP'] = details[2]
    ip['Country'] = details[4]
    ip['Suffix'] = details[3]
    ip['City'] = details[6]
    ip['Province'] = details[5]
    ip['Latitude'] = details[8]
    ip['Longitude'] = details[9]
    ip['UTC'] = details[10]
    
    print(f"Query Status: {ip['Status']}")
    print(f"IP Address: {ip['IP']}")
    print(f"Country: {ip['Country']}")
    print(f"TLD Suffix: {ip['Suffix']}")
    print(f"Location Details: {ip['City']} of {ip['Province']} Province, {ip['Country']}")
    print(f"Latitude: {ip['Latitude']}, Longitude: {ip['Longitude']}")
    print(f"UTC/Timezone: {ip['UTC']}")


