"""
ADIF 2 XML

Get the lib adif_io from pypi
pip3 install adif-io

"""

from xml.dom.minidom import parseString
from dicttoxml import dicttoxml
import adif_io

qsos_raw, adif_header = adif_io.read_from_file("QSO.adi")
Qs = {}


for q, contact in enumerate(qsos_raw):
    Qs[f"QSO_{q}"] = contact

XML_TO_OUTPUT = dicttoxml(Qs, attr_type=False, custom_root="CONTACTS")

with open("QSO.xml", "w", encoding="UTF-8") as xmlfile:
    xmlfile.write(parseString(XML_TO_OUTPUT).toprettyxml())
