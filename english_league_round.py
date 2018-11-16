"""Put all English league clubs, and make every round of tournaments for one season"""

teams = ["Arsenal", "Bournemouth", "Brighton", "Burnley", "Cardiff City", "Chelsea", "Crystal", "Everton", "Fulham", 
"Huddersfield", "Leicester City", "Liverpool", "Manchester City", "Manchester United", "Newcastle United", "Southampton", 
"Tottenham Hotspur", "Watford", "West Ham", "Wolverhampton"]

import operator
import functools
def competition(teams):
    if len(teams) % 2:
        teams.append('Day off')  # if team number is odd - use 'day off' as fake team     

    rotation = list(teams)       # copy the list // new_list = list(old_list)

    competition = []
    for i in range(0, len(teams)-1):
        competition.append(rotation)
        rotation = [rotation[0]] + [rotation[-1]] + rotation[1:-1]

    return competition

# for one match each - use this block only
matches = competition(teams)
num_round = 1
print ("      ")
print ("      ")
for f in matches:  
    x = (zip(*[iter(f)]*2))
    print ("Round", num_round)
    num_round += 1
    o = [(f[i],f[i+1]) for i in range(0,len(matches),2)]
    print (o)
    
# if you want return matches 
reverse_teams =  [list(x) for x in zip(teams[1::2], teams[::2])]
reverse_teams = functools.reduce(operator.add,  reverse_teams)    # swap team1 with team2, and so on ....

#then run the competition again
matches = competition(reverse_teams)
print ("      ")
print ("Return matches")
print ("      ")

for f in matches:
    print ("Round", num_round)
    num_round += 1
    o = [(f[i],f[i+1]) for i in range(0,len(matches),2)]
    print (o)
    
    
