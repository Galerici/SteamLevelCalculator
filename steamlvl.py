import colorama 
from colorama import Fore, Back, Style
from sys import exit
from math import ceil
from time import sleep

colorama.init()

print(Fore.CYAN)
print( """\

╔═╗╔╦╗╔═╗╔═╗╔╦╗  ╦  ╔═╗╦  ╦╔═╗╦    ╔═╗╔═╗╦  ╔═╗╦ ╦╦  ╔═╗╔╦╗╔═╗╦═╗
╚═╗ ║ ║╣ ╠═╣║║║  ║  ║╣ ╚╗╔╝║╣ ║    ║  ╠═╣║  ║  ║ ║║  ╠═╣ ║ ║ ║╠╦╝
╚═╝ ╩ ╚═╝╩ ╩╩ ╩  ╩═╝╚═╝ ╚╝ ╚═╝╩═╝  ╚═╝╩ ╩╩═╝╚═╝╚═╝╩═╝╩ ╩ ╩ ╚═╝╩╚═
Discord: discord.gg/HMMGKdC
Github: github.com/Galerici
                                                                                                                         
                                                       
 """ )

# Basic information printed every time
print(	">>>Enter the following information to calculate cost of desired Steam level",
	"\n>>>Calculations are based on XP\n>>>To force exit press CTRL + C\n")

# Formatting
hyp_count = 29		# Number of hyphens printed
right_align = 21	# Right aligning input() message
secs = 5		# Sleep for this many seconds

error_msgs = 	{
			0 : "\n>>>ERROR: minimum value is 0",
			1 : "\n>>>ERROR: identical Current XP and Desired XP",
			2 : "\n>>>ERROR: higher Current XP than Desired XP",
			3 : "\n>>>ERROR: minimum value is 100",
			4 : "\n>>>ERROR: positive value required",
			5 : "\n>>>ERROR: minimum value is 5",
			6 : "\n>>>ERROR: maximum value is 15",
			7 : "\n>>>ERROR: enter a whole number",
			8 : "\n>>>Force exited"
	}

def print_error(msg):
	"""The function takes an integer parameter.
	Prints hyphens, error messages, and takes care of stopping script execution"""
	global secs
	print("-" * hyp_count)
	print(error_msgs[msg])		# Here the message is referened and printed from error_msgs
	if msg == 8:
		secs = 0		# Should have instant effect in the case of CTRL + C
	sleep(secs)
	exit()

try:
	"""User input inside of try for exception handling"""
	print("-" * hyp_count)
	print("{:>{}}".format("INPUT", right_align + 5))
	current_xp = int(input("{:>{}}".format("Current XP: ", right_align)))
	if current_xp < 0:
		print_error(0)

	desired_level_xp = int(input("{:>{}}".format("Desired XP: ", right_align)))
	if desired_level_xp == current_xp:
		print_error(1)

	elif desired_level_xp < current_xp:
		print_error(2)

	elif desired_level_xp < 100:
		print_error(3)

	card_cost = round(float(input("{:>{}}".format("Cost of one card: ", right_align))), 2)
	if card_cost <= 0:
		print_error(4)

	num_of_cards = int(input("{:>{}}".format("Cards in badge: ", right_align)))
	if num_of_cards < 5:
		print_error(5)

	elif 15 < num_of_cards:
		print_error(6)

except ValueError:
	print_error(7)
except KeyboardInterrupt:
	print()					# Print newline character, else hyphens printed in input line
	print_error(8)

def roundup(xp):				# Round up by 100 because one badge equals 100 XP
	return int(ceil(xp / 100.0)) * 100 	# Example: you have 25 XP and want to reach level 1 (100 XP),
						#          you therefore need one badge. Since getting a fraction of
						#          a badge is not possible, you need the whole badge.
						# Not taking this into account would result in an incorrect
						# amount of badges needed (i.e. n-1).
def main():
	""""All of the calculations take place inside of main(), so that it's easier to see what's going on"""
	
	# Calculations
	xp_needed = (desired_level_xp - current_xp)
	num_of_badges_needed = (roundup(xp_needed) / 100)
	badge_cost = float(card_cost * num_of_cards)
	desired_level_cost = float(badge_cost * num_of_badges_needed)
	
	# Printing the result
	print("\n{:>{}}".format("OUTPUT", right_align + 6))
	if str(desired_level_cost).endswith("0"): 		# If a whole number, print it in int format (i.e. print 5 not 5.0)
		print("{:>{}}{:,}".format("Cost: ", right_align, int(desired_level_cost)))
	else:
		print("{:>{}}{:,.2f}".format("Cost: ", right_align, desired_level_cost))
	print("{:>{}}{:,}".format("Badges needed: ", right_align, int(num_of_badges_needed)))
	print("-" * hyp_count)
	sleep(secs)

if __name__ == "__main__":
	main()
