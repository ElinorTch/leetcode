# Link: https://leetcode.com/problems/strictly-palindromic-number/


def isStrictlyPalindromic(n):
    """
    :type n: int
    :rtype: bool
    """
    def to_base(n, base):
        if n == 0:
            return "0"
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res = []
        while n > 0:
            res.append(digits[n % base])
            n //= base
        return "".join(reversed(res))
    
    i = 2
    while i <= (n - 2):
        val = str(to_base(n, i))
        i += 1
        for j in range(len(val)):
            if val[j] != val[len(val) - j - 1]:
                return False
            
    return True
        
print(isStrictlyPalindromic(4))