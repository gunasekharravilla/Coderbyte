def EightQueens(strArr): 
    x = list([[int(i) for i in p[1:-1].split(',')[0]] for p in strArr])
    y = list([[int(i) for i in p[1:-1].split(',')[1]] for p in strArr])
    #queenList = list([ [int(i) for i in p[1:-1].split(',')[0], int(j) for j in p[1:-1].split(',')[1]] for p in strArr ])
    queenList = []
    for i in range(0,len(x)):
        queenList.append((x[i][0],y[i][0]))

    for i in range(0, len(x)-1):
        for j in range(i+1, len(x)):
            x1, y1 = queenList[i]
            x2, y2 = queenList[j]
            if x1 == x2 or y1 == y2 or (x1 == y2 and x2 == y1) or x1 - y1 == x2 - y2:
                return '(' + str(x1) + ',' + str(y1) + ')'
    return 'true'
    
# keep this function call here  
print EightQueens(raw_input())
