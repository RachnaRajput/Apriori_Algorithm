import json
import sys

# with open(sys.argv[1]) as json_file: #Accessing the json data.
#     json_data = json.load(json_file)
#     print(type(json_data))
class Rachna_Rajput_apriori:
    def apriori(self,json_data, value):
        array = json_data
        thres = 0.3 * len(array)
        # print thres
        phase1_list = []

        res = [];
        for item in array:
            res = list(set(res)| set(item))

        mylist = []
        d = [[res[elem]] for elem in xrange(len(res))]
        if value == True:
            print "C1:",d

        dict = {}
        for arr in array:
            for subarr in arr:
                if subarr not in dict:
                    dict[subarr] = 1
                else:
                    count = dict[subarr]
                    count = count + 1
                    dict[subarr] = count

        for item in d:
            for subitem in item:
                count = dict[subitem]
                if count >= thres:
                    mylist.append(subitem)

        l1 = [[res[elem]] for elem in xrange(len(mylist))]
        if value == True:
            print "L1:",l1
        else:
            for item in l1:
                phase1_list.append(item)

        c2 = []
        dict = {}
        k = 1

        for i in range(1,len(l1)+1):
            for j in range(i+1,len(l1)+1):
                mylist = []
                mylist.append(i)
                mylist.append(j)
                dict[k] = 1
                k = k + 1
                c2.append(mylist)
        if value == True:
            print "C2:",c2

        k = 1
        for elem in c2:
            count = 0
            for arr in array:
                if (set(elem)<=set(arr)):
                    # print elem, " : ", arr
                    count = count + 1
                    dict[k] = count
            k = k + 1

        l2 = []

        for i in range(1, len(dict)+1):
            if dict[i] >= thres:
               l2.append(c2[i-1])

        if value == True:
            print "L2: ",l2
        else:
            for item in l2:
                phase1_list.append(item)

        y = 3
        while(len(l2)!=0):
            c3 = []
            for i in range(0,len(l2)/2+1):
                for j in range(i+1,len(l2)/2+1):
                    if (l2[i][0]==l2[j][0]):
                        mylist=[]
                        for x in range(1,len(l2[i])):
                            mylist.append(l2[i][x])
                            mylist.append(l2[j][x])
                        mylist.sort()
                        for item in l2:
                            if set(mylist) == set(item):
                                mylist.append(l2[i][0])
                                mylist.sort()
                                myset = set(mylist)
                                mylist = list(myset)
                                c3.append(mylist)
            s = "C"
            s += str(y)
            s += ": "

            if value == True:
                print s,c3

            k = 1
            dict = {}
            for elem in c3:
                count = 0
                for arr in array:
                    if (set(elem)<=set(arr)):
                        count = count + 1
                        dict[k] = count
                k = k + 1

            l3 = []

            for i in range(1, len(dict)+1):
                if dict[i] >= thres:
                   l3.append(c3[i-1])

            s = "L"
            s += str(y)
            s += ": "
            if value == True:
                print s,l3
            else:
                for item in l3:
                    phase1_list.append(item)
            l2 = l3
            y = y + 1
        return phase1_list

    if __name__ == '__main__':
        with open(sys.argv[1]) as json_file: #Accessing the json data.
            json_data = json.load(json_file)
        checker = True
        apriori(json_data,checker)



