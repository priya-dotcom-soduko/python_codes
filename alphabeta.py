max_val=1000
min_val=-1000

def alpha_beta(depth,node_value,maxp,v,A,B):
    if depth==3:
        return v[node_value]
    if maxp:
        best=min_val
        for i in range(0,2):
            value=alpha_beta(depth+1,node_value*2+i,False,v,A,B)
            best=max(best,value)
            A=max(A,best)
            if B<=A:
                break
        return best
    
    else:
        best=max_val
        for i in range(0,2):
            value=alpha_beta(depth+1,node_value*2+i,True,v,A,B)
            best=min(best,value)
            A=min(A,best)
            if B<=A:
                break
        return best
        
graph=[]
x=int(input("enter the number of nodes: "))
for i in range(x):
    y=int(input("enter the node value: "))
    graph.append(y)

depth=int(input("depth: "))
node=int(input("node: "))

print("optimal value: ",alpha_beta(depth,node,True,graph,min_val,max_val))