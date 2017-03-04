import json
import sys
import MapReduce
import Rachna_Rajput_apriori
# import Rachna_Rajput_son_phase2
import io

mr = MapReduce.MapReduce()
ap = Rachna_Rajput_apriori.Rachna_Rajput_apriori()
# ph = Rachna_Rajput_son_phase2.Rachna_Rajput_son_phase2()
mylist = []
dict = {'1':[]}

def mapper(record):
    mylist = []
    mylist = ap.apriori(record,False)
    # print mylist,"@@@@@@@@@@@@@@@@@@@@"
    mr.emit_intermediate(1,mylist)

def uniq(lst):
    last = object()
    for item in lst:
        if item == last:
            continue
        yield item
        last = item

def reducer(key, value):
    mylist = []
    for item in value:
        for some in item:
            mylist.append(some)
            # print some
    output = list(uniq(sorted(mylist, reverse=False)))
    for item in output:
        # print item
        mr.emit(item)



if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    output = mr.execute(inputdata, mapper,reducer)