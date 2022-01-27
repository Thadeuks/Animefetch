def user_info(info):
	user = getuser() #user
	node = platform.node()#node
	user_node = f'{Style.RESET_ALL}{Fore.CYAN+user}{Style.RESET_ALL+"@"}{Fore.CYAN+node}{Style.RESET_ALL}'

def os_information(info):
	#OS
	os = platform.system() #Operative system
	os_version = platform.release() #OS version (release)
	architecture = platform.architecture(bits='') #System architecture
	os_info = f'{Fore.CYAN+"OS:"} {Style.RESET_ALL+os} {os_version} x{architecture[0]}'

	#Boot time
	boot_time = datetime.datetime.strptime(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
	bt_hour= int(boot_time.hour) #Boot time hour
	bt_minute = int(boot_time.minute) # Boot time minute

	#Time now
	dt = datetime.datetime.now() #Datetime now
	n_hour = int(dt.hour) #Hour now
	n_minute = int(dt.minute) #Minute now

def uptime_information(info):
	#Uptime
	uptime_hour = n_hour-bt_hour #Uptime hour
	uptime_minute = n_minute-bt_minute #Uptime minute
	if uptime_hour<0:
		uptime_hour = (uptime_hour*-1) +24
	if uptime_minute < 0:
		uptime_hour = uptime_hour-1
		uptime_minute = 60 - (uptime_minute*-1)
	uptime_info = f'{Fore.CYAN + "Uptime: "}{Style.RESET_ALL+str(uptime_hour)} hrs {str(uptime_minute)} mins'
		
def cpu_information(info):
	#CPU
	cpu = platform.processor() #Processor
	cpu_frequency = psutil.cpu_freq() #CPU frequency info
	max_freq = f'@ {round(cpu_frequency.max/1000, 2)} Ghz' #CPU maximum frequency (Gigahertz)
	cpu_info = f'{Fore.CYAN+ "CPU:"} {Style.RESET_ALL + cpu} {max_freq}'
		

def memory_information(info):
	#RAM
	memory = psutil.virtual_memory() #Memory info
	total_memory = f'{round(memory.total / 1000000000, 2)} Gb' #Total memory (Gigabytes)
	memory_info = f'{Fore.CYAN+"Memory:"} {Style.RESET_ALL+total_memory}'

	#Return the system info
	if info == 'user/node': #Info to return
		return user_node
	elif info == 'os':
		return os_info
	elif info == 'uptime':
		return uptime_info
	elif info == 'cpu':
		return cpu_info
	elif info == 'memory':
		return memory_info

def create_themes():
	theme_1 = f""" 
{Fore.MAGENTA+"⢸⣿⣿⣿⣿⠃⠄⢀⣴⡾⠃⠄⠄⠄⠄⠄⠈⠺⠟⠛⠛⠛⠛⠻⢿⣿⣿⣿⣿⣶⣤⡀⠄"}
{Fore.MAGENTA+"⢸⣿⣿⣿⡟⢀⣴⣿⡿⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣸⣿⣿⣿⣿⣿⣿⣿⣷ "} {user_information('user/node')} 
{Fore.MAGENTA+"⢸⣿⣿⠟⣴⣿⡿⡟⡼⢹⣷⢲⡶⣖⣾⣶⢄⠄⠄⠄⠄⠄⢀⣼⣿⢿⣿⣿⣿⣿⣿⣿⣿ "} -----------------------------
{Fore.MAGENTA+"⢸⣿⢫⣾⣿⡟⣾⡸⢠⡿⢳⡿⠍⣼⣿⢏⣿⣷⢄⡀⠄⢠⣾⢻⣿⣸⣿⣿⣿⣿⣿⣿⣿ "} {os_information('os')}
{Fore.MAGENTA+"⡿⣡⣿⣿⡟⡼⡁⠁⣰⠂⡾⠉⢨⣿⠃⣿⡿⠍⣾⣟⢤⣿⢇⣿⢇⣿⣿⢿⣿⣿⣿⣿⣿ "} {uptime_information('uptime')}
{Fore.MAGENTA+"⣱⣿⣿⡟⡐⣰⣧⡷⣿⣴⣧⣤⣼⣯⢸⡿⠁⣰⠟⢀⣼⠏⣲⠏⢸⣿⡟⣿⣿⣿⣿⣿⣿ "} {cpu_information('cpu')}
{Fore.MAGENTA+"⣿⣿⡟⠁⠄⠟⣁⠄⢡⣿⣿⣿⣿⣿⣿⣦⣼⢟⢀⡼⠃⡹⠃⡀⢸⡿⢸⣿⣿⣿⣿⣿⡟ "} {memory_information('memory')}
{Fore.MAGENTA+"⣿⣿⠃⠄⢀⣾⠋⠓⢰⣿⣿⣿⣿⣿⣿⠿⣿⣿⣾⣅⢔⣕⡇⡇⡼⢁⣿⣿⣿⣿⣿⣿⢣ "}	
{Fore.MAGENTA+"⣿⡟⠄⠄⣾⣇⠷⣢⣿⣿⣿⣿⣿⣿⣿⣭⣀⡈⠙⢿⣿⣿⡇⡧⢁⣾⣿⣿⣿⣿⣿⢏⣾  "}	
{Fore.MAGENTA+"⣿⡇⠄⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢻⠇⠄⠄⢿⣿⡇⢡⣾⣿⣿⣿⣿⣿⣏⣼⣿ "}	
{Fore.MAGENTA+"⣿⣷⢰⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⢰⣧⣀⡄⢀⠘⡿⣰⣿⣿⣿⣿⣿⣿⠟⣼⣿⣿ "}	
{Fore.MAGENTA+"⢹⣿⢸⣿⣿⠟⠻⢿⣿⣿⣿⣿⣿⣿⣿⣶⣭⣉⣤⣿⢈⣼⣿⣿⣿⣿⣿⣿⠏⣾⣹⣿⣿ "}	
{Fore.MAGENTA+"⢸⠇⡜⣿⡟⠄⠄⠄⠈⠙⣿⣿⣿⣿⣿⣿⣿⣿⠟⣱⣻⣿⣿⣿⣿⣿⠟⠁⢳⠃⣿⣿⣿ "}	
{Fore.MAGENTA+"⠄⣰⡗⠹⣿⣄⠄⠄⠄⢀⣿⣿⣿⣿⣿⣿⠟⣅⣥⣿⣿⣿⣿⠿⠋⠄⠄⣾⡌⢠⣿⡿⠃ "}	
{Fore.MAGENTA+"⠜⠋⢠⣷⢻⣿⣿⣶⣾⣿⣿⣿⣿⠿⣛⣥⣾⣿⠿⠟⠛⠉⠄⠄ "}	

	"""
	theme_2 = f"""
{Fore.MAGENTA+"⠄⠄⠄⢰⣧⣼⣯⠄⣸⣠⣶⣶⣦⣾⠄⠄⠄⠄⡀⠄⢀⣿⣿⠄⠄⠄⢸⡇⠄⠄"}	
{Fore.MAGENTA+"⠄⠄⠄⣾⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄⠸⢀⣿⠄"}	{user_information('user/node')}
{Fore.MAGENTA+"⠄⠄⢀⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿⣿⠄"}	-------------------------------
{Fore.MAGENTA+"⠄⠄⢸⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⠄"}	{os_information('os')}
{Fore.MAGENTA+"⠄⢀⢸⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠉⠋⣰"}	{uptime_information('uptime')}
{Fore.MAGENTA+"⠄⣼⣖⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⠇⢀⣤"}	{cpu_information('cpu')}
{Fore.MAGENTA+"⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴⣿⡗"}	{memory_information('memory')}
{Fore.MAGENTA+"⢀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄"}	
{Fore.MAGENTA+"⢸⣿⣦⣌⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄"}	
{Fore.MAGENTA+"⠘⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿⣿⣿⣵⣾⠃⠄"}	
{Fore.MAGENTA+"⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠃⠄⠄"}	
{Fore.MAGENTA+"⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁⠄⠄⠄"}	
{Fore.MAGENTA+"⠄⠄⠄⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁⠄⠄⠄⠄⠄"}	
{Fore.MAGENTA+"⠄⠄⠄⠄⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁⠄⠄⠄⠄⠄⢀⣠⣴"}	
{Fore.MAGENTA+"⣿⣿⣿⣶⣶⣮⣥⣒⠲⢮⣝⡿⣿⣿⡆⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⣠⣴⣿⣿⣿"}	
	"""
	theme_3 = f"""
{Fore.MAGENTA+"⡆⣐⢕⢕⢕⢕⢕⢕⢕⢕⠅⢗⢕⢕⢕⢕⢕⢕⢕⠕⠕⢕⢕⢕⢕⢕⢕⢕⢕⢕"}
{Fore.MAGENTA+"⢐⢕⢕⢕⢕⢕⣕⢕⢕⠕⠁⢕⢕⢕⢕⢕⢕⢕⢕⠅⡄⢕⢕⢕⢕⢕⢕⢕⢕⢕"}	{get_sys_info('user/node')}
{Fore.MAGENTA+"⢕⢕⢕⢕⢕⠅⢗⢕⠕⣠⠄⣗⢕⢕⠕⢕⢕⢕⠕⢠⣿⠐⢕⢕⢕⠑⢕⢕⠵⢕"}	---------------------------
{Fore.MAGENTA+"⢕⢕⢕⢕⠁⢜⠕⢁⣴⣿⡇⢓⢕⢵⢐⢕⢕⠕⢁⣾⢿⣧⠑⢕⢕⠄⢑⢕⠅⢕"}	{os_information('os')}
{Fore.MAGENTA+"⢕⢕⠵⢁⠔⢁⣤⣤⣶⣶⣶⡐⣕⢽⠐⢕⠕⣡⣾⣶⣶⣶⣤⡁⢓⢕⠄⢑⢅⢑"}	{uptime_information('uptime')}
{Fore.MAGENTA+"⠍⣧⠄⣶⣾⣿⣿⣿⣿⣿⣿⣷⣔⢕⢄⢡⣾⣿⣿⣿⣿⣿⣿⣿⣦⡑⢕⢤⠱⢐"}	{cpu_information('cpu')}
{Fore.MAGENTA+"⢠⢕⠅⣾⣿⠋⢿⣿⣿⣿⠉⣿⣿⣷⣦⣶⣽⣿⣿⠈⣿⣿⣿⣿⠏⢹⣷⣷⡅⢐"}	{memory_information('memory')}
{Fore.MAGENTA+"⣔⢕⢥⢻⣿⡀⠈⠛⠛⠁⢠⣿⣿⣿⣿⣿⣿⣿⣿⡀⠈⠛⠛⠁⠄⣼⣿⣿⡇⢔"}
{Fore.MAGENTA+"⢕⢕⢽⢸⢟⢟⢖⢖⢤⣶⡟⢻⣿⡿⠻⣿⣿⡟⢀⣿⣦⢤⢤⢔⢞⢿⢿⣿⠁⢕"}
{Fore.MAGENTA+"⢕⢕⠅⣐⢕⢕⢕⢕⢕⣿⣿⡄⠛⢀⣦⠈⠛⢁⣼⣿⢗⢕⢕⢕⢕⢕⢕⡏⣘⢕"}
{Fore.MAGENTA+"⢕⢕⠅⢓⣕⣕⣕⣕⣵⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣷⣕⢕⢕⢕⢕⡵⢀⢕⢕"}
{Fore.MAGENTA+"⢑⢕⠃⡈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢃⢕⢕⢕"}
{Fore.MAGENTA+"⣆⢕⠄⢱⣄⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢁⢕⢕⠕⢁"}
{Fore.MAGENTA+"⣿⣦⡀⣿⣿⣷⣶⣬⣍⣛⣛⣛⡛⠿⠿⠿⠛⠛⢛⣛⣉⣭⣤⣂⢜⠕⢑⣡⣴⣿"}
	"""

	theme_4 = f"""
{Fore.MAGENTA+"⡿⠋⠄⣀⣀⣤⣴⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣌⠻⣿⣿"}
{Fore.MAGENTA+"⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠹⣿"}	{get_sys_info('user/node')}
{Fore.MAGENTA+"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠹"}	------------------------
{Fore.MAGENTA+"⣿⣿⡟⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡛⢿⣿⣿⣿⣮⠛⣿⣿⣿⣿⣿⣿⡆"}	{os_information('os')}
{Fore.MAGENTA+"⡟⢻⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣣⠄⡀⢬⣭⣻⣷⡌⢿⣿⣿⣿⣿⣿"}	{uptime_information('uptime')}
{Fore.MAGENTA+"⠃⣸⡀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠈⣆⢹⣿⣿⣿⡈⢿⣿⣿⣿⣿"}	{cpu_information('cpu')}
{Fore.MAGENTA+"⠄⢻⡇⠄⢛⣛⣻⣿⣿⣿⣿⣿⣿⣿⣿⡆⠹⣿⣆⠸⣆⠙⠛⠛⠃⠘⣿⣿⣿⣿"}	{memory_information('memory')}
{Fore.MAGENTA+"⠄⠸⣡⠄⡈⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠁⣠⣉⣤⣴⣿⣿⠿⠿⠿⡇⢸⣿⣿⣿"}
{Fore.MAGENTA+"⠄⡄⢿⣆⠰⡘⢿⣿⠿⢛⣉⣥⣴⣶⣿⣿⣿⣿⣻⠟⣉⣤⣶⣶⣾⣿⡄⣿⡿⢸"}
{Fore.MAGENTA+"⠄⢰⠸⣿⠄⢳⣠⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣼⣿⣿⣿⣿⣿⣿⡇⢻⡇⢸"}
{Fore.MAGENTA+"⢷⡈⢣⣡⣶⠿⠟⠛⠓⣚⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢸⠇⠘"}
{Fore.MAGENTA+"⡀⣌⠄⠻⣧⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠛⠛⢿⣿⣿⣿⣿⣿⡟⠘⠄⠄"}
{Fore.MAGENTA+"⣷⡘⣷⡀⠘⣿⣿⣿⣿⣿⣿⣿⣿⡋⢀⣠⣤⣶⣶⣾⡆⣿⣿⣿⠟⠁⠄⠄⠄⠄"}
{Fore.MAGENTA+"⣿⣷⡘⣿⡀⢻⣿⣿⣿⣿⣿⣿⣿⣧⠸⣿⣿⣿⣿⣿⣷⡿⠟⠉⠄⠄⠄⠄⡄⢀"}
{Fore.MAGENTA+"⣿⣿⣷⡈⢷⡀⠙⠛⠻⠿⠿⠿⠿⠿⠷⠾⠿⠟⣛⣋⣥⣶⣄⠄⢀⣄⠹⣦⢹⣿"}
	"""

	themes = [0] #For the themes index to start in 1
	#Add the themes to the themes list
	themes.append(theme_1)
	themes.append(theme_2)
	themes.append(theme_3)
	themes.append(theme_4)


	return themes #Return themes list


def main(theme):
	try:
		themes = create_themes() #All the themes (list)
		print(themes[int(theme)]) #Print the theme that the user selected (default: 3)
	except:
		print("That Animefetch theme isn't available")