
# Q2 CALCULATE EXPONANTIAL
def calculateExponantial(base, exp):
    
    if(exp == 1):
        return base
    if(exp % 2 == 0):
        return (base**(exp/2))*calculateExponantial(base , (exp/2))
    else:
        return (base**((exp+1)/2))*calculateExponantial(base , ((exp-1)/2))

#END Q2


#BEGINNIG OF Q1

#GRAPH RESPRESENTATION USING DICTIONARY
graph = {
        "CSE102" : ["CSE241"],
        "CSE241" : ["CSE222"],
        "CSE222" : ["CSE321"],
        "CSE211" : ["CSE321"],
        "CSE321" : ["CSE422"],
        "CSE422" : []
        }


#DFS ALGO

def  dfs(graph):
     
    visited = []
    finishOrder = []
    stack = []
    
    def dfsRec(node):
        if(node not in visited):
            visited.append(node)
            stack.append(node)
            for node in graph[node]:
                dfsRec(node)
            finishOrder.append(stack.pop())
                    
        
    for node in graph.keys():
        if(node not in visited):
            dfsRec(node)
    
    return finishOrder

# TOPOLOGICAL SORT V1 USING DFS
def topologicalSortV1(graph):
    result = dfs(graph)
    result.reverse()
    return result




#TOPOLOGICAL SORT V2 not DFS
def topologicalSortV2(graph):

    finishOrder = []
    count = {}
    keyList = graph.keys()
    def fillWithZero():
        
        for key in keyList:
            count[key] = 0
    
    def findCount():
        for key in keyList:
            for node in graph[key]:
                count[node] = count[node] +1
    
    def findSource():      
        for key in keyList:
            if(count[key] == 0):
                finishOrder.append(key)
                count[key] = -1
                decraseCount(graph[key])

    def decraseCount(vertex):
        
        for edges in vertex:
            count[edges] -=1
    

    fillWithZero()
    findCount()
    findSource()
    return finishOrder  
    
#END OF Q3

#BEGINNIG OF Q2

#SUDOKU REPRESENTATION USING 2D ARRAY
sudoku  = [ [0,0,3,9,0,0,7,6,0],
            [0,4,0,0,0,6,0,0,9],
            [6,0,7,0,1,0,0,0,4],
            [2,0,0,6,7,0,0,9,0],
            [0,0,4,3,0,5,6,0,0],
            [0,1,0,0,4,9,0,0,7],
            [7,0,0,0,9,0,2,0,1],
            [3,0,0,2,0,0,0,4,0],
            [0,2,9,0,0,8,5,0,0]]

 

#SUDOKU SOLVER 
def sudokuSolver9x9(sudoku):
   
    def isValid(val,r,c):
            result = True
            if(val in sudoku[r]):
                result = False
            if(result and (val in [sudoku[i][c] for i in range(0,9)])):
                result = False
            if(result and (val in [sudoku[i][j] for i in range(((r//3)*3),(((r//3)*3)+3)) for j in range(((c//3)*3),(((c//3)*3)+3))])):
                result = False
            
            return result
        
    def solve (sudoku , r=0,c=0):
         
        if(r == 9):
            return True
        elif(c == 9):
            return solve(sudoku,r+1,0)
        elif (sudoku[r][c] != 0):
            return solve(sudoku , r,c+1)
        else :
            for i in range (1,10):
                if(isValid(i,r,c)):
                    sudoku[r][c] = i
                    if(solve(sudoku,r,c+1)):
                        return True
                else: 
                    sudoku[r][c] = 0
            return False
            
    solve(sudoku)
        
        
#PRINT SUDOKU
def printSudoku():
        
        for col in sudoku:
            print("\t",col,"\n")

#END OF THE Q3




#DRIVER CODE
def driver():
    while(True):
        print("1-) TOPOLOGICAL SORT\n2-) CALCULATE EXPONANTIAL AT LOGN TIME\n3-) SUDOKU 9X9 SOLVER\n0-) Exit\n")
        select = int(input("Choice : "))
        if(select == 1):
            while(True):
                print("\t1-) V1\n\t2-) V2\n\t0-) Back to the Menu")
                select2 = int(input("Choice : "))
                if(select2 == 1):
                    print("\nResult: ",topologicalSortV1(graph))
                    
                elif(select2 == 2):
                    print("\nResult : ",topologicalSortV2(graph))
                    
                elif(select2 == 0):
                    break
                else :
                    print("\nPlease Enter Right Choice\n")
        elif(select == 2):
            
            base = int(input("\tPlease Enter Base :"))
            exp = int(input("\tPlase Exponantial :"))
            print("\tResult : ", calculateExponantial(base,exp))
        elif(select == 3):
            
            print("\tSudoku Solver\n")
            print("\tOld Sudoku Grid\n")
            printSudoku()
            print("\tSolved Sudoku\n")
            sudokuSolver9x9(sudoku)
            printSudoku()
        elif(select == 0):
            break
        
        else :
            print("\nPlease Enter Right Choice\n")
#CALL DRIVER   
driver()