#import os module
import os

#import csv
import csv

#define your variables
total_votes = 0
vote_Khan = 0
vote_Correy = 0
vote_Li = 0
vote_OTooley = 0


#open csv file
with open('C:/Users/rwbut/python-challenge/PyPoll/Resources/election_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    #use a for loop to count the votes
    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] == "Khan":
            vote_Khan = vote_Khan + 1
        elif row[2] == "Correy":
            vote_Correy = vote_Correy + 1
        elif row[2] == "Li":
            vote_Li = vote_Li + 1
        elif row[2] == "O'Tooley":
            vote_OTooley = vote_OTooley + 1
#calculate the percentage of the vote
Khan_Percent = "{:.3%}".format(vote_Khan / total_votes)
Correy_Percent = "{:.3%}".format(vote_Correy / total_votes)
Li_Percent = "{:.3%}".format(vote_Li / total_votes)
OToolet_Percent = "{:.3%}".format(vote_OTooley / total_votes)

#find the winner
winner = max(vote_Khan, vote_Correy, vote_Li, vote_OTooley)
if winner == vote_Khan:
    winner_name = "Khan"
elif winner == vote_Correy:
    winner_name = "Correy"
elif winner == vote_Li:
    winner_name = "Li"
elif winner == vote_OTooley:
    winner_name = "O'Tooley"

#set variable for election results
election_results = (f"Election Results\n--------------------------\nTotal Votes: {total_votes}\nKhan: {Khan_Percent} ({vote_Khan})\nCorrey: {Correy_Percent} ({vote_Correy})\nLi: {Li_Percent} ({vote_Li})\nO'Tooley: {OToolet_Percent} ({vote_OTooley})\n--------------------------\nWinner: {winner_name}\n--------------------------")

#print results
print(election_results)

f = open('C:/Users/rwbut/Python-challenge/PyPoll/analysis/Election_Results.txt', 'w')

f.write(election_results)
f.close