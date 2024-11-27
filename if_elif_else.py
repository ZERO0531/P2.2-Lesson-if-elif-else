# 1. Why do you suppose the output says "Both Teams A and B have the same number of wins." when team_a_wins is initialized as only 15 and team_b_wins is initialized as 16? It seems Team B has more wins. What is going on? 
# The increment operation only occurs when a team wins, which is determined by the points. The wins were incremented before the comparison. 

# 2. What do you think elif and else are doing? Answer in a comment. 
# elif is used to check another condition if the initial condition is false. else is used to specify a block of code to execute if all the preceding conditions are false. 

# 3. Pick one of the elif statements and change it to if instead. What difference does that make? Why? Answer in a comment. 
if team_a_points > team_b_points:
print("Team A wins!")
if team_b_points > team_a_points:
print("Team B wins!")
else:
print("Tie.")
