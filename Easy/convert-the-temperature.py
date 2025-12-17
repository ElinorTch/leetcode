# Link: https://leetcode.com/problems/convert-the-temperature/

def convertTemperature(celsius):
    """
    :type celsius: float
    :rtype: List[float]
    """
    return [round(celsius + 273.15, 5), round(celsius * 1.80 + 32.00, 5)]

if __name__ == "__main__":
    print(convertTemperature(36.50))