def pairSortUsingStability(l):
    list_x = []
    list_y = []
    list_first_sort = []
    final_list = []
    for i in l:
        list_x.append(i[0])
    list_x.sort()
    for i in range(len(list_x)):
        for j in l:
            if j[0] == list_x[i]:
                list_first_sort.append(j)
                l.remove(j)
                break

    for i in list_first_sort:
        list_y.append(i[1])
    list_y.sort()

    for i in range(len(list_y)):
        for j in list_first_sort:
            if j[1] == list_y[i]:
                final_list.append(j)
                list_first_sort.remove(j)
                break


    return final_list
        


x = [(100,200),(3,4),(2,5),(6,7),(2,6),(6,7),(6,8),(6,8)]
#print(pairSortUsingStability(x))


def pairSortFast(l):
    list_sum = []
    for i in l:
        x = i[0] + i[1]
        list_sum.append(x)

    maxValue = max(list_sum)
    listSort = [0] * (maxValue + 1)
    list_final = [0]*(len(l))

    for i in list_sum:
        listSort[i] += 1

    k = 0
    for i in range(0, len(l)):
        while listSort[k] == 0:
            k += 1
        list_final[i] = k
        listSort[k] -= 1

    list_output = []
    for i in list_final:
        for j in l:
            if i == j[0] + j[1]:
                list_output.append(j)
                l.remove(j)
                break

    return list_output
#print(pairSortFast(x))

def pairSortFast1(l):
    if len(l) != 0 :
        maxValue = 0
        list_sum = []
        final_out = [0]*len(l)
        for i in l:
            h = i[0] + i[1]
            list_sum.append(h)
        maxValue = max(list_sum)

        list_final = [[] for i in range (maxValue + 1)]

        for i in l:
            sum = i[0] + i[1]
            list_final[sum].append(i) 
        print(list_final)
        print(len(list_final))
        k = 0
        for i in range(0, len(l)):
            while len(list_final[k]) == 0:
                k = k + 1
            final_out[i] = list_final[k][0]
            list_final[k].remove(list_final[k][0])
        return final_out



x = [(100,200),(0,8),(2,5),(0,4),(6,7),(2,6),(6,7),(6,8),(6,8)]

for i in x:
    print(i)

print(pairSortFast1(x))









