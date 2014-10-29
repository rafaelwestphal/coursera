f = open('IntegerArray.txt', 'r')
i = 0;
integer_array = []
for line in f:
  # print line + " : " + str(i)
  integer_array.insert(i, int(line))
  i+=1
print"Counting inversions of a list with size " + str(len(integer_array))



