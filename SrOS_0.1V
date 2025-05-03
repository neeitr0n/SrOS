import sys
from datetime import datetime
import os
import subprocess
import json
import time
import shutil
from pathlib import Path
import paramiko
import platform
import math

COLORS = {
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "reset": "\033[0m"
}
current_color = COLORS["white"]

COLOR_CONFIG_FILE = "conf./colorconfig.json"
USER_CONFIG_FILE = "conf./usrlist.json"
MARKER_FILE = "fl.marker"

REQUIRED_LIBRARIES = ["paramiko"] 

def install_package(package):
    try:
        __import__(package)
    except ImportError:
        print(f"Download missing library: {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

for lib in REQUIRED_LIBRARIES:
    install_package(lib)

def qalc():

    print("It's a Qalc - Ver. 0.6")
    print("")

    global x,y,z

    def add(x,y):
        print()
        print(f"Result: ",x," + ",y," = ",x+y)
        print()

    def subtract(x,y):
        print()
        print(f"Result: ",x," - ",y," = ",x-y)
        print()

    def multiply(x,y):
        print()
        print(f"Result: ",x," * ",y," = ",x*y)
        print()

    def divide(x,y):
        print()
        print(f"Result: ",x," / ",y," = ",x/y) 
        print()

    def power(x,y):
        print()
        print(f"Result: ",x," ^ ",y," = ",x**y)
        print()

    def root(x):
        print()
        print(f"Result: "," √",x," = ",math.sqrt(x))
        print()

    def factorial(x):
        print()
        print(f"Result: ", x, "!", " =", math.factorial(x))
        print()

    def qes(x,y,z):
        try:
            x = float(input("Input the A - "))
            y = float(input("Input the B - "))
            z = float(input("Input the C - "))
            
            discr = y ** 2 - 4 * x * z 
            print("Discriminant = %.2f" % discr)
            print()

            if discr > 0:
                x1 = (-y + math.sqrt(discr)) / (2*x)
                x2 = (-y - math.sqrt(discr)) / (2*x)
                print("Two real roots:", x1,';', x2, "\n")
            elif discr == 0:
                x3 = -y / (2*x)
                print("Single root:", x3, "\n")
            else:
                print("No real roots (complex solutions exist)\n")
        except ValueError:
            print("Error: Invalid input\n")

    def percentcal(x,y):
        try:
            prcfirnumber = float(input("Enter the first number(main) - "))
            prcact = input("Enter the action(+; -; *; /) - ").strip()
            prcsecnumber = float(input("Enter the second number(percent) - "))
            print() 

            if prcact == "+":
                prcresult = prcfirnumber + prcfirnumber/100*prcsecnumber
                print(f"Result: {prcfirnumber} + {prcsecnumber}% = {prcresult:.2f}\n")
            elif prcact == "-":
                prcresult = prcfirnumber - prcfirnumber/100*prcsecnumber
                print(f"Result: {prcfirnumber} - {prcsecnumber}% = {prcresult:.2f}\n")
            elif prcact == "*":
                prcresult = prcfirnumber * (prcsecnumber / 100)
                print(f"Result: {prcfirnumber} * {prcsecnumber}% = {prcresult:.2f}\n")
            elif prcact == "/":
                if prcsecnumber == 0:
                    print("Error: Division by zero!\n")
                else:
                    prcresult = prcfirnumber / (prcsecnumber / 100)
                    print(f"Result: {prcfirnumber} / {prcsecnumber}% = {prcresult:.2f}\n")
            else:
                print("Invalid Operation!\n")
        except ValueError:
            print("Error: Invalid input\n")
 
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Root")
        print("7. Factorial")
        print("8. Quadratic Equation Solver")
        print("9. Percent Calculator")
        print("0. Exit")

        action = int(input("- "))
        print()

        if action in (1, 2, 3, 4, 5, 6, 7):
            x = int(input("Write first number: "))

            if action not in (6, 7, 9):
                y = int(input("Write second number: "))

        if action == 0:
            break

        if action == 1:
            add(x,y)
         
        if action == 2:
            subtract(x,y)

        if action == 3:
            multiply(x,y)
        
        if action == 4:
            divide(x,y)
        
        if action == 5:
            power(x,y)

        if action == 6:
            root(x)

        if action == 7:
            factorial(x)

        if action == 8:
            qes(0,0,0)

        if action == 9:
            percentcal(0,0)
                          
def clear_initial_output():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print("\033c", end='')

def handle_ssh_connection(host, port, username, password, current_color, COLORS):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port=port, username=username, password=password)
        print(f"{current_color}Successfully connected to {host}!{COLORS['reset']}")
        print('')
        
        while True:
            command = input(f"{current_color}{username}@{host}$ {COLORS['reset']}").strip()
            if command.lower() in ("exit", "quit"):
                break
                
            stdin, stdout, stderr = ssh.exec_command(command)
            output = stdout.read().decode()
            if output:
                print(output)
            
            error = stderr.read().decode()
            if error:
                print(f"{current_color}ERROR: {error}{COLORS['reset']}")
        
        ssh.close()
        print(f"{current_color}SSH session will ended.{COLORS['reset']}")
        print('')
        
    except paramiko.AuthenticationException:
        print(f"{current_color}Authentication ERROR! Check login/password.{COLORS['reset']}")
        print('')
    except paramiko.SSHException as e:
        print(f"{current_color}SSH ERROR: {e}{COLORS['reset']}")
        print('')
    except Exception as e:
        print(f"{current_color}Unknown ERROR: {e}{COLORS['reset']}")
        print('')

def os_info():
    
    print(f"{current_color} 'Creator: neeitr0n (Dmitriy Gagarin)'")    
    print(f"{current_color} 'Name: SrOS'")
    print(f"{current_color} 'Version: 0.R (dev)'")
    print(f"{current_color} 'Based on: Python'")
    print(f"{current_color} 'Status: in development'")
    print(f"{current_color} 'GithubRepo Link: '")
    print('')      

def save_usrconfig():
    try:
        config = {"username": username}
        with open(USER_CONFIG_FILE, 'w') as f:
            json.dump(config, f)
    except Exception as e:
        print(f"Error saving user config: {e}")

def load_usrconfig():
    global username
    if os.path.exists(USER_CONFIG_FILE):
        try:
            with open(USER_CONFIG_FILE, 'r') as f:
                config = json.load(f)
                username = config.get("username")
                return username is not None
        except Exception as e:
            print(f"Error loading user config: {e}")
    return False            

def save_colorconfig():
    try:
        color_name = next((name for name, code in COLORS.items() if code == current_color), "white")
        config = {"color": color_name}
        with open(COLOR_CONFIG_FILE, 'w') as f:
            json.dump(config, f)
    except Exception as e:
        print(f"Error saving config: {e}")

def load_colorconfig():
    global current_color
    if os.path.exists(COLOR_CONFIG_FILE):
        try:
            with open(COLOR_CONFIG_FILE, 'r') as f:
                config = json.load(f)
                color_name = config.get("color", "white")
                if color_name in COLORS:
                    current_color = COLORS[color_name]
        except Exception as e:
            print(f"Error loading config: {e}")        

def first_run_checker():
    if not os.path.exists(MARKER_FILE):
        with open(MARKER_FILE, 'w') as f:
            json.dump({"first_run": False}, f)
        return True
    return False

def change_directory(new_dir):
    try:
        if not new_dir: 
            new_dir = "home"
        
        if new_dir == "..":
            os.chdir("..")
        elif new_dir == ".":
            pass 
        elif new_dir == "-":
            pass
        else:
            os.chdir(new_dir)
            
        print(f"{current_color}Current directory: {os.getcwd()}{COLORS['reset']}")
    except FileNotFoundError:
        print(f"{current_color}Directory not found: {new_dir}{COLORS['reset']}")
    except Exception as e:
        print(f"{current_color}Error changing directory: {e}{COLORS['reset']}")
    print('')

def ls_init():
    try:
        current_dir = os.getcwd()
        print(f"{current_color}Contents of '{current_dir}':{COLORS['reset']}")
        
        with os.scandir(current_dir) as entries:
            for entry in sorted(entries, key=lambda x: x.name.lower()):
                if entry.is_dir():
                    print(f"  \033[4m{current_color}{entry.name}\033[0m{COLORS['reset']}")
                elif entry.is_file():
                    print(f"  {current_color}{entry.name}{COLORS['reset']}")
    except Exception as e:
        print(f"{current_color}Error listing directory: {e}{COLORS['reset']}")
    print('')

def clear_environment():
    print('')
    script_dir = Path(__file__).parent
    
    targets = [
        script_dir / "home.",   
        script_dir / "temp.",
        script_dir / "conf.",   
        script_dir / "fl.marker"  
    ]
    
    for target in targets:
        try:
            if target.is_dir():
                shutil.rmtree(target)
                print(f"Directory {target.name} was deleted")
            elif target.is_file():
                os.remove(target)
                print(f"File {target.name} was deleted")
        except Exception as e:
            print(f"ERROR: {target.name}: {e}")

def auto_cd_home():
    os.chdir('home')

def ping(host):
    host = host.strip("'\"")  
    try:
        count_flag = "-n" if platform.system().lower() == "windows" else "-c"
        result = subprocess.run(
            ["ping", count_flag, "4", host],
            text=True,
            capture_output=True,
            check=True
        )
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Ping failed: {e.stderr}")
    except Exception as e:
        print(f"Error: {e}")
    print('')        

def directoryCr():
    global directory_home, directory_temp

    directory_home = "home."
    try:
        print('[STARTING INSTALLATION:]')
        print('')
        os.mkdir(directory_home)
        print(f"Directory '{directory_home}' created successfully.")
    
    except FileExistsError:
        print(f"Directory '{directory_home}' already exists.")

    except PermissionError:
        print(f"Permission denied: Unable to create '{directory_home}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

    directory_temp = "temp."
    try:
        os.mkdir(directory_temp)
        print(f"Directory '{directory_temp}' created successfully.")
        print('')
    
    except FileExistsError:
        print(f"Directory '{directory_temp}' already exists.")

    except PermissionError:
        print(f"Permission denied: Unable to create '{directory_temp}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

    directory_conf = 'conf.'
    try:
        os.mkdir(directory_conf)
        print(f"Directory '{directory_conf}' created successfully.")
        print('')
    
    except FileExistsError:
        print(f"Directory '{directory_conf}' already exists.")

    except PermissionError:
        print(f"Permission denied: Unable to create '{directory_conf}'.")
    except Exception as e:
        print(f"An error occurred: {e}")    
    print("[Installation was successfully!]")
    print('')

def create_file(filename):
    try:
        with open(filename, 'w'):
            pass
        print(f"{current_color}File '{filename}' created successfully{COLORS['reset']}")
    except Exception as e:
        print(f"{current_color}Error creating file: {e}{COLORS['reset']}")
    print('')

def edit_file(filename):
    try:
        if not os.path.exists(filename):
            print(f"{current_color}File doesn't exist. Create it first? (y/n){COLORS['reset']}")
            choice = input().lower()
            if choice == 'y':
                create_file(filename)
            else:
                return

        file_size = os.path.getsize(filename)
        if file_size > 1024*1024: 
            print(f"{current_color}Warning: File is large ({file_size} bytes). Continue? (y/n){COLORS['reset']}")
            if input().lower() != 'y':
                return

        with open(filename, 'r') as f:
            content = f.read()

        print(f"{current_color}Editing '{filename}'. Enter your text (Ctrl+D/Ctrl+Z to save):{COLORS['reset']}")
        print(content)
        
        new_content = []
        print(f"{current_color}--- Start editing (end with empty line) ---{COLORS['reset']}")
        while True:
            try:
                line = input()
                new_content.append(line)
            except EOFError:
                break
            if line == "":
                break

        with open(filename, 'w') as f:
            f.write('\n'.join(new_content[:-1]))
        
        print(f"{current_color}File '{filename}' saved successfully{COLORS['reset']}")
    except Exception as e:
        print(f"{current_color}Error editing file: {e}{COLORS['reset']}")
    print('')

def remove_file(filename):
    try:
        if not os.path.exists(filename):
            print(f"{current_color}File doesn't exist{COLORS['reset']}")
            return
            
        print(f"{current_color}Are you sure you want to delete '{filename}'? (y/n){COLORS['reset']}")
        if input().lower() == 'y':
            os.remove(filename)
            print(f"{current_color}File '{filename}' removed successfully{COLORS['reset']}")
        else:
            print(f"{current_color}Operation canceled{COLORS['reset']}")
    except Exception as e:
        print(f"{current_color}Error removing file: {e}{COLORS['reset']}")
    print('')

def create_directory(dirname):
    try:
        os.mkdir(dirname)
        print(f"{current_color}Directory '{dirname}' created successfully{COLORS['reset']}")
    except FileExistsError:
        print(f"{current_color}Directory already exists{COLORS['reset']}")
    except Exception as e:
        print(f"{current_color}Error creating directory: {e}{COLORS['reset']}")
    print('')

def remove_directory(dirname):
    try:
        if not os.path.exists(dirname):
            print(f"{current_color}Directory doesn't exist{COLORS['reset']}")
            return
            
        if os.listdir(dirname):
            print(f"{current_color}Directory is not empty. Delete anyway? (y/n){COLORS['reset']}")
            if input().lower() != 'y':
                print(f"{current_color}Operation canceled{COLORS['reset']}")
                return

        os.rmdir(dirname)
        print(f"{current_color}Directory '{dirname}' removed successfully{COLORS['reset']}")
    except Exception as e:
        print(f"{current_color}Error removing directory: {e}{COLORS['reset']}")
    print('')                    

def helpCom():
    print(f"{current_color}List of command:")
    print("  'help' - view all commands")
    print("  'info' - all info about os")
    print('')
    print("  'time' - view current time and date")
    print("  'echo <text>' - display a line of text")
    print("  'color <color>' - change terminal color")
    print("  'calc' - open a calculator")
    print('')
    print("  'cd <directory>' - change directory")
    print("  'touch <file>' - create new file")
    print("  'edit <file>' - edit file content")
    print("  'rm <file>' - remove file")
    print("  'mkdir <dir>' - create directory")
    print("  'rmdir <dir>' - remove directory")
    print('')
    print("  'ssh' - work with ssh")
    print("  'ping <host>' - check network connectivity")
    print('')
    print("  'exit' - exit the os")
    print("  'clear' - clean terminal")
    print("  'clearenv' - delete the whole system!")
    print(f"{COLORS['reset']}")

def startMessage():
    clear_initial_output()
    print(f'{current_color}')
    print("Welcome to SrOS DEV.BUILD 0.R Ver!")
    print('')
    print("Type 'help' to see command list")
    print(f'{COLORS["reset"]}')

def register_user():
    global username
    clear_initial_output()
    print(f"{current_color}=== USER REGISTRATION ===")
    print("Please enter your username:")
    while True:
        username = input("> ").strip()
        if username:
            save_usrconfig()
            print(f"Welcome, {username}! Registration complete.")
            print('')
            break
        else:
            print("Username cannot be empty. Please try again.")    

def shell():
    global shellQ, current_datetime, echoText, path, confirm, current_color

    current_datetime =  datetime.now()

    shellQ = input(f'{current_color}''shell# ')
    print('')

    if shellQ == 'help':
        helpCom() 

    elif shellQ == 'time':
        print(f"{current_color}Current time and date: {current_datetime}{COLORS['reset']}")
        print('')

    elif shellQ == 'clear':
        os.system('cls' if os.name == 'nt' else 'clear')

    elif shellQ == "clearenv":
        print('')
        confirm = input(f'{current_color}Delete system? Y/N - ').lower().strip()
        if confirm == "y":
                clear_environment()
                print('')
                print(f'{current_color}System was deleted successfully!')
                print('')
                exit()
        else:
            print('')
            print(f'{current_color}Canceled!{COLORS["reset"]}')
            print('')

    elif shellQ == 'ls':
        ls_init()

    elif shellQ.startswith('ssh '):
        args = shellQ.split()[1:]
    
        if len(args) < 4:
            print(f"{current_color}Use: ssh <host> <port> <username> <password>{COLORS['reset']}")
            print(f"{current_color}Example: ssh 192.168.1.100 22 admin password123{COLORS['reset']}")
            print('')
        else:
            host, port, username_ssh, password = args[0], int(args[1]), args[2], args[3]
            handle_ssh_connection(host, port, username_ssh, password, current_color, COLORS)    

    elif shellQ == 'cd':
        change_directory("")

    elif shellQ == 'calc':
        qalc()

    elif shellQ == 'info':
        os_info()         
    
    elif shellQ.startswith('cd '):
        dir_arg = shellQ[3:].strip()
        change_directory(dir_arg)

    elif shellQ.startswith('touch '):
        filename = shellQ[6:].strip()
        if filename:
            create_file(filename)
        else:
            print(f"{current_color}Please specify filename{COLORS['reset']}")

    elif shellQ.startswith('edit '):
        filename = shellQ[5:].strip()
        if filename:
            edit_file(filename)
        else:
            print(f"{current_color}Please specify filename{COLORS['reset']}")

    elif shellQ.startswith('rm '):
        filename = shellQ[3:].strip()
        if filename:
            remove_file(filename)
        else:
            print(f"{current_color}Please specify filename{COLORS['reset']}")

    elif shellQ.startswith('mkdir '):
        dirname = shellQ[6:].strip()
        if dirname:
            create_directory(dirname)
        else:
            print(f"{current_color}Please specify directory name{COLORS['reset']}")

    elif shellQ.startswith('rmdir '):
        dirname = shellQ[6:].strip()
        if dirname:
            remove_directory(dirname)
        else:
            print(f"{current_color}Please specify directory name{COLORS['reset']}")                              

    elif shellQ.startswith('echo '):
        print(f'{current_color}{shellQ[5:]}{COLORS["reset"]}')
        print('')  

    elif shellQ.startswith('color '):
        color_name = shellQ.split(' ')[1].lower()
        if color_name in COLORS:
            current_color = COLORS[color_name]
            save_colorconfig()
            print(f'{current_color}Color changed to {color_name}!{COLORS["reset"]}')
        else:
            print(f'{current_color}Unknown color! Available: {", ".join(COLORS.keys())}{COLORS["reset"]}')
        print('')  

    elif shellQ.startswith('ping '):
        host = shellQ[5:].strip()
        if host:
            ping(host)
        else:
            print(f"{current_color}Usage: ping <host>{COLORS['reset']}")
            print('')      

    elif shellQ not in ['help', 'time', 'exit', 'clear', 'clearenv', 'color', 'ls', 'cd', 'ssh', 'calc'] and not shellQ.startswith(('echo', 'cd', 'touch', 'edit', 'rm', 'mkdir', 'rmdir', 'ssh', 'ping')):
        print(f'"{shellQ}" = Unknown command!')
        print('')
    return True                             

if first_run_checker():
    directoryCr()
    save_colorconfig()
    register_user()

else:
    load_colorconfig()
    if not load_usrconfig():
        register_user()
    startMessage()
    auto_cd_home()

    while True:
        shell()

        if shellQ == 'exit':
            break    
