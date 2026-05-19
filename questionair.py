
questions = [

    ["The number of edges from the root to the node is called   of the tree?", "Height", "Depth ","Length","Width",2],
    ["The number of edges from the node to the deepest leaf is called   of the tree?","Height","Depth","Length","Width", 1],
    ["What is a full binary tree?","Each node has exactly zero or two children","Each node has exactly two children","All the leaves are at the same level","Each node has exactly one or two children",1],
    ["What is a complete binary tree?","Each node has exactly zero or two children","A binary tree which is completely filled with the possible exception of the bottom level, which is filled from right to left","A binary tree, which is completely filled, with the possible exception of the bottom level, which is filled from left to right"," A tree In which all nodes have degree 2", 3]
    
]

prizes = [100000, 320000, 400000, 450000 ]
          
i = 0         
for question in questions:
    print(question[0])
    print(f"a. {question[1]}") 
    print(f"b. {question[2]}") 
    print(f"c. {question[3]}") 
    print (f"d. {question[4]}")

    
    a = int(input("Enter your answer. 1 for a, 2 for b, 3 for c, 4 for d\n")) 
    if(question [5] ==a):
       print("Correct Answer")
    else:
       print (f"Incorrect, the correct answer was {question[5]}")
       print("Better luck next time!")
       break
    print (f"You won {prizes[i]}")
    i +=1