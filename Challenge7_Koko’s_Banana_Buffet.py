def calculate_minimum_speed(piles,k):
    left=1
    right=max(piles)
    result=right
    while left<=right:
        mid=(left+right)//2
        total_hours=0
        for bananas in piles:
            if bananas%mid==0:
                total_hours+=bananas//mid
            else:
                total_hours+=(bananas//mid)+1
        if total_hours<=k:
            result=mid
            right=mid-1
        else:
            left=mid+1
    return result

piles1=[5, 10, 3]
k1=4
if 1<=len(piles1)<=10**4 and all(1<=b<=10**9 for b in piles1) and len(piles1)<=k1<=10**9:
    print('Example 1: The Tight Deadline')
    print('Piles:',piles1)
    print('Time limit (k):',k1)
    print("Result:", calculate_minimum_speed(piles1, k1),"bananas/hr")
else:
    print("Example 1 - Invalid input according to constraints")

piles2=[5, 10, 15, 20]
k2=7
if 1<=len(piles2)<=10**4 and all(1<=b<=10**9 for b in piles2) and len(piles2)<=k2<=10**9:
    print('\nExample 2: The Giant Feast')
    print('Piles:',piles2)
    print('Time limit (k):',k2)
    print("Result:", calculate_minimum_speed(piles2,k2),"bananas/hr")
else:
    print("Example 2 - Invalid input according to constraints")