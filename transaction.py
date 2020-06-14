

from queue import Queue

from account import Account
from binarysearchtree import BinarySearchTree
from binarysearchtree import Node


class Transaction():
    def __init__(self, line = ""):
        self.__line = line
        self.__type = None
        self.__accountNumber = None
        self.__fundsType = None
        self.__name = None
        self.__amount = 0
        self.__accountTransferNumber = None
        self.__fundsTransferNumber = None
        self.__account = ""

    def getLine(self):
        return self.__line

    def setLine(self, line):
        self.__line = line

    def getType(self):
        return self.__type

    def setType(self, type):
        self.__type = type

    def getAccountNumber(self):
        return self.__accountNumber

    def setAccountNumber(self, accountNumber):
        self.__accountNumber = accountNumber

    def getFundsType(self):
        return self.__fundsType

    def setFundsType(self, fundsType):
        self.__fundsType = fundsType

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def printName(self):
        return str(self.__name)

    def getAmount(self):
        return self.__amount

    def setAmount(self, amount):
        self.__amount = amount

    def getAccountTransferNumber(self):
        return self.__accountTransferNumber
    
    def setAccountTransferNumber(self, accountTransferNumber):
        self.__accountTransferNumber = accountTransferNumber

    def getFundsTransferNumber(self):
        return self.__fundsTransferNumber

    def setFundsTransferNumber(self, fundsTransferNumber):
        self.__fundsTransferNumber = fundsTransferNumber

    def getAccount(self):
        newAccount = Account()
        newAccount.createAccount()  
        newAccount.setName(self.getName())
        newAccount.setAccountNumber(self.getAccountNumber())
        return newAccount

    def separatingFromPopQueue(self):
        try:
            splitLine = self.__line.split()
            if splitLine[0] == "O":
                self.__type = splitLine[0]
                self.__name = str(splitLine[2]) + " " + str(splitLine[1])
                self.__accountNumber = splitLine[3]
            elif splitLine[0] == "D":
                self.__type = splitLine[0]
                self.__amount = splitLine[2]
                separatingFundsFromAccount = list(str(splitLine[1]))
                self.__fundsType = separatingFundsFromAccount.pop()
                result = ""
                for element in separatingFundsFromAccount:
                    result += str(element)
                self.__accountNumber = result
            elif splitLine[0] == "W":
                self.__type = splitLine[0]
                self.__amount = splitLine[2]
                separatingFundsFromAccount = list(str(splitLine[1]))
                self.__fundsType = separatingFundsFromAccount.pop()
                result = ""
                for element in separatingFundsFromAccount:
                    result += str(element)
                self.__accountNumber = result
            elif splitLine[0] == "T":
                self.__type = "T"
                self.__amount = splitLine[2]

                separatingFundsFromAccount = list(str(splitLine[1]))
                self.__fundsType = separatingFundsFromAccount.pop()
                result1 = ""
                for element1 in separatingFundsFromAccount:
                    result1 += str(element1)
                self.__accountNumber = result1

                transferingFundsFromAccount = list(str(splitLine[3]))
                self.__fundsTransferNumber = transferingFundsFromAccount.pop()
                result2 = ""
                for element2 in transferingFundsFromAccount:
                    result2 += str(element2)
                self.__accountTransferNumber = result2
            elif splitLine[0] == "H":
                self.__type = splitLine[0]
                separatingFundsFromAccount = list(str(splitLine[1]))
                if len(separatingFundsFromAccount) == 5:
                    self.__fundsType = separatingFundsFromAccount.pop()
                result = ""
                for element in separatingFundsFromAccount:
                    result += str(element)
                self.__accountNumber = result

        except ValueError as te:
            print(te)
            
    def __str__(self):
        return ("Type = " + str(self.getType()) + "\nAccount Number = " + str(self.getAccountNumber()) + "\nAccount Transfer Number = " +
               str(self.getAccountTransferNumber()) + "\nFunds Type = " + str(self.getFundsType()) + "\nFunds Transfer Number = "  +
               str(self.getFundsTransferNumber()) + "\nName = " + str(self.getName()) + "\nAmount = " + str(self.getAmount()))

    def __repr__(self):
        return ("Type = " + str(self.getType()) + "\nAccount Number = " + str(self.getAccountNumber()) + "\nAccount Transfer Number = " +
               str(self.getAccountTransferNumber()) + "\nFunds Type = " + str(self.getFundsType()) + "\nFunds Transfer Number = "  +
               str(self.getFundsTransferNumber()) + "\nName = " + str(self.getName()) + "\nAmount = " + str(self.getAmount()))

