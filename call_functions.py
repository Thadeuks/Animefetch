#libraries/modules
from getpass import getuser
import platform 
import psutil #docs -> https://pypi.org/project/psutil/
from colorama import Fore, init, Style #docs -> https://pypi.org/project/colorama/
import time
import datetime
import argparse
import functions

init() #start colorama modules

parser = argparse.ArgumentParser(description='System Information Tool')
parser.add_argument('-th', '--theme', type=int, default=3, required=False, help='Theme you want to be shown (4 themes available') #Add theme argument (default: 3)

args = parser.parse_args()


def main(theme):
	try:
		themes = create_themes() #All the themes (list)
		print(themes[int(theme)]) #Print the theme that the user selected (default: 3)
	except:
		print("That Animefetch theme isn't available")

main(args.theme) 
#Code made by Thadeuks