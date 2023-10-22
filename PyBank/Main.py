import pandas as pd
from pathlib import Path

#create text output and title
f = open("budget_analysis.txt", "w")
print("Financial Analysis:",file=f)
print ('----------------------------------------------------------------------------',file=f)
print("Financial Analysis:")
print ('----------------------------------------------------------------------------')

#create path to the csv file and read the csv file
budget_path = Path("python-challenge/PyBank/budget_data.csv")
budget_data = pd.read_csv(budget_path)

#The first five rows is available to view. Remove the comment(hashtag) to view this.
#print (budget_data.head())

#output total months
Total_month = budget_data["Date"].count()
print ("The total number of months included in the data set: ",Total_month,file=f)
print(file=f)
print ("The total number of months included in the data set: ",Total_month)
print()

# output total profit and loss over the entire period
Total = budget_data["Profit/Losses"].sum()
print ("Total amount of profit/losses over the entire period: ",Total,file=f)
print(file=f)
print ("Total amount of profit/losses over the entire period: ")
print()


#Output the changes in "Profit/Losses" over the entire period
difference = budget_data["Profit/Losses"].diff()
print ("The changes in profit/losses over the entire period: \n",difference,file=f)
print(file=f)
print ("The changes in profit/losses over the entire period: \n",difference)
print()

#Output the average of the changes in profit/losses over the entire period
Average_change = difference.mean()
print ("The average changes in profit/losses over the entire period: ",Average_change.round(2),file=f)
print(file=f)
print ("The average changes in profit/losses over the entire period: ",Average_change.round(2))
print()


#Output greatest increase in profit
increase_profit = difference.max()
print("Greatest increase in profit: ",increase_profit,file=f)
print(file=f)
print("Greatest increase in profit: ",increase_profit)
print()

#Output greatest decrese in profit
decrease_profit = difference.min()
print ("Greatest decrease in profit: ",decrease_profit,file=f)
print ("Greatest decrease in profit: ",decrease_profit)

f.close()