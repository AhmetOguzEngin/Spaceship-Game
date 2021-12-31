
x = int(input())
y = int(input())
g = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
statement = 'whatagame'
if x == 0:
    print('YOU WON!')
    statement = 'winner'

game = []
for k in range(1, x + 1):
    astroidline = []
    for i in range(1, y + 1):
        astroidline.append('*')
    game.append(astroidline)

if y % 2 == 0:
    for a in range(1, g + 2):
        spaceship = []
        for j in range(1, y + 1):
            if j == y / 2 and a == g + 1:
                spaceship.append('@')
            else:
                spaceship.append(' ')
        game.append(spaceship)
else:
    for a in range(1, g + 2):
        spaceship = []
        for j in range(1, y + 1):
            if j == y // 2 + 1 and a == g + 1:
                spaceship.append('@')
            else:
                spaceship.append(' ')
        game.append(spaceship)

for s in game:
    for d in s:
        print(d, end='')
    print('')
print(72 * '-', )
score = 0
time = 0
while statement == 'whatagame':
    action = input('Choose your action!\n')
    action = action.lower()
    time += 1

    if action == 'fire':
        ind = game[-1].index('@')

        for i in range(g + x, 0, -1):
            if game[i - 1][ind] == ' ':
                game[i - 1][ind] = '|'
                if game[i][ind] != '@' and game[i][ind] == '|':
                    game[i][ind] = ' '
            elif game[i - 1][ind] == '*':
                if game[i][ind] != '@':
                    game[i][ind] = ' '
                game[i - 1][ind] = ' '
                score += 1
                break
            for s in game:
                for d in s:
                    print(d, end='')
                print('')
            print(72 * '-')
            if game[i - 1][ind] != '@' and i - 1 == 0:
                game[i - 1][ind] = ' '

    if action == 'right':
        ind = game[-1].index('@')
        if ind != len(game[-1]) - 1:
            game[-1][ind] = ' '
            game[-1][ind + 1] = '@'

    if action == 'left':
        ind = game[-1].index('@')
        if ind != 0:
            game[-1][ind] = ' '
            game[-1][ind - 1] = '@'

    if action == 'exit':
        statement = 'done'

    if time > 0 and time % 5 == 0 and action!='exit':
        for k in game[-2]:
            if k == '*':
                statement = 'OVER'
                break
        else:
            whitespaces = []
            for k in range(1, y + 1):
                whitespaces.append(' ')
            game.insert(0, whitespaces)
            game.pop(-2)

    if statement == 'OVER':
        print('GAME OVER')

    if score == x * y:
        statement = 'winner'
        print('YOU WON!')

    for s in game:
        for d in s:
            print(d, end='')
        print('')
    print(72 * '-')

if statement == 'OVER' or statement == 'done' or statement == 'winner':
    print('YOUR SCORE:', score)
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
