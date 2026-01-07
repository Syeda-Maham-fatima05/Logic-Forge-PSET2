def maximize_freelance_profit(deadlines, profits):
    n=len(deadlines)
    job_list=[]
    for i in range(n):
        job_list.append((profits[i],deadlines[i]))
    job_list.sort(reverse=True)
    max_deadline=max(deadlines)
    parent=list(range(max_deadline+1))
    def find(slot):
        if parent[slot]!=slot:
            parent[slot]=find(parent[slot])
        return parent[slot]
    def union(u,v):
        parent[u]=v
    profit=0
    jobs=0
    for p,d in job_list:
        available_slot=find(d)
        if available_slot>0:
            profit+=p
            jobs+=1
            union(available_slot,available_slot-1)
    return [jobs,profit]
Deadlines1=[4, 1, 1, 1]
Profit1=[20, 10, 40, 30]
print('Example 1: The First Hour Rush')
print('Deadlines:',Deadlines1)
print('Profit:',Profit1)
if 1<=len(Deadlines1)<=10**5 and all(1<=d<=10**5 for d in Deadlines1) and all(1<=p<=10**4 for p in Profit1):
    print('Output:', maximize_freelance_profit(Deadlines1,Profit1))
else:
    print('Error: Input does not satisfy constraints!')

Deadlines2=[2, 1, 2, 1, 1]
Profits2=[100, 19, 27, 25, 15]
print('\nExample 2: Overlapping Deadlines')
print('Deadlines:',Deadlines2)
print('Profit:',Profits2)
if 1<=len(Deadlines2)<=10**5 and all(1<=d<=10**5 for d in Deadlines2) and all(1<=p<=10**4 for p in Profits2):
    print('Output:', maximize_freelance_profit(Deadlines2,Profits2))
else:
    print('Error: Input does not satisfy constraints!')
