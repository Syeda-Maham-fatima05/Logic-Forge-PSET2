def min_cancelled_bookings(intervals):
    if len(intervals)<=1:
        return 0
    intervals.sort(key=lambda x:x[1])
    removals=0
    last_end=intervals[0][1]
    for i in range(1,len(intervals)):
        if intervals[i][0]<last_end:
            removals+=1
        else:
            last_end=intervals[i][1]
    return removals

# intervals1=[[1, 2],[2, 3],[3, 4],[1, 3]]
# print("Example 1: The Tight Schedule")
# print("Requests: ",intervals1)
# print("Result: ",min_cancelled_bookings(intervals1),"removals")
#
# intervals2=[[1, 3],[1, 3],[1, 3]]
# print("\nExample 2: The Triple Booking")
# print("Requests: ",intervals2)
# print("Result: ",min_cancelled_bookings(intervals2),"removals")
#
# intervals3=[[1, 2],[5, 10],[18, 35]]
# print("\nExample 3: The Social Distancer")
# print("Requests: ",intervals3)
# print("Result: ",min_cancelled_bookings(intervals3),"removals")
# Input intervals
intervals=[[1, 2],[2, 3],[3, 4],[1, 3]]
if not (1<=len(intervals)<=10**5):
    print("Invalid input: number of intervals out of range")
else:
    valid=True
    for interval in intervals:
        if len(interval)!=2:
            valid=False
            break
        start,end=interval
        if not (-5*10**4<=start<end<=5*10**4):
            valid=False
            break
    if not valid:
        print("Invalid input: interval constraints violated")
    else:
        result=min_cancelled_bookings(intervals)
        print("Requests:",intervals)
        print("Minimum removals:",result)