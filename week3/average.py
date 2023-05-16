stop = True
list_to_avg = []
while stop:
    new_number = int(input("Please select a positive number, use negative numbers to interrupt this"))
    if new_number < 0:
        stop = False
    else:
        list_to_avg.append(new_number)
sum_of_numbers = 0
for el in list_to_avg:
    sum_of_numbers += el
print(sum_of_numbers/len(list_to_avg))
