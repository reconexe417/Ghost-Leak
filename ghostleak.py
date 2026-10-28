from xposedornot import XposedOrNot
import sys
import time
from termcolor import cprint, colored
from pyfiglet import figlet_format, Figlet

cprint(figlet_format('Ghost Leak', font='slant'), 'green', attrs=['bold'])

usr_in = sys.argv[1:]

if not usr_in:
	print("No arguments provided to the program, quitting...")
	time.sleep(2)
	sys.exit(0)

XON = XposedOrNot()

for item in usr_in:
	print(f"Checking mail: {item}")
	check = XON.check_email(item)


	if check.status != "success":
		print(f"could not find any breaches of {usr_in}.")
		sys.exit(1)



	for number, breach in enumerate(check.breaches, start=1):
                print(f"[{number}] {breach}")


