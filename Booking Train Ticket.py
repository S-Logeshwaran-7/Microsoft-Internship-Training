print("-------------------------------------Cost of Tickets--------------------------------------------------")
print("Senior Citizens - 30 Rupees")
print("Children - 20 Rupees")
print("Normal Prize - 50 Rupees")
print("------------------------------------------------------------------------------------------------------")
A=int(input("Enter the No. of Senior Citizens whose age is greter than 60:"))
B=int(input("Enter the No. of Children whose age is less than 12:"))
C=int(input("Enter the No. of of Other Persons whose age doesn't fall on the above conditions:"))
Q=A+B+C;
print("Total Quantity:",Q)
Total_Cost=((A*30)+(B*20)+(C*50));
print("Total Prize of the Tickets:",Total_Cost)

    
