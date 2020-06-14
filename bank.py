

from queue import Queue
from transaction import Transaction
from account import Account
from binarysearchtree import BinarySearchTree
from binarysearchtree import Node

class BankManager:
    def __init__(self, fileName = ""):
        self.__fileName = fileName

    def getFileName(self):
        return self.__fileName

    def setFileName(self, fileName):
        self.__fileName = fileName

    def pullingLinesFromFile(self):
        queueContainingTransactions = Queue()
        fileName = open(self.__fileName, "r")
        line = fileName.readline().strip()
        while line != "":
            transactionLine = Transaction(line)
            transactionLine.separatingFromPopQueue()
            queueContainingTransactions.put(transactionLine)
            line = fileName.readline().strip()
        fileName.close()
        return queueContainingTransactions

    def printAllAccounts(self):
        jollyTree = BinarySearchTree()
        jollyTree.get()



    def excuteTranasctions(self):
        newQueue = Queue()
        newQueue = self.pullingLinesFromFile()
        jollyTree = BinarySearchTree()
        line = Transaction()
        openAccounts = []
        while not newQueue.empty():
            line = newQueue.get()

            if line.getType() == "O":
                if (jollyTree.contains(line.getAccountNumber())):
                    print("ERROR: Account " + line.getAccountNumber() + " is already open. Transaction refused.")
                elif(int(line.getAccountNumber()) > 9999):
                    print("ERROR: Account " + line.getAccountNumber() + " is an invalid ID. Transaction refued." )
                else:
                    openAccounts.append(line.getAccountNumber())
                    jollyTree.insert(line.getAccountNumber(), line.getAccount())

            elif line.getAccountNumber() not in openAccounts:
                    print("ERROR: Account " + line.getAccountNumber() + " does not exist. Transaction refused.")

            elif line.getType() == "D":
                
                error = ""
                depositAccount = jollyTree.get(line.getAccountNumber())
                if (int(line.getAmount()) < 0):
                    print("ERROR: Incorrect funds to deposit $" + str(line.getAmount()) + " from " + str(depositAccount.getName()) + " " + str(depositAccount.getFunds()[int(line.getFundsType())]))
                    error = " (Failed)"
                else:
                    depositAccount.depositFunds(line.getFundsType(), line.getAmount())

                if line.getFundsType() == "0":
                    history0 = jollyTree.get(line.getAccountNumber()).getFundsHistory0()
                    history0.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                elif line.getFundsType() == "1":
                    history1 = jollyTree.get(line.getAccountNumber()).getFundsHistory1()
                    history1.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                elif line.getFundsType() == "2":
                    history2 = jollyTree.get(line.getAccountNumber()).getFundsHistory2()
                    history2.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                elif line.getFundsType() == "3":
                    history3 = jollyTree.get(line.getAccountNumber()).getFundsHistory3()
                    history3.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                elif line.getFundsType() == "4":
                    history4 = jollyTree.get(line.getAccountNumber()).getFundsHistory4()
                    history4.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                elif line.getFundsType() == "5":
                    history5 = jollyTree.get(line.getAccountNumber()).getFundsHistory5()
                    history5.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                elif line.getFundsType() == "6":
                    history6 = jollyTree.get(line.getAccountNumber()).getFundsHistory6()
                    history6.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                elif line.getFundsType() == "7":
                    history7 = jollyTree.get(line.getAccountNumber()).getFundsHistory7()
                    history7.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                elif line.getFundsType() == "8":
                    history8 = jollyTree.get(line.getAccountNumber()).getFundsHistory8()
                    history8.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                elif line.getFundsType() == "9":
                    history9 = jollyTree.get(line.getAccountNumber()).getFundsHistory9()
                    history9.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)

            elif line.getType() == "W":

                error = ""
                withdrawAccount = jollyTree.get(line.getAccountNumber())
                errorCheck = withdrawAccount.getBalance()
                if (int(line.getAmount()) < 0):
                    print("ERROR: Not enough funds to withdraw $" + str(line.getAmount()) + " from " + str(withdrawAccount.getName()) + " " + str(withdrawAccount.getFunds()[int(line.getFundsType())]))
                    error = " (Failed)"
                    if line.getFundsType() == "0":
                        history0 = jollyTree.get(line.getAccountNumber()).getFundsHistory0()
                        history0.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                    elif line.getFundsType() == "1":
                        history1 = jollyTree.get(line.getAccountNumber()).getFundsHistory1()
                        history1.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                    elif line.getFundsType() == "2":
                        history2 = jollyTree.get(line.getAccountNumber()).getFundsHistory2()
                        history2.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                    elif line.getFundsType() == "3":
                        history3 = jollyTree.get(line.getAccountNumber()).getFundsHistory3()
                        history3.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                    elif line.getFundsType() == "4":
                        history4 = jollyTree.get(line.getAccountNumber()).getFundsHistory4()
                        history4.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                    elif line.getFundsType() == "5":
                        history5 = jollyTree.get(line.getAccountNumber()).getFundsHistory5()
                        history5.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                    elif line.getFundsType() == "6":
                        history6 = jollyTree.get(line.getAccountNumber()).getFundsHistory6()
                        history6.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                    elif line.getFundsType() == "7":
                        history7 = jollyTree.get(line.getAccountNumber()).getFundsHistory7()
                        history7.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                    elif line.getFundsType() == "8":
                        history8 = jollyTree.get(line.getAccountNumber()).getFundsHistory8()
                        history8.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                    elif line.getFundsType() == "9":
                        history9 = jollyTree.get(line.getAccountNumber()).getFundsHistory9()
                        history9.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)

                elif (line.getFundsType() == "0" or line.getFundsType() == "1") and int(line.getAmount()) >= int(errorCheck[int(line.getFundsType())]):                    
                    if(int(errorCheck[0]) + int(errorCheck[1])) >= int(line.getAmount()): 
                        history0 = jollyTree.get(line.getAccountNumber()).getFundsHistory0()
                        history1 = jollyTree.get(line.getAccountNumber()).getFundsHistory1()
                        
                        if line.getFundsType() == "0":
                            balance0 = jollyTree.get(line.getAccountNumber()).getBalance()[0]
                            remainingAmount = int(line.getAmount()) - int(balance0)
                            history0.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(balance0))
                            history1.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(remainingAmount))
                            withdrawAccount.withdrawCombineAccount(int(line.getFundsType()), int(line.getAmount()))
                        else:
                            balance1 = jollyTree.get(line.getAccountNumber()).getBalance()[1]
                            remainingAmount = int(line.getAmount()) - int(balance1)
                            history1.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(remainingAmount))
                            history0.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(balance1))
                            withdrawAccount.withdrawCombineAccount(int(line.getFundsType()), int(line.getAmount()))
                    else:
                        print("ERROR: Not enough funds to withdraw $" + str(line.getAmount()) + " from " + str(withdrawAccount.getName()) + " " + str(withdrawAccount.getFunds()[int(line.getFundsType())]))
                        error = " (Failed)"
                        if line.getFundsType() == "0":
                            history0 = jollyTree.get(line.getAccountNumber()).getFundsHistory0()
                            history0.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                        elif line.getFundsType() == "1":
                            history1 = jollyTree.get(line.getAccountNumber()).getFundsHistory1()
                            history1.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)


                elif (line.getFundsType() == "2" or line.getFundsType() == "3") and int(line.getAmount()) >= int(errorCheck[int(line.getFundsType())]):
                    if(int(errorCheck[2]) + int(errorCheck[3])) >= int(line.getAmount()):
                        history2 = jollyTree.get(line.getAccountNumber()).getFundsHistory2()
                        history3 = jollyTree.get(line.getAccountNumber()).getFundsHistory3()
                        if line.getFundsType() == "2":
                            balance2 = jollyTree.get(line.getAccountNumber()).getBalance()[2]
                            remainingAmount = int(line.getAmount()) - int(balance2)
                            history2.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(balance2))
                            history3.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(remainingAmount))
                            withdrawAccount.withdrawCombineAccount(int(line.getFundsType()), int(line.getAmount()))
                        else:
                            balance3 = jollyTree.get(line.getAccountNumber()).getBalance()[3]
                            remainingAmount = int(line.getAmount()) - int(balance3)
                            history3.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(remainingAmount))
                            history2.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(balance3))
                            withdrawAccount.withdrawCombineAccount(int(line.getFundsType()), int(line.getAmount()))
                    else:
                            print("ERROR: Not enough funds to withdraw $" + str(line.getAmount()) + " from " + str(withdrawAccount.getName()) + " " + str(withdrawAccount.getFunds()[int(line.getFundsType())]))
                            error = " (Failed)"
                            if line.getFundsType() == "2":
                                history2 = jollyTree.get(line.getAccountNumber()).getFundsHistory2()
                                history2.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                            elif line.getFundsType() == "3":
                                history3 = jollyTree.get(line.getAccountNumber()).getFundsHistory3()
                                history3.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)                                         

                elif(int(errorCheck[int(line.getFundsType())]) < int(line.getAmount())):
                    print("ERROR: Not enough funds to withdraw $" + str(line.getAmount()) + " from " + str(withdrawAccount.getName()) + " " + str(withdrawAccount.getFunds()[int(line.getFundsType())]))
                    error = " (Failed)"
                    if line.getFundsType() == "0":
                        history0 = jollyTree.get(line.getAccountNumber()).getFundsHistory0()
                        history0.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                    elif line.getFundsType() == "1":
                        history1 = jollyTree.get(line.getAccountNumber()).getFundsHistory1()
                        history1.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                    elif line.getFundsType() == "2":
                        history2 = jollyTree.get(line.getAccountNumber()).getFundsHistory2()
                        history2.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                    elif line.getFundsType() == "3":
                        history3 = jollyTree.get(line.getAccountNumber()).getFundsHistory3()
                        history3.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                    elif line.getFundsType() == "4":
                        history4 = jollyTree.get(line.getAccountNumber()).getFundsHistory4()
                        history4.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                    elif line.getFundsType() == "5":
                        history5 = jollyTree.get(line.getAccountNumber()).getFundsHistory5()
                        history5.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                    elif line.getFundsType() == "6":
                        history6 = jollyTree.get(line.getAccountNumber()).getFundsHistory6()
                        history6.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                    elif line.getFundsType() == "7":
                        history7 = jollyTree.get(line.getAccountNumber()).getFundsHistory7()
                        history7.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                    elif line.getFundsType() == "8":
                        history8 = jollyTree.get(line.getAccountNumber()).getFundsHistory8()
                        history8.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                    elif line.getFundsType() == "9":
                        history9 = jollyTree.get(line.getAccountNumber()).getFundsHistory9()
                        history9.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                else:
                    withdrawAccount.withdrawFunds(line.getFundsType(), line.getAmount())

                    if line.getFundsType() == "0":
                        history0 = jollyTree.get(line.getAccountNumber()).getFundsHistory0()
                        history0.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                    elif line.getFundsType() == "1":
                        history1 = jollyTree.get(line.getAccountNumber()).getFundsHistory1()
                        history1.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                    elif line.getFundsType() == "2":
                        history2 = jollyTree.get(line.getAccountNumber()).getFundsHistory2()
                        history2.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                    elif line.getFundsType() == "3":
                        history3 = jollyTree.get(line.getAccountNumber()).getFundsHistory3()
                        history3.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                    elif line.getFundsType() == "4":
                        history4 = jollyTree.get(line.getAccountNumber()).getFundsHistory4()
                        history4.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                    elif line.getFundsType() == "5":
                        history5 = jollyTree.get(line.getAccountNumber()).getFundsHistory5()
                        history5.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                    elif line.getFundsType() == "6":
                        history6 = jollyTree.get(line.getAccountNumber()).getFundsHistory6()
                        history6.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                    elif line.getFundsType() == "7":
                        history7 = jollyTree.get(line.getAccountNumber()).getFundsHistory7()
                        history7.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                    elif line.getFundsType() == "8":
                        history8 = jollyTree.get(line.getAccountNumber()).getFundsHistory8()
                        history8.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)
                    elif line.getFundsType() == "9":
                        history9 = jollyTree.get(line.getAccountNumber()).getFundsHistory9()
                        history9.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + error)

            elif line.getType() == "T":
                error = ""
                transferAccount = jollyTree.get(line.getAccountNumber())
                errorCheck = transferAccount.getBalance()
                if (line.getAccountNumber() not in openAccounts or line.getAccountTransferNumber() not in openAccounts):
                    print("ERROR: Account ID " + str(line.getAccountTransferNumber()) + " is not an open account. Transaction refused.")
                elif (int(line.getAmount()) < 0):
                    print("Error: Not enough funds to transfer " + str(line.getAmount()) + " from " + str(transferAccount.getName()) + " " + str(depositAccount.getFunds()[int(line.getFundsType())]) + "to " + str(depositAccount.getFunds()[int(line.getFundsTransferNumber())]))
                    error = " (Failed)"
                elif (line.getFundsType() == "0" or line.getFundsType() == "1") and int(line.getAmount()) >= int(errorCheck[int(line.getFundsType())]):
                    if(int(errorCheck[0]) + int(errorCheck[1])) >= int(line.getAmount()):
                        history0 = jollyTree.get(line.getAccountNumber()).getFundsHistory0()
                        history1 = jollyTree.get(line.getAccountNumber()).getFundsHistory1()
                        if line.getFundsType() == "0":
                            balance0 = jollyTree.get(line.getAccountNumber()).getBalance()[0]
                            remainingAmount = int(line.getAmount()) - int(balance0)
                            history0.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(balance0) + " " + str(line.getAccountTransferNumber()) + str(line.getFundsTransferNumber()))
                            history1.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(remainingAmount) + " " + str(line.getAccountTransferNumber()) + str(line.getFundsTransferNumber()))
                            transferAccount.transferCombineAccounts(int(line.getFundsType()), int(line.getFundsTransferNumber()), int(line.getAmount()))
                        else:
                            balance1 = jollyTree.get(line.getAccountNumber()).getBalance()[1]
                            remainingAmount = int(line.getAmount()) - int(balance2)
                            history1.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(balance1) + " " + str(line.getAccountTransferNumber()) + str(line.getFundsTransferNumber()))
                            history0.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(remainingAmount) + " " + str(line.getAccountTransferNumber()) + str(line.getFundsTransferNumber()))
                            transferAccount.transferCombineAccounts(int(line.getFundsType()), int(line.getFundsTransferNumber()), int(line.getAmount()))

                elif (line.getFundsType() == "2" or line.getFundsType() == "3") and int(line.getAmount()) >= int(errorCheck[int(line.getFundsType())]):
                    if(int(errorCheck[2]) + int(errorCheck[3])) >= int(line.getAmount()):
                        history2 = jollyTree.get(line.getAccountNumber()).getFundsHistory2()
                        history3 = jollyTree.get(line.getAccountNumber()).getFundsHistory3()
                        if line.getFundsType() == "2":
                            balance2 = jollyTree.get(line.getAccountNumber()).getBalance()[2]
                            remainingAmount = int(line.getAmount()) - int(balance2)
                            history2.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(balance2) + " " + str(line.getAccountTransferNumber()) + str(line.getFundsTransferNumber()))
                            history3.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(remainingAmount) + " " + str(line.getAccountTransferNumber()) + str(line.getFundsTransferNumber()))
                            transferAccount.transferCombineAccounts(int(line.getFundsType()), int(line.getFundsTransferNumber()), int(line.getAmount()))
                        else:
                            balance3 = jollyTree.get(line.getAccountNumber()).getBalance()[3]
                            remainingAmount = int(line.getAmount()) - int(balance3)
                            history3.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(balance3) + " " + str(line.getAccountTransferNumber()) + str(line.getFundsTransferNumber()))
                            history2.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(remainingAmount) + " " + str(line.getAccountTransferNumber()) + str(line.getFundsTransferNumber()))
                            transferAccount.transferCombineAccounts(int(line.getFundsType()), int(line.getFundsTransferNumber()), int(line.getAmount()))                       


                elif int(line.getAmount()) > int(errorCheck[int(line.getFundsType())]): 
                    print("Error: Not enough funds to transfer " + str(line.getAmount()) + " from " + str(transferAccount.getName()) + " " + str(depositAccount.getFunds()[int(line.getFundsType())]) + "to " + str(depositAccount.getFunds()[int(line.getFundsTransferNumber())]) )
                    error = " (Failed)"
                else: 
                    transferAccount.transferFunds(line.getFundsType(), line.getFundsTransferNumber(), line.getAmount())                
                    if line.getFundsType() == "0":
                        history0 = jollyTree.get(line.getAccountNumber()).getFundsHistory0()
                        history0.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + " " + str(line.getAccountTransferNumber()) + str(line.getFundsTransferNumber())  + error)
                    elif line.getFundsType() == "1":
                        history1 = jollyTree.get(line.getAccountNumber()).getFundsHistory1()
                        history1.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + " " + str(line.getAccountTransferNumber()) + str(line.getFundsTransferNumber())  + error)
                    elif line.getFundsType() == "2":
                        history2 = jollyTree.get(line.getAccountNumber()).getFundsHistory2()
                        history2.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + " " + str(line.getAccountTransferNumber()) + str(line.getFundsTransferNumber())  + error)
                    elif line.getFundsType() == "3":
                        history3 = jollyTree.get(line.getAccountNumber()).getFundsHistory3()
                        history3.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + " " + str(line.getAccountTransferNumber()) + str(line.getFundsTransferNumber())  + error)
                    elif line.getFundsType() == "4":
                        history4 = jollyTree.get(line.getAccountNumber()).getFundsHistory4()
                        history4.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + " " + str(line.getAccountTransferNumber()) + str(line.getFundsTransferNumber())  + error)
                    elif line.getFundsType() == "5":
                        history5 = jollyTree.get(line.getAccountNumber()).getFundsHistory5()
                        history5.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + " " + str(line.getAccountTransferNumber()) + str(line.getFundsTransferNumber())  + error)
                    elif line.getFundsType() == "6":
                        history6 = jollyTree.get(line.getAccountNumber()).getFundsHistory6()
                        history6.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + " " + str(line.getAccountTransferNumber()) + str(line.getFundsTransferNumber())  + error)
                    elif line.getFundsType() == "7":
                        history7 = jollyTree.get(line.getAccountNumber()).getFundsHistory7()
                        history7.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + " " + str(line.getAccountTransferNumber()) + str(line.getFundsTransferNumber())  + error)
                    elif line.getFundsType() == "8":
                        history8 = jollyTree.get(line.getAccountNumber()).getFundsHistory8()
                        history8.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + " " + str(line.getAccountTransferNumber()) + str(line.getFundsTransferNumber())  + error)
                    elif line.getFundsType() == "9":
                        history9 = jollyTree.get(line.getAccountNumber()).getFundsHistory9()
                        history9.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + " " + str(line.getAccountTransferNumber()) + str(line.getFundsTransferNumber())  + error)
                

                    if line.getFundsTransferNumber() == "0":
                        history0 = jollyTree.get(line.getAccountNumber()).getFundsHistory0()
                        history0.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + " " + str(line.getAccountTransferNumber()) + str(line.getFundsTransferNumber())  + error)
                    elif line.getFundsTransferNumber() == "1":
                        history1 = jollyTree.get(line.getAccountNumber()).getFundsHistory1()
                        history1.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + " " + str(line.getAccountTransferNumber()) + str(line.getFundsTransferNumber())  + error)
                    elif line.getFundsTransferNumber() == "2":
                        history2 = jollyTree.get(line.getAccountNumber()).getFundsHistory2()
                        history2.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + " " + str(line.getAccountTransferNumber()) + str(line.getFundsTransferNumber())  + error)
                    elif line.getFundsTransferNumber() == "3":
                        history3 = jollyTree.get(line.getAccountNumber()).getFundsHistory3()
                        history3.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + " " + str(line.getAccountTransferNumber()) + str(line.getFundsTransferNumber())  + error)
                    elif line.getFundsTransferNumber() == "4":
                        history4 = jollyTree.get(line.getAccountNumber()).getFundsHistory4()
                        history4.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + " " + str(line.getAccountTransferNumber()) + str(line.getFundsTransferNumber())  + error)
                    elif line.getFundsTransferNumber() == "5":
                        history5 = jollyTree.get(line.getAccountNumber()).getFundsHistory5()
                        history5.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + " " + str(line.getAccountTransferNumber()) + str(line.getFundsTransferNumber())  + error)
                    elif line.getFundsTransferNumber() == "6":
                        history6 = jollyTree.get(line.getAccountNumber()).getFundsHistory6()
                        history6.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + " " + str(line.getAccountTransferNumber()) + str(line.getFundsTransferNumber())  + error)
                    elif line.getFundsTransferNumber() == "7":
                        history7 = jollyTree.get(line.getAccountNumber()).getFundsHistory7()
                        history7.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + " " + str(line.getAccountTransferNumber()) + str(line.getFundsTransferNumber())  + error)
                    elif line.getFundsTransferNumber() == "8":
                        history8 = jollyTree.get(line.getAccountNumber()).getFundsHistory8()
                        history8.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + " " + str(line.getAccountTransferNumber()) + str(line.getFundsTransferNumber())  + error)
                    elif line.getFundsTransferNumber() == "9":
                        history9 = jollyTree.get(line.getAccountNumber()).getFundsHistory9()
                        history9.append(str(line.getType()) + " " + str(line.getAccountNumber()) + str(line.getFundsType()) + " " + str(line.getAmount()) + " " + str(line.getAccountTransferNumber()) + str(line.getFundsTransferNumber())  + error)

            elif line.getType() == "H":
                historyAccount = jollyTree.get(line.getAccountNumber())

                if line.getFundsType() == "0":
                    historyAccount.printIndividualFundsHistory0()
                elif line.getFundsType() == "1":
                    historyAccount.printIndividualFundsHistory1()
                elif line.getFundsType() == "2":
                    historyAccount.printIndividualFundsHistory2()
                elif line.getFundsType() == "3":
                    historyAccount.printIndividualFundsHistory3()
                elif line.getFundsType() == "4":
                    historyAccount.printIndividualFundsHistory4()
                elif line.getFundsType() == "5":
                    historyAccount.printIndividualFundsHistory5()
                elif line.getFundsType() == "6":
                    historyAccount.printIndividualFundsHistory6()
                elif line.getFundsType() == "7":
                    historyAccount.printIndividualFundsHistory7()
                elif line.getFundsType() == "8":
                    historyAccount.printIndividualFundsHistory8()
                elif line.getFundsType() == "9":
                    historyAccount.printIndividualFundsHistory9()
                else:
                    print("Transaction History for " + str(historyAccount.getName()) + " by fund.")
                    historyAccount.historyFunds()
            
        print("\nProcessing Done. Final Balances")
        for accountNumbers in openAccounts:
            jollyTree.get(accountNumbers).printAllData()

    def __str__(self):
        return str(self.__fileName)

    def __repr__(self):
        return str(self.__fileName)



