def can_balance_scales(arr):
    total_sum=sum(arr)
    if total_sum%2!=0:
        return total_sum,False
    else:
        target=total_sum//2
        def can_make_sum(index,remaining):
            if remaining==0:
                return True
            if remaining<0 or index==len(arr):
                return False
            include=can_make_sum(index+1,remaining-arr[index])
            exclude=can_make_sum(index+1,remaining)
            return include or exclude
        return total_sum,can_make_sum(0,target)

arr1=[1,5,11,5]
sum1,can_split1=can_balance_scales(arr1)
print(f"Total Sum of Array:{arr1} = {sum1} ,Result: {can_split1}")
arr2=[1,3,5]
sum2,can_split2=can_balance_scales(arr2)
print(f"\nTotal sum of Array:{arr2} = {sum2} ,Result: {can_split2}")

