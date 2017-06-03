import copy
M=1000000
def Floyd(G):
    n=len(G)
    path=copy.deepcopy(G)
    for k in range(0,n):
        for i in range(0,n):
            for j in range(0,n):
                print("Comparing path[%s][%s] and {path[%s][%s]+path[%s][%s]}"%(i,j,i,k,k,j))
                print("Former path[%s][%s] = %s"%(i,j,path[i][j]))
                path[i][j]=min(path[i][j],path[i][k]+path[k][j])
                print("Present path[%s][%s] = %s\n"%(i,j,path[i][j]))
    return path
        

if __name__=='__main__':
    G=[
        [0,30,15,M,M,M],
        [5,0,M,M,20,30],
        [M,10,0,M,M,15],
        [M,M,M,0,M,M],
        [M,M,M,10,0,M],
        [M,M,M,30,10,0]
        ]
    print("---------------Floyd----------------")
    path=Floyd(G)
    print("Graph = ")
    for i in range(0,len(G)):
        print (path[i])
