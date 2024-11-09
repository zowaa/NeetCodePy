class Solution:

	#Hash set
	def hasDuplicate(self, nums):
		seen = set()
		for n in nums:
			if n in seen:
				return True
			else:
				seen.add(n)
		return False
	#Time complexity O(n)
	#Space complexity O(n)

	# def hasDuplicate(self, nums):
	# 	new_l = []
	# 	for n in nums:
	# 		if n in new_l:
	# 			return True
	# 		else:
	# 			new_l.append(n)
	# 	return False
	# #Time complexity O(n^2)
	# #Space complexity O(n)

	#Brut Force
	# def hasDuplicate(self, nums):
	# 	for i in range(len(nums) - 1):
	# 		for j in range(i+1, len(nums)):
	# 			if nums[i] == nums[j]:
	# 				return True
	# 	return False
	# #Time Complexity: O(n^2)
	# #Space Complexity: O(1)

	#Hash Set Length
	# def hasDuplicate(self, nums):
	# 	new_set = set(nums)
	# 	if len(new_set) == len(nums):
	# 		return False
	# 	else:
	# 		return True
	# #Time Complexity: O(n)
	# #Space Complexity: O(n)

	
nums = [1, 2, 3, 1]
print(Solution().hasDuplicate(nums))