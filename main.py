## -*- coding: utf-8 -*-
import sys
import ijson
import MySQLdb
from ConfigParser import SafeConfigParser

reload(sys)
sys.setdefaultencoding('utf-8')

parser = SafeConfigParser()
parser.read('config.ini')

conn = MySQLdb.connect(host=parser.get('MySQL', 'host'), user=parser.get('MySQL', 'username'), passwd=parser.get('MySQL', 'password'), db=parser.get('MySQL', 'db'))
x = conn.cursor()

f = open(parser.get('GeoFile', 'filename'))
objects = ijson.items(f, 'item')
for obj in objects:
  loong, lat = obj['adgangsadresse']['adgangspunkt']['koordinater']
  if obj['etage'] is None and obj[u'dør'] is None:
    x.execute("""INSERT INTO geodata VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",(obj['adgangsadresse']['vejstykke']['navn'],obj['adgangsadresse']['husnr'],None,None,obj['adgangsadresse']['postnummer']['nr'],obj['adgangsadresse']['postnummer']['navn'], loong, lat))
    conn.commit()
  elif obj['etage'] is not None and obj[u'dør'] is None:
    x.execute("""INSERT INTO geodata VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",(obj['adgangsadresse']['vejstykke']['navn'],obj['adgangsadresse']['husnr'],None,obj['etage'],obj['adgangsadresse']['postnummer']['nr'],obj['adgangsadresse']['postnummer']['navn'], loong, lat))
    conn.commit()
  elif obj['etage'] is None and obj[u'dør'] is not None:
    x.execute("""INSERT INTO geodata VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",(obj['adgangsadresse']['vejstykke']['navn'],obj['adgangsadresse']['husnr'],obj[u'dør'],None,obj['adgangsadresse']['postnummer']['nr'],obj['adgangsadresse']['postnummer']['navn'], loong, lat))
    conn.commit()
  elif obj['etage'] is not None and obj[u'dør'] is not None:
    x.execute("""INSERT INTO geodata VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",(obj['adgangsadresse']['vejstykke']['navn'],obj['adgangsadresse']['husnr'],obj[u'dør'],obj['etage'],obj['adgangsadresse']['postnummer']['nr'],obj['adgangsadresse']['postnummer']['navn'], loong, lat))
    conn.commit()
