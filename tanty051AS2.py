#
# File: tanty051AS2.py
# Description: A brief description of this Python module.
# Author: Thanh Nam Tang
# Student ID: 110394306
# Email ID: tanty051
# This is my own work as defined by 
#    the University's Academic Misconduct Policy.
#

from abc import ABC, abstractmethod
import random

"""Class to modify AllThatDice and their attribute """
class AllThatDice:
    def __init__(self):
        self.players = {}  # A dictionary to keep track of players by their name
        self.games = []  # List to store instances of Games
        self.current_game = None  # Active game instance
        # Options for menu
        self.options = {'r': self.register_player, 'p': self.play_game, 
                        's': self.display_leaderboard, 'q': self.quit}
    
    def register_player(self):
        """Handles the registration of a player."""
        player_name = input("Enter player name: ")
        # Check if player already exists
        if player_name in self.players:
            print("Player already registered.")
            return
        # Otherwise, register the new player
        new_player = Player(player_name)  # Assuming a Player class exists with the appropriate constructor
        self.players[player_name] = new_player
        print(f"Player {player_name} registered successfully.")
        print("")

    def play_game(self):
        """Handles the gameplay logic."""
        if not self.players:
            print("No players registered. Please register players before starting a game.")
            return
        # Display game options here and instantiate a game based on the choice
        game_choice = input("Choose a game to play (OddOrEven/Maxi/Bunco): ").lower()
        if game_choice.lower() == "oddoreven":
            self.current_game = OddOrEven(self.players)
        elif game_choice.lower() == "maxi":
            self.current_game = MaxiGame(self.players)
        elif game_choice.lower() == "bunco":
            self.current_game = BuncoGame(self.players)
        else:
            print("Invalid game choice.")
            return
        # Start and manage the game
        self.current_game.start_game()

    def display_leaderboard(self):
        """Displays the leaderboard."""
        # Ensure Leaderboard class exists with a method to display the leaderboard
        leaderboard = Leaderboard()  # Assuming Leaderboard class has the appropriate constructor
        leaderboard.display_leaderboard()  # Correct method name to match the Leaderboard class definition
    
    def quit(self):
        """Quits the application."""
        print("Exiting All That Dice. Thank you for playing!")
        exit()

    def run(self):
        """Main method that runs the application"""
        print("Welcome to All That Dice!")
        print("Developed by Alan Turing")
        print("COMP 1048 Object-Oriented Programming")
        while True:
            print("Please choose an option:")
            print("[r] Register Player")
            print("[p] Play Game")
            print("[s] Show Leaderboard")
            print("[q] Quit")
            choice = input("> ").lower()
            action = self.options.get(choice)
            if action:
                action()
            else:
                print("Invalid option, please try again.")

"""Class to modify Player and their attribute """
class Player:
    def __init__(self, name, chips=100, games_played=0, games_won=0, bid_amount=0):
        self.name = name
        self.chips = chips
        self.games_played = games_played
        self.games_won = games_won
        self.bid_amount = bid_amount


    def get_name(self):
        return self.name

    def get_chips(self):
        return self.chips

    def get_games_played(self):
        return self.games_played

    def get_games_won(self):
        return self.games_won

    def add_chips(self, amount):
        self.chips += amount

    def remove_chips(self, amount):
        if amount > self.chips:
            raise ValueError("Not enough chips to remove.")
        self.chips -= amount

    def update_games_played(self):
        self.games_played += 1

    def update_games_won(self):
        self.games_won += 1

    def bid(self, amount):
        self.remove_chips(amount)
        self.bid_amount = amount

    def win_bid(self, multiplier=2):  # Assuming the win is double the bid
        win_amount = self.bid_amount * multiplier
        self.add_chips(win_amount)

    def __str__(self):
        return f"Player {self.name} has {self.chips} chips, {self.games_played} played, and {self.games_won} won."

"""Class to modify Games class and their attribute """
class Game:
    def __init__(self, title, players, max_players, min_players):
        self.title = title
        self.players = players  # This should be a list of Player objects
        self.current_round = 0
        self.round_in_play = False
        self.winner = None
        self.max_players = max_players
        self.min_players = min_players


    def _start_game(self):
        """Protected method to perform the start game setup."""
        print(f"Starting game: {self.title}")
        self.round_in_play = True
        self.current_round = 1

    def start_game(self):
        """Public method to start the game."""
        self._start_game()

    def _end_game(self):
        """Ends the game."""
        print(f"Game finished: {self.title}")
        self.round_in_play = False
        if self.winner:
            print(f"The winner is {self.winner.get_name()}!")

    def _next_round(self):
        """Proceeds to the next round."""
        self.current_round += 1
        print(f"Round {self.current_round} starts.")

    def _calculate_winner_of_round(self):
        """Calculates the winner of the current round."""
        # Placeholder for calculation logic
        pass

    def _calculate_winner_of_game(self):
        """Calculates the overall winner of the game."""
        # Placeholder for calculation logic
        pass

    def _check_valid_num_player(self):
        """Checks if the number of players is valid for the game."""
        # Placeholder for checking logic
        pass

"""Class to modify the top player class and their attribute """
class Leaderboard:
    def __init__(self):
        self.player_scores = {}  # Dictionary to keep track of scores by player name

    def add_player(self, player):
        """Add a player to the leaderboard."""
        if player.name not in self.player_scores:
            self.player_scores[player.name] = player.chips

    def update_leaderboard(self, player):
        """Update a player's score on the leaderboard."""
        self.player_scores[player.name] = player.chips

    def display_leaderboard(self):
        """Display the leaderboard."""
        if not self.player_scores:
            print("No players to display on the leaderboard.")
            return
        # Sort the leaderboard by chips, descending
        sorted_scores = sorted(self.player_scores.items(), key=lambda item: item[1], reverse=True)
        print("Leaderboard:")
        for rank, (player_name, score) in enumerate(sorted_scores, start=1):
            print(f"{rank}. {player_name}: {score}")

"""Class to modify OddOrEven Game class and its attribute """
import random

class OddOrEven(Game):
    def __init__(self, players, max_players=4, min_players=2):
        super().__init__("OddOrEven", players, max_players, min_players)
        self.game_over = False  # Initialize the game_over attribute

    def play_game(self):
        """Handles the gameplay logic."""
        if not self.players:
            print("No players registered. Please register players before starting a game.")
            return

        # Initialize a list of player scores
        player_scores = {player.get_name(): 0 for player in self.players}

        # Simulate 3 rounds of the game (you can adjust the number of rounds)
        for round_number in range(3):
            print(f"Round {round_number + 1} starts.")
            for player in self.players:
                print(f"{player.get_name()}'s turn:")
                guess = input(f"{player.get_name()}, guess 'odd' or 'even': ").lower()
                while guess not in ["odd", "even"]:
                    print("Invalid guess. Please type 'odd' or 'even'.")
                    guess = input(f"{player.get_name()}, guess 'odd' or 'even': ").lower()

                # Simulate a dice roll (assuming Die class is defined)
                die = Die()
                roll = die.roll()
                print(f"The dice rolled a {roll}")

                if ((roll % 2 == 0 and guess == "even") or (roll % 2 != 0 and guess == "odd")):
                    print("Correct guess!")
                    player_scores[player.get_name()] += 1
                else:
                    print("Wrong guess.")

            # Display round results
            print("Round Results:")
            for player_name, score in player_scores.items():
                print(f"{player_name}: {score} points")

        # Determine the round winner
        round_winner = max(player_scores, key=player_scores.get)
        print(f"Round {self.current_round} winner: {round_winner}")
        self.current_round += 1

        # After 3 rounds, determine the game winner
        self.check_win_condition()

    def check_win_condition(self):
        # Implement the logic to check if a player has won the game
        # For example, if a player reaches a certain number of points, they win
        winning_score = 5  # Adjust this to your desired winning score
        for player in self.players:
            if player_scores[player.get_name()] >= winning_score:
                self._end_game(winner=player)
                return

        # If no one has won yet, continue to the next round
        self._next_round()

    def start_game(self):
        """Starts the game of Odd or Even."""
        self._start_game()
        while not self.game_over:
            self.play_game()

    def _end_game(self, winner=None):
        if winner:
            print(f"The winner of {self.title} is {winner.get_name()}!")
        else:
            print(f"{self.title} ended.")
        self.round_in_play = False


    def round_winner(self, player):
        pass
    def game_winner(self, player):
        pass

"""Class to modify Bunco Game class and its attribute """
class Bunco(Game):
    def __init__(self, title, players):
        super().__init__(title, players)

    def noPlayerPrompt(self):
        noPlayer = input("How many players? ")
        # Check the number of players and set it in your logic
        
    
    def play(self):
        """Play the Bunco game."""
        if not self.players:
            print("No players registered. Please register players before starting the game.")
            return

    def start_game(self):
        """Starts the Bunco game."""
        self._start_game()
        while not self.game_over:
            self.play()

    def playerNamePrompt(self):
        for i in range(1, self.__noPlayer + 1):  # Fix range to include the last player
            validPlayer = False
            while not validPlayer:
                playerName = input(f"What is the name of player #{i}?\n> ")
                existed = self.__playerManager.checkExistedPlayer(playerName)
                if existed:
                    if self.__playerManager.checkCurrentPlayer(playerName):
                        print("Player already in the game.")
                    else:
                        print(f"Player {playerName} registered successfully.")
                        self.__playerManager.addCurrentPlayer(playerName)
                        validPlayer = True
                else:
                    print("Player does not exist")


    def _end_game(self):
        pass
    def round_winner(self, player):
        pass
    def game_winner(self, player):
        pass

"""Class to modify Maxi Game class and its attribute """
class Maxi(Game):
    def __init__(self, title, players):
        # Call the superclass constructor with the title and the list of players
        super().__init__(title, players)

    def noPlayerPrompt(self):
        noPlayer = input("How many players? ")
        # Check the number of players and set it in your logic
        
    def play(self):
        """Play the Maxi game."""
        if not self.players:
            print("No players registered. Please register players before starting the game.")
            return

    def playerNamePrompt(self):
        for i in range(1, self.__noPlayer):
            validPlayer = False
            while not validPlayer:
                playerName = input(f"What is the name of player #{i}?\n> ")
                existed = self.__playerManager.checkExistedPlayer(playerName)
                if existed:
                    if self.__playerManager.checkCurrentPlayer(playerName):
                        print("Player already in the game.")
                    else:
                        self.__playerManager.addCurrentPlayer(playerName)
                        validPlayer = True
                else:
                    print("Player does not exist")

    def start_game(self):
        """Starts the Maxi game."""
        self._start_game()
        while not self.game_over:
            self.play()

    def _end_game(self):
        pass
    def round_winner(self, player):
        pass
    def game_winner(self, player):
        pass

"""Class to generate dice"""
class Die:
    def __init__(self, sides=6):
        self.sides = sides
        self.value = None  # Initialize the value attribute

    def roll(self):
        self.value = random.randint(1, self.sides)  # Use self.sides for the number of sides
        return self.value

    def __str__(self):
        return f"A {self.sides}-sided die with a current value of {self.value}"


"""Class to check valid number of Players"""
class ValidPlayerNumber:
    def __init__(self, min_players, max_players):
        self.min_players = min_players
        self.max_players = max_players

    def is_valid(self, num_players):
        """Check if the number of players is within the valid range."""
        return self.min_players <= num_players <= self.max_players

    def get_valid_range(self):
        """Get the valid range of players as a tuple (min_players, max_players)."""
        return self.min_players, self.max_players



"""Class for chip"""
class Chip:
    def __init__(self, value):
        self.value = value
        self.bid = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def add_bid(self, amount):
        if self.bid is None:
            self.bid = 0
        self.bid += amount

    def set_bid(self, amount):
        self.bid = amount

    def get_bid(self):
        return self.bid

    def clear_bid(self):
        self.bid = None

    def __str__(self):
        return f"Chip with value {self.value}, bid: {self.bid if self.bid is not None else 'None'}"


# Assuming other classes (Player, OddOrEven, MaxiGame, BuncoGame, Leaderboard) are defined appropriately
# according to the UML diagram and provided snippets.
if __name__ == "__main__":
    game_app = AllThatDice()
    game_app.run()
    # Create a six-sided die
    six_sided_die = Die()
     # Roll the die and print the result
    result = six_sided_die.roll()
    print(f"Rolling the die... Result: {result}")

    # Roll the die again
    result = six_sided_die.roll()
    print(f"Rolling the die again... Result: {result}")


    # Define a valid player range for a game (e.g., between 2 and 4 players)
    valid_player_range = ValidPlayerNumber(min_players=2, max_players=4)

    # Check if a specific number of players is valid
    num_players = 3  # Change this to the number of players you want to check
    if valid_player_range.is_valid(num_players):
        print(f"{num_players} players is a valid number for this game.")
    else:
        min_players, max_players = valid_player_range.get_valid_range()
        print(f"Number of players must be between {min_players} and {max_players}.")