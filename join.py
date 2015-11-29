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
    mr.emit_intermediate(key_id, record)



def reducer(key, list_of_values):

 counter=0
 length=len(list_of_values)
 values=[]
 result ={}
 for i in range(1,length):
    values+=list_of_values[0]#order
    values+=list_of_values[i]#i-th join
    result[counter]=values#temporarily store the full joined row
    values=[]
    mr.emit(result[counter])#print it and move to the next one
    counter+=1


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

