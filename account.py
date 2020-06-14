from queue import Queue

from binarysearchtree import BinarySearchTree
from binarysearchtree import Node
from funds import Funds

class Account():
    def __init__(self):
        self.__funds = []
        self.__balance = []
        self.__name = None
        self.__accountNumber = ""

        self.__fundsHistory0 = []
        self.__fundsHistory1 = []
        self.__fundsHistory2 = []
        self.__fundsHistory3 = []
        self.__fundsHistory4 = []
        self.__fundsHistory5 = []
        self.__fundsHistory6 = []
        self.__fundsHistory7 = []
        self.__fundsHistory8 = []
        self.__fundsHistory9 = []

    def getFundsHistory0(self):
        return self.__fundsHistory0

    def setFundsHistory0(self, fundsHistory0 = []):
        self.__fundsHistory0 = fundsHistory0

    def getFundsHistory1(self):
        return self.__fundsHistory1

    def setFundsHistory1(self, fundsHistory1 = []):
        self.__fundsHistory1 = fundsHistory1

    def getFundsHistory2(self):
        return self.__fundsHistory2

    def setFundsHistory2(self, fundsHistory2 = []):
        self.__fundsHistory2 = fundsHistory2

    def getFundsHistory3(self):
        return self.__fundsHistory3

    def setFundsHistory3(self, fundsHistory3 = []):
        self.__fundsHistory3 = fundsHistory3

    def getFundsHistory4(self):
        return self.__fundsHistory4

    def setFundsHistory4(self, fundsHistory4 = []):
        self.__fundsHistory4 = fundsHistory4

    def getFundsHistory5(self):
        return self.__fundsHistory5

    def setFundsHistory5(self, fundsHistory5 = []):
        self.__fundsHistory5 = fundsHistory5

    def getFundsHistory6(self):
        return self.__fundsHistory6

    def setFundsHistory6(self, fundsHistory6 = []):
        self.__fundsHistory6 = fundsHistory6

    def getFundsHistory7(self):
        return self.__fundsHistory7

    def setFundsHistory7(self, fundsHistory7 = []):
        self.__fundsHistory7 = fundsHistory7

    def getFundsHistory8(self):
        return self.__fundsHistory8

    def setFundsHistory8(self, fundsHistory8 = []):
        self.__fundsHistory8 = fundsHistory8

    def getFundsHistory9(self):
        return self.__fundsHistory9

    def setFundsHistory9(self, fundsHistory9 = []):
        self.__fundsHistory9 = fundsHistory9

    def printFundsHistory0(self):
        funds = self.getFunds()
        balance = self.getBalance()
        history0 = self.getFundsHistory0()
        if len(history0) > 0:
            print(funds[0] + ": $" + str(balance[0]))
            for i in history0:
                print("\t" + i)

    def printFundsHistory1(self):
        funds = self.getFunds()
        balance = self.getBalance()
        history1 = self.getFundsHistory1()
        if len(history1) > 0:
            print(funds[1] + ": $" + str(balance[1]))
            for i in history1:
                print("\t" + i)

    def printFundsHistory2(self):
        funds = self.getFunds()
        balance = self.getBalance()
        history2 = self.getFundsHistory2()
        if len(history2) > 0:
            print(funds[2] + ": $" + str(balance[2]))
            for i in history2:
                print("\t" + i)

    def printFundsHistory3(self):
        funds = self.getFunds()
        balance = self.getBalance()
        history3 = self.getFundsHistory3()
        if len(history3) > 0:
            print(funds[3] + ": $" + str(balance[3]))
            for i in history3:
                print("\t" + i)

    def printFundsHistory4(self):
        funds = self.getFunds()
        balance = self.getBalance()
        history4 = self.getFundsHistory4()
        if len(history4) > 0:
            print(funds[4] + ": $" + str(balance[4]))
            for i in history4:
                print("\t" + i)

    def printFundsHistory5(self):
        funds = self.getFunds()
        balance = self.getBalance()
        history5 = self.getFundsHistory5()
        if len(history5) > 0:
            print(funds[5] + ": $" + str(balance[5]))
            for i in history5:
                print("\t" + i)

    def printFundsHistory6(self):
        funds = self.getFunds()
        balance = self.getBalance()
        history6 = self.getFundsHistory6()
        if len(history6) > 0:
            print(funds[6] + ": $" + str(balance[6]))
            for i in history6:
                print("\t" + i)

    def printFundsHistory7(self):
        funds = self.getFunds()
        balance = self.getBalance()
        history7 = self.getFundsHistory7()
        if len(history7) > 0:
            print(funds[7] + ": $" + str(balance[7]))
            for i in history7:
                print("\t" + i)

    def printFundsHistory8(self):
        funds = self.getFunds()
        balance = self.getBalance()
        history8 = self.getFundsHistory8()
        if len(history8) > 0:
            print(funds[8] + ": $" + str(balance[8]))
            for i in history8:
                print("\t" + i)

    def printFundsHistory9(self):
        funds = self.getFunds()
        balance = self.getBalance()
        history9 = self.getFundsHistory9()
        if len(history9) > 0:
            print(funds[9] + ": $" + str(balance[9]))
            for i in history9:
                print("\t" + i)

    def printIndividualFundsHistory0(self):
        funds = self.getFunds()
        balance = self.getBalance()
        history = self.getFundsHistory0()
        print("Transaction History for " + self.getName() + " " + funds[0] + ": $" + str(balance[0]))
        for i in history:
            print("\t" + i)

    def printIndividualFundsHistory1(self):
        funds = self.getFunds()
        balance = self.getBalance()
        history = self.getFundsHistory1()
        print("Transaction History for " + self.getName() + " " + funds[1] + ": $" + str(balance[1]))
        for i in history:
            print("\t" + i)

    def printIndividualFundsHistory2(self):
        funds = self.getFunds()
        balance = self.getBalance()
        history = self.getFundsHistory2()
        print("Transaction History for " + self.getName() + " " + funds[2] + ": $" + str(balance[2]))
        for i in history:
            print("\t" + i)

    def printIndividualFundsHistory3(self):
        funds = self.getFunds()
        balance = self.getBalance()
        history = self.getFundsHistory3()
        print("Transaction History for " + self.getName() + " " + funds[3] + ": $" + str(balance[3]))
        for i in history:
            print("\t" + i)

    def printIndividualFundsHistory4(self):
        funds = self.getFunds()
        balance = self.getBalance()
        history = self.getFundsHistory4()
        print("Transaction History for " + self.getName() + " " + funds[4] + ": $" + str(balance[4]))
        for i in history:
            print("\t" + i)

    def printIndividualFundsHistory5(self):
        funds = self.getFunds()
        balance = self.getBalance()
        history = self.getFundsHistory5()
        print("Transaction History for " + self.getName() + " " + funds[5] + ": $" + str(balance[5]))
        for i in history:
            print("\t" + i)

    def printIndividualFundsHistory6(self):
        funds = self.getFunds()
        balance = self.getBalance()
        history = self.getFundsHistory6()
        print("Transaction History for " + self.getName() + " " + funds[6] + ": $" + str(balance[6]))
        for i in history:
            print("\t" + i)

    def printIndividualFundsHistory7(self):
        funds = self.getFunds()
        balance = self.getBalance()
        history = self.getFundsHistory7()
        print("Transaction History for " + self.getName() + " " + funds[7] + ": $" + str(balance[7]))
        for i in history:
            print("\t" + i)

    def printIndividualFundsHistory8(self):
        funds = self.getFunds()
        balance = self.getBalance()
        history = self.getFundsHistory8()
        print("Transaction History for " + self.getName() + " " + funds[8] + ": $" + str(balance[8]))
        for i in history:
            print("\t" + i)

    def printIndividualFundsHistory9(self):
        funds = self.getFunds()
        balance = self.getBalance()
        history = self.getFundsHistory9()
        print("Transaction History for " + self.getName() + " " + funds[9] + ": $" + str(balance[9]))
        for i in history:
            print("\t" + i)

    def getName(self):
        return self.__name

    def setAccountNumber(self, accountNumber):
        self.__accountNumber = accountNumber

    def setName(self, name):
        self.__name = name

    def getAccountNumber(self):
        return self.__accountNumber

    def getBalance(self):
        return self.__balance

    def setBalance(self, balance = []):
        self.__balance = balance

    def getFunds(self):
        return self.__funds

    def setFunds(self, funds = []):
        self.__funds = funds

    def createAccount(self):
        newAccount = Funds()
        self.setFunds(newAccount.getFundslist())
        self.setBalance(newAccount.getBalancelist())

    def depositFunds(self, fundsType, amount):
        balance = self.getBalance()
        balance[int(fundsType)] += int(amount)

    def withdrawFunds(self, fundsType, amount):
        balance = self.getBalance()
        balance[int(fundsType)] -= int(amount)

    def withdrawCombineAccount(self, fundsType, amount):
        balance = self.getBalance()
        if fundsType == 0:
            amount1 = balance[int(fundsType)]
            amount2 = amount - balance[int(fundsType)]
            balance[1] -= amount2
            balance[int(fundsType)] -= balance[int(fundsType)]
        elif fundsType == 1:
            amount1 = balance[int(fundsType)]
            amount2 = amount - balance[int(fundsType)]
            balance[0] -= amount2
            balance[int(fundsType)] -= balance[int(fundsType)]
        elif fundsType == 2:
            amount1 = balance[int(fundsType)]
            amount2 = amount - balance[int(fundsType)]
            balance[3] -= amount2
            balance[int(fundsType)] -= balance[int(fundsType)]
        elif fundsType == 3:
            amount1 = balance[int(fundsType)]
            amount2 = amount - balance[int(fundsType)]
            balance[2] -= amount2
            balance[int(fundsType)] -= balance[int(fundsType)]

    def transferFunds(self, fundsType1, fundsType2, amount):
        balance = self.getBalance()
        balance[int(fundsType1)] -= int(amount)
        balance[int(fundsType2)] += int(amount)

    def transferCombineAccounts(self, fundsType1, fundsType2, amount):
        balance = self.getBalance()
        if fundsType1 == 0:
            amount1 = balance[int(fundsType1)]
            amount = amount - balance[int(fundsType1)]
            balance[int(fundsType1)] -= balance[int(fundsType1)]
            balance[1] -= amount
            balance[int(fundsType2)] += amount + amount1
        elif fundsType1 == 1:
            amount1 = balance[int(fundsType1)]
            amount = amount - balance[int(fundsType1)]
            balance[int(fundsType1)] -= balance[int(fundsType1)]
            balance[0] -= amount
            balance[int(fundsType2)] += amount + amount1
        elif fundsType1 == 2:
            amount1 = balance[int(fundsType1)]
            amount = amount - balance[int(fundsType1)]
            balance[int(fundsType1)] -= balance[int(fundsType1)]
            balance[3] -= amount
            balance[int(fundsType2)] += amount + amount1
        elif fundsType1 == 3:
            amount1 = balance[int(fundsType1)]
            amount = amount - balance[int(fundsType1)]
            balance[int(fundsType1)] -= balance[int(fundsType1)]
            balance[2] -= amount
            balance[int(fundsType2)] += amount + amount1
            

    def historyFunds(self):
        funds = self.getFunds()
        balance = self.getBalance()
        
        self.printFundsHistory0()
        self.printFundsHistory1()
        self.printFundsHistory2()
        self.printFundsHistory3()
        self.printFundsHistory4()
        self.printFundsHistory5()
        self.printFundsHistory6()
        self.printFundsHistory7()
        self.printFundsHistory8()
        self.printFundsHistory9()

    def printAllData(self):
        funds = self.getFunds()
        balance = self.getBalance()

        print(self.getName() + " Account ID: " + self.getAccountNumber())
        print("\t" + funds[0] + ": $" + str(balance[0]))
        print("\t" + funds[1] + ": $" + str(balance[1]))
        print("\t" + funds[2] + ": $" + str(balance[2]))
        print("\t" + funds[3] + ": $" + str(balance[3]))
        print("\t" + funds[4] + ": $" + str(balance[4]))
        print("\t" + funds[5] + ": $" + str(balance[5]))
        print("\t" + funds[6] + ": $" + str(balance[6]))
        print("\t" + funds[7] + ": $" + str(balance[7]))
        print("\t" + funds[8] + ": $" + str(balance[8]))
        print("\t" + funds[9] + ": $" + str(balance[9]))
        print()

    def __str__(self):
        return str(self.__funds) + " " + str(self.__balance)

    def __repr__(self):
        return str(self.__funds) + " " + str(self.__balance)






