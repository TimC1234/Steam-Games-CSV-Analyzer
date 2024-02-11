# a5.py
#
# Full Name: Kuan Ting (Tim) Chou
#    SFU ID: 301562019
# SFU Email: tim_chou@sfu.ca
#

import turtle  # this is the only module you can import!

#Q1a
def get_num_lines(fname):
    csvfile = open(fname)
    num_lines = 0
    for line in csvfile:
        num_lines += 1
    return num_lines

#Q1b
def print_num_games(fname):
    num_games = get_num_lines(fname)
    print(f"{fname} has {num_games} games")

#Q2
def split_game_line(csv_line):
    lst = [1, 2, 3, 4]
    new_line = csv_line.replace("$", "")
    next_line = new_line.replace("\n", "")
    csv_line = next_line.split(",")
    lst[0] = str(csv_line[0])
    lst[1] = int(csv_line[1])
    lst[2] = int(csv_line[2])
    if csv_line[3] == " free":
        lst[3] = 0.0
    else:
        lst[3] = float(csv_line[3])

    return lst

#Q3a
def print_most_recommendations(fname):
    data = open(fname)
    max_recs = -1
    rec_names = []
    for line in data:
        value = split_game_line(line)
        name = value[0]
        num_recs = value[2]
        if num_recs > max_recs:
            rec_names = [name]
            max_recs = num_recs
        elif num_recs == max_recs:
            rec_names.append(name)

    rec_names.sort()

    print(f"These games have the most recommendations")
    print(f"They each have {max_recs} recommendations.")
    for name in rec_names:
        print(f"  {name}")
    print()

#Q3b
def print_highest_price(fname):
    data = open(fname)
    num_price = -1
    expensive_names = []
    for line in data:
        value = split_game_line(line)
        name = value[0]
        price = value[3]
        if price > num_price:
            expensive_names = [name]
            num_price = price
        elif price == num_price:
            expensive_names.append(name)

    expensive_names.sort()

    print(f"These games have the highest price.")
    print(f"They each cost ${num_price}.")
    for name in expensive_names:
        print(f"  {name}")
    print()

#Q4a
def get_recommendation_average(fname):
    data = open(fname)
    count = 0
    total = 0
    for line in data:
        value = line.split(",")
        name = value[0]
        recs = int(value[2])
        if recs > 0:
            total += recs
            count += 1
    return total / count

#Q4b
def get_price_average(fname):
    data = open(fname)
    count = 0
    total = 0
    for line in data:
        new_line = line.replace("$", "")
        next_line = new_line.replace(" ", "")
        final_line = next_line.replace("\n", "")
        value = final_line.split(",")
        price = value[3]
        if price == "free":
            count += 1
        else:
            price = float(value[3])
            total += price
            count += 1
    return total / count

#Q5a
def get_game_dict(fname):
    csv_file = open(fname)
    game_dict = {}
    for line in csv_file:
        line.strip()
        name = line.split(',')
        if name[0] in game_dict:
            game_dict[name[0]] +=1
        else:
            game_dict[name[0]] = 1
    return game_dict

#Q5b
def print_duplicates1(fname):
    game_dict = get_game_dict(fname)
    for name, num_duplicated in game_dict.items():
        if num_duplicated != 1:
            print(name)
        else:
            pass

#Q5c
def print_duplicates2(fname):
    game_dict = get_game_dict(fname)
    line_num = 1
    alpha_games = []
    for name, num_duplicated in game_dict.items():
        if num_duplicated != 1:
            alpha_games.append(name)
        else:
            pass
    alpha_games.sort()

    for games in alpha_games:
        print(f'{line_num}. "{games}" is a duplicate')
        line_num += 1

#Q5d
def print_duplicates3(fname):
    game_dict = get_game_dict(fname)
    line_num = 1
    alpha_games = []
    for name, num_duplicated in game_dict.items():
        if num_duplicated != 1:
            alpha_games.append(name)
        else:
            pass
    alpha_games.sort()
    for games in alpha_games:
        num_dupes = game_dict[games]
        print(f'{line_num}. "{games}" occurs {num_dupes} times')
        line_num += 1

#Q6
def draw_histogram(fname):
    games = open(fname)
    scores = []
    rect1 = 0
    rect2 = 0
    rect3 = 0
    rect4 = 0
    rect5 = 0
    rect6 = 0
    rect7 = 0
    rect8 = 0
    rect9 = 0
    rect10 = 0
    for lines in games:
        metascore = split_game_line(lines)[1]
        if metascore == 0:
            pass
        else:
            scores.append(metascore)

    for metacritic in scores:
        if 0 < metacritic and metacritic <= 10:
           rect1 += 1
        elif 10 < metacritic and metacritic <= 20:
           rect2 += 1
        elif 20 < metacritic and metacritic <= 30:
           rect3 += 1
        elif 30 < metacritic and metacritic <= 40:
           rect4 += 1
        elif 40 < metacritic and metacritic <= 50:
           rect5 += 1
        elif 50 < metacritic and metacritic <= 60:
           rect6 += 1
        elif 60 < metacritic and metacritic <= 70:
           rect7 += 1
        elif 70 < metacritic and metacritic <= 80:
           rect8 += 1
        elif 80 < metacritic and metacritic <= 90:
           rect9 += 1
        elif 90 < metacritic and metacritic <= 100:
           rect10 += 1
    bars = []
    bars.append(rect1)
    bars.append(rect2)
    bars.append(rect3)
    bars.append(rect4)
    bars.append(rect5)
    bars.append(rect6)
    bars.append(rect7)
    bars.append(rect8)
    bars.append(rect9)
    bars.append(rect10)

    turtle.penup()
    turtle.goto(-200, -300)
    turtle.down()
    for i in bars:
        turtle.begin_fill()
        turtle.setheading(90)
        turtle.forward(i)
        turtle.write(i)
        turtle.right(90)
        turtle.forward(30)
        turtle.right(90)
        turtle.forward(i)
        turtle.right(90)
        turtle.forward(30)
        x, y = turtle.position()
        turtle.end_fill()
        turtle.up()
        turtle.goto(x+40, y)
        turtle.down()

    x, y = turtle.position()
    turtle.up()
    turtle.goto(x-260, y - 40)
    turtle.write(f'{fname} metacritic scores')
    turtle.down()
    turtle.hideturtle()

print_most_recommendations('asn_games.csv')
print_highest_price('asn_games.csv')
get_price_average('asn_games.csv')
get_game_dict('small_games.csv')
#print_duplicates1('small_games.csv')
print_duplicates1('asn_games.csv')
p#rint_duplicates2('small_games.csv')
print_duplicates2('asn_games.csv')
#print_duplicates3('small_games.csv')
print_duplicates3('asn_games.csv')


draw_histogram('asn_games.csv')
