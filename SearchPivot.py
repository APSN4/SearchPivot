array = [1,3,4,2,2]
Debug = False

def SearchPivotIndex():
	for pivot_number in range(len(array)):
		if pivot_number != 0:
			later_sum = 0
			for later_check in range(0, pivot_number):
				later_sum += array[later_check]

			if Debug == True: print("later:" + str(later_sum))
			after_sum = 0
			for after_check in range(len(array) - 1, pivot_number, -1):
				after_sum += array[after_check]

			if Debug == True: print("after:" + str(after_sum))
			if later_sum == after_sum: return pivot_number

print(SearchPivotIndex())