numlist = list()
while True:
    inp = input('Enter some digits: ') # user inputs random digits
    if inp == 'done' : break # break statement terminates the loop here on
    v = float(inp) # changes digits into float values
    numlist.append(v) # adds value in variable v to the empty list

average = sum(numlist) / len(numlist) # divides the sum of the numlist to
                                      # the length of numbers in list to find average.
print('Average:', average)
