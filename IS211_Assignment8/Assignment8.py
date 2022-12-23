#!user/bin/env python
# -*- coding: utf-8 -*-
"""
This module shows an update of a simple game called Pig using the Factory and
Proxy patterns.
"""
import random
import datetime
import argparse

class Die:
    """The die which has 6 sides."""
    def __init__(self, seed=None):
        """Initialize the die with an optional seed for the random number generator."""
        if seed is not None:
            random.seed(seed)

    def roll(self):
        """Return a random integer between 1 and 6, inclusive."""
        return random.randint(1, 6)

def create_player(player_type: str, name: str) -> 'Player':
    """Create a player based on the specified type."""
    if player_type == 'human':
        return HumanPlayer(name)
    if player_type == 'computer':
        return ComputerPlayer(name)
    else:
        print("Invalid input.")
        exit()


class Player:
    """Constructor for a player in the Pig game."""
    def __init__(self, name: str):
        self.name = name
        self.total_score = 0
        self.turns_score = 0


class HumanPlayer(Player):
    """Constructor for a human player in the Pig game."""
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.strategy = False

class ComputerPlayer(Player):
    """Constructor for a computer player in the Pig game."""
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.strategy = True

def create_game(player1: 'Player', player2: 'Player', timed: bool=False, seed: int=None) -> 'Game':
    """Create a Pig game with the specified players and optional seed and timing."""
    if timed:
        return TimedGame(player1, player2, seed)
    else:
        return Game(player1, player2, seed)

class Game:
    """Constructor for the Pig game."""
    def __init__(self, player1: 'Player', player2: 'Player', seed: int=None):  
        self.player1 = player1
        self.player2 = player2
        self.die = Die(seed)

    def turn(self, player: 'Player'):
        """A player's turn in the Pig game."""
        print(f'\nIt is Player {player.name}\'s turn.')
        roll = self.die.roll()
        print(f'\nYou rolled a {roll}.')
        if roll == 1:
            player.turns_score = 0
            print(f'\nOops! You rolled a 1, next player.')
            print('-' * 60, '\n')
            self.next_player(player)
        else:
            player.turns_score += roll
            player.total_score += roll
            print(f'Your total this turn is {player.turns_score}.')
            if player.total_score >= 100:
                print(f'{player.name} is the winner with a score of {player.total_score}!')
                exit()
            if isinstance(player, ComputerPlayer):
                self.strategy(player)
            else:
                self.player_ans(player)
    
    def strategy(self, player: 'ComputerPlayer'):
        """Determine the computer player's strategy for the turn."""
        if player.turns_score < 25:
            self.turn(player)
        else:
            print('\nYour turn is now over.\n')
            player.turns_score = 0
            print(f'{player.name}\'s total score is now {player.total_score}.\n\n')
            print('-' * 60, '\n')
            self.next_player(player)
                

    def next_player(self, player: 'Player'):
        """Switch to the next player's turn."""
        if player == self.player1:
            self.turn(self.player2)
        else:
            self.turn(self.player1)

    def player_ans(self, player: 'HumanPlayer'):
        """Determine the human player's response to their roll."""
        print(f'The total for this player is {player.total_score}.')
        ans = input('Would you like to roll again? r = roll h = hold ').lower()
        if ans == 'h':
            print('\nYour turn is now over.\n')
            player.turns_score = 0
            print(f'{player.name}\'s total score is now {player.total_score}.\n\n')
            print('-' * 60, '\n')
            self.next_player(player)
        elif ans == 'r':
            self.turn(player)
        else:
            print('Invalid option, r = roll h = hold')
            self.player_ans(player)

    def next_player(self, player: 'Player'):
        """Switch to the next player's turn."""
        if player == self.player1:
            self.turn(self.player2)
        else:
            self.turn(self.player1)


class TimedGame(Game):
    """A timed version of the Pig game."""
    def __init__(self, player1: 'Player', player2: 'Player', seed: int=None):
        super().__init__(player1, player2, seed)
        self.start_time = datetime.datetime.now()

    def turn(self, player: 'Player'):
        """A player's turn in the timed Pig game."""
        super().turn(player)
        if (datetime.datetime.now() - self.start_time).seconds >= 10:
            print('Time is up!')
            exit()


def main():
    """The main function for the Pig game."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--timed', action='store_true', help='play a timed version of the game')
    parser.add_argument('--seed', type=int, help='seed for the random number generator')
    parser.add_argument('player1', type=str, help='type of player 1')
    parser.add_argument('--player1_name', type=str, help='name of the first player')
    parser.add_argument('player2', type=str, help='type of player 2')
    parser.add_argument('--player2_name', type=str, help='name of the second player')

    args = parser.parse_args()

    player1 = HumanPlayer(args.player1_name)
    player2 = HumanPlayer(args.player2_name)
    game = create_game(player1, player2, args.timed, args.seed)
    game.turn(player1)


    # player1 = create_player(args.player1, args.player1_name)
    # player2 = create_player(args.player2, args.player2_name)
    # game = create_game(player1, player2, args.timed, args.seed)
    # game.turn(player1)


if __name__ == '__main__':
    main()



    # player1 = create_player('human', 'Alice')
    # player2 = create_player('computer', 'Bob')
    # game = create_game(player1, player2, timed=False, seed=123)
