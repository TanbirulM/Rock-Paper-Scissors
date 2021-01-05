import random

def play_game():
	print('Welcome to Rock Paper Scissors!')

	player_score = 0
	bot_score = 0

	while True: 
		print('Make your choice:')
		choice = str(input()).lower()

		print("My choice is", choice)

		choices = ['rock', 'paper', 'scissor', 'end']
		bot_choices = ['rock', 'paper', 'scissor']

		bot_choice = random.choice(bot_choices)

		print("Computer choice is", bot_choice)
		if choice in choices:
			if choice == bot_choice:
				print('it is a tie')
			elif choice == 'rock':
				if bot_choice == 'paper':
					print('sorry, you lose')
					bot_score += 1
				elif bot_choice == 'scissor':
					print('You win!')
					player_score += 1
			elif choice == 'paper':
				if bot_choice == 'scissor':
					print('sorry, you lose')
					bot_score += 1
				elif bot_choice == 'rock':
					print('You win!')
					player_score += 1
			elif choice == 'scissor':
				if bot_choice == 'rock':
					print('sorry, you lose')
					bot_score += 1
				elif bot_choice == 'paper':
					print('You win!')
					player_score += 1
			elif choice == 'end':
				if player_score > bot_score:
					print('game has ended, player has won :D')
				elif player_score < bot_score:
					print('game has ended, computer has won :(')
				else:
					print('game has ended in a draw')
				break

			print('Player Score: ', player_score, ', Bot Score: ', bot_score)
		
		else:
			print('invalid choice, try again')

		print('--------------------------------')


def main():
    play_game()

# Standard call for main() function
if __name__ == '__main__':
    main()
