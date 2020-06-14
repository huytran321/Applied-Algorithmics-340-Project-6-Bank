from queue import Queue
from bank import BankManager
from transaction import Transaction
from binarysearchtree import BinarySearchTree
from binarysearchtree import Node
from funds import Funds
from account import Account
import sys 

jollyBank = BankManager(sys.argv[1])
jollyBank.pullingLinesFromFile()
jollyBank.excuteTranasctions()
