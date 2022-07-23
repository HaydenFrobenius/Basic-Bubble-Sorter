arrayinput = input()
array = arrayinput.split(',')
temp = 0

newarray = array

arraylength = len(array)

for i in range(0,arraylength):
    array[i] = int(array[i])

for x in range(0,arraylength-1):
    for y in range(0,arraylength-1):
        if(array[y] > array[y+1]):
            temp = array[y+1]
            newarray[y+1] = newarray[y]
            newarray[y] = temp
print(str(newarray))
