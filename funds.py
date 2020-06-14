class Funds():
    def __init__(self):
        self.__fundslist = ["Money Market ", "Prime Money Market", "Long-Term Bond ", "Short-Term Bond",
                           "500 Index Fund", "Capital Value Fund", "Growth Equity Fund", "Growth Index Fund",
                           "Value Fund", "Value Stock Index"]

        self.__balancelist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def getFundslist(self):
        return self.__fundslist

    def getBalancelist(self):
        return self.__balancelist



