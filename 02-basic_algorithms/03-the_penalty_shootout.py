# Author: harundemir918
# The Penalty Shootout
# Counts how many penalties and goals in a game
# 2's are penalties
# 21's are goals
# 0's are nothing 

# The method that takes score as parameter
def thePenaltyShootout(score):
    score = str(score)                              # Convert the score parameter to string
    penalty = score.count("2")                      # Check how many 2's in the score and assign it to penalty
    goal = score.count("21")                        # Check how many 21's in the score and assign it to goal

    # If there are penalties and goals
    if penalty and goal > 0:
        print("Penalties:", penalty)
        print("Goals:", goal)

    # If there are none
    else:
        print("No goals achieved.")

# Call the method with score parameter: 1021201021201201021021201021020
# Penalties are: 10
# Goals are: 5
thePenaltyShootout(1021201021201201021021201021020)
