print("---------------------------------MENU------------------------------")
print("Pizza - 200 Rupees")
print("Burger - 180 Rupees")
print("Briyani - 250 Rupees")
print("Dosa - 80 Rupees")
print("Idly - 50 Rupees")
print("-------------------------------------------------------------------")
A=int(input("No of Pizza:"))
B=int(input("No of Burger:"))
C=int(input("No of Briyani:"))
D=int(input("No of Dosa:"))
E=int(input("No of Idly:"))
Total_Quantity=(A+B+C+D+E);
print("Total Quantity of Food Ordered:",Total_Quantity)
Total_cost=((A*200)+(B*180)+(C*250)+(D*80)+(E*50));
if(Total_cost>500):
    print("--Congratulations You Have Got 10% Discount--")
    New_cost=Total_cost-((10/100)*Total_cost);
    print("Your Grand Total:",New_cost,"/-")
else:
    print("Your Grand Total:",Total_cost,"/-")
