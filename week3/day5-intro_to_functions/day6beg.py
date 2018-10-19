

def update_library2(books, library):
    new_books = []
    for book in books:
        if book not in library:
            print_new_book(book)
            new_books.append(book)
        library.add(book)
    print(library)
    return new_books

def print_new_book(book):
    print('The book, {} is new!'.format(book))


#########

def play_rock_paper_scissors(n_rounds):
    '''
    Input:  Int - number of rounds to play rock paper scissors for
    '''
    for _ in range(n_rounds):
        player_1 = input('Player 1 play (r/p/s): ')
        player_2 = input('Player 2 play (r/p/s): ')
        if player_1 == player_2:
            print("It's a tie!")
        elif player_1 == 'r' and player_2 == 's':
            printwinner("Player 1")
        elif player_1 == 'r' and player_2 == 'p':
            printwinner("Player 2")
        elif player_1 == 'p' and player_2 == 'r':
            printwinner("Player 1")
        elif player_1 == 'p' and player_2 == 's':
            printwinner("Player 2")
        elif player_1 == 's' and player_2 == 'r':
            printwinner("Player 2")
        elif player_1 == 's' and player_2 == 'p':
            printwinner("Player 1")
        else:
            print("Someone didn't play right!")

def printwinner(player):
    print('{} wins!'.format(player))


###

def findline(file_name, line_num):
    line = None
    with open(file_name) as f:
        for i, file_line in enumerate(f, 1):
            if i == line_num:
                line = file_line.strip()
    return line


def generate_copies(file_name, line_num, num_copies):
    line = findline(file_name, line_num)
    if not line:
        copies_of_line = 'There were not {} lines in the document'.format(line_num)
    else:
        copies_of_line = [line for _ in range(num_copies)]
    return copies_of_line

###


import this

def decode_text(coded_zen):
    zen_decoder = this.d
    decoded_chars = []
    for char in coded_zen:
        if char.isalpha():
            decoded_chars.append(zen_decoder[char])
        else:
            decoded_chars.append(char)
    return decoded_chars


def decode_zen_of_python2():
    coded_zen = this.s
    print(coded_zen)
    decoded_chars = decode_text(coded_zen)
    decoded_text = ''.join(decoded_chars)
    print('\n' + decoded_text)



##

def get_month_season(month):
    '''
    Input:  Str - Abbreviation of month
    Output: Str - Season of inputted month
    '''
    season_months = {'fall' : ['oct', 'nov', 'dec'], 'winter':['jan', 'feb', 'mar'], 'spring': ['apr', 'may', 'jun'], 'summer': ['jul', 'aug', 'sept']}
    monthseason = ""
    for season,months in season_months.items():
        for toy in months:
            if toy == month:
                monthseason = season
                break
    return(monthseason)

def month_info(month, category):
    '''
    Input:  Str - Abbreviation of month, Str - information category to get for month
    Output: Str - category information for the specified month

    Categories supported: 'full name'   ex: month_info('jan', 'full_name') -----> 'January'
                          'num_month'   ex: month_info('may', 'num_month') ----->  5
                          'birth_stone' ex: month_info('jul', 'birth_stone') ---> 'Ruby'
                          'season'      ex: month_info('oct', 'season') --------> 'Fall'
    '''
    full_names = {'jan': 'January', 'feb': 'February', 'mar': 'March', 'apr': 'April',
                  'may': 'May', 'jun': 'June', 'jul': 'July', 'aug': 'August',
                  'sep': 'September', 'oct': 'October', 'nov': 'November', 'dec': 'December'}

    month_nums = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
                  'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12}

    birth_stones = {'jan': 'Garnet', 'feb': 'Amethyst', 'mar': 'Aquamarine', 'apr': 'Diamond',
                    'may': 'Emerald', 'jun': 'Pearl', 'jul': 'Ruby', 'aug': 'Peridot',
                    'sep': 'Sapphire', 'oct': 'Opal', 'nov': 'Topaz', 'dec': 'Turquoise'}

    # Depending on the category get information about month from correct source and return

    info = ""
    if category == 'fullname':
        info = full_names[month]
    elif category == 'num':
        info = month_nums[month]
    elif category == 'birthstone':
        info = birth_stones[month]
    elif category == 'season':
        info = get_month_season(month)
    else:
        print ("category not recognized")
    return(info)

######


def perfect_square(num):
    '''
    Input:  Int
    Output: Bool

    Return True if num is a perfect square, e.g. 9 = 3 x 3. Return False if num is not
    a perfect square, 8 isn't any integer multiplied by itself.
    '''
    issquare = False
    for number in range(num+1):
        if number * number == num:
            issquare = True
            break
    return issquare


def next_perfect_square(num):
    '''
    Input:  Int
    Output: Int

    Ex: next_perfect_square(10) --> -1
        next_perfect_square(9) ---> 16
        next_perfect_square(25) --> 36
        next_perfect_square(37) --> -1

    Returns the next perfect square (a number that is the square of an integer e.g. 81 = 9 x 9)
    greater than the inputted number. If the inputted number is not a perfect square, return -1.
    (i.e. the inputted number must also be a perfect square).
    '''
    issquare = perfect_square(num)
    ans = 0
    if not issquare:
        ans = -1
    else:
        starting = num+1
        while starting > 0:
            if perfect_square(starting):
                ans = starting
                break
            else:
                starting += 1
    return ans


def next_perfect_square(num):
    issquare = perfect_square(num)
    ans = 0
    if not issquare:
        ans = -1
    else:
        starting = num+1
        while starting > 0:
            if perfect_square(starting):
                ans = starting
                break
            else:
                starting += 1
    return ans

###########

import random

def flip_coin():
    value = random.random()
    if value >= .5:
        return "H"
    else:
        return "T"

def roll_die():
    value = random.randint(1,6)
    return value

def flip_coin_roll_die(n_times):
    results = []
    for n in range(n_times):
        newresult = (flip_coin(), roll_die())
        results.append(newresult)
    return results

#########

'''
Write a function that rolls two sets of dice to model players playing a game with dice. It will accept two arguments, the number of dice to roll for the first player, and the number of dice to roll for the second player. Then, the function will do the following:
Model rolling the appropriate number of dice for each player.
Sum the total values of the corresponding dice rolls.
Print which player rolled the higher total.
Return the total sum of each players rolls in a tuple.

In [1]: player_rolls = model_dice_rolls(3, 2)
Player 1 wins!
In [2]: player_rolls
Out[2]: (13, 7)
'''

import random

def roll_die():
    value = random.randint(1,6)
    return value

def dices_roll_sum(int):
    sum_of_rolls = 0
    list = []
    for i in range(int):
        add = roll_die()
        sum_of_rolls += add
        list.append(add)
    print(list)
    return sum_of_rolls


def model_dice_rolls(numa, numb):
    player1sum = dices_roll_sum(numa)
    player2sum = dices_roll_sum(numb)
    if player1sum > player2sum:
        print("Player 1 wins!")
    elif player1sum < player2sum:
        print("Player 2 wins!")
    elif player1sum == player2sum:
        print("Tie!")
    return (player1sum, player2sum)

#########

'''
Write a function that will calculate the total amount of a dinner bill, given the total before tax, the tax rate, and the tip percentage. Your function will accept these three values as arguments. It will then do the following:
Apply the tax rate to the bill total.
Apply the tip percentage to the total amount.
Return the total amount of bill before and after tip.
Here's an example of how we would call the function:

In [1]: bill_with_tax, bill_with_tax_and_tip = calc_total_bill(100, 0.10, 0.10)

In [2]: bill_with_tax_and_tip
Out[2]: 121.0
'''

def calc_total_bill(billtotal, taxrate, tippct):
    bill_with_tax = billtotal * (1 + taxrate)
    bill_with_tax_and_tip = bill_with_tax * (1 + tippct)
    return bill_with_tax_and_tip
