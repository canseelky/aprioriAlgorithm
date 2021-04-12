'''
canselhky


'''




from itertools import combinations
import pandas as pd
import time


transactions_txt = "./Datasets/Transactions.txt"

transactions_Xlsx = "./Datasets/Transactions.xlsx"

min_support = 0.07





def getTransactions(fileName):

    transaction = []
    try:
        with open(fileName) as fileObj:
            
            for line in fileObj:
                return ([tuple(line.strip().strip("\n").split(",")) for line in fileObj])
    except FileNotFoundError:
        print(f"The {fileName} not found in the directory!")
        return 0;
        

def candidateGen(F,size):
    allCandidates = list(set(combinations(F, size)))
    return [candidate for item in transaction for candidate in allCandidates
            if(set(candidate).issubset(set(item)))]
    
def getNumberOfCandidate(items):
    counts = {}
    for i in items:
        for k in transaction:
            if i in k:
                if i in counts:
                    counts[i] += 1
                else:
                    counts[i] = 1
    return counts
    


def getItemSet(transaction):
    itemset = []
    for line in transaction:
        for (item) in line:
            if (item not in itemset):
                itemset.append(item)
    return itemset
    

def generateF(itemcounts):
    f1 = []
    total = []
    number_of_transaction = len(transaction)
    for i in itemcounts:
        if (itemcounts[i] /number_of_transaction >= min_support ):
            total.append(itemcounts[i]/number_of_transaction)
            f1.append(i)

    return f1
    

def getNumberOfCandidates(items):
    counts = {}
    items = remove_dup(items)
    for i in items:
        for k in transaction:
            if set(i).issubset(set(k)):
                if i in counts:
                    counts[i] += 1
                else:
                    counts[i] = 1
    return counts

def apriori(Transaction):
    c1 = getItemSet(Transaction)
    candidates = getNumberOfCandidate(c1)
    F1 = generateF(candidates)

    f1 = tuple(sorted(F1))
    k_itemSet=(Transaction)
    dict = getNumberOfCandidate(f1)

    for i in range(2,len(k_itemSet)):
        temp = remove_dup(generateF(candidates))
        Fk = generateF(dict)
        candidates = candidateGen(Fk,i)
        candidates = getNumberOfCandidates(candidates)
        fson = remove_dup(generateF(candidates))
        if (len(fson) == 0):
            return temp
        
def remove_dup(x):
    return list(dict.fromkeys(x))





    
def getTransactions_Xlx(fileName):

    data = pd.read_excel(fileName,header =0, usecols =[0,1])
    tup = {}
    for index, row in data.iterrows():

        products = str(row["Product ID"]).split(",")
        if row["Transaction ID"] not in tup:
            tup[row["Transaction ID"]] = []
            for i in range(len(products)):
                 tup[row["Transaction ID"]].append(products[i].strip())
            
        else:
            for i in range(len(products)):
                tup[row["Transaction ID"]].append(products[i].strip())
    return [tuple(item) for item in tup.values()]
    



transaction = getTransactions(transactions_txt)


def totalTime(start,stop):
    return stop - start


if (transaction != 0):
    start = time.time()
 
    print(f"Related items are: {apriori(transaction)}")
    stop =  time.time()
    print("Total time: ",totalTime(start, stop))
    
print("----------------------")

start = time.time()
transaction = getTransactions_Xlx(transactions_Xlsx)
stop = time.time()
print(f"Related items are: {apriori(transaction)} ")
print(f"Total time: {totalTime(start, stop)}")






