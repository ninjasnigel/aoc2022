win, tie, loss = 6,3,0

# Sissor C Z
# Rock = A X
# Paper = B Y

# Honestly shit code is shitty, I was a bit hungover land lost track on
# how to struckture my code. Should have used a dictionary

def sol():
    sol1score = 0
    sol2score = 0
    with open('data.txt') as f:
        for line in f.readlines():
            game = line.split(' ')
            opp, you = game[0][0], game[1][0]
            sol1score += gamescore(opp, you)
            sol2game = pick_hand(opp, you)
            sol2score += gamescore(sol2game[0], sol2game[1])
    print(sol1score)
    print(sol2score)

def gamescore(opp, you):
    if istie(opp,you): return handscore(you) + tie
    match opp:
        case 'A':
            if you == 'Z': return handscore(you) + loss
            else: return handscore(you)          + win
        case 'B':
            if you == 'X': return handscore(you) + loss
            else: return handscore(you)          + win
        case 'C':
            if you == 'Y': return handscore(you) + loss
            else: return handscore(you)          + win
    return 0

def handscore(hand):
    match hand:
        case 'Y':
            return 2
        case 'X':
            return 1
        case 'Z':
            return 3
        case _:
            return 0

def istie(opp, you):
    if (opp == 'A') & (you == 'X'): return True
    elif (opp == 'B') & (you == 'Y'): return True
    elif (opp == 'C') & (you == 'Z'): return True
    return False

def win_loss_tie(opp):
    if opp == 'A': return ['Y', 'Z', 'X']
    elif opp == 'B': return ['Z', 'X', 'Y']
    else: return ['X', 'Y', 'Z']

def pick_hand(opp, you):
    choices = win_loss_tie(opp)
    match you:
        case 'Y': return opp, choices[2]
        case 'X': return opp, choices[1]
        case 'Z': return opp, choices[0]
