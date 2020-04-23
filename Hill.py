import time, random
from random import shuffle


def TimeNow():
    return int(round(time.time() * 1000))


def Check(queensaList):
    le = len(queensaList)
    for inde in range(le):
        for jnde in range(le):
            deltaRow = abs(inde - jnde)
            deltaCol = abs(queensaList[inde] - queensaList[jnde])
            if (deltaRow == deltaCol or queensaList[inde] == queensaList[
                jnde]) and inde != jnde:  # deltaRow == deltaCol
                # to check
                # the digonal while queensList[i] == queensList[j] is to check row conflict (Note: Implicitly,
                # it doesnt have to check for column conflict)
                return False
    for indec in range(le):
        if queensaList[indec] == 0:
            return False
    return True


def Check0(QueensList, indd):
    for jnd in range(indd):
        deltaRow = abs(indd - jnd)
        deltaCol = abs(QueensList[indd] - QueensList[jnd])
        if (deltaRow == deltaCol) and indd != jnd:
            return False
    return True


def nextList(QueensL, index, Qn):
    possibleV = []
    for ii in range(1, Qn + 1):
        possibleV.append(ii)
    set2 = set(possibleV)
    set1 = set(QueensL)
    nextSet = set2 - set1
    Next_List_I = list(nextSet)
    random.shuffle(Next_List_I)
    Next_List = list(Next_List_I)
    for jj in range(len(Next_List_I)):
        QueensLi = list(QueensL)
        QueensLi[index] = int(Next_List_I[jj])
        if not Check0(QueensLi, int(index)):
            Next_List.remove(Next_List_I[jj])
    return Next_List


def Hill(QueensOrder, NumberOfQueens, ic, Stochast):
    all_list = []
    all_list.append(list(QueensOrder))
    for icount in range(ic, NumberOfQueens):
        print(icount, QueensOrder)
        QU, iM, nQ = list(QueensOrder), int(icount), int(NumberOfQueens)
        next_list = nextList(QU, iM, nQ)
        print("OrgFunction", QueensOrder, icount, NumberOfQueens, next_list)
        if Stochast:
            random.shuffle(next_list)
        if len(next_list) > 0:
            QueensOrder[icount] = next_list[0]
            all_list.append(list(QueensOrder))
            print(icount, len(next_list), QueensOrder)
        else:
            c = Check(QueensOrder)
            if not c:
                print(icount, c, QueensOrder)
                return False, QueensOrder, all_list
    return True, QueensOrder, all_list


def hillStart(Initial, Qnumber, StochasChoix):
    queensList = []
    for i in range(Qnumber):
        queensList.append(0)
    if Qnumber >= Initial >= 0:
        queensList[0] = Initial
        condition, nl, lists = Hill(queensList, Qnumber, 1, StochasChoix)
        print(condition, nl, lists)
        return condition, nl, lists
    return False
 

if __name__ == '__main__':
    hillStart(4,5,True)
