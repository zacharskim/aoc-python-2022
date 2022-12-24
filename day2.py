from aocd import data, get_data


#load data
data = get_data(day=2, year=2022)


#split input into arr with each element representing a RPS game
data = data.replace(' ', '')
rps_games = data.split('\n')

scoring_hm = {'X': 1, 'Y': 2, 'Z': 3}
translation_hm = {'X': 'rock', 'Y': 'paper', 'Z':'scissors', 'A':'rock', 'B': 'paper', 'C':'scissors'}

#rock beats scissors
#paper beats rock
#scissors beats paper

score = 0
for game in rps_games:
    elf, self = game[0], game[1]

    #winning cases 
    if translation_hm[self] == 'rock' and  translation_hm[elf] == 'scissors':
        score += scoring_hm[self] + 6

    elif translation_hm[self] == 'paper' and  translation_hm[elf] == 'rock':
        score += scoring_hm[self] + 6

    elif translation_hm[self] == 'scissors' and  translation_hm[elf] == 'paper':
        score += scoring_hm[self] + 6

    #losing cases 
    elif translation_hm[self] == 'scissors' and  translation_hm[elf] == 'rock':
        score += scoring_hm[self] + 0

    elif translation_hm[self] == 'rock' and  translation_hm[elf] == 'paper':
        score += scoring_hm[self] + 0

    elif translation_hm[self] == 'paper' and  translation_hm[elf] == 'scissors':
        score += scoring_hm[self] + 0

    #drawing cases
    elif translation_hm[self] == 'scissors' and  translation_hm[elf] == 'scissors':
        score += scoring_hm[self] + 3

    elif translation_hm[self] == 'rock' and  translation_hm[elf] == 'rock':
        score += scoring_hm[self] + 3

    elif translation_hm[self] == 'paper' and  translation_hm[elf] == 'paper':
        score += scoring_hm[self] + 3

#part 1 answer
print(score)


#part 2 answer

#x means you need to lose, y means you need to draw, z means you need to win

hand_hm = {'X': 'lose', 'Y': 'draw', 'Z': 'win'}
scoring_hm = {'paper': 2, 'rock': 1, 'scissors': 3}

score = 0
for game in rps_games:
    elf, self = game[0], game[1]

    if hand_hm[self] == 'win':

        if translation_hm[elf] == 'rock':
            score += scoring_hm['paper'] + 6

        elif translation_hm[elf] == 'scissors':
            score += scoring_hm['rock'] + 6

        elif translation_hm[elf] == 'paper':
            score += scoring_hm['scissors'] + 6


    elif hand_hm[self] == 'lose':

         if translation_hm[elf] == 'rock':
            score += scoring_hm['scissors'] + 0

         elif translation_hm[elf] == 'scissors':
            score += scoring_hm['paper'] + 0

         elif translation_hm[elf] == 'paper':
            score += scoring_hm['rock'] + 0


    elif hand_hm[self] == 'draw':
        if translation_hm[elf] == 'rock':
            score += scoring_hm['rock'] + 3

        elif translation_hm[elf] == 'scissors':
            score += scoring_hm['scissors'] + 3

        elif translation_hm[elf] == 'paper':
            score += scoring_hm['paper'] + 3

#part 2 answer
print(score)