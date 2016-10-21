from numpy import*
from pylab import*
#seed(3)
N = 11 # number of neurons
spins = zeros((N,N))
# star pattern
pat1 = array([[-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1],[-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1],[1,1,1,1,-1,-1,-1,1,1,1,1],[-1,1,-1,-1,-1,-1,-1,-1,-1,1,-1],[-1,-1,1,-1,-1,1,-1,-1,1,-1,-1],[-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1],[-1,-1,1,-1,-1,1,-1,-1,1,-1,-1],[-1,1,-1,-1,1,-1,-1,1,-1,1,-1],[1,-1,1,1,-1,-1,-1,1,1,-1,1],[1,1,-1,-1,-1,1,-1,-1,-1,1,1]])
# Z pattern
pat2 = array([[1,1,1,1,1,1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1,1,1,1,1,1]])
alpha = 0.1
beta = 0.6
patcount = array([0,0])
      

               
J = zeros((N,N,N,N))                     
# Loop that creates an 4 dimensional J matrix 
for a in range(N):
    for b in range(N):
        pi = pat1[a,b]
        for c in range(N):
            for d in range(N):
                J[a,b,c,d] = pi * pat1[c,d]

# Learning Algorithm
for a in range(N):
    for b in range(N):
        pi = pat2[a,b]
        for c in range(N):
            for d in range(N):
                J[a,b,c,d] = alpha*J[a,b,c,d] + beta*pi*pat2[c,d]
                    
for q in range(2000):                    
    # Creates random spin state that will be used later
    for i in range(N):
         for j in range(N):
             p = rand()
             if p < 0.5:
                 spins[i,j] = -1
             else:
                 spins[i,j] = 1



    E = zeros((N,N,N,N)) # Energy of the system


                    
    spinsold = spins
    spinsnew = spins+1

    # Uses the energy to make our random spin orientation exactly like the stored one(s)
    # In other words, it is recalling a memory
    while (spinsold == spinsnew).any() == False:
        spinsold = spins                           
        for i in range(N):
            for j in range(N):
                si = spins[i,j]
                Esum = 0                
                for m in range(N):
                    for n in range(N):
                        sj = spins[m,n]
                        if i != m or j != n:
                            Esum += -J[i,j,m,n]*si*sj
                if Esum > 0:
                    spins[i,j] = -si
        spinsnew = spins
        
    # Creates a matrix that is similar to the J, but it shows energy instead
    for i in range(N):
       for j in range(N):
           si = spins[i,j]
           for m in range(N):
               for n in range(N):
                   sj = spins[m,n]
                   if i != m or j != n:
                       E[i,j,m,n] += -J[i,j,m,n]*si*sj
                   else:
                        E[i,j,m,n] = 0            


    # spins2 = spins

    # for k in range(N):
    #     for l in range(N):
    #         if spins2[k,l] == -1:
    #             spins2[k,l] = 0
                
    if (spins == pat1).all() == True:
        patcount[0] += 1
    elif (-spins == pat1).all() == True:
        patcount[0] += 1
    elif (spins == pat2).all() == True:
        patcount[1] += 1
    else:
        patcount[1] += 1

print patcount

val = 3+10*rand(5)    # the bar lengths
pos = arange(2)+.5    # the bar centers on the y axis

barh(pos,patcount, align='center')
yticks(pos, ('Pattern 1', 'Pattern 2'))
xlabel('Counts')
title('Number of times each memory was recalled')
grid(True)

show()