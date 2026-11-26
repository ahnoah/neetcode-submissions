class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        place = nums.copy()
        place2 = nums.copy()
        differences = []
        for num in nums:
            differences.append(target - num)
        if target/2 in nums and nums.count(target/2) < 2:
            place.remove(target/2)
            differences.remove(target/2)

        # now place should be [4, 6] and diff should be [6, 4]

        indeces = []
        for num in place:
            if num in differences:
                indeces.append(nums.index(num))
                place2.remove(num)
                indeces.append(place2.index(target - num) + 1)
                break

        return sorted(indeces)
