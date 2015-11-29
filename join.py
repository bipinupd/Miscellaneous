import MapReduce
import sys

"""
Inverted index based in Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    name = record[0]
    key_id = record[1]
    output = ""
    for rec in record:
	output = output + rec + ","
    output = output[0:-1]
    mr.emit_intermediate(key_id, output)
	
	

def reducer(key, list_of_values):
    mr.emit((key, list_of_values))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
