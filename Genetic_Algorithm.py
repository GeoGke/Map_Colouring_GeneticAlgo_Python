import numpy as np
import random
import math
from random import shuffle
print "Colours encoding:" + "\n" + "Blue 00" + "\n" + "Red 01" + "\n"+"Green 10"+ "\n"+"Yellow 11"


def Create_Problem()


def Fits(P1,P2):  # Parents Fitness P1--->Parents array P2 ---->Neighbours array
    PSC=[] # Parents Score
    n=0
    for x in P1: # Every row of parents array 
        score=0
        for i in range(0,P1.shape[1],2): # Every even column of Parents array
            for j in range(P2.shape[1]): # Every column of Neighbours array
                if P2[i/2,j]==1: # If one node has a Neighbour(==1) 
                    if (P1[n,i]!=P1[n,j*2]) or (P1[n,i+1]!=P1[n,(j*2)+1]): #Checking if 2 Neighbours do not have the same color, they will get one point, else they will get zero
                        score=score+1
        n=n+1
        PSC.append(score)              
    return PSC
def ParSel(S): #Parents Selection : Technique Roulette. S -> Parents Score List (ParSco)
    n1=0 # counter for loop
    SelPar=[] # Declaration of Selected Parents
    NoC=len(S)/2 #number of pairs that will be used to create parents selection
    if(NoC%2!=0):# we need even number for crossover
        NoC=NoC-1  
    while n1<NoC:
        NumSel1=random.randint(0,sum(S)) # random integer between 0 and sum of all elements in Parents Score List ( ParSco)
        NumSum1=0 # keeping the sum of the numbers for loop
        Index1=0 # keeping index of current parent
        for i in S:
            NumSum1=NumSum1+i
            if (NumSum1>=NumSel1): #adding elements of the Parents Score List  until reach the random selected number
                SelPar.append(Index1)
                break
            Index1=Index1+1
        NumSel2 = random.randint(0, sum(S))  # random integer between 0 and sum of all elements in Parents Score List ( ParSco)
        NumSum2 = 0  # keeping the sum of the numbers for loop
        Index2 = 0  # keeping index of current parent
        n2=0 #counter for second inner loop
        while n2<len(S): # Using while loop, in case we have same parent in a row , it will restart
            NumSum2 = NumSum2 + S[n2]
            if (NumSum2 >= NumSel2):  # adding elements of the Parents Score List  until reach the random selected number
                if(Index1==Index2):
                    NumSel2 = random.randint(0, sum(S))
                    NumSum2=0
                    Index2=-1 #they will be zero ( Index2+=1 , n2+=1)
                    n2=-1
                else:
                    SelPar.append(Index2)
                    break
            Index2 = Index2 + 1
            n2=n2+1
        n1=n1+1
    return SelPar
def S_P_Crossover(SP,Par): #Single_Point_Crossover SP ----> SelPars = Selected Parents list, Par ---> Parents Array
    children = np.zeros([len(SP), Par.shape[1]], dtype=int) #Declaring children with zero bits.Par.shape[1]= number of columns in Parents Array
    for i in range(0,len(SP),2): #Taking 2 Parents from Selected Parents List and repeat until finish
        children[i,0:Par.shape[1]/2]=Par[SP[i],0:Par.shape[1]/2] #[i,0:(Parent/2)bits]. Example if we have 32 bits , we choose [0:15]
        children[i,(Par.shape[1]/2)+1:]=Par[SP[i+1],(Par.shape[1]/2)+1:] #example with 32 bits , we choose [16:31]
        children[i+1,0:Par.shape[1]/2] = Par[SP[i+1], 0:Par.shape[1]/2]
        children[i+1,(Par.shape[1]/2)+1:] = Par[SP[i],(Par.shape[1]/2)+1:]
    return children
def mutation(Childr): # Make 10% mutation to children
    nofmut=int(math.ceil(Childr.shape[0]*(10/100.))) # Calculating the number of mutations.1)rows of children array * 10 % 2) Rounding Up the float number(ceiling) 3) float to integer
    for i in range(nofmut):
        CFM=random.randint(0,Childr.shape[0]-1) #Choose randomly Child For Mutation(CFM)
        BPFM=random.randint(0,Childr.shape[1]-1) #Choose randomly Bit Position For Mutation(BPFM)
        if Childr[CFM,BPFM]==0:
            Childr[CFM, BPFM]=1
        else:
            Childr[CFM, BPFM]=0
    return Childr
def PartialRefresh(Pars): #function to recreate Parents Array ,Pars --> Parents . Partial Refresh with 50 % Crossover
    if (Pars.shape[0]%2==0): # we need even number for Crossover
        NoP=Pars.shape[0]/2
    else:
        NoP=(Pars.shape[0]-1)/2
    SelParr=[x for x in range(0,Pars.shape[0])] #Selected Parents for Partial Refresh. Give values [0,1,2...number of random parents]
    RemPar=[] #Remaining Parents
    while(NoP!=len(RemPar)): #loop until we fill Remaining Parents list with (number of parents)/2 elements
        number=random.randint(0,Pars.shape[0]-1) #choose random numbers
        x=number in SelParr #checking if the number exists in the list
        if (x):
            SelParr.remove(number)
            RemPar.append(number)
    return SelParr,RemPar
#Neighbours=np.array([[0,1,1,1,0,0,0,0,0,0,0,0,1,0,1,1],[0,0,1,0,1,0,0,1,1,0,0,0,0,1,1,1],[0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0], #Declaring Neighbours for 16 example
                   [0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0],
                   [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0],
                   [0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
NoNodes=16
NofRPar=80

#while True:
#    try:
#        NoNodes = int(raw_input("Please enter the number of nodes: ")) # Number of nodes
#        break
#    except (ValueError):
#        print "Please put only numbers, not characters"
#NofRPar=NoNodes*5  # Number of random parents
#Neighbours=np.zeros([NoNodes,NoNodes],dtype=int)
#Creating Neighbours Array
#print "Please enter Neighbours for every node. When i=j, it puts automatically zero"
#for i in range(NoNodes):
#    for j in range(i+1,NoNodes):
#        if (i==j):
#            Neighbours[i,j]=0
#        else:
#            while True:
#                try:
 #                   print "Is node ",i+1," with ",j+1," neighbours?"
  #                  number=int(raw_input("Please enter 0(No) or 1(Yes):"))
   #                 if (number==0) or (number==1) :
    #                    Neighbours[i, j]=number
     #                   break
      #              else:
       #                raise ValueError()
        #        except (ValueError):
         #           print "Please put only numbers(0 or 1)"
MaxScore=np.sum(Neighbours) #Max score that one parent can take
parents = np.random.randint(2,size=(NofRPar,NoNodes*2))#Initialize random parents with 0 or 1 and size, Number of nodes * 2 ,because we have 4 colours 2^2bit=4
MaxSolutionTuple=(0,np.zeros([1,parents.shape[1]],dtype=int)) #Initialize MaxSolution with zeros for loop. (0,[0...0])
n=0 # loop counter
SecCha=True #Second Chance with Partial Refresh
avgsc=[] # avg scores
while (MaxSolutionTuple[0]!=MaxScore): # loop until find the max solution or Second Chance is False
    ParSco=Fits(parents,Neighbours)#Parents Score
    MaxSolutionTuple= (max(ParSco), parents[ParSco.index(max(ParSco)), :])
    SelPars=ParSel(ParSco) # Selected Parents
    Children=S_P_Crossover(SelPars,parents)#Crossover of Selected parents
    ChildAfMut=mutation(Children) # Children After Mutation
    parents=ChildAfMut
    avgsc.append(sum(ParSco)/float(len(ParSco))) #we need accurate averages
    # In the first loop , we do not count it (n>0) , so we can check the next 5 average scores
    if (n>0) and (n%5==0) : #cheking for progress in average scores of Parents fitness
        Progress=False # if we have progress in every 5 average scores
        MaxAvgS=avgsc[0] # the first element of the avgsc list is the maximum of the 5 previous loops
        for i in range(1,len(avgsc)):
            if(avgsc[i])>MaxAvgS: # we compare the maximum avgsc[0] with the other 5 averages of avgsc list
                Progress=True
                MaxAvgS=avgsc[i]
        if(Progress): #if we have progress
            avgsc=[] #we recreate the list
            Progress=False
            avgsc.append(MaxAvgS) #add the maximum avgsc as the first element of the list
        else:
            if (SecCha): #Giving Second chance , if we have already used , the program will stop
                SelP,RemP=PartialRefresh(parents)
                random.shuffle(SelP,random.random) #shuffling Selected Parents from Partial Refresh function, so it will be random crossover
                PRChildren=S_P_Crossover(SelP,parents) #Partiar Refresh Children
                for i in range(parents.shape[0]/2): #Recreating Parents array with Partial Refresh Children and Remaining Parents
                    parents[i,:]=PRChildren[i,:]
                    parents[i+25,:]=parents[RemP[i],:]
                SecCha=False
            else:
                break # if we do not have progress , stop and print the maximum solution
    n+=1
print "Solution found",MaxSolutionTuple[1],"with overall score "+str(MaxSolutionTuple[0])+"/"+str(MaxScore)
