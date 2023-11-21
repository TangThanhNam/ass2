#
# File: filename.py
# Description: A brief description of this Python module.
# Author: Thanh Nam Tang
# Student ID: 
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

    def play_game(self):
        """Handles the gameplay logic."""
        if not self.players:
            print("No players registered. Please register players before starting a game.")
            return
        # Display game options here and instantiate a game based on the choice
        game_choice = input("Choose a game to play (OddOrEven/Maxi/Bunco): ").lower()
        if game_choice == "oddoreven":
            self.current_game = OddOrEven(self.players)
        elif game_choice == "maxi":
            self.current_game = MaxiGame(self.players)
        elif game_choice == "bunco":
            self.current_game = BuncoGame(self.players)
        else:
            print("Invalid game choice.")
            return
        # Start and manage the game
        self.current_game.start_game()

    def display_leaderboard(self):
        """Displays the leaderboard."""
        # Assuming Leaderboard class exists with a method to display the leaderboard
        leaderboard = Leaderboard()  # Assuming Leaderboard class has the appropriate constructor
        leaderboard.display()  # Assuming a method to display the leaderboard

    def quit(self):
        """Quits the application."""
        print("Exiting All That Dice. Thank you for playing!")
        exit()

    def run(self):
        """Main method that runs the application."""
        while True:
            print("Welcome to All That Dice!")
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
    def __init__(self, name, chips, games_played, games_won, bid_amount):
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
    def __init__(self, title, players):
        self.title = title
        self.players = players  # This should be a list of Player objects
        self.current_round = 0
        self.round_in_play = False
        self.winner = None

    def _start_game(self):
        """Starts the game."""
        print(f"Starting game: {self.title}")
        self.round_in_play = True

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

"""Class to modify OddOrEven Game class and its attribute """
class OddOrEven(Game):
    def __init__(self, players):
        super().__init__("Odd or Even", players)

    def play_round(self):
        """Implements playing a round specific to OddOrEven."""
        if not self.round_in_play:
            self._start_game()
        self._next_round()
        # Round play logic for OddOrEven

    def play_turn(self, player):
        """Implements playing a turn for the given player."""
        # Turn play logic for OddOrEven
        pass

    def check_win_condition(self):
        """Checks the win condition specific to OddOrEven."""
        # Win condition checking logic for OddOrEven
        pass

"""Class to generate dice"""
class Dice:
    def __init__(self, die):
        self.__die = die

    def roll(self):
        self.__die = random.randint(1, 6)
        if self.__die == 1:
            print("⚀\n")
        elif self.__die == 2:
            print("⚁\n")
        elif self.__die == 3:     
            print("⚂\n")
        elif self.__die == 4:
            print("⚃\n")
        elif self.__die == 5:
            print("⚄\n")
        elif self.__die == 6:
            print("⚅\n")
# Assuming other classes (Player, OddOrEven, MaxiGame, BuncoGame, Leaderboard) are defined appropriately
# according to the UML diagram and provided snippets.

if __name__ == "__main__":
    game_app = AllThatDice()
    game_app.run()