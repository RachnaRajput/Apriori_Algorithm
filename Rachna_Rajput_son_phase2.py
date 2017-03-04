import json
import sys
import MapReduce

mr = MapReduce.MapReduce()
dict = {}

class Rachna_Rajput_son_phase2:
    def mapper(record):
        f = open(sys.argv[1])
        mylist = []
        # print record

        for line in f:
            chunkdata = json.loads(line)
            # print chunkdata     #chunks_1
            # for item in record:
            k = 0
            count = 0
            length = len(chunkdata)
            # print length
            for chunkline in chunkdata:
                # print chunkline
                if set(chunkline) >= set(record):
                    count = count + 1
            # mylist = []
            # mylist.append(record)
            mylist.append(count)
            mylist.append(length)
            recordtuple = tuple(record)
            # recordstr = str(record)
            k = k + 1
            # basket_length=sum([pair[1] for pair in chunkdata])
            # if recordstr in dict.keys():
            #     somelist = []
            #     somelist = dict[recordstr]
            #     for item in somelist:
            #         mylist.append(item)
            #     dict[recordstr] = mylist
            #
            # else:
            dict[recordtuple] = mylist
        mr.emit_intermediate(recordtuple,mylist)

    def reducer(key, value):
        # print len(value)
        # print len(value[0])
        # print key
        # print value
        x = 0
        count = 0
        mylist = []
        i = 0
        while(i < len(value[0])):
            # for j in range(0,len(value[i])):
            count = count + value[0][i]
            i = i + 2
        somelist = []
        # for d in key:
        #     if d.isdigit():
        #         somelist.append(int(d))
        mylist.append(key)
        # if count > float(37*30)/100:
        mylist.append(count)
        # print mylist
        mr.emit(mylist)

    if __name__ == '__main__':
        inputdata = open(sys.argv[2])
        output = mr.execute(inputdata, mapper,reducer)