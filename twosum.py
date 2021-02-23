def twosum(list_of_numbers,target):
	for first_loopig_element in range(len(list_of_numbers)):
		for second_looping_element in range(first_loopig_element+1,len(list_of_numbers)):
			if list_of_numbers[first_loopig_element] + list_of_numbers[second_looping_element] == target:
				print("got it the index numbers are {} and {}".format(first_loopig_element,second_looping_element))
				return(first_loopig_element,second_looping_element)				
print(twosum([-1,-2,-3,-4,-5],-8))
