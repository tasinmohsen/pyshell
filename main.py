# usr/bin/python3

######################## READ IT FIRST PLEASE #########################
#######################################################################
################################ About ################################
#######################################################################

# This is a shell program which bassid on python3.This program
# made inpressed by linux konsole.Many of linux command are in this program
# You can use as [#root] but be careful it's can harm your system it's recommended
# run as [non-$root] (Some facility have need root permission it will be asked )
# aviable in there.This program can run in windows but some facility
# you maynot found in windows but i try to add all.This program also
# can run in android(ex:Termux).This pykonsole program is a
# opensource program.You can edit as you wish.But be careful when
# you edit.If you are not a python programer or devlover it's well
# wish please don't do anything there.It's can be crash the program
# or can harm you oprateing system too.This program is program is
# made for educational purpose only if you using it for you bad purpose
# I will responsiable for this best of luck.........
#
# Time & Date       : Saturday,October 31, 2020 7:11:25 PM +06 (when this program start made)
# python Version    : Python 3.8.5(At older version some facility may not work)
# Coding By         : Mohsen Bin Taher Tasin (From Bangladesh)
# pykonsole Version : 1.0.0
#######################################################################
#######################################################################
#######################################################################


import socket
import time
import os
import sys
import fnmatch
import shutil
from pathlib import Path
#---------------Color-------------#
if sys.platform in ['linux', 'linux1', 'linux2']:
    W = '\033[1;37m'
    B = '\033[1;34m'
    R = '\033[1;31m'
    G = '\033[1;32m'
    Y = '\033[1;33m'
    C = '\033[1;36m'
else:
    W = ''
    B = ''
    R = ''
    G = ''
    Y = ''
    C = ''
#------------right wrong alert failed-------------#
RI = ("%s[+]%s" % (G, W))  # Right
WR = ("%s[x]%s" % (R, W))  # Wrong
AL = ("%s[!]%s" % (Y, W))  # Alert
FA = ("%s[-]%s" % (R, W))  # Failed
#------------Checking Root,host& python version----------------#

user_host = socket.gethostname()
if os.geteuid() != 0:
    user_as = (("%s"+user_host) % (W))
    user_sim = "$"
else:
    print(f"{Y}[!]{G}Be careful you are running as {R}#root{W}")
    user_as = ("%sroot" % (R))
    user_sim = "#"
if sys.version_info[0] < 3:
    print(f"{WR}Please Using python 3.x.x or Install python 3.x.x version")
    exit("{AL}Quiting pykonsole. See you again")
#----------- clear program----------------#


def clear():
    if sys.platform in ["linux1", "linux2", "linux"]:
        os.system("clear")
    elif sys.platform in ["win32", "win64"]:
        os.system("cls")
    else:
        pass

#-----------------History---------------#


his_lo = os.getcwd()


def history(user, his_lo):
    his = ''.join(user)
    with open(f"{his_lo}/history.txt", "a+") as history:
        history.write('''%s \n''' % (his))
        history.close()
# --------------Help menu--------------------#


def help():
    """
    Help menu getting help
    """
    print('''
     Command                   Description

       cd               changing directory go to directory to other
       mkdir            making directory in current workplace
       rm               remove file or dircetory(rm -r for remove dircetory)
       rename           change file name(ex: rename old.txt new.txt)
       cat              read any file(ex: cat hello.txt)
       exit             exit or close the pykonsole 
    ''')


#---------------User Input form-------------#

clear()


def main():
    try:
        while True:
            cwd = os.getcwd()
            user = input(f"{R}┌──[{R}%s{Y}@{C}%s{R}]─[{G}~{cwd}{R}]\n└──╼ {Y}%s{W}" %
                         (user_as, user_host, user_sim)).split()
            history(user, his_lo)
            # input form in dir ┌─[@]─[~/dir/dir]└──╼ $
            if user == []:
                pass
            #########################################################
            #-----------Directory add,remove,rename,list dir--------#
            #########################################################
            #----------------------Rename file/directory------------#
            elif user[0] == "rename":
                if user[-1] == "rename":
                    print(f"{FA} flie name not found!")
                elif user[-1] == "":
                    print(f"{FA} new file name missing")
                else:
                    ro_1 = user[1]
                    ro_2 = user[2]
                    try:
                        os.rename(ro_1, ro_2)
                    except FileNotFoundError:
                        print(f"{FA} '{ro_1}': file not found")
                    except PermissionError:
                        print(f"{FA} Permession denied (tip:run as #root)")
                    # rename (option) 's/oldname/newname/' file1.ext file24.ext
            #---------------------Removing Directory-------------#
            elif user[0] == "rm":
                fo = user[-1]
                if fo == "rm":
                    print(f"{WR} no file/directory name found")
                    pass
                else:
                    fo = user[1]
                    if user[1] == "-r":
                        fl_nm = user[-1]
                        if fl_nm == "-r":
                            print(f"{FA} no file name found!")
                        else:
                            try:
                                os.rmdir(fl_nm)
                            except OSError:
                                try:
                                    shutil.rmtree(fl_nm)
                                except FileNotFoundError:
                                    print(f"{FA} '{fl_nm}' File not found")
                            except FileNotFoundError:
                                print(f"{FA} '{fl_nm}' File not found")
                            except PermissionError:
                                print(
                                    f"{FA} '{fl_nm}': Permisson error (try run as #root)")
                    else:
                        try:
                            os.remove(fo)  # Removing file
                        except IsADirectoryError:
                            print(
                                f"{AL} '{fo}': is a directory (use:rm -r to remove dir)")
                        except FileNotFoundError:
                            print(f"{FA} '{fo}': File not found")
                        except PermissionError:
                            print(
                                f"{FA} '{fo}': Permisson error (try run as #root)")
            #----------------List of Directory---------------#
            elif user[0] == "ls":
                # list(filter(os.path.isfile, os.listdir())) (for dir)
                # list(filter(os.path.isdir, os.listdir())) (for file)
                pa = os.listdir()
                for x in pa:
                    print(x)
            #----------------------Making Directory-------------#
            elif user[0] == "mkdir":
                NAM = user[-1]
                if NAM == "mkdir":
                    print(f"{WR} folder name can't empty")
                else:
                    try:
                        os.mkdir(NAM)
                    except PermissionError:
                        print(
                            f"{AL} '{NAM}': Permission denied [Need {G}#root{W} Permission]")
                        pass
                    except FileExistsError:
                        print(f"{FA} '{NAM}': File exists")
            #----------------Changing Directory-------------#
            elif user[0] == "cd":
                DIR = user[-1]
                # DIR = user[-1]
                if DIR == "cd":
                    home = str(Path.home())
                    os.chdir(home)
                else:
                    try:
                        os.chdir(DIR)
                    except FileNotFoundError:
                        print(f"{FA} '{DIR}': No such file or directory")
                    except PermissionError:
                        print(
                            f"{AL} '{DIR}': Permission denied [Need {G}#root{W} Permission]")
                        pass
            ############################################################################
            elif user[0] == "help":
                help()
            #----------------------Cat--------------#
            elif user[0] == 'cat':
                fi = user[-1]
                try:
                    with open(fi, "r+") as _fi:
                        li = _fi.read()
                        print(li)
                except FileNotFoundError:
                    print(f"{FA} '{fi}': file not found ")
                    pass
                except PermissionError:
                    print(f"{FA} '{fi}': permission denied")
                except IsADirectoryError:
                    print(f"{WR} '{fi}': is dircetory")
            elif user[0] == "exit":
                exit(f"{RI} Exiting PyKonsole, See You Again")
                time.sleep(1)
            else:
                print(f"{FA} {user}: command not found!")
    except KeyboardInterrupt:
        pass
        print(f"\n{WR} use exit to close termenal")
        main()


try:
    home = str(Path.home())
    os.chdir(home)
    main()
except KeyboardInterrupt:
    pass
    print(f"\n{WR}use exit to close termenal")
    main()
