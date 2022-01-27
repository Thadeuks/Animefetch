#libraries/modules
from getpass import getuser
import platform 
import psutil #docs -> https://pypi.org/project/psutil/
from colorama import Fore, init, Style #docs -> https://pypi.org/project/colorama/
import time
import datetime
import argparse

init() #start colorama modules

parser = argparse.ArgumentParser(description='System Information Tool')
parser.add_argument('-th', '--theme', type=int, default=3, required=False, help='Theme you want to be shown (4 themes available') #Add theme argument (default: 3)

args = parser.parse_args()

main(args.theme) 
#Code made by Thadeuks