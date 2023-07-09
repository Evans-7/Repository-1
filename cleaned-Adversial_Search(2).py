#!/usr/bin/env python
# coding: utf-8

# **Assignment 4: Adverserial Search (Given: 28 Feb 2023, Due: 19 Mar 2023)**
# 

# **General instructions**
# 
# * Solutions are to be typed in the `.ipynb` file provided and uploaded in the lab course page in Moodle on the due date. 
# * Your code should be well commented and should be compatible with python3.
# * For this assignment, you are allowed to import the libraries `random` and `copy` of python3. No other libraries may be imported.
# 

# # Adverserial search

# The Tic-Tac-Toe game starts on a 3x3 grid with two players "X" and "O" who take turns and play. The rules are as follows: each player gets a turn with player "X" (resp. "O") writing an "X" (resp. "O") in an empty cell of the grid. The game starts with the move of the "O" player. The first player to write on three horizontal or vertical or diagonal cells wins.

# (a) Use the minimax strategy to design an AI that plays the game optimally. The leaf nodes where "X" wins gets 1 and "O" wins gets -1 and neither wins gets a zero. A sample game play is given below.

# In[62]:


l3=[]
dep=0
def minimax(l):
    (v3,index,depth)=maxval(l)
    return (index,depth)
def maxval(l):
    global dep
    t=isterminal(l)
    if t==1 or t==-1 or t==0:
        dep=dep+1
        return (t,None,1)
    else:
        v=-3
        l5=[]
        for i in range(len(l)):
            if l[i]=="*":
                l1=l.copy()#a copy of the list is made and passed to the function
                l1[i]="X"#adding X since this is maxval function
                (val2,indi,depth)=minval(l1)
                l5.append(depth)
                if val2>=v:
                    v=val2
                    newtuple1=(val2,i,max(l5)+1)#height is calculated by adding 1 to the current height from the leaf node
        return newtuple1
def minval(l):
    global dep
    t=isterminal(l)
    if t==1 or t==-1 or t==0:
        dep=dep+1#dep is caulcating the number of leaf nodes
        #if l not in l3:
         #   l3.append(l)
        return (t,None,1)
    else:
        v1=3
        l6=[]
        for i in range(len(l)):
            if l[i]=="*":
                l2=l.copy()
                l2[i]="O"
                (val3,indi,depth)=maxval(l2)
                l6.append(depth)
                if val3<=v1:
                    v1=val3
                    newtuple2=(val3,i,max(l6)+1)
        return newtuple2
    
def isterminal(l):#states being hard coded
    if l[0]+l[1]+l[2]=="XXX":
        return 1
    elif l[0]+l[1]+l[2]=="OOO":
        return -1
    elif l[0]+l[3]+l[6]=="XXX":
        return 1
    elif l[0]+l[3]+l[6]=="OOO":
        return -1
    elif l[0]+l[4]+l[8]=="XXX":
        return 1
    elif l[0]+l[4]+l[8]=="OOO":
        return -1
    elif l[6]+l[4]+l[2]=="XXX":
        return 1
    elif l[6]+l[4]+l[2]=="OOO":
        return -1
    elif l[6]+l[7]+l[8]=="XXX":
        return 1
    elif l[6]+l[7]+l[8]=="OOO":
        return -1
    elif l[2]+l[5]+l[8]=="XXX":
        return 1
    elif l[2]+l[5]+l[8]=="OOO":
        return -1
    elif l[3]+l[4]+l[5]=="OOO":
        return -1
    elif l[3]+l[4]+l[5]=="XXX":
        return 1
    elif l[1]+l[4]+l[7]=="OOO":
        return -1
    elif l[1]+l[4]+l[7]=="XXX":
        return 1
    else:
        for i in range(len(l)):
            if l[i]=="*":
                return 3
        else:
            return 0
l5=["*"]*9
print(l5)
count=0
t=isterminal(l5)
l7=[]
while t==3:#3 is returned as long as the game does not end
    expdep=0
    n=int(input("enter the position"))
    l5[n-1]="O"
    t=isterminal(l5)
    if t==1 or t==-1 or t==0:
        break
    (index1,dept)=minimax(l5)
    l5[index1]="X"
    l7.append(dept)
    for i in range(3):
        print(l5[3*i],l5[3*i+1],l5[3*i+2])#printing the current maze
    t=isterminal(l5)
    if t==1 or t==-1 or t==0:
        break
print("\n")        
for i in range(3):
        print(l5[3*i],l5[3*i+1],l5[3*i+2]) 
print(len(l3))
print(dep)#number of leaves
print(max(l7))#depth
  


    
    
        
    


# 
# 
# 
# # (b) Modify the previous answer to calculate in each game the following:
# 
# * the maximum depth of exploration of the game tree in a game, and
# * number of leaves of the game tree whose scores were computed be the end of the game.
# 
# 
# 

# In[ ]:





# (c) Implement alpha-beta pruning minimax search to solve the Tic-Tac-Toe and repeat part (b). 
# 
# Compare your results with vanilla minimax search and see on which all parameters part (b) is alpha-bet pruning search better. Also obtain by what factor is it better.

# In[60]:


leaf=0
y=0
def alphaminimax(l):
    
    (value,index,depth2)=alphamaxval(l,-1000,1000)#passig -1000 ans 1000 as alpha and beta
    return (index,depth2)
def alphamaxval(l,a,b):
    global y
    global leaf
    terminal=isterminal(l)
    if terminal==1 or terminal==0 or terminal==-1:
        if y==0:
            print(y)
            leaf=leaf+1
            print(leaf)
        return(terminal,None,0)
    else:
        l8=[]
        currval=-1000
        for i in range(len(l)):
            if l[i]=="*":
                newlist=l.copy()
                newlist[i]="X"
                v2,a2,depth1=alphaminval(newlist,a,b)
                l8.append(depth1)
                if v2>currval:
                    currval,index=v2,i
                #making alpha the greater of a and currval
                if currval>=b:
                    return(currval,i,max(l8)+1)#pruning happens here...if the current value is greater than b,then the AI does not have to look for any further coz 
                #maximum is anyways going to take a value greater than b,and since the ancestor node somehwere on the min level already
                #has an option of chooosing a value lesser than the current value,it is obviiously going to choose that
                a=max(a,currval)
        return (currval,index,max(l8)+1) 
def alphaminval(l,a,b):
    global y
    global leaf
    terminal=isterminal(l)
    if terminal==1 or terminal==0 or terminal==-1:
        if y==0:
            leaf=leaf+1
        return(terminal,None,0)
    else:
        l9=[]
        currval1=1000#declaring current value 1 to be a value greater than 1
        for i in range(len(l)):
            if l[i]=="*":
                newlist=l.copy()
                newlist[i]="O"
                v2,a2,depth1=alphamaxval(newlist,a,b)
                l9.append(depth1)
                if v2<currval1:
                    currval1,index=v2,i
                    #making alpha the greater of a and currval
                if currval1<=a:
                    return(currval1,i,max(l9)+1)#pruning 2 happens here
                #since the current value is lesser than a ,some ancestor node at the max value already has an option that is greater than a and min node is 
                #obviously going to choose a value that is lesser than a...so going any deeper is useless
        
                b=min(b,currval1)
        return (currval1,index,max(l9)+1)  
    
    
lis=["*"]*9
print(lis)
l10=[]
terminal=isterminal(lis)
while terminal==3:
    n=int(input("enter the position"))
    lis[n-1]="O"
    t=isterminal(lis)
    if t==1 or t==-1 or t==0:
        break
    index1,depth2=alphaminimax(lis)
    lis[index1]="X"
    y=1
    l10.append(depth2)
    for i in range(3):
        print(lis[3*i],lis[3*i+1],lis[3*i+2])
    t=isterminal(lis)
    if terminal==1 or terminal==-1 or terminal==0:
        break                
print(leaf)#prints the number of leaves
print(max(l10))#prints the depth


# In[ ]:





# In[ ]:




