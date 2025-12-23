# Link: https://leetcode.com/problems/defanging-an-ip-address/

def defangIPaddr(address: str):
    """
    :type address: str
    :rtype: str
    """
    return address.replace(".", "[.]")

print(defangIPaddr("255.100.50.0"))