# # sets are unique sequence moje da dyrji samo unikalni elementi i ne e podredena
#
# nums = {1, 2, 3, 1} # nums = set() ako iskam prazen inache shte e dict
# print(type(nums))
# print(nums)
#
# nums.add(124)
# print(nums)

nums1 = {1, 2, 3, 4}
nums2 = {3, 4, 5, 6}

result = nums1.union(nums2) # nums1 | nums2 obedinenie na setove - ne dyrjat dublikat
print(result)

result = nums1.difference(nums2) # nums1 - nums2 shte dade el samo ot nums1
print(result)

result = nums1.symmetric_difference(nums2) # nums1 ^ nums2 elementite koito ne se povtarqt v dvata seta
print(result)

result = nums1.intersection(nums2) # nums1 & nums2 elementite koito se sreshtat v dvata seta
print(result)

a = {1, 2}
b = {3, 1, 2}

print(a.issubset(b)) # dali elmentite ot a se namirat v b / a <= b
print(b.issuperset(a))  # b > a
