import itertools

def isSorted(permutation):
    test=True
    for v in xrange(len(permutation)):
        test=(test and permutation[v]==(v+1))
    return test
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
def oneSort(inList,stack,outList):
    if (len(inList)==0):
        for i in xrange(len(stack)):
            outList.append(stack.pop(-1))
        verify=isSorted(outList)            
        if (not verify):
            return "cannot be sorted with one stack."
        else:
            return "can be sorted with one stack."
    else:
        if (len(stack)==0):
            stack.append(inList.pop(0))
            #count=count+1
            return oneSort(inList,stack,outList)
        elif (stack[-1]>inList[0]):
            stack.append(inList.pop(0))
            #count=count+1
            return oneSort(inList,stack,outList)
        elif (stack[-1]<inList[0]):
            outList.append(stack.pop(-1))
            #count=count+1
            return oneSort(inList,stack,outList)
        else:
            print "ERROR: UNKNOWN CAUSE"
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
def leftGreedy(inList,numStacks,stackList,outList,count):
    #numStacks=2
    if (numStacks != 0):
        for n in xrange(numStacks):
            stackList.append([])
        #numStacks=0
    if (len(inList)==0):
        if (len(stackList[1])==0):
            for i in xrange(len(stackList[0])):
                outList.append(stackList[0].pop(-1))
                count+=1
            verify=isSorted(outList)
            if (not verify):
                return "cannot be sorted with the left-greedy algorithm."
            else:
                return "can be sorted with the left-greedy algorithm in %d steps." % (count)
        elif (len(stackList[0])==0):
            stackList[0].append(stackList[1].pop(-1))
            count+=1
            return leftGreedy(inList,numStacks,stackList,outList,count)
        elif (stackList[0][-1]>stackList[1][-1]):
            stackList[0].append(stackList[1].pop(-1))
            count+=1
            return leftGreedy(inList,numStacks,stackList,outList,count)
        elif (stackList[0][-1]<stackList[1][-1]):
            outList.append(stackList[0].pop(-1))
            count+=1
            return leftGreedy(inList,numStacks,stackList,outList,count)
    else:
        if (len(stackList[0])==0):
            if (len(stackList[1])==0):
                stackList[1].append(inList.pop(0))
                count+=1
                return leftGreedy(inList,numStacks,stackList,outList,count)
            else:
                stackList[0].append(stackList[1].pop(-1))
                count+=1
                return leftGreedy(inList,numStacks,stackList,outList,count)
        elif (len(stackList[1])==0):
            stackList[1].append(inList.pop(0))
            count+=1
            return leftGreedy(inList,numStacks,stackList,outList,count)
        elif (stackList[0][-1]>stackList[1][-1]):
            stackList[0].append(stackList[1].pop(-1))
            count+=1
            return leftGreedy(inList,numStacks,stackList,outList,count)
        elif (stackList[0][-1]<stackList[1][-1]):
            if (stackList[1][-1]>inList[0]):
                stackList[1].append(inList.pop(0))
                count+=1
                return leftGreedy(inList,numStacks,stackList,outList,count)
            else:
                outList.append(stackList[0].pop(-1))
                count+=1
                return leftGreedy(inList,numStacks,stackList,outList,count)
        else:
            print "ERROR: UNKNOWN CAUSE"
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
def rightGreedy(inList,numStacks,stackList,outList,count):
    #numStacks=2
    for n in xrange(numStacks):
        stackList.append([])
    if (len(inList)==0):
        if (len(stackList[1])==0):
            for i in xrange(len(stackList[0])):
                outList.append(stackList[0].pop(-1))
            verify=isSorted(outList)            
            if (not verify):
                return "cannot be sorted with the right-greedy algorithm on %d stacks." % (numStacks)
            else:
                return "can be sorted with the right-greedy algorithm on %d stacks." % (numStacks)
        elif (len(stackList[0])==0):
            stackList[0].append(stackList[1].pop(-1))
            return rightGreedy(inList,numStacks,stackList,outList,count)
        elif (stackList[0][-1]>stackList[1][-1]):
            stackList[0].append(stackList[1].pop(-1))
            return rightGreedy(inList,numStacks,stackList,outList,count)
        elif (stackList[0][-1]<stackList[1][-1]):
            outList.append(stackList[0].pop(-1))
            return rightGreedy(inList,numStacks,stackList,outList,count)
    else:
        if (len(stackList[1])==0):
            stackList[1].append(inList.pop(0))
            return rightGreedy(inList,numStacks,stackList,outList,count)
        elif (stackList[1][-1]>inList[0]):
            stackList[1].append(inList.pop(0))
            return rightGreedy(inList,numStacks,stackList,outList,count)
        elif (stackList[1][-1]<inList[0]):
            if (len(stackList[0])==0):
                stackList[0].append(stackList[1].pop(0))
                return rightGreedy(inList,numStacks,stackList,outList,count)
            elif (stackList[0][-1]>stackList[1][-1]):
                stackList[0].append(stackList[1].pop(0))
                return rightGreedy(inList,numStacks,stackList,outList,count)
            else:
                outList.append(stackList[0].pop(-1))
                return rightGreedy(inList,numStacks,stackList,outList,count)
        else:
            print "ERROR: UNKNOWN CAUSE"
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
def mySort(inList,numStacks,stackList,outList,count,minNum):
    #numStacks=2
    if (numStacks != 0): #Initialize stacks
        for n in xrange(numStacks):
            stackList.append([])
        #numStacks=0
    if (len(inList)==0): #Check if input is empty.
        if (len(stackList[1])==0): #Check if first stack is empty
            if (len(stackList[0])==0): #Check if second stack is empty
                verify=isSorted(outList)
                if (not verify):
                    return "cannot be sorted with the mySort algorithm."
                else:
                    return "can be sorted with the mySort algorithm in %d steps." % (count)
            else: #Ouput until second stack is empty
                for i in xrange(len(stackList[0])):
                    outList.append(stackList[0].pop(-1))
                    count+=1
            verify=isSorted(outList)
            if (not verify):
                return "cannot be sorted with the mySort algorithm."
            else:
                return "can be sorted with the mySort algorithm in %d steps." % (count)
        elif (len(stackList[0])==0): #If second stack is empty, move from first stack
            stackList[0].append(stackList[1].pop(-1))
            count+=1
            return mySort(inList,numStacks,stackList,outList,count,minNum)
        elif (stackList[0][-1]>stackList[1][-1]): #If top of second is greater than top of first, move from first to second
            stackList[0].append(stackList[1].pop(-1))
            count+=1
            return mySort(inList,numStacks,stackList,outList,count,minNum)
        elif (stackList[0][-1]<stackList[1][-1]): #If top of second is less than top of first, output from second
            outList.append(stackList[0].pop(-1))
            count+=1
            return mySort(inList,numStacks,stackList,outList,count,minNum)
    else:
        if (inList[0]==minNum): #If the current minimum is on top on the input, pass it strat through and add 3 to the count.
            stackList[1].append(inList.pop(0))
            stackList[0].append(stackList[1].pop(-1))
            outList.append(stackList[0].pop(-1))
            count+=3
            return mySort(inList,numStacks,stackList,outList,count,minNum+1)
        elif (len(stackList[1])!=0 and stackList[1][-1]==minNum): #If the current minimum is in the "first" stack, pass it through. ~~OBSOLETE~~ 
            stackList[0].append(stackList[1].pop(-1))
            outList.append(stackList[0].pop(-1))
            count+=2
            return mySort(inList,numStacks,stackList,outList,count,minNum+1)
        elif (len(stackList[0])!=0 and stackList[0][-1]==minNum):#If the current minimum is in the "second" stack, pass it through. ~~OBSOLETE~~ 
            outList.append(stackList[0].pop(-1))
            count+=1
            return mySort(inList,numStacks,stackList,outList,count,minNum+1)
        elif (len(stackList[1])==0): #If the first stack is empty, push an input.
            stackList[1].append(inList.pop(0))
            count+=1
            return mySort(inList,numStacks,stackList,outList,count,minNum)
        elif (len(stackList[0])!=0 and stackList[0][-1]==stackList[1][-1]+1): #if the second stack is not empty and the top is 1 more than the top of the first stack, move the smaller to the top of the second stack.
                stackList[0].append(stackList[1].pop(-1))
                count+=1
                return mySort(inList,numStacks,stackList,outList,count,minNum)
        elif (inList[0]>stackList[1][-1]): #If the next input is greater than the top of the first stack, decide what to do.
            if (len(stackList[0])!=0 and inList[0]>stackList[0][-1] and stackList[1][-1]<stackList[0][-1]):  #If the second stack is not empty and the input > top of second stack and top of first < top of second, moe top of first to second.
                stackList[0].append(stackList[1].pop(-1))
                count+=1
                return mySort(inList,numStacks,stackList,outList,count,minNum)
            else: #Otherwise move input to top of first.
                stackList[1].append(inList.pop(0))
                count+=1
                return mySort(inList,numStacks,stackList,outList,count,minNum)
        elif (inList[0]<stackList[1][-1]): #If the input is less than the top of the first stack, decide what to do.
            if (len(stackList[0])==0 or stackList[1][-1]<stackList[0][-1]): #If the second stack is empty or the top of first is less than top of second, move top of first to second.
                stackList[0].append(stackList[1].pop(-1))
                count+=1
                return mySort(inList,numStacks,stackList,outList,count,minNum)
            elif (inList[0]==stackList[1][-1]-1 or inList[0]>stackList[0][-1]): #If the input is one less than the top of the first or input is greater than top of second, move input to first.
                stackList[1].append(inList.pop(0))
                count+=1
                return mySort(inList,numStacks,stackList,outList,count,minNum)
            elif (inList[0]<stackList[0][-1]): #If input is less than top of second, move input through to second.
                stackList[1].append(inList.pop(0))
                stackList[0].append(stackList[1].pop(-1))
                count+=2
                return mySort(inList,numStacks,stackList,outList,count,minNum)
            else: #Otherwise, output top of second.
                outList.append(stackList[0].pop(-1))
                count+=1
                return mySort(inList,numStacks,stackList,outList,count,minNum)
        else:
            print "ERROR: UNKNOWN CAUSE"
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
perms=list(itertools.permutations([1,2,3,4,5,6]))
##perms=[(5,3,2,4,6,1),(4,2,6,3,5,1),(4,2,5,3,6,1),(3,5,2,4,6,1),(3,2,4,6,5,1)]

##for i in xrange(len(perms)):
##    print "The list %s" % (str(perms[i])), oneSort(list(perms[i]),[],[])
##
##for i in xrange(len(perms)):
##    print "The list %s" % (str(perms[i])), leftGreedy(list(perms[i]),2,[],[])
##    print "The list %s" % (str(perms[i])), rightGreedy(list(perms[i]),2,[],[])
##  
for i in xrange(len(perms)):
##    print "The list %s" % (str(perms[i])), leftGreedy(list(perms[i]),2,[],[],0)
    print "The list %s" % (str(perms[i])), mySort(list(perms[i]),2,[],[],0,1)

