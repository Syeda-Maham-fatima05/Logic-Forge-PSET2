def count_payment_combinations(coins,total_sum):
    def make_sum(index,remaining):
        if remaining==0:
            return 1
        if remaining<0:
            return 0
        if index==len(coins):
            return 0
        include=make_sum(index,remaining-coins[index])
        skip=make_sum(index+1,remaining)
        return include+skip
    return make_sum(0,total_sum)

coins1=[1,2,3]
target1=4
if not 1<=len(coins1)<=1000 and not 1<=target1<=1000:
    for i in coins1:
        if not 1<=i<=1000:
            print("Enter numbers in range of 1-1000")
print("Case A: Small Change")
print("Target Sum: ",target1)
print("Vault Coins: ",coins1)
print("Total ways: ",count_payment_combinations(coins1,target1))
coins2=[2,5,3,6]
target2=10
if not 1<=len(coins2)<=1000 and not 1<=target2<=1000:
    for i in coins2:
        if not 1<=i<=1000:
            print("Enter numbers in range of 1-1000")
print("\nCase B: Specific Denominations")
print("Target Sum: ",target2)
print("Vault Coins: ",coins2)
print("Total ways: ",count_payment_combinations(coins2,target2))
coins3=[4]
target3=5
if not 1<=len(coins1)<=1000 and not 1<=target1<=1000:
    for i in coins1:
        if not 1<=i<=1000:
            print("Enter numbers in range of 1-1000")
print("\nCase C: The Impossible Payment")
print("Target Sum: ",target3)
print("Vault Coins: ",coins3)
print("Total ways: ",count_payment_combinations(coins3,target3))