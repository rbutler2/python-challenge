#import os module
import os

#import csv
import csv

#define your variables
total_months = 0
total = 0
total_change = 0
average_change = 0
last_month = 867884
largest_increase = 0
largest_loss = 0

with open('C:/Users/rwbut/python-challenge/PyBank/Resources/budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        total_months= total_months +1
        total = total + int(row[1])
        current_change = (int(row[1]) - last_month)
        total_change = total_change + current_change
        if current_change > largest_increase:
            largest_increase = current_change
            greatest_increase_month = row[0]
            greatest_increase_value = current_change
        if current_change < largest_loss:
            largest_loss = current_change
            largest_loss_month = row [0]
            largest_loss_value = current_change
        last_month = int(row[1])
        last_month_change = current_change
average_change = format((total_change/(total_months - 1)),".2f")

print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_value})")
print(f"Greatest Decrease in Profits: {largest_loss_month} (${largest_loss_value})")
