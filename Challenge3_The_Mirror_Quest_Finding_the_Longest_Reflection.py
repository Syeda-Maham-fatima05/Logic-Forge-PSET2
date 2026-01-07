def find_longest_mirror_length(s):
    n=len(s)
    if n==1:
        return 1
    # Table to store longest palindromic subsequence lengths
    mirror_lengths=[[0] *n for _ in range(n)]
    for i in range(n):
        mirror_lengths[i][i]=1
    for length in range(2,n+1):
        for start in range(n-length+1):
            end=start+length-1
            if s[start]==s[end]:
                if length==2:
                    mirror_lengths[start][end]=2
                else:
                    mirror_lengths[start][end]=mirror_lengths[start+1][end-1]+2
            else:
                mirror_lengths[start][end]=max(mirror_lengths[start+1][end],mirror_lengths[start][end-1])
    return mirror_lengths[0][n-1]

s=str(input("Enter the Input String : "))
if 1<=len(s)<=1000 and s.isupper():
    print("The length of the longest palindromic subsequence : ", find_longest_mirror_length(s))
else:
    print("Enter Uppercase characters in range 1-1000")
