import sys
import random

max_nr = int(sys.argv[1])
if max_nr not in range(1, 50):
    print("Enter a number between 1 and 49")
    exit(1)

draw_size = int(sys.argv[2])
if draw_size not in range(3, 11):
    print("Enter a draw size between 3 and 10")
    exit(1)

no_of_players = int(sys.argv[3])
if no_of_players not in range(2, 10):
    print("Enter a number of players between 2 and 10")

winning = list()

while len(winning) < draw_size:
    random_num = random.randint(1, max_nr)
    if random_num not in winning:
        winning.append(random_num)

players_draws_list = []
for i in range(0, no_of_players):
    player_draw = []
    while len(player_draw) < draw_size:
        random_num = random.randint(1, max_nr)
        player_draw.append(random_num)
    players_draws_list.append(player_draw)
    player_draw = []

player_comb = []

print("WIN:", end="")
print(winning)
print()

for x in range(0, no_of_players):
    for y in range(0, len(players_draws_list[x])):
        if players_draws_list[x][y] in winning:
            player_comb.append(players_draws_list[x][y])
    print("Player %d guessed %d number(s)" % (x + 1, len(player_comb)))
    print("The guessed numbers are: ", end="")
    print(player_comb)
    print()
    player_comb = []
