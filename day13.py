# from aocd import data, get_data

#load data
# data = get_data(day=13, year=2022)
# data = data.split('\n')


test = '[1,1,3,1,1]\n[1,1,5,1,1]\n\n[[1],[2,3,4]]\n[[1],4]\n\n[9]\n[[8,7,6]]\n\n[[4,4],4,4]\n[[4,4],4,4,4]\n\n[7,7,7,7]\n[7,7,7]\n\n[]\n[3]\n\n[[[]]]\n[[]]\n\n[1,[2,[3,[4,[5,6,7]]]],8,9]\n[1,[2,[3,[4,[5,6,0]]]],8,9]'

test = test.split('\n\n')

#sum the indices of the pairs that are already in the right order...

#a packets is in the right order if...
# for each value within a packet.... *values are either ints or lists of ints...each value is csv...
# left packet, the first one, is smaller than the right side...
# cases:
#   int and int, simple comparision
#   2 lists of ints, compare every int within the list 
#   one int and a list, convert int to list of itself, eg 1 -> [1] than compare as 2 lists...
#   right side must have >= items as the left...

#continue checking input when....
#ints are equal
#lists are same length + no comparision makes a decision about order...




packets_list = []
for packets in test:
    l, r = packets.split('\n')
    packets_list.append((r,l))


def validVal(val, val_list):
    
    if val.isdigit():
        return val

    elif val == '' or val == '[]':
        return []

    elif val == '[[]]':
        return [[]]
    
    elif '[' in val and ']' in val:
        val = val.replace('[', '')
        val = val.replace(']', '')
        val = [val]
        return val
    
    elif '[' in val:
        val = val[1:]
        val_arr = [val]
        while val_list:
            ch = val_list.pop(0)
            if ']' in ch:
                ch = ch[:-1]
                val_arr.append(ch)
                break
            val_arr.append(ch)
        return val_arr

    


def compareTwoLists(rv, lv):


    if type(rv) != type([1,2,3]):
        rv = rv.replace('[', '')
        rv = rv.replace(']', '')
        rv = rv.split()
    if type(lv) != type([1,2,3]):
        lv = lv.replace('[', '')
        lv = lv.replace(']', '')
        lv = lv.split()

    while lv and rv:
        curr_lv, curr_rv = lv.pop(0), rv.pop(0)

        if int(curr_rv) < int(curr_lv):
            return False


def processPackets(right, left):
    right, left = right[1:len(right)-1], left[1:len(left)-1]
    right_vals, left_vals = right.split(','), left.split(',')
    print(left_vals, right_vals, 'packets...')

    while right_vals and left_vals:
        rv, lv = right_vals.pop(0), left_vals.pop(0)
        print(lv, rv, 'vals to be compared...')
        
        lv, rv = validVal(lv, left_vals), validVal(rv, right_vals)
        print(lv, rv, 'post validation...')

        if type(lv) is str and type(rv) is str:
            if int(lv) > int(rv):
                return False

        elif type(lv) is list and type(rv) is list:
            while lv and rv:
                l, r = lv.pop(0), rv.pop(0)
                if int(l) > int(r):
                    return False
        
        elif (type(lv) is list and type(rv) is str) or (type(rv) is list and type(lv) is str):
            if type(rv) is str:
                rv = [rv]
            else:
                lv = [lv]
        
            while lv and rv:
                l, r = lv.pop(0), rv.pop(0)
                if int(l) > int(r):
                    return False
            

        
            #breaks down on the largest most nested edge case...


#this should prolly just use some data structure or something...

        #3 cases now...
   

    #     elif '[' in rv or '[' in lv:
    #         if '[' in rv and '[' in lv:
    #             rv = rv[1:]
    #             rv = rv.split()
    #             while True:
    #                 el = right_vals.pop(0)
    #                 if ']' in el:
    #                     el = el[:-1]
    #                     rv.append(el)
    #                     break
    #                 rv.append(el)

    #             lv = lv[1:]
    #             lv = lv.split()
    #             while True:
    #                 el = left_vals.pop(0)
    #                 if ']' in el:
    #                     el = el[:-1]
    #                     lv.append(el)
    #                     break
    #                 lv.append(el)
                 
    #         elif '[' in lv:
    #             #right needs to be converted...
    #             rv = rv.split()
                
    #             lv = lv[1:]
    #             lv = lv.split()
    #             while True:
    #                 el = left_vals.pop(0)
    #                 if ']' in el:
    #                     el = el[:-1]
    #                     lv.append(el)
    #                     break
    #                 lv.append(el)

    #         else:
    #             lv = lv.split()
                
    #             rv = rv[1:]
    #             rv = rv.split()
    #             while True:
    #                 el = right_vals.pop(0)
    #                 if ']' in el:
    #                     el = el[:-1]
    #                     rv.append(el)
    #                     break
    #                 rv.append(el)

    #         if compareTwoLists(rv, lv) == False:
    #             return False

            
    #     else:
    #         #two ints comparision
    #         if rv and lv:
    #             if int(rv) < int(lv):
    #                 return False
    #         elif lv and not rv:
    #             return False


    # if left_vals and not right_vals:
    #     return False

    return True
            



index, indexSum = 1, 0
for r, l in packets_list:
    if processPackets(r, l):
        indexSum += index
    
    index += 1



