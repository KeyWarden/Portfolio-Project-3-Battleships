"""code needed to connect game to leaderboard in Google Sheets, as well as to
produce random numbers"""
import random
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('project3_leaderboard')

leaderboard = SHEET.worksheet('board')

data = leaderboard.get_all_values()

"""declare constants to be used for input verification"""
MENU_INPUT = ["1", "s", "start", "2", "o", "options", "3", "l", "leaderboard"]
OPTIONS_INPUT = ["1", "d", "difficulty", "2", "m", "map", "3", "b", "back"]
AI_INPUT = [
    "1", "e", "easy", "2", "n", "normal", "3", "h", "hard", "4", "b", "back"
    ]
MAP_SIZE_INPUT = [
    "1", "s", "small", "2", "m", "medium", "3", "l", "large", "4", "b", "back"
    ]
LEADERBOARD_INPUT = ["1", "b", "back"]
SHIP_INPUT = ["1", "p", "place", "2", "r", "rotate"]


class MapGrid:
    """define a class to handle the map grids for the game"""
    def __init__(self, size):
        self.size = size
        if self.size == 0:
            self.row0 = [
                "  |", " A |", " B |", " C |", " D |", " E |", " F |", " G |",
                " H |", " I |", " J |"
                ]
            self.row1 = [
                "1 |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |"
                ]
            self.row2 = [
                "2 |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |"
                ]
            self.row3 = [
                "3 |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |"
                ]
            self.row4 = [
                "4 |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |"
                ]
            self.row5 = [
                "5 |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |"
                ]
            self.row6 = [
                "6 |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |"
                ]
            self.row7 = [
                "7 |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |"
                ]
            self.row8 = [
                "8 |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |"
                ]
            self.row9 = [
                "9 |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |"
                ]
            self.row10 = [
                "10|", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |"
                ]
            self.row_divide = [
                "--|", "---|", "---|", "---|", "---|", "---|", "---|", "---|",
                "---|", "---|", "---|"
            ]
        elif self.size == 1:
            self.row0 = [
                "  |", " A |", " B |", " C |", " D |", " E |", " F |", " G |",
                " H |", " I |", " J |", " K |", " L |", " M |", " N |", " O |"
                ]
            self.row1 = [
                "1 |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |", "   |", "   |", "   |"
                ]
            self.row2 = [
                "2 |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |", "   |", "   |", "   |"
                ]
            self.row3 = [
                "3 |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |", "   |", "   |", "   |"
                ]
            self.row4 = [
                "4 |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |", "   |", "   |", "   |"
                ]
            self.row5 = [
                "5 |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |", "   |", "   |", "   |"
                ]
            self.row6 = [
                "6 |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |", "   |", "   |", "   |"
                ]
            self.row7 = [
                "7 |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |", "   |", "   |", "   |"
                ]
            self.row8 = [
                "8 |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |", "   |", "   |", "   |"
                ]
            self.row9 = [
                "9 |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |", "   |", "   |", "   |"
                ]
            self.row10 = [
                "10|", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |", "   |", "   |", "   |"
                ]
            self.row11 = [
                "11|", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |", "   |", "   |", "   |"
                ]
            self.row12 = [
                "12|", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |", "   |", "   |", "   |"
                ]
            self.row13 = [
                "13|", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |", "   |", "   |", "   |"
                ]
            self.row14 = [
                "14|", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |", "   |", "   |", "   |"
                ]
            self.row15 = [
                "15|", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |", "   |", "   |", "   |"
                ]
            self.row_divide = [
                "--|", "---|", "---|", "---|", "---|", "---|", "---|", "---|",
                "---|", "---|", "---|", "---|", "---|", "---|", "---|", "---|"
            ]
        elif self.size == 2:
            self.row0 = [
                "  |", " A |", " B |", " C |", " D |", " E |", " F |", " G |",
                " H |", " I |", " J |", " K |", " L |", " M |", " N |", " O |",
                " P |", " Q |", " R |", " S |", " T |"
                ]
            self.row1 = [
                "1 |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |"
                ]
            self.row2 = [
                "2 |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |"
                ]
            self.row3 = [
                "3 |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |"
                ]
            self.row4 = [
                "4 |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |"
                ]
            self.row5 = [
                "5 |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |"
                ]
            self.row6 = [
                "6 |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |"
                ]
            self.row7 = [
                "7 |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |"
                ]
            self.row8 = [
                "8 |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |"
                ]
            self.row9 = [
                "9 |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |"
                ]
            self.row10 = [
                "10|", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |"
                ]
            self.row11 = [
                "11|", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |"
                ]
            self.row12 = [
                "12|", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |"
                ]
            self.row13 = [
                "13|", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |"
                ]
            self.row14 = [
                "14|", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |"
                ]
            self.row15 = [
                "15|", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |"
                ]
            self.row16 = [
                "16|", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |"
                ]
            self.row17 = [
                "17|", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |"
                ]
            self.row18 = [
                "18|", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |"
                ]
            self.row19 = [
                "19|", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |"
                ]
            self.row20 = [
                "20|", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |", "   |", "   |", "   |",
                "   |", "   |", "   |", "   |", "   |"
                ]
            self.row_divide = [
                "--|", "---|", "---|", "---|", "---|", "---|", "---|", "---|",
                "---|", "---|", "---|", "---|", "---|", "---|", "---|", "---|",
                "---|", "---|", "---|", "---|", "---|"
            ]

    def print_grid(self):
        """function to print the grid to the console"""
        dividing_row = ""
        title_row = ""
        first_row = ""
        second_row = ""
        third_row = ""
        fourth_row = ""
        fifth_row = ""
        sixth_row = ""
        seventh_row = ""
        eighth_row = ""
        ninth_row = ""
        tenth_row = ""
        eleventh_row = ""
        twelth_row = ""
        thirteenth_row = ""
        fourteenth_row = ""
        fifteenth_row = ""
        sixteenth_row = ""
        seventeenth_row = ""
        eighteenth_row = ""
        ninteenth_row = ""
        twentieth_row = ""
        if self.size == 0:
            for i in range(0, 11):
                dividing_row += self.row_divide[i]
                title_row += self.row0[i]
                first_row += self.row1[i]
                second_row += self.row2[i]
                third_row += self.row3[i]
                fourth_row += self.row4[i]
                fifth_row += self.row5[i]
                sixth_row += self.row6[i]
                seventh_row += self.row7[i]
                eighth_row += self.row8[i]
                ninth_row += self.row9[i]
                tenth_row += self.row10[i]
            print(title_row)
            print(dividing_row)
            print(first_row)
            print(dividing_row)
            print(second_row)
            print(dividing_row)
            print(third_row)
            print(dividing_row)
            print(fourth_row)
            print(dividing_row)
            print(fifth_row)
            print(dividing_row)
            print(sixth_row)
            print(dividing_row)
            print(seventh_row)
            print(dividing_row)
            print(eighth_row)
            print(dividing_row)
            print(ninth_row)
            print(dividing_row)
            print(tenth_row)
            print(dividing_row)
        if self.size == 1:
            for i in range(0, 16):
                dividing_row += self.row_divide[i]
                title_row += self.row0[i]
                first_row += self.row1[i]
                second_row += self.row2[i]
                third_row += self.row3[i]
                fourth_row += self.row4[i]
                fifth_row += self.row5[i]
                sixth_row += self.row6[i]
                seventh_row += self.row7[i]
                eighth_row += self.row8[i]
                ninth_row += self.row9[i]
                tenth_row += self.row10[i]
                eleventh_row += self.row11[i]
                twelth_row += self.row12[i]
                thirteenth_row += self.row13[i]
                fourteenth_row += self.row14[i]
                fifteenth_row += self.row15[i]
            print(title_row)
            print(dividing_row)
            print(first_row)
            print(dividing_row)
            print(second_row)
            print(dividing_row)
            print(third_row)
            print(dividing_row)
            print(fourth_row)
            print(dividing_row)
            print(fifth_row)
            print(dividing_row)
            print(sixth_row)
            print(dividing_row)
            print(seventh_row)
            print(dividing_row)
            print(eighth_row)
            print(dividing_row)
            print(ninth_row)
            print(dividing_row)
            print(tenth_row)
            print(dividing_row)
            print(eleventh_row)
            print(dividing_row)
            print(twelth_row)
            print(dividing_row)
            print(thirteenth_row)
            print(dividing_row)
            print(fourteenth_row)
            print(dividing_row)
            print(fifteenth_row)
            print(dividing_row)
        if self.size == 2:
            for i in range(0, 21):
                dividing_row += self.row_divide[i]
                title_row += self.row0[i]
                first_row += self.row1[i]
                second_row += self.row2[i]
                third_row += self.row3[i]
                fourth_row += self.row4[i]
                fifth_row += self.row5[i]
                sixth_row += self.row6[i]
                seventh_row += self.row7[i]
                eighth_row += self.row8[i]
                ninth_row += self.row9[i]
                tenth_row += self.row10[i]
                eleventh_row += self.row11[i]
                twelth_row += self.row12[i]
                thirteenth_row += self.row13[i]
                fourteenth_row += self.row14[i]
                fifteenth_row += self.row15[i]
                sixteenth_row += self.row16[i]
                seventeenth_row += self.row17[i]
                eighteenth_row += self.row18[i]
                ninteenth_row += self.row19[i]
                twentieth_row += self.row20[i]
            print(title_row)
            print(dividing_row)
            print(first_row)
            print(dividing_row)
            print(second_row)
            print(dividing_row)
            print(third_row)
            print(dividing_row)
            print(fourth_row)
            print(dividing_row)
            print(fifth_row)
            print(dividing_row)
            print(sixth_row)
            print(dividing_row)
            print(seventh_row)
            print(dividing_row)
            print(eighth_row)
            print(dividing_row)
            print(ninth_row)
            print(dividing_row)
            print(tenth_row)
            print(dividing_row)
            print(eleventh_row)
            print(dividing_row)
            print(twelth_row)
            print(dividing_row)
            print(thirteenth_row)
            print(dividing_row)
            print(fourteenth_row)
            print(dividing_row)
            print(fifteenth_row)
            print(dividing_row)
            print(sixteenth_row)
            print(dividing_row)
            print(seventeenth_row)
            print(dividing_row)
            print(eighteenth_row)
            print(dividing_row)
            print(ninteenth_row)
            print(dividing_row)
            print(twentieth_row)
            print(dividing_row)


class EnemyAI:
    """defining a class to manage the AI"""
    def __init__(self, difficulty, size):
        self.difficulty = difficulty
        if size == 0:
            self.map_size = 10
        elif size == 1:
            self.map_size = 15
        elif size == 2:
            self.map_size = 20
        self.turn_row = 0
        self.turn_collumn = 0

    def turn(self, last_turn, sunk_last):
        if self.difficulty == 0:
            self.turn_row = random.rand


def valid_menu_input(choice):
    """function to check validity of input on menu screen"""

    num = 0
    is_valid = False
    while num < 9:
        if choice == MENU_INPUT[num]:
            is_valid = True
            num = 9
        else:
            num += 1
    return is_valid


def ai_difficulty(difficulty):
    """function translates difficulty into text for user"""
    result = ""
    if difficulty == 0:
        result = "Easy"
    elif difficulty == 1:
        result = "Normal"
    elif difficulty == 2:
        result = "Hard"
    return result


def map_size(size):
    """function translates map size into text for user"""
    result = ""
    if size == 0:
        result = "Small"
    elif size == 1:
        result = "Medium"
    elif size == 2:
        result = "Large"
    return result


def start_game(difficulty, size):
    """funtion that controls the game starting"""
    player_map = MapGrid(size)
    print("YOUR GRID:")
    player_map.print_grid()


def menu_output(validity, choice, difficulty, size):
    """funtion controls result of user input on menu screen"""
    if not validity:
        print(
            f"Invalid input, please input one of the following: {MENU_INPUT}"
            )
        menu_screen(difficulty, size)

    if choice == "1" or choice == "s" or choice == "start":
        start_game(difficulty, size)
    elif choice == "2" or choice == "o" or choice == "options":
        options_screen(difficulty, size)
    elif choice == "3" or choice == "l" or choice == "leaderboard":
        leaderboard_screen(difficulty, size)


def menu_screen(difficulty, size):
    """function that controls menu screen"""
    a_i = ai_difficulty(difficulty)
    game_map = map_size(size)

    print("BATTLESHIPS")
    print(f"Current Difficulty: {a_i} - Current Map Size: {game_map}")
    print("1. [S]tart")
    print("2. [O]ptions")
    print("3. [L]eaderboard")
    choice = input("Please enter your choice here: ").lower()
    validity = valid_menu_input(choice)
    menu_output(validity, choice, difficulty, size)


def valid_options_input(choice):
    """function to check validity of input on options screen"""

    num = 0
    is_valid = False
    while num < 9:
        if choice == OPTIONS_INPUT[num]:
            is_valid = True
            num = 9
        else:
            num += 1
    return is_valid


def options_output(validity, choice, difficulty, size):
    """funtion controls result of user input on menu screen"""
    if not validity:
        print(
            f"Invalid input, please input one of the following:{OPTIONS_INPUT}"
            )
        options_screen(difficulty, size)

    if choice == "1" or choice == "d" or choice == "difficulty":
        difficulty_screen(difficulty, size)
    elif choice == "2" or choice == "m" or choice == "map":
        map_screen(difficulty, size)
    elif choice == "3" or choice == "b" or choice == "back":
        menu_screen(difficulty, size)


def options_screen(difficulty, size):
    """funtion that controls the options screen"""
    a_i = ai_difficulty(difficulty)
    game_map = map_size(size)
    print("OPTIONS")
    print(f"Current Difficulty: {a_i} - Current Map Size: {game_map}")
    print("1. [D]ifficulty")
    print("2. [M]ap")
    print("3. [B]ack")
    choice = input("Please enter your choice here: ").lower()
    validity = valid_options_input(choice)
    options_output(validity, choice, difficulty, size)


def valid_difficulty_input(choice):
    """function to check validity of input on difficulty screen"""

    num = 0
    is_valid = False
    while num < 12:
        if choice == AI_INPUT[num]:
            is_valid = True
            num = 12
        else:
            num += 1
    return is_valid


def difficulty_output(validity, choice, difficulty, size):
    """funtion controls result of user input on difficulty screen"""
    if not validity:
        print(
            f"Invalid input, please input one of the following: {AI_INPUT}"
            )
        difficulty_screen(difficulty, size)

    if choice == "1" or choice == "e" or choice == "easy":
        difficulty = 0
        difficulty_screen(difficulty, size)
    elif choice == "2" or choice == "n" or choice == "normal":
        difficulty = 1
        difficulty_screen(difficulty, size)
    elif choice == "3" or choice == "h" or choice == "hard":
        difficulty = 2
        difficulty_screen(difficulty, size)
    elif choice == "4" or choice == "b" or choice == "back":
        options_screen(difficulty, size)


def difficulty_screen(difficulty, size):
    """funtion that controls the difficulty screen"""
    a_i = ai_difficulty(difficulty)
    game_map = map_size(size)
    print("DIFFICULTY")
    print(f"Current Difficulty: {a_i} - Current Map Size: {game_map}")
    print("1. [E]asy")
    print("2. [N]ormal")
    print("3. [H]ard")
    print("4. [B]ack")
    choice = input("Please enter your choice here: ").lower()
    validity = valid_difficulty_input(choice)
    difficulty_output(validity, choice, difficulty, size)


def valid_map_input(choice):
    """function to check validity of input on map size screen"""

    num = 0
    is_valid = False
    while num < 12:
        if choice == MAP_SIZE_INPUT[num]:
            is_valid = True
            num = 12
        else:
            num += 1
    return is_valid


def map_output(validity, choice, difficulty, size):
    """funtion controls result of user input on map size screen"""
    if not validity:
        print(
            f"Invalid input, please input from the following: {MAP_SIZE_INPUT}"
            )
        map_screen(difficulty, size)

    if choice == "1" or choice == "s" or choice == "small":
        size = 0
        map_screen(difficulty, size)
    elif choice == "2" or choice == "m" or choice == "medium":
        size = 1
        map_screen(difficulty, size)
    elif choice == "3" or choice == "l" or choice == "large":
        size = 2
        map_screen(difficulty, size)
    elif choice == "4" or choice == "b" or choice == "back":
        options_screen(difficulty, size)


def map_screen(difficulty, size):
    """funtion that controls the map size screen"""
    a_i = ai_difficulty(difficulty)
    game_map = map_size(size)
    print("MAP SIZE")
    print(f"Current Difficulty: {a_i} - Current Map Size: {game_map}")
    print("1. [S]mall (10x10)")
    print("2. [M]edium (15x15)")
    print("3. [L]arge (20x20)")
    print("4. [B]ack")
    choice = input("Please enter your choice here: ").lower()
    validity = valid_map_input(choice)
    map_output(validity, choice, difficulty, size)


def leaderboard_screen(difficulty, size):
    """function that controls the leaderboard screen"""
    print("placeholder")


menu_screen(0, 0)
