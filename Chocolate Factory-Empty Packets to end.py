arr=[]
N=int(input("Enter the Number of Elements:"))
for i in range(0,N):
    E=int(input())
    arr.append(E);
Numbers=[]
Zeros=[]
for j in arr:
    if (j==0):
        Zeros.append(j);
    else:
        Numbers.append(j);
Sort=sorted(Numbers);
Sorted_Array=Numbers+Zeros;   #Array after moving Empty Packets to end
print("The Array after moving the empty Packets to End:\n",Sorted_Array)
    
