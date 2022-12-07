#!/usr/bin/python3

"""
ADIF 2 XML

Get the lib adif_io from pypi
pip3 install adif-io

"""
import sys
from xml.dom.minidom import parseString
import argparse

try:
    from dicttoxml import dicttoxml
except ModuleNotFoundError:
    print("Library dictoxml Not Found. You can get it with: pip3 install dictoxml")
    sys.exit()

try:
    import adif_io
except ModuleNotFoundError:
    print("Library adif_io Not Found. You can get it with: pip3 install adif-io")
    sys.exit()

parser = argparse.ArgumentParser(
    prog="adif2xml.py", description="Converts an ADIF file to XML"
)

parser.add_argument("filename")
parser.add_argument(
    "-o", "--output", default="QSO.xml", type=argparse.FileType("w", encoding="UTF-8")
)

args = parser.parse_args()

if not args.filename:
    print("No filename given. Please provide a filename.")
    sys.exit()

qsos_raw, adif_header = adif_io.read_from_file(args.filename)
Qs = {}


for q, contact in enumerate(qsos_raw):
    Qs[f"QSO_{q}"] = contact

XML_TO_OUTPUT = dicttoxml(Qs, attr_type=False, custom_root="CONTACTS")

args.output.write(parseString(XML_TO_OUTPUT).toprettyxml())
