def merge_sorted_lists(list1, list2):
    remove = []
    for element in list2:
        for i in range(len(list1)):
            if element < list1[i]:
                list1.insert(i, element)
                remove.append(element)
                break
    for element in remove:
        list2.remove(element)
    for element in list2:
        list1.append(element)
    return list1

a = [0,2,4,6]
b = [1,3,3,3,5,7,9]

print(merge_sorted_lists(a,b))