from lxml import etree
import sys
class DTD_XML_Validator:
 def __init__(self)->None:
  self
 def validate(self,path_dtd:str,path_xml:str)->bool:
  self
  try:
   dtd=etree.DTD(path_dtd)
   xsd=etree.parse(path_xml)
   o=dtd.validate(xsd)
   if dtd.error_log:
    print(dtd.error_log)
   return o
  except Exception as e:
   print(e)
   return False
def main()->int:
 etree.XMLParser(load_dtd=True,dtd_validation=True,resolve_entities=True)
 validator=DTD_XML_Validator()
 a=validator.validate(sys.argv[1],sys.argv[2])
 if not a:
  return 1
 return 0
aa=main()
print(f"🏁 exit {aa}")
if not aa:
 oo='E'
 while True:
  oo+=oo+oo