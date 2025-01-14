from docxtpl import DocxTemplate
from datetime import date 
import json
import sys, getopt

def main(argv):
   templatefile = ''
   outputfile = ''
   contextfile = ''
   try:
      opts, args = getopt.getopt(argv,"hc:o:t:",["help", "cfile=","ofile=","tfile="])
   except getopt.GetoptError:
      print ('generate.py -c <contextfile> -t <templatefile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('generate.py -c <contextfile> -t <templatefile> -o <outputfile>')
         sys.exit()
      elif opt in ("-t", "--tfile"):
         templatefile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
      elif opt in ("-c", "--cfile"):
         contextfile = arg
   print ('Template file is "', templatefile)
   print ('Output file is "', outputfile)
   print ('Context file is "', contextfile)

   doc = DocxTemplate(templatefile)
   with open(contextfile, 'r') as json_data:
      context = json.load(json_data)
      json_data.close()
   if context["docdate"] == "":
      formatted_date = date.today().strftime('%d %B %Y')
      context["docdate"] = formatted_date 
   doc.render(context)
   doc.save(outputfile)

if __name__ == "__main__":
   main(sys.argv[1:])
