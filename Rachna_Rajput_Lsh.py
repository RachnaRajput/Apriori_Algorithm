import json
import sys

def lsh_algo(self,json_data):
 array = json_data
 print array
 print ":::::::::::::"

if __name__ == '__main__':
    with open(sys.argv[1]) as json_file: #Accessing the json data.
      json_data = json.load(json_file)
    lsh_algo(json_data)