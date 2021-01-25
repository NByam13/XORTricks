# Some tricks using XOR to solve some standard coding interview questions

# Full credits to: https://florian.github.io/xor-trick/



# Swap two numbers without introducing a third number to help:
# usual way
print("\n\n~~Using addition and subtraction to swap~~")

x = 5
y = 10

print("starting values:")
print("x=" + str(x) + ", y=" + str(y) +"\n")

x = x+y # x = 15
y = x-y # y = 15 - 10 = 5
x = x-y # x = 15 - 5 = 10

print("After Swapping:")
print("x=" + str(x) + ", y=" + str(y) +"\n")

# x = 10
# y = 5

# now with XOR

x = 5
y = 10

print("~~Using XOR to swap~~")

print("starting values:")
print("x=" + str(x) + ", y=" + str(y) +"\n")

x ^= y # x = x^y, y = y
y ^= x # x = x^y, y = y^y^x = x
x ^= y # x = x^x^y = y, y = x

print("After Swapping:")
print("x=" + str(x) + ", y=" + str(y) +"\n")
# x = 10
# y = 5

# There is an array from range 1 to N, there is a number missing from this range, find out what it is.
# We will use XOR to find this number.

def find_missing_num(arr, N):
	
	result = 0

	#XOR is a bitwise comparison, so we will it to test against each element of a range from 1 to N.
	for num in range(1, N+1): 	#N is included 
		result ^= num 			# this will end up looking like result = 1^2^3^4 ...^N-1^N

	# now we want to compare our result against the given array that is missing a number.
	# every number will be cancelled out that is duplicated, leaving only the missing number.

	for num in arr:
		result ^= num 			# This will look like 1^1^2^2^3^3^x^5^5...^N-1^N-1^N^N Everything will cancel out except for 'x' our missing number

	return result

print("\n\n~~Finding a missing number in a range using XOR~~")
maxNum = input("Please specify a max number: ")
maxNum = int(maxNum)

tmp = range(1, maxNum+1)

# just going to pick out some number from the array
numToRemove = maxNum/2 + 1
numToRemove = int(numToRemove)

arr = [] # make an empty list

for num in tmp:
	if num != numToRemove:
		arr.append(num) 			# fill the array with all the numbers except one.
	else:
		continue

missing = find_missing_num(arr, maxNum)

print("The missing number is: " + str(missing))