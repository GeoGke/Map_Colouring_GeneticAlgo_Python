import numpy as np
import random
import math
from random import shuffle

print ("Colours encoding:" + "\n" + "Blue 00" + "\n" + "Red 01" + "\n"+"Green 10"+ "\n"+"Yellow 11")

'''
def Fits(P1,P2):  # GA_Population Fitness P1--->GA_Population array P2 ---->MAP array
    PSC=[] # GA_Population Score
    n=0
    for x in P1: # Every row of GA_Population array 
        score=0
        for i in range(0,P1.shape[1],2): # Every even column of GA_Population array
            for j in range(P2.shape[1]): # Every column of MAP array
                if P2[i/2,j]==1: # If one node has a Neighbour(==1) 
                    if (P1[n,i]!=P1[n,j*2]) or (P1[n,i+1]!=P1[n,(j*2)+1]): #Checking if 2 Cities do not have the same color, they will get one point, else they will get zero
                        score=score+1
        n=n+1
        PSC.append(score)              
    return PSC

def ParSel(S): #GA_Population Selection : Technique Roulette. S -> GA_Population Score List (ParSco)
    n1=0 # counter for loop
    SelPar=[] # Declaration of Selected GA_Population
    NoC=len(S)/2 #number of pairs that will be used to create GA_Population selection
    if(NoC%2!=0):# we need even number for crossover
        NoC=NoC-1  
    while n1<NoC:
        NumSel1=random.randint(0,sum(S)) # random integer between 0 and sum of all elements in GA_Population Score List ( ParSco)
        NumSum1=0 # keeping the sum of the numbers for loop
        Index1=0 # keeping index of current parent
        for i in S:
            NumSum1=NumSum1+i
            if (NumSum1>=NumSel1): #adding elements of the GA_Population Score List  until reach the random selected number
                SelPar.append(Index1)
                break
            Index1=Index1+1
        NumSel2 = random.randint(0, sum(S))  # random integer between 0 and sum of all elements in GA_Population Score List ( ParSco)
        NumSum2 = 0  # keeping the sum of the numbers for loop
        Index2 = 0  # keeping index of current parent
        n2=0 #counter for second inner loop
        while n2<len(S): # Using while loop, in case we have same parent in a row , it will restart
            NumSum2 = NumSum2 + S[n2]
            if (NumSum2 >= NumSel2):  # adding elements of the GA_Population Score List  until reach the random selected number
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

def S_P_Crossover(SP,Par): #Single_Point_Crossover SP ----> SelPars = Selected GA_Population list, Par ---> GA_Population Array
    children = np.zeros([len(SP), Par.shape[1]], dtype=int) #Declaring children with zero bits.Par.shape[1]= number of columns in GA_Population Array
    for i in range(0,len(SP),2): #Taking 2 GA_Population from Selected GA_Population List and repeat until finish
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

def PartialRefresh(Pars): #function to recreate GA_Population Array ,Pars --> GA_Population . Partial Refresh with 50 % Crossover
    if (Pars.shape[0]%2==0): # we need even number for Crossover
        NoP=Pars.shape[0]/2
    else:
        NoP=(Pars.shape[0]-1)/2
    SelParr=[x for x in range(0,Pars.shape[0])] #Selected GA_Population for Partial Refresh. Give values [0,1,2...number of random GA_Population]
    RemPar=[] #Remaining GA_Population
    while(NoP!=len(RemPar)): #loop until we fill Remaining GA_Population list with (number of GA_Population)/2 elements
        number=random.randint(0,Pars.shape[0]-1) #choose random numbers
        x=number in SelParr #checking if the number exists in the list
        if (x):
            SelParr.remove(number)
            RemPar.append(number)
    return SelParr,RemPar
'''
def Map_Initiation(choice):
    if choice==1:
        NumberOfCities=16 
        GA_Population_size=80 #MAP size multiplied by 5 
        MAP=np.array([[0,1,1,1,0,0,0,0,0,0,0,0,1,0,1,1],[0,0,1,0,1,0,0,1,1,0,0,0,0,1,1,1],[0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0], 
                   [0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0],
                   [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0],
                   [0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
    else: 
        while True:
            try:
                NumberOfCities = int(input("Please enter the size of the map: ")) 
                break
            except (ValueError):
                print ("Please use only numbers, not characters")
        GA_Population_size=NumberOfCities*5  
        MAP=np.zeros([NumberOfCities,NumberOfCities],dtype=int)
        print ("Please type the relations between cities on the map. When i=j, the value is automatically zero")
        #Only the values above the main diagonal of the MAP matrix are calculated 
        for i in range(NumberOfCities):
            for j in range(i+1,NumberOfCities):
                if (i==j):
                    MAP[i,j]=0
                else:
                    while True:
                        try:
                            print ("Is city ",i+1," with ",j+1," neighbour?")
                            number=int(input("Please enter 0(No) or 1(Yes):"))
                            if (number==0) or (number==1) :
                                MAP[i, j]=number
                                break
                            else:
                                raise ValueError()
                        except ValueError as e:
                           print ("Please type only numbers(0 or 1)")
        return NumberOfCities,GA_Population_size,MAP
'''
def SolutionFinder_Process(BestScore_Solution_tuple,Solution_MaxScore,GA_Population,MAP):
    n=0 # loop counter
    Second_Chance=True #Second Chance with Partial Refresh
    avgsc=[] # avg scores
    while (BestScore_Solution_tuple[0]!=Solution_MaxScore): # loop until find the max solution or Second Chance is False
        ParSco=Fits(GA_Population,MAP)#GA_Population Score
        BestScore_Solution_tuple= (max(ParSco), GA_Population[ParSco.index(max(ParSco)), :])
        SelPars=ParSel(ParSco) # Selected GA_Population
        Children=S_P_Crossover(SelPars,GA_Population)#Crossover of Selected GA_Population
        ChildAfMut=mutation(Children) # Children After Mutation
        GA_Population=ChildAfMut
        avgsc.append(sum(ParSco)/float(len(ParSco))) #we need accurate averages
        # In the first loop , we do not count it (n>0) , so we can check the next 5 average scores
        if (n>0) and (n%5==0) : #cheking for progress in average scores of GA_Population fitness
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
                    SelP,RemP=PartialRefresh(GA_Population)
                    random.shuffle(SelP,random.random) #shuffling Selected GA_Population from Partial Refresh function, so it will be random crossover
                    PRChildren=S_P_Crossover(SelP,GA_Population) #Partiar Refresh Children
                    for i in range(GA_Population.shape[0]/2): #Recreating GA_Population array with Partial Refresh Children and Remaining GA_Population
                        GA_Population[i,:]=PRChildren[i,:]
                        GA_Population[i+25,:]=GA_Population[RemP[i],:]
                    SecCha=False
                else:
                    break # if we do not have progress , stop and print the maximum solution
        n+=1
    return BestScore_Solution_tuple
'''  
    
def Genetic_Algorithm_Process():
    while True:
        try:
            choose_map = int(input("Would you like to use the default map? Type 1 for Yes and 0 for No."))
            if  (choose_map==1) or (choose_map==0):
                break 
            else:
                print("Pleaste answer with 1 or 0")
        except ValueError as e:
            print("Pleaste answer with 1 or 0")
    NumberOfCities,GA_Population_size,MAP=Map_Initiation(choose_map)
    Solution_MaxScore=np.sum(MAP)
    #Number of possible colours is 4. Every candidate solution needs 2 bits(2^2 bits=4) to define the possible combination of colours, so this is multiplied by the number of cities.
    GA_Population=np.random.randint(2,size=(GA_Population_size,NumberOfCities*2))
    BestScore_Solution_tuple=(0,np.zeros([1,GA_Population.shape[1]],dtype=int)) #(0,[0...0])
    return SolutionFinder_Process(BestScore_Solution_tuple,Solution_MaxScore,GA_Population,MAP),Solution_MaxScore

BestScore_Solution_tuple,Solution_MaxScore=Genetic_Algorithm_Process()
print ("Solution found",[1],"with overall score "+str(BestScore_Solution_tuple[0])+"/"+str(Solution_MaxScore))


            
