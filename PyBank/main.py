import os 
import csv

csvpath = os.path.join("Resources/budget_data.csv")

with open(csvpath, newline="") as budgetfile:
    reader = csv.reader(budgetfile, delimiter=",")
    header = next(reader)

    total_months = []
    net = []
    greatest_increase = []   
    lowest_increase = []

    month_count = 0
    net_profit = 0
    prior_profit = 0
    current_profit = 0
    profit_change = 0

    for row in reader:
        month_count += 1
        current_profit = int(row[1])
        net_profit += current_profit

        if (month_count == 1):
            prior_profit = current_profit
            continue
        else: 
            profit_change = current_profit - prior_profit
            total_months.append(row[0])
            net.append(profit_change)
            prior_profit = current_profit

    net = profit_change
    average = round(net/(month_count -1),2)

    greatest_increase = max(profit_change)
    lowest_increase = min(profit_change)

    best_month_index = profit_change.index(greatest_increase)
    worst_month_index = profit_change.index(lowest_increase)

    best_month = total_months[best_month_index]
    worst_month = total_months[worst_month_index]

results = (["Financial Analysis",
"----------------------",
"Total Months: {total_months}",
"Total: {net}",
"Average Change: ${average}",
"Greatest Increase in Profits: {best_month} (${greatest_increase})",
"Greatest Decrease in Profits: {worst_month} (${lowest_increase})"])

print(results)

write_results = os.path.join("analysis.txt")
with open(results,'w') as textfile:
    textfile.write(results)