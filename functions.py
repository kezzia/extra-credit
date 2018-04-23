'''
1) Mean
2) Variance
3) Minimum and Maximum
4) Median
5) Mode
'''

def Mean(N):
# put numbers into an array called N
# get length of N
# for each number in N:
# 	add number to sum
# average = sum/(length of N)
# print average
    sum = 0
    average = 0
    list_length = len(N)
    for number in N:
        sum = sum + number
    average = sum / list_length
    print("The mean of N is " + str(average) + "\n")

def SampleMean(N):
# put numbers into an array called N
# get length of N
# for each number in N:
# 	add number to sum
# average = sum/(length of N)
# print average
    sum = 0
    average = 0
    list_length = len(N) - 1
    for number in N:
        sum = sum + number
    average = sum / list_length
    print("The sample mean of N is " + str(average) + "\n")

def Variance(N):
# put numbers into an array called N
# get length of N
# for each number in N:
# 	add number to sum
# let average = sum/(length of N)
# reset sum
# for each number in N:
# find (x - average)2
# add to (x - average)2 to sum
# let variance = sum/(length of N)
# print variance
    sum = 0
    average = 0
    variance = 0
    list_length = len(N)
    for number in N:
        sum = sum + number
    average = sum / list_length
    sum = 0

    for number in N:
        sum = sum + (number - average)**2
    variance = sum / list_length
    print("The variance of N is " + str(variance) + "\n")

def SampleVariance(N):
# put numbers into an array called N
# get length of N
# for each number in N:
# 	add number to sum
# let average = sum/(length of N)
# reset sum
# for each number in N:
# find (x - average)2
# add to (x - average)2 to sum
# let variance = sum/(length of N)
# print variance
    sum = 0
    average = 0
    variance = 0
    list_length = len(N) - 1
    for number in N:
        sum = sum + number
    average = sum / list_length
    sum = 0

    for number in N:
        sum = sum + (number - average)**2
    variance = sum / list_length
    print("The sample variance of N is " + str(variance) + "\n")


def MinMaxRange(N):
# put numbers into an array called N
# set minimum to 0
# set maximum to 0
# for each number in N:
# 	if number > current maximum:
# let current maximum = number
# if number < current minimum:
# 	let current minimum = number
# let range = current minimum, current maximum
# print minimum
# print maximum
# print range
    N.sort()
    min = N[0]
    max = N[-1]
    range = "(" + str(min) + ", " + str(max) + ")\n"
    print("The min of N is " + str(min))
    print("The max of N is " + str(max))
    print("The range of N is " + range)


def Median(N):
# put numbers into an array called N
# get length of N as a float
# let middle index = (length of N)/2
# sort N in ascending order
# if (length of N) is odd:
# 	let median = N[middle index]
# if (length of N) is even:
# 	let middle index 1 = middle index - 0.5 (as an int)
# 	let middle index 2 = middle index + 0.5 (as an int)
# 	let median = (middle index 1 + middle index 2)/2
# print median
    list_length = float(len(N))
    mid = list_length/2
    mid1 = 0
    mid2 = 0
    median = 0
    N.sort()
    if list_length % 2 == 1:
        median = N[mid]
    else:
        mid1 = int(mid - 0.5)
        mid2 = int(mid + 0.5)
        median = (N[mid1] + N[mid2]) / 2
    print("The median of N is " + str(median) + "\n")


def Mode(N):
# put numbers into an array called N
# sort N in ascending order
# let current frequency = 0
# let highest frequency = 0
# let current number be the first number in the array
# let mode = 0
# for each number in N:
# 	if number == current number:
# increment current frequency
# if number != current number:
# let current number = number
# Let current frequency = 1
# if current frequency > highest frequency:
# 	let highest frequency = current frequency
# 	let mode = current number
# print mode
    modes = []
    N.sort()
    current_frequency = 0
    highest_frequency =  0
    mode = 0
    mode_frequency = 0
    current_number = N[0]
    for number in N:
        if number == current_number:
            current_frequency = current_frequency + 1
        else:
            current_number = number
            current_frequency = 1
        if current_frequency > highest_frequency:
            highest_frequency = current_frequency
            mode = current_number
    mode_frequency = highest_frequency
    modes.append(mode)
    while mode in N:
        N.remove(mode)

    for i in range(len(N)):
        current_frequency = 0
        mode = 0
        current_number = N[0]
        for number in N:
            if number == current_number:
                current_frequency = current_frequency + 1
            else:
                current_number = number
                current_frequency = 1
            if current_frequency == mode_frequency:
                mode = current_number
                modes.append(mode)
                while mode in N:
                    N.remove(mode)

    modes.sort()
    print("Modes: ")
    print(modes)


N = [1.09, 1.92, 2.31, 1.79, 2.28, 1.74, 1.47, 1.97, .95, 1.24, 1.58, 2.03,
1.70, 2.17, 2.55, 2.11, 1.86, 1.90, 1.68, 1.51, 1.64, 0.72, 1.69, 1.85, 1.82,
1.79, 2.46, 1.88, 2.08, 1.67, 1.37, 1.93, 1.40, 1.64, 2.09, 1.75, 1.63, 2.37,
1.75, 1.63]


Mean(N)
SampleMean(N)
Variance(N)
SampleVariance(N)
MinMaxRange(N)
Median(N)
Mode(N)
