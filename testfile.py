class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = str(x)
        if num[0] == "-":
            return False
        if num[-1] == "0" and num != "0":
            return False
        return num == num[::-1]

## string slicing, like a cake ? probably

list  = [1,2,3,4,5]
yom = list[1:0:-1]


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits) -1, - 1, -1):
            if digits[i] < 0:
                digits[i] +=1
                return digits
            elif digits[i] == 9:
                digits[i] = 0