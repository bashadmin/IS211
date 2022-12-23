import random

class Die:
    def roll(self):
        return random.randint(1, 6)

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.turn_score = 0

    def roll(self):
        roll = die.roll()
        if roll == 1:
            self.turn_score = 0
            return "You rolled a 1! Your turn is over and you scored 0 points this turn."
        else:
            self.turn_score += roll
            return "You rolled a {}. Your turn score is now {}.".format(roll, self.turn_score)

    def hold(self):
        self.score += self.turn_score
        self.turn_score = 0
        return "You decided to hold. Your total score is now {}.".format(self.score)

class Game:
    def __init__(self, players):
        self.players = players
        self.die = Die()
        self.current_player = 0

    def play_turn(self):
        player = self.players[self.current_player]
        print("It's {}'s turn.".format(player.name))
        while True:
            decision = input("Enter 'r' to roll or 'h' to hold: ")
            if decision == 'r':
                result = player.roll()
                print(result)
            elif decision == 'h':
                result = player.hold()
                print(result)
                break
            else:
                print("Invalid decision. Please enter 'r' or 'h'.")
    
    def is_game_over(self):
        return any(player.score >= 100 for player in self.players)
    
    def play(self):
        while not self.is_game_over():
            self.play_turn()
            self.current_player = (self.current_player + 1) % len(self.players)
        print("Game over! The winner is {}!".format(self.players[self.current_player].name))

# Create the players
player1 = Player("Player 1")
player2 = Player("Player 2")
players = [player1, player2]

# Start the game
game = Game(players)
game.play()