import sys
from datetime import datetime
import os
import subprocess
import json
import time
import shutil
from pathlib import Path
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

LANGUAGE = {"en", "ru", "de", "fr"}

COLOR_CONFIG_FILE = "conf/colorconfig.json"
USER_CONFIG_FILE = "conf/usrlist.json"
LANGUAGE_CONFIG_FILE = "conf/langconfig.json"
MARKER_FILE = "fl.marker"

REQUIRED_LIBRARIES = ["paramiko"] 

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

def os_info():
    
    print(f"{current_color} 'Creator: neeitr0n (Dmitriy Gagarin)'")    
    print(f"{current_color} 'Name: SrOS'")
    print(f"{current_color} 'Version: 0.2 (regular)'")
    print(f"{current_color} 'Based on: Python'")
    print(f"{current_color} 'Status: in development'")
    print(f"{current_color} 'GithubRepo Link: https://github.com/neeitr0n/SrOS '")
    print('')
    
def love_text():
    print()
    print(' ______        __         ______   __     __  ________        __    __             ')
    print('/      |      /  |       /      \ /  |   /  |/        |      /  |  /  |            ')
    print('$$$$$$/       $$ |      /$$$$$$  |$$ |   $$ |$$$$$$$$/       $$ |  $$ |            ')
    print('  $$ |        $$ |      $$ |  $$ |$$ |   $$ |$$ |__          $$ |  $$ |            ')
    print('  $$ |        $$ |      $$ |  $$ |$$  \ /$$/ $$    |         $$ |  $$ |            ')
    print('  $$ |        $$ |      $$ |  $$ | $$  /$$/  $$$$$/          $$ |  $$ |            ')
    print(' _$$ |_       $$ |_____ $$ \__$$ |  $$ $$/   $$ |_____       $$ \__$$ |            ')
    print('/ $$   |      $$       |$$    $$/    $$$/    $$       |      $$    $$/             ')
    print('$$$$$$/       $$$$$$$$/  $$$$$$/      $/     $$$$$$$$/        $$$$$$/              ')
    print('                                                                                   ')
    print('                                                                                   ')
    print('                                                                                   ')
    print()          

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

def save_languageconfig():
    try:
        config = {"language": language}
        with open(LANGUAGE_CONFIG_FILE, 'w') as f:
            json.dump(config, f)
    except Exception as e:
        print(f"Error saving user config: {e}")

def load_languageconfig():
    global language
    if os.path.exists(LANGUAGE_CONFIG_FILE):
        try:
            with open(LANGUAGE_CONFIG_FILE, 'r') as f:
                config = json.load(f)
                language = config.get("language")
                return language is not None
        except Exception as e:
            print(f"Error loading language config: {e}")
    return False           

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
    print("  'love' - print <3 text")
    print(" 'language' - select system language")
    print('')
    print("  'ls' - list files")
    print("  'cd <directory>' - change directory")
    print("  'touch <file>' - create new file")
    print("  'edit <file>' - edit file content")
    print("  'rm <file>' - remove file")
    print("  'mkdir <dir>' - create directory")
    print("  'rmdir <dir>' - remove directory")
    print('')
    print("  'ping <host>' - check network connectivity")
    print('')
    print("  'exit' - exit the os")
    print("  'clear' - clean terminal")
    print("  'clearenv' - delete the whole system!")
    print(f"{COLORS['reset']}")
    
def helpCom_ru():
    print(f"{current_color}Список команд:")
    print(" 'help' - просмотр всех команд")
    print(" 'info' - вся информация об ОС")
    print('')
    print(" 'time' - просмотр текущего времени и даты")
    print(" 'echo <text>' - отображение строки текста")
    print(" 'color <color>' - изменение цвета терминала")
    print(" 'calc' - открытие калькулятора")
    print(" 'love' - печать <3 текста")
    print(" 'language' - выбрать язык системы")
    print('')
    print(" 'ls' - список файлов")
    print(" 'cd <directory>' - смена каталога")
    print(" 'touch <file>' - создание нового файла")
    print(" 'edit <file>' - редактирование содержимого файла")
    print(" 'rm <file>' - удаление файла")
    print(" 'mkdir <dir>' - создание каталога")
    print(" 'rmdir <dir>' - удалить каталог")
    print('')
    print(" 'ping <host>' - проверить сетевое подключение")
    print('')
    print(" 'exit' - выйти из ОС")
    print(" 'clear' - очистить терминал")
    print(" 'clearenv' - удалить всю систему!")
    print(f"{COLORS['reset']}")
    
def change_directory_ru(new_dir):
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
            
        print(f"{current_color}Текущая директория: {os.getcwd()}{COLORS['reset']}")
    except FileNotFoundError:
        print(f"{current_color}Директория не найдена: {new_dir}{COLORS['reset']}")
    except Exception as e:
        print(f"{current_color}Ошибка при смене директории: {e}{COLORS['reset']}")
    print('')

def ls_init_ru():
    try:
        current_dir = os.getcwd()
        print(f"{current_color}Содержит в себе: '{current_dir}':{COLORS['reset']}")
        
        with os.scandir(current_dir) as entries:
            for entry in sorted(entries, key=lambda x: x.name.lower()):
                if entry.is_dir():
                    print(f"  \033[4m{current_color}{entry.name}\033[0m{COLORS['reset']}")
                elif entry.is_file():
                    print(f"  {current_color}{entry.name}{COLORS['reset']}")
    except Exception as e:
        print(f"{current_color}Ошибка при просмотре директории: {e}{COLORS['reset']}")
    print('')

def clear_environment_ru():
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
                print(f"Директория {target.name} была удалена")
            elif target.is_file():
                os.remove(target)
                print(f"Файл {target.name} был удален")
        except Exception as e:
            print(f"ОШИБКА: {target.name}: {e}")

def ping_ru(host):
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
        print(f"Пинг не удался: {e.stderr}")
    except Exception as e:
        print(f"ОШИБКА: {e}")
    print('')        

def directoryCr_ru():
    global directory_home, directory_temp

    directory_home = "home."
    try:
        print('[НАЧАЛО УСТАНОВКИ:]')
        print('')
        os.mkdir(directory_home)
        print(f"Директория '{directory_home}'  была создана успешно.")
    
    except FileExistsError:
        print(f"Директория '{directory_home}' уже существует.")

    except PermissionError:
        print(f"Ошибка доступа: Невозможно создать '{directory_home}'.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

    directory_temp = "temp."
    try:
        os.mkdir(directory_temp)
        print(f"Директория '{directory_temp}' создана успешно.")
        print('')
    
    except FileExistsError:
        print(f"Директория '{directory_temp}' уже существует.")

    except PermissionError:
        print(f"Ошибка доступа: Невозможно создать '{directory_temp}'.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

    directory_conf = 'conf.'
    try:
        os.mkdir(directory_conf)
        print(f"Директория '{directory_conf}' была создана успешно.")
        print('')
    
    except FileExistsError:
        print(f"Директория '{directory_conf}' уже существует.")

    except PermissionError:
        print(f"Ошибка доступа: Невозможно создать '{directory_conf}'.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")    
    print("[Установка прошла успешно!]")
    print('')

def create_file_ru(filename):
    try:
        with open(filename, 'w'):
            pass
        print(f"{current_color}Файл '{filename}' успешно создан{COLORS['reset']}")
    except Exception as e:
        print(f"{current_color}Ошибка при создании файла: {e}{COLORS['reset']}")
    print('')

def edit_file_ru(filename):
    try:
        if not os.path.exists(filename):
            print(f"{current_color}Файл не существует. Создать? (y/n){COLORS['reset']}")
            choice = input().lower()
            if choice == 'y':
                create_file(filename)
            else:
                return

        file_size = os.path.getsize(filename)
        if file_size > 1024*1024: 
            print(f"{current_color}Предупреждение: файл имеет большой размер ({file_size} байтов). Продолжить? (y/n){COLORS['reset']}")
            if input().lower() != 'y':
                return

        with open(filename, 'r') as f:
            content = f.read()

        print(f"{current_color}Редактирование '{filename}'. Введите ваш текст (Ctrl+D/Ctrl+Z чтобы сохранить):{COLORS['reset']}")
        print(content)
        
        new_content = []
        print(f"{current_color}--- Начало редактирования (закончить пустой линией) ---{COLORS['reset']}")
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
        
        print(f"{current_color}Файл '{filename}' успешно сохранен{COLORS['reset']}")
    except Exception as e:
        print(f"{current_color}Ошибка при редактировании файла: {e}{COLORS['reset']}")
    print('')

def remove_file_ru(filename):
    try:
        if not os.path.exists(filename):
            print(f"{current_color}Файл не существует{COLORS['reset']}")
            return
            
        print(f"{current_color}Вы уверен что хотите удалить '{filename}'? (y/n){COLORS['reset']}")
        if input().lower() == 'y':
            os.remove(filename)
            print(f"{current_color}Файл '{filename}' успешно удалён{COLORS['reset']}")
        else:
            print(f"{current_color}Операция отменена{COLORS['reset']}")
    except Exception as e:
        print(f"{current_color}Ошибка при редактировании файла: {e}{COLORS['reset']}")
    print('')

def create_directory_ru(dirname):
    try:
        os.mkdir(dirname)
        print(f"{current_color}Директория '{dirname}' успешно создана{COLORS['reset']}")
    except FileExistsError:
        print(f"{current_color}Директория уже существует{COLORS['reset']}")
    except Exception as e:
        print(f"{current_color}Ошибка при создании директории: {e}{COLORS['reset']}")
    print('')

def remove_directory_ru(dirname):
    try:
        if not os.path.exists(dirname):
            print(f"{current_color}Директория не существует{COLORS['reset']}")
            return
            
        if os.listdir(dirname):
            print(f"{current_color}Директория содержит в себе файлы. Удалить в любом случае? (y/n){COLORS['reset']}")
            if input().lower() != 'y':
                print(f"{current_color}Операция отменена{COLORS['reset']}")
                return

        os.rmdir(dirname)
        print(f"{current_color}Директория '{dirname}' успешно удалена{COLORS['reset']}")
    except Exception as e:
        print(f"{current_color}Ошибка при удалении директории: {e}{COLORS['reset']}")
    print('')

def helpCom_de():
    print(f"{current_color}Befehlsliste:")
    print(" 'help' - alle Befehle anzeigen")
    print(" 'info' - alle Informationen über das Betriebssystem")
    print('')
    print(" 'time' - aktuelle Uhrzeit und Datum anzeigen")
    print(" 'echo <text>' - Textzeile anzeigen")
    print(" 'color <color>' - Terminalfarbe ändern")
    print(" 'calc' - Taschenrechner öffnen")
    print(" 'love' - <3 Text drucken")
    print(" 'language' - Systemsprache auswählen")
    print('')
    print(" 'ls' - Dateiliste")
    print(" 'cd <directory>' - Verzeichnis wechseln")
    print(" 'touch <file>' - neue Datei erstellen")
    print(" 'edit <file>' - Dateiinhalt bearbeiten")
    print(" 'rm <file>' - Datei löschen")
    print(" 'mkdir <dir>' - Verzeichnis erstellen")
    print(" 'rmdir <dir>' - Verzeichnis löschen")
    print('')
    print(" 'ping <host>' - Netzwerkverbindung prüfen")
    print('')
    print(" 'exit' - Betriebssystem verlassen")
    print(" 'clear' - Terminal bereinigen")
    print(" 'clearenv' - gesamtes System löschen!")
    print(f"{COLORS['reset']}")
    
def change_directory_de(new_dir):
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
            
        print(f"{current_color}Aktuelles Verzeichnis: {os.getcwd()}{COLORS['reset']}")
    except FileNotFoundError:
        print(f"{current_color}Verzeichnis nicht gefunden: {new_dir}{COLORS['reset']}")
    except Exception as e:
        print(f"{current_color}Fehler beim Verzeichniswechsel: {e}{COLORS['reset']}")
    print('')

def ls_init_de():
    try:
        current_dir = os.getcwd()
        print(f"{current_color}Enthält in sich: '{current_dir}':{COLORS['reset']}")
        
        with os.scandir(current_dir) as entries:
            for entry in sorted(entries, key=lambda x: x.name.lower()):
                if entry.is_dir():
                    print(f"  \033[4m{current_color}{entry.name}\033[0m{COLORS['reset']}")
                elif entry.is_file():
                    print(f"  {current_color}{entry.name}{COLORS['reset']}")
    except Exception as e:
        print(f"{current_color}Fehler beim Anzeigen des Verzeichnisses: {e}{COLORS['reset']}")
    print('')

def clear_environment_de():
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
                print(f"Verzeichnis {target.name} wurde gelöscht")
            elif target.is_file():
                os.remove(target)
                print(f"Datei {target.name} wurde gelöscht")
        except Exception as e:
            print(f"FEHLER: {target.name}: {e}")

def ping_de(host):
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
        print(f"Ping fehlgeschlagen: {e.stderr}")
    except Exception as e:
        print(f"FEHLER: {e}")
    print('')        

def directoryCr_de():
    global directory_home, directory_temp

    directory_home = "home."
    try:
        print('[INSTALLATIONSSTART:]')
        print('')
        os.mkdir(directory_home)
        print(f"Verzeichnis '{directory_home}' wurde erfolgreich erstellt.")
    
    except FileExistsError:
        print(f"Verzeichnis '{directory_home}' existiert bereits.")

    except PermissionError:
        print(f"Zugriffsfehler: Kann '{directory_home}' nicht erstellen.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

    directory_temp = "temp."
    try:
        os.mkdir(directory_temp)
        print(f"Verzeichnis '{directory_temp}' erfolgreich erstellt.")
        print('')
    
    except FileExistsError:
        print(f"Verzeichnis '{directory_temp}' existiert bereits.")

    except PermissionError:
        print(f"Zugriffsfehler: Kann '{directory_temp}' nicht erstellen.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

    directory_conf = 'conf.'
    try:
        os.mkdir(directory_conf)
        print(f"Verzeichnis '{directory_conf}' wurde erfolgreich erstellt.")
        print('')
    
    except FileExistsError:
        print(f"Verzeichnis '{directory_conf}' existiert bereits.")

    except PermissionError:
        print(f"Zugriffsfehler: Kann '{directory_conf}' nicht erstellen.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")    
    print("[Installation erfolgreich abgeschlossen!]")
    print('')

def create_file_de(filename):
    try:
        with open(filename, 'w'):
            pass
        print(f"{current_color}Datei '{filename}' erfolgreich erstellt{COLORS['reset']}")
    except Exception as e:
        print(f"{current_color}Fehler beim Erstellen der Datei: {e}{COLORS['reset']}")
    print('')

def edit_file_de(filename):
    try:
        if not os.path.exists(filename):
            print(f"{current_color}Datei existiert nicht. Erstellen? (y/n){COLORS['reset']}")
            choice = input().lower()
            if choice == 'y':
                create_file(filename)
            else:
                return

        file_size = os.path.getsize(filename)
        if file_size > 1024*1024: 
            print(f"{current_color}Warnung: Datei ist groß ({file_size} bytes). Fortfahren? (y/n){COLORS['reset']}")
            if input().lower() != 'y':
                return

        with open(filename, 'r') as f:
            content = f.read()

        print(f"{current_color}Bearbeite '{filename}'. Geben Sie Ihren Text ein (Ctrl+D/Ctrl+Z zum Speichern):{COLORS['reset']}")
        print(content)
        
        new_content = []
        print(f"{current_color}--- Bearbeitung starten (mit leerer Zeile beenden) ---{COLORS['reset']}")
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
        
        print(f"{current_color}Datei '{filename}' erfolgreich gespeichert{COLORS['reset']}")
    except Exception as e:
        print(f"{current_color}Fehler beim Bearbeiten der Datei: {e}{COLORS['reset']}")
    print('')

def remove_file_de(filename):
    try:
        if not os.path.exists(filename):
            print(f"{current_color}Datei existiert nicht{COLORS['reset']}")
            return
            
        print(f"{current_color}Sind Sie sicher, dass Sie '{filename}' löschen möchten? (y/n){COLORS['reset']}")
        if input().lower() == 'y':
            os.remove(filename)
            print(f"{current_color}Datei '{filename}' erfolgreich gelöscht{COLORS['reset']}")
        else:
            print(f"{current_color}Vorgang abgebrochen{COLORS['reset']}")
    except Exception as e:
        print(f"{current_color}Fehler beim Bearbeiten der Datei: {e}{COLORS['reset']}")
    print('')

def create_directory_de(dirname):
    try:
        os.mkdir(dirname)
        print(f"{current_color}Verzeichnis '{dirname}' erfolgreich erstellt{COLORS['reset']}")
    except FileExistsError:
        print(f"{current_color}Verzeichnis existiert bereits{COLORS['reset']}")
    except Exception as e:
        print(f"{current_color}Fehler beim Erstellen des Verzeichnisses: {e}{COLORS['reset']}")
    print('')

def remove_directory_de(dirname):
    try:
        if not os.path.exists(dirname):
            print(f"{current_color}Verzeichnis existiert nicht{COLORS['reset']}")
            return
            
        if os.listdir(dirname):
            print(f"{current_color}Verzeichnis enthält Dateien. Trotzdem löschen? (y/n){COLORS['reset']}")
            if input().lower() != 'y':
                print(f"{current_color}Vorgang abgebrochen{COLORS['reset']}")
                return

        os.rmdir(dirname)
        print(f"{current_color}Verzeichnis '{dirname}' erfolgreich gelöscht{COLORS['reset']}")
    except Exception as e:
        print(f"{current_color}Fehler beim Löschen des Verzeichnisses: {e}{COLORS['reset']}")
    print('')
    
def helpCom_fr():
    print(f"{current_color}Liste des commandes:")
    print(" 'help' - voir toutes les commandes")
    print(" 'info' - toutes les informations sur le système d'exploitation")
    print('')
    print(" 'time' - voir l'heure et la date actuelles")
    print(" 'echo <text>' - afficher une ligne de texte")
    print(" 'color <color>' - changer la couleur du terminal")
    print(" 'calc' - ouvrir la calculatrice")
    print(" 'love' - imprimer du texte <3")
    print(" 'language' - sélectionner la langue du système")
    print('')
    print(" 'ls' - liste des fichiers")
    print(" 'cd <directory>' - changer de répertoire")
    print(" 'touch <file>' - créer un nouveau fichier")
    print(" 'edit <file>' - modifier le contenu d'un fichier")
    print(" 'rm <file>' - supprimer un fichier")
    print(" 'mkdir <dir>' - créer un répertoire")
    print(" 'rmdir <dir>' - supprimer un répertoire")
    print('')
    print(" 'ping <host>' - vérifier la connexion réseau")
    print('')
    print(" 'exit' - quitter le système d'exploitation")
    print(" 'clear' - effacer le terminal")
    print(" 'clearenv' - supprimer tout le système!")
    print(f"{COLORS['reset']}")
    
def change_directory_fr(new_dir):
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
            
        print(f"{current_color}Répertoire actuel: {os.getcwd()}{COLORS['reset']}")
    except FileNotFoundError:
        print(f"{current_color}Répertoire non trouvé: {new_dir}{COLORS['reset']}")
    except Exception as e:
        print(f"{current_color}Erreur lors du changement de répertoire: {e}{COLORS['reset']}")
    print('')

def ls_init_fr():
    try:
        current_dir = os.getcwd()
        print(f"{current_color}Contenu de '{current_dir}':{COLORS['reset']}")
        
        with os.scandir(current_dir) as entries:
            for entry in sorted(entries, key=lambda x: x.name.lower()):
                if entry.is_dir():
                    print(f"  \033[4m{current_color}{entry.name}\033[0m{COLORS['reset']}")
                elif entry.is_file():
                    print(f"  {current_color}{entry.name}{COLORS['reset']}")
    except Exception as e:
        print(f"{current_color}Erreur lors de l'affichage du répertoire: {e}{COLORS['reset']}")
    print('')

def clear_environment_fr():
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
                print(f"Répertoire {target.name} a été supprimé")
            elif target.is_file():
                os.remove(target)
                print(f"Fichier {target.name} a été supprimé")
        except Exception as e:
            print(f"ERREUR: {target.name}: {e}")

def ping_fr(host):
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
        print(f"Échec du ping: {e.stderr}")
    except Exception as e:
        print(f"ERREUR: {e}")
    print('')        

def directoryCr_fr():
    global directory_home, directory_temp

    directory_home = "home."
    try:
        print('[DÉBUT DE L\'INSTALLATION:]')
        print('')
        os.mkdir(directory_home)
        print(f"Répertoire '{directory_home}' créé avec succès.")
    
    except FileExistsError:
        print(f"Le répertoire '{directory_home}' existe déjà.")

    except PermissionError:
        print(f"Erreur d'accès: Impossible de créer '{directory_home}'.")
    except Exception as e:
        print(f"Une erreur s'est produite: {e}")

    directory_temp = "temp."
    try:
        os.mkdir(directory_temp)
        print(f"Répertoire '{directory_temp}' créé avec succès.")
        print('')
    
    except FileExistsError:
        print(f"Le répertoire '{directory_temp}' existe déjà.")

    except PermissionError:
        print(f"Erreur d'accès: Impossible de créer '{directory_temp}'.")
    except Exception as e:
        print(f"Une erreur s'est produite: {e}")

    directory_conf = 'conf.'
    try:
        os.mkdir(directory_conf)
        print(f"Répertoire '{directory_conf}' créé avec succès.")
        print('')
    
    except FileExistsError:
        print(f"Le répertoire '{directory_conf}' existe déjà.")

    except PermissionError:
        print(f"Erreur d'accès: Impossible de créer '{directory_conf}'.")
    except Exception as e:
        print(f"Une erreur s'est produite: {e}")    
    print("[Installation terminée avec succès!]")
    print('')

def create_file_fr(filename):
    try:
        with open(filename, 'w'):
            pass
        print(f"{current_color}Fichier '{filename}' créé avec succès{COLORS['reset']}")
    except Exception as e:
        print(f"{current_color}Erreur lors de la création du fichier: {e}{COLORS['reset']}")
    print('')

def edit_file_fr(filename):
    try:
        if not os.path.exists(filename):
            print(f"{current_color}Le fichier n'existe pas. Créer? (y/n){COLORS['reset']}")
            choice = input().lower()
            if choice == 'y':
                create_file(filename)
            else:
                return

        file_size = os.path.getsize(filename)
        if file_size > 1024*1024: 
            print(f"{current_color}Avertissement: le fichier est volumineux ({file_size} octets). Continuer? (y/n){COLORS['reset']}")
            if input().lower() != 'y':
                return

        with open(filename, 'r') as f:
            content = f.read()

        print(f"{current_color}Édition de '{filename}'. Entrez votre texte (Ctrl+D/Ctrl+Z pour sauvegarder):{COLORS['reset']}")
        print(content)
        
        new_content = []
        print(f"{current_color}--- Début de l'édition (finir par une ligne vide) ---{COLORS['reset']}")
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
        
        print(f"{current_color}Fichier '{filename}' sauvegardé avec succès{COLORS['reset']}")
    except Exception as e:
        print(f"{current_color}Erreur lors de l'édition du fichier: {e}{COLORS['reset']}")
    print('')

def remove_file_fr(filename):
    try:
        if not os.path.exists(filename):
            print(f"{current_color}Le fichier n'existe pas{COLORS['reset']}")
            return
            
        print(f"{current_color}Êtes-vous sûr de vouloir supprimer '{filename}'? (y/n){COLORS['reset']}")
        if input().lower() == 'y':
            os.remove(filename)
            print(f"{current_color}Fichier '{filename}' supprimé avec succès{COLORS['reset']}")
        else:
            print(f"{current_color}Opération annulée{COLORS['reset']}")
    except Exception as e:
        print(f"{current_color}Erreur lors de l'édition du fichier: {e}{COLORS['reset']}")
    print('')

def create_directory_fr(dirname):
    try:
        os.mkdir(dirname)
        print(f"{current_color}Répertoire '{dirname}' créé avec succès{COLORS['reset']}")
    except FileExistsError:
        print(f"{current_color}Le répertoire existe déjà{COLORS['reset']}")
    except Exception as e:
        print(f"{current_color}Erreur lors de la création du répertoire: {e}{COLORS['reset']}")
    print('')

def remove_directory_fr(dirname):
    try:
        if not os.path.exists(dirname):
            print(f"{current_color}Le répertoire n'existe pas{COLORS['reset']}")
            return
            
        if os.listdir(dirname):
            print(f"{current_color}Le répertoire contient des fichiers. Supprimer quand même? (y/n){COLORS['reset']}")
            if input().lower() != 'y':
                print(f"{current_color}Opération annulée{COLORS['reset']}")
                return

        os.rmdir(dirname)
        print(f"{current_color}Répertoire '{dirname}' supprimé avec succès{COLORS['reset']}")
    except Exception as e:
        print(f"{current_color}Erreur lors de la suppression du répertoire: {e}{COLORS['reset']}")
    print('')            

def start_message_ascii():
    print('  ______   _______    ______    ______          ______      _______         __     __ ')
    print(' /      \ /       \  /      \  /      \        /      \    /       \       /  |   /  |')
    print('/$$$$$$  |$$$$$$$  |/$$$$$$  |/$$$$$$  |      /$$$$$$  |   $$$$$$$  |      $$ |   $$ |')
    print('$$ \__$$/ $$ |__$$ |$$ |  $$ |$$ \__$$/       $$$  \$$ |   $$ |__$$ |      $$ |   $$ |')
    print('$$      \ $$    $$< $$ |  $$ |$$      \       $$$$  $$ |   $$    $$<       $$  \ /$$/ ')
    print(' $$$$$$  |$$$$$$$  |$$ |  $$ | $$$$$$  |      $$ $$ $$ |   $$$$$$$  |       $$  /$$/  ')
    print('/  \__$$ |$$ |  $$ |$$ \__$$ |/  \__$$ |      $$ \$$$$ |__ $$ |  $$ |        $$ $$/   ')
    print('$$    $$/ $$ |  $$ |$$    $$/ $$    $$/       $$   $$$//  |$$ |  $$ |         $$$/    ')
    print(' $$$$$$/  $$/   $$/  $$$$$$/   $$$$$$/         $$$$$$/ $$/ $$/   $$/           $/     ')
    print('                                                                                      ')
    print('                                                                                      ')
    print('                                                                                      ')

def startMessage():
    clear_initial_output()
    print(f'{current_color}')
    start_message_ascii()                                         
    print()
    print("Welcome to SrOS 0.2 Ver!")
    print('')
    print("Type 'help' to see command list")
    print(f'{COLORS["reset"]}')

def startMessage_ru():
    clear_initial_output()
    print(f'{current_color}')
    start_message_ascii()                                                
    print()
    print("Добро пожаловать в SrOS 0.2 Ver!")
    print('')
    print("Напишите 'help' чтобы увидеть список комманд")
    print(f'{COLORS["reset"]}')

def startMessage_de():
    clear_initial_output()
    print(f'{current_color}')
    start_message_ascii()                                                
    print()
    print("Willkommen bei SrOS 0.2 Ver!")
    print('')
    print("Geben Sie 'help' um die Befehlsliste anzuzeigen")
    print(f'{COLORS["reset"]}')
    
def startMessage_fr():
    clear_initial_output()
    print(f'{current_color}')
    start_message_ascii()
    print()
    print("Bienvenue à SrOS 0.2 Ver!")
    print('')
    print("Tapez 'help' pour voir la liste des commandes")
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
          
def language_select():
    global language
    clear_initial_output()
    print(f"{current_color}")
    print("Select language[NEED REBOOT]:")
    print("English - en")
    print("Russian - ru")
    print("German - de")
    print("French - fr")
    while True:
        language = input("> ").strip()
        if language:
            save_languageconfig()
            print(f"Language: , {language} was selected!")
            print('')
            break
        
def language_select_ru():
    global language
    clear_initial_output()
    print(f"{current_color}")
    print("Выберите язык [НЕОБХОДИМА ПЕРЕЗАГРУЗКА]:")
    print("English - en")
    print("Russian - ru")
    print("German - de")
    print("French - fr")
    while True:
        language = input("> ").strip()
        if language:
            save_languageconfig()
            print(f"Language: , {language} was selected!")
            print('')
            break
        
def language_select_de():
    global language
    clear_initial_output()
    print(f"{current_color}")
    print("Sprache auswählen [NEUSTART ERFORDERLICH]:")
    print("English - en")
    print("Russian - ru")
    print("German - de")
    print("French - fr")
    while True:
        language = input("> ").strip()
        if language:
            save_languageconfig()
            print(f"Language: , {language} was selected!")
            print('')
            break
        
def language_select_fr():
    global language
    clear_initial_output()
    print(f"{current_color}")
    print("Select language[NEED REBOOT]:")
    print("English - en")
    print("Russian - ru")
    print("German - de")
    print("French - fr")
    while True:
        language = input("> ").strip()
        if language:
            save_languageconfig()
            print(f"Language: , {language} was selected!")
            print('')
            break          
        
def language_selectfirst():
    global language
    clear_initial_output()
    print(f"{current_color}")
    print('=== LANGUAGE SELECT ===')
    print("Please select language:")
    print("English - eng")
    print("Russian - ru")
    print("German - gr")
    print("French - fr")
    while True:
        language = input("> ").strip()
        if language:
            save_languageconfig()
            print(f"Language: , {language} was selected!")
            print('')
            break                      

def shell():
    global shellQ, current_datetime, echoText, path, confirm, current_color

    current_datetime =  datetime.now()

    shellQ = input(f'{current_color}''>>> ')
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

    elif shellQ == 'cd':
        change_directory("")

    elif shellQ == 'calc':
        qalc()

    elif shellQ == 'info':
        os_info()
        
    elif shellQ == 'love':
        love_text()
        
    elif shellQ == 'language':
        language_select()                 
    
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

    elif shellQ not in ['help', 'time', 'exit', 'clear', 'clearenv', 'color', 'ls', 'cd', 'calc', 'language'] and not shellQ.startswith(('echo', 'cd', 'touch', 'edit', 'rm', 'mkdir', 'rmdir', 'ping')):
        print(f'"{shellQ}" = Unknown command!')
        print('')
    return True 

current_language = ()
                          
if first_run_checker():
    directoryCr()
    save_colorconfig()
    register_user()
    language_select()

else:
    load_colorconfig()
    if not load_usrconfig():
        register_user()
    load_languageconfig()
    current_language = language
    if current_language == 'ru':
        helpCom = helpCom_ru
        change_directory = change_directory_ru
        ls_init = ls_init_ru
        clear_environment = clear_environment_ru
        ping = ping_ru
        directoryCr = directoryCr_ru
        create_file = create_file_ru
        edit_file = edit_file_ru
        remove_file = remove_file_ru
        create_directory = create_directory_ru
        remove_directory = remove_directory_ru
        language_select = language_select_ru
        startMessage = startMessage_ru
    if current_language == 'de':
        helpCom = helpCom_de
        change_directory = change_directory_de
        ls_init = ls_init_de
        clear_environment = clear_environment_de
        ping = ping_de
        directoryCr = directoryCr_de
        create_file = create_file_de
        edit_file = edit_file_de
        remove_file = remove_file_de
        create_directory = create_directory_de
        remove_directory = remove_directory_de
        language_select = language_select_de
        startMessage = startMessage_de
    if current_language == 'fr':
        helpCom = helpCom_fr
        change_directory = change_directory_fr
        ls_init = ls_init_fr
        clear_environment = clear_environment_fr
        ping = ping_fr
        directoryCr = directoryCr_fr
        create_file = create_file_fr
        edit_file = edit_file_fr
        remove_file = remove_file_fr
        create_directory = create_directory_fr
        remove_directory = remove_directory_fr
        language_select = language_select_fr
        startMessage = startMessage_fr        
    if not load_languageconfig():
        language_selectfirst()    
    startMessage()
    print(current_language)

    while True:
        shell()

        if shellQ == 'exit':
            break            
