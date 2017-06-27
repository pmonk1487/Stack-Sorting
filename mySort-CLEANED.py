import itertools

def isSorted(permutation):
    test=True
    for v in xrange(len(permutation)):
        test=(test and permutation[v]==(v+1))
    return test

#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------

def mySort(inList,numStacks,stackList,outList,minNum):
    if (numStacks != 0):
        for n in xrange(numStacks):
            stackList.append([])
    if (len(inList)==0):
        if (len(stackList[1])==0):
            if (len(stackList[0])==0):
                verify=isSorted(outList)
                if (not verify):
                    return 1
                else:
                    return 0
            else:
                for i in xrange(len(stackList[0])):
                    outList.append(stackList[0].pop(-1))

            verify=isSorted(outList)

            if (not verify):
                return 1
            else:
                return 0
        elif (len(stackList[0])==0):
            stackList[0].append(stackList[1].pop(-1))
            return mySort(inList,numStacks,stackList,outList,minNum)
        elif (stackList[0][-1]>stackList[1][-1]):
            stackList[0].append(stackList[1].pop(-1))
            return mySort(inList,numStacks,stackList,outList,minNum)
        elif (stackList[0][-1]<stackList[1][-1]):
            outList.append(stackList[0].pop(-1))
            return mySort(inList,numStacks,stackList,outList,minNum)
    else:
        if (inList[0]==minNum):
            stackList[1].append(inList.pop(0))
            stackList[0].append(stackList[1].pop(-1))
            outList.append(stackList[0].pop(-1))
            return mySort(inList,numStacks,stackList,outList,minNum+1)
        elif (len(stackList[1])!=0 and stackList[1][-1]==minNum):
            stackList[0].append(stackList[1].pop(-1))
            outList.append(stackList[0].pop(-1))
            return mySort(inList,numStacks,stackList,outList,minNum+1)
        elif (len(stackList[0])!=0 and stackList[0][-1]==minNum):
            outList.append(stackList[0].pop(-1))
            return mySort(inList,numStacks,stackList,outList,minNum+1)
        elif (len(stackList[1])==0):
            stackList[1].append(inList.pop(0))
            return mySort(inList,numStacks,stackList,outList,minNum)
        elif (len(stackList[0])!=0 and stackList[0][-1]==stackList[1][-1]+1):
                stackList[0].append(stackList[1].pop(-1))
                return mySort(inList,numStacks,stackList,outList,minNum)
        elif (inList[0]>stackList[1][-1]):
            if (len(stackList[0])!=0 and inList[0]>stackList[0][-1] and stackList[1][-1]<stackList[0][-1]):
                stackList[0].append(stackList[1].pop(-1))
                return mySort(inList,numStacks,stackList,outList,minNum)
            else:
                stackList[1].append(inList.pop(0))
                return mySort(inList,numStacks,stackList,outList,minNum)
        elif (inList[0]<stackList[1][-1]):
            if (len(stackList[0])==0 or stackList[1][-1]<stackList[0][-1]):
                stackList[0].append(stackList[1].pop(-1))
                return mySort(inList,numStacks,stackList,outList,minNum)
            elif (inList[0]==stackList[1][-1]-1 or inList[0]>stackList[0][-1]):
                stackList[1].append(inList.pop(0))
                return mySort(inList,numStacks,stackList,outList,minNum)
            elif (inList[0]<stackList[0][-1]):
                stackList[1].append(inList.pop(0))
                stackList[0].append(stackList[1].pop(-1))
                return mySort(inList,numStacks,stackList,outList,minNum)
            else:
                outList.append(stackList[0].pop(-1))
                return mySort(inList,numStacks,stackList,outList,minNum)
        else:
            print "ERROR: UNKNOWN CAUSE"
            
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------

perms=list(itertools.permutations([1,2,3,4,5,6]))
##perms=[(5,3,2,4,6,1),(4,2,6,3,5,1),(4,2,5,3,6,1),(3,5,2,4,6,1),(3,2,4,6,5,1)]
 
for i in xrange(len(perms)):
    if mySort(list(perms[i]),2,[],[],1) == 1: #print permutation if sorting fails
        print "%s" % (str(perms[i]))
