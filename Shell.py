import os
from time import ctime, sleep, time
import sys
import getpass
import subprocess
import webbrowser
import qrcode
import win32clipboard
import string
from PIL import Image
from io import BytesIO
from PIL import ImageGrab
import win32con
import re
import errno
import requests
from datetime import datetime
import numpy as np
import cv2
import pyglet
import tweepy
import pyfiglet
from pyfiglet import Figlet 
import ctypes
import pytube
from pytube import YouTube
import ffmpeg
import subprocess
from moviepy.editor import *
import youtube_dl
from plyer import notification
import random

#VARIABLES
a = os.path.expanduser('~').replace('\\', '/')
comd = 0
exit = 0
delte = 0
t = time()
tim = (ctime(t))
usrnm = "anna"
hostnm = "AnnaOS"
passwd = "123"
#CHANGE THESE 
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
visual = 'C:/Program Files/Microsoft VS Code/Code.exe', a + "/Documents/pytho/AnnaShell.py"
whatsapp = a + "/AppData/Local/WhatsApp/Whatsapp.exe"
notepad = "C:/Program Files/Notepad++/notepad++.exe"
explorer = "C:/Windows/explorer.exe"
spotify = a + "/AppData/Roaming/Spotify/Spotify.exe"
vim = a + "/Downloads/Vim/vim82/vim.exe"
osu  = a + "/AppData/Local/osu!/osu!.exe"
home = a + '/Documents/pytho/'

os.chdir(a + '/Downloads')
dir = os.getcwd()
arch = 0
version = '0.1-' + str(datetime.now().date())

#LOGIN
def login():
    right = 0
    with open(str(home) + "password.txt") as psw:
        password = psw.read()
    with open(str(home) + "quietstartup.txt") as qs:
        quietstartup = qs.read() 

    _ = os.system('cls')
    if quietstartup == 'off':
        print("Welcome to AnnaSH!")
        print("It's Currently " + str(tim) + '\n')

    while right == 0:
        passwd = getpass.getpass(prompt = "Enter Password: ")
        if passwd == password:
            print ("Login successful!")
            right = 1
            if quietstartup == 'on':
                sleep(0.2)
                _ = os.system('cls')
        else:
            print("Wrong password") 

login()
 
#COMMAND HANDLING
def cmdhandling():
    comd = 0
    #exit = 0
    delte = 0
    t = time()
    tim = (ctime(t))
    
    hostnm = "AnnaOS"
    passwd = "123"
    dir = os.getcwd()
    shrdir = dir.replace('\\', '/')
    shrtdir = "~"
    arch = 0
    
    with open(str(home) + 'username.txt') as un:
        usrnm = un.read()
        #print(usrnm)

    with open(str(home) + 'hostname.txt') as hn:
        hostnm = hn.read()
        #print(hostnm)
        #print(passwd)

    with open(str(home) + "quietstartup.txt") as qs:
        quietstartup = qs.read() 

    while delte == 0 and arch == 0 :
        ps2 = open(str(home) + "PS1.txt").read()


        if ps2 == "full":
            comd = input("[" + str(usrnm) + "@" + str(hostnm) + " " + str(shrtdir) + "]$ ")
        elif ps2 == "simple":
            comd = input("> ")
        if comd == "sudo rm -rf /":
            print ("deleting all file.... \n")
            sleep(2)
            print("Done!")
            delte = 1

        if comd == "rm -rf /":
            print("rm: permission denied")

        if comd == "exit":
            _ = os.system('cls')
            quit()

        if comd == "clear" or comd == "cl" or comd == 'l' or comd == '':
            _ = os.system('cls')

        if comd == "neofetch":
            with open(str(home) + "neofetch.txt") as nf:
                print(nf.read())

        if comd == "no":
            with open(str(home) + "troll.txt") as tr:
                print(tr.read())

        if comd.startswith("calc"):
            if comd == "calc 9+10":
                print(21)
            else:
                print (str(eval(comd.replace('calc', ''))))

        if comd == "username":
            usrnm = input("Enter new username: ")
            usn = open(str(home) + "username.txt", "w")
            usn.write(usrnm)
            usn.close()


        if comd == "hostname":
            hostnm = input("Enter new hostname: ")
            hsn = open(str(home) + "hostname.txt", "w")
            hsn.write(hostnm)
            hsn.close()

        if comd == "passwd":
            passwd = getpass.getpass(prompt = "Enter new password: ")
            psw = open(str(home) + "password.txt", "w")
            psw.write(passwd)
            psw.close()

        if comd == "logout":
            login()

        if comd == "time":
            print(str(tim))

        if comd.startswith("run"):
            prog = comd.replace('run ','')
            if prog == "visual":
                subprocess.call([visual])

            if prog == "wapp":
                subprocess.call([whatsapp])

            if prog == "npad":
                subprocess.call([notepad])

            if prog == "files":
                subprocess.call([explorer])

            if prog == "music":
                subprocess.call([spotify])
            
            if prog == "vim":
                subprocess.call([vim])

            if prog == "osu":
                subprocess.call([osu])

        if comd == "qr":
            win32clipboard.OpenClipboard()
            url = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            img = qrcode.make(url)

            output = BytesIO()
            img.convert('RGB').save(output, 'BMP')
            data = output.getvalue()[14:]
            output.close()
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(win32con.CF_DIB, data)
            win32clipboard.CloseClipboard()

        if comd.startswith('cd'):
            if comd == 'cd':
                os.chdir(a)
                dir = os.getcwd()
            else:
                try:
                    os.chdir(comd.replace('cd ', ''))
                    dir = os.getcwd()
                except FileNotFoundError:
                    try:
                        os.chdir(dir + '/' + comd.replace('cd', ''))
                    finally:
                        print('Directory not found')

        if comd.startswith("web"):
            address = comd.replace('web', '')
            #uncomment for internet explorer
            #webbrowser.open(address, new=2)
            webbrowser.get(chrome_path).open(address)

        if comd == "pwd":
            print(dir)

        if comd == "hwd":
            shrtdir = "~"

        if comd == "swd":
            shrtdir = shrdir.replace('C:', '')

        if comd.startswith('ls') or comd.startswith('dir'):
            try:
                if comd == 'ls' or comd == 'dir':
                        ls = os.listdir(dir)
                        for file in ls: 
                            print(file)

                if comd == "ls img" or comd == "dir img":
                        ls = os.listdir(dir)
                        for file in ls:
                            if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.jfif') or file.endswith('.webp') or file.endswith('.gif'):
                                print(file)
                if comd == "ls vid" or comd == "dir vid":
                        ls = os.listdir(dir)
                        for file in ls:
                            if file.endswith('.mp4') or file.endswith('.mov') or file.endswith('.avi') or file.endswith('.mkv') or file.endswith('.avi') or file.endswith('.flv') or file.endswith('.webmv'):
                                print(file)

                if comd == "ls mus" or comd == "dir mus":
                        ls = os.listdir(dir)
                        for file in ls:
                            if file.endswith('mp3') or file.endswith('m4a') or file.endswith('wav') or file.endswith('wma') or file.endswith('aac') or file.endswith('mpeg'):
                                print(file)

                if comd.startswith("ls") or comd.startswith("dir"):
                    if 'ls' in comd:
                        typ = comd.replace('ls ', '')
                    elif 'dir' in comd:
                        typ = comd.replace('dir ', '')
                    ls = os.listdir(dir)
                    for file in ls:
                        if file.endswith(typ):
                            print(file)
            except PermissionError:
                print(dir + ': Permission denied')




        if comd.startswith('open '):
            file1 = comd.replace('open ', '')
            try:
                os.startfile(file1)
            except FileNotFoundError:
                print("File not found") 


        if comd == "archinstall":
            arch = 1

        if comd == "m19":
            futuredate = datetime.strptime('Mar 19 2022  9:30', '%b %d %Y %H:%M')
            nowdate = datetime.now()
            count = int((futuredate-nowdate).total_seconds())
            days = count//86400
            hours = (count-days*86400)//3600
            minutes = (count-days*86400-hours*3600)//60
            seconds = count-days*86400-hours*3600-minutes*60
            print("{} days {} hours {} minutes {} seconds left".format(days, hours, minutes, seconds))

        if comd == "m26":
            futuredate2 = datetime.strptime('Mar 26 2022  9:30', '%b %d %Y %H:%M')
            nowdate = datetime.now()
            count2 = int((futuredate2-nowdate).total_seconds())
            days2 = count2//86400
            hours2 = (count2-days2*86400)//3600
            minutes2 = (count2-days2*86400-hours2*3600)//60
            seconds2 = count2-days2*86400-hours2*3600-minutes2*60
            print("{} days {} hours {} minutes {} seconds left".format(days2, hours2, minutes2, seconds2))

        if comd.startswith("src"):
            search = comd.replace('src ', '')
            ls = os.listdir(dir)
            for file in ls:
                if search in file:
                    print(file)

        if comd.startswith("echo"):
            if '>>' in comd:
                destination = input("Enter destination file: ")
                strToWrite = '\n' + comd.replace('echo >> ', '').replace('\\n', '\n')
                strng = open(str(destination), "a")
                strng.write(strToWrite)
                strng.close()

            if '-ovrw' in comd:
                destination = input("Enter destination file: ")
                strToWrite = comd.replace('echo -ovrw ', '')
                strng = open(str(destination), "w")
                strng.write(strToWrite)
                strng.close()

            if not '>>' in comd and not '-ovrw' in comd:
                print (comd.replace('echo ', ''))

        if comd.startswith('cat'):
            source = comd.replace('cat ', '')
            try:
                with open(str(source)) as src:
                    string = src.read()
                    print(string)
            except FileNotFoundError:
                print("File not found")
            
            except UnicodeDecodeError:
                print("No thanks")

        if comd.startswith("tweet"):
            auth = tweepy.OAuthHandler("bjdkMziuun0hmvYh6zDKMLtHz", "mSJeF47aL4K1oX0MHyuEgQJnrGdRYVN6fQwykuMvCHJUiUoUXu")
            auth.set_access_token("1090967005967069184-vh2E0nmMYuhqv0ObE1qJDlw0xGqVnd", "WiNL5bOF8JhLY0LlnNEmOLb4n8wQ668TJK57KnimlMmC7")
            api = tweepy.API(auth)
            if '-img' in comd: 
                tweet = comd.replace('tweet -img ', '')
                image = input("Select image: ")
                api.update_status_with_media(tweet, image)
                print ("Done!")

            else:
                tweet = comd.replace('tweet ', '')
                api.update_status(status =(tweet))
                print ("Done!")

        if comd == 'g':
            webbrowser.get(chrome_path).open('google.com')
            
        if comd == 'r':
            webbrowser.get(chrome_path).open('reddit.com')

        if comd == 't':
            webbrowser.get(chrome_path).open('twitter.com')

        if comd == 'yt':
            webbrowser.get(chrome_path).open('youtube.com')
     
        if comd.startswith('google '):
            webbrowser.get(chrome_path).open('https://www.google.com/search?q=' + comd.replace('google ', '').replace(' ', '+'))

        if comd.startswith('r '):
            webbrowser.get(chrome_path).open('https://reddit.com/search?/q=' + comd.replace('r ', '').replace(' ', '%20'))

        if comd.startswith('t '):
            webbrowser.get(chrome_path).open('https://twitter.com/search?q=' + comd.replace('t ', '').replace(' ', '%20'))

        if comd.startswith('yt '):
            webbrowser.get(chrome_path).open('https://www.youtube.com/results?search_query=' + comd.replace('yt ', '').replace(' ', '+'))

        if comd.startswith('ascii '):
            fontspath = str(home) + 'fonts.txt'
            if '-font' in comd:
                font = input("Select font (l to list all): ")
                if font == 'l':
                    with open(fontspath) as fnt:
                        fonts = fnt.read()
                        print(fonts)
                    font = input('Select font (l to list all): ')
                with open(fontspath) as fnt:
                    fontss = fnt.read()
                    if font in fontss:
                        custom_fig = Figlet(font=font)
                        print(custom_fig.renderText(comd.replace('ascii -font ', '')))
            else:
                text = pyfiglet.figlet_format(comd.replace('ascii ', ''))
                print(text)

        if 'goku' in comd:
            with open (str(home) + 'gonku.txt') as gku:
                goku = gku.read()
                print(goku)
        
        if comd == "family guy is NOT funny":
            text = "So that's what you think huh?"
            for l in text:
                sys.stdout.write(l)
                sys.stdout.flush()
                sleep(0.05)
            sleep(0.9)
            print(' ')
            text = "Well then what do you think about this?"
            for l in text:
                sys.stdout.write(l)
                sys.stdout.flush()
                sleep(0.05)
            print(' ')
            sleep(0.6)
            text = "Wiping drive C: in 5....."
            for l in text:
                sys.stdout.write(l)
                sys.stdout.flush()
                sleep(0.03)
            sleep(0.7)
            text = "4...."
            for l in text:
                sys.stdout.write(l)
                sys.stdout.flush()
                sleep(0.03)
            sleep(0.7)
            text = "3..."
            for l in text:
                sys.stdout.write(l)
                sys.stdout.flush()
                sleep(0.03)
            sleep(0.7)
            text = "2.."
            for l in text:
                sys.stdout.write(l)
                sys.stdout.flush()
                sleep(0.03)
            sleep(0.7)
            text = "1"
            for l in text:
                sys.stdout.write(l)
                sys.stdout.flush()
                sleep(0.03)
            sleep(0.7)
            print('')
            text = "LAST CHANCE: IS FAMILY GUY FUNNY? "
            for l in text:
                sys.stdout.write(l)
                sys.stdout.flush()
                sleep(0.1)
            funny = input('')
            
            print('')
            if funny == 'no':
                text = "Alright thats it"
                for l in text:
                    sys.stdout.write(l)
                    sys.stdout.flush()
                    sleep(0.04)
                sleep(0.5)
                print('')
                text = "Drive C: wiped succesfully! System will shutdown."
                for l in text:
                    sys.stdout.write(l)
                    sys.stdout.flush()
                    sleep(0.03)
                sleep(5)
                os.system("shutdown -s -t 1")
            if funny == 'yes':
                text = "You're lying!"
                for l in text:
                    sys.stdout.write(l)
                    sys.stdout.flush()
                    sleep(0.05)
                print('')
                sleep(0.5)
                text = "Drive C: wiped succesfully! System will shutdown."
                for l in text:
                    sys.stdout.write(l)
                    sys.stdout.flush()
                    sleep(0.03)
                sleep(5)
                os.system("shutdown -s -t 1")

        if comd == 'gub':
            webbrowser.get(chrome_path).open('github.com/anna-bannanna/anna-bannanna.github.io')

        if comd == 'homepage':
            webbrowser.get(chrome_path).open('anna-bannanna.github.io/coolhomepage')

        if comd == 'movie':
            webbrowser.get(chrome_path).open('anna-bannanna.github.io')

        if comd == 'amp':
            webbrowser.get(chrome_path).open('anna-bannanna.github.io/moviefree/amphibia')

        if comd == 'toh':
            webbrowser.get(chrome_path).open('anna-bannanna.github.io/moviefree/toh')

        if comd.startswith('amp '):
            address = 'anna-bannanna.github.io/moviefree/' + comd.replace('amp ', '').replace('s', 'S').replace('e', 'E')
            webbrowser.get(chrome_path).open(address)

        if comd.startswith('toh '):
            address = 'anna-bannanna.github.io/moviefree/t' + comd.replace('toh ', '').replace('s', 'S').replace('e', 'E')
            webbrowser.get(chrome_path).open(address)

        #SET WALLPAPER
        if comd.startswith('wp '):
            wp = str(shrdir) + '/' + comd.replace('wp ', '')
            SPI_SETDESKWALLPAPER = 0x14
            SPIF_UPDATEINIFILE   = 0x2
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, wp, 0)

        if comd == 'anrbx':
            webbrowser.get(chrome_path).open('https://www.roblox.com/users/215609186/profile')

        #YOUTUBE VIDEO DOWNLOADER, 3 FOR AUDIO, 4 FOR VIDEO (Syntax: ytd 3/4 *link*)
        if comd.startswith("ytd 4 "):
            link = comd.replace("ytd 4 ", "")
            video = YouTube(link)
            print("Title: ",video.title)
            print("Number of views: ",video.views)
            print("Length of video: ",video.length,"seconds")
            print("Description: ",video.description)
            print("Ratings: ",video.rating)
            ys = video.streams.get_highest_resolution()
            text = "Downloading.... \n"
            for l in text:
                sys.stdout.write(l)
                sys.stdout.flush()
                sleep(0.1)
            ys.download(a + '/Downloads')
            print("Done!")

        if comd.startswith("ytd 3 "):
            link = comd.replace("ytd 3 ", "")
            yt = YouTube(link)
            print("Title: ",video.title)
            print("Number of views: ",video.views)
            print("Length of video: ",video.length,"seconds")
            print("Description: ",video.description)
            print("Ratings: ",video.rating)
            video = yt.streams.filter(only_audio=True).first()
            destination = a + '/Downloads/'
            out_file = video.download(output_path=destination)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            print(yt.title + " has been successfully downloaded")

        if comd == 'hit --act1':
            with open ('ACT1.txt') as a1:
                act1 = a1.read()
                print(act1)

        #WAS THAT THE BITE OF '87???
        if comd == "fnaf":
            try:
                os.startfile(a + '/Downloads/Was that the bite of 87 (Meme Template).mp4')
            except FileNotFoundError:
                video = YouTube('https://www.youtube.com/watch?v=qM2tAkqDTYs')
                ys = video.streams.get_highest_resolution()
                ys.download(a + '/Downloads/')
                os.startfile(a + '/Downloads/' + video.title.replace('?', '') + '.mp4')
            print(pyfiglet.figlet_format("WAS THAT THE BITE OF '87???"))


        if comd == "cancell":
            print("Are you sure you want to cancell the instaleiaton?\n[ok i'll/cancell]")
            oc = input("")
            if "ok i'll" in oc:
                quit()
            if 'cancell' in oc:
                print("Cancellled cancellling the instaleiation")

        if comd.startswith('cc'):
            url = 'cloudconvert.com/' + comd.replace('cc ', '').replace(' ', '-to-')
            webbrowser.get(chrome_path).open(url)

        if comd == 'inf':
            print("AnnaShell version " + str(version) + "\nDeveloped by Anna O.\nMy Twitter: @AguSedoo\nMy Github: anna-bannanna\nMy Stackoverflow: 18298990\nMy Reddit: u/AguSedo")

        if comd == "restart":
            os.execv(sys.executable, ['python'] + sys.argv)
        
        if comd == "notif send":
            tll = input('Enter notification title: ')
            msg = input('Enter notification message: ')
            notification.notify(
                title = tll,
                message = msg,
                app_icon = str(home) + 'annash.ico',
                timeout = 50,
            )

        if comd.startswith('sbahj '):
            if '--random in comd':
                page = random.randint(1, 54)
                webbrowser.get(chrome_path).open("https://www.homestuck.com/sweet-bro-and-hella-jeff/" + str(page)) 
            else:
                page = comd.replace('sbahj ', '')
                webbrowser.get(chrome_path).open('https://www.homestuck.com/sweet-bro-and-hella-jeff/' + page)  

        if comd == 'quietstartup':
            if quietstartup == 'off':
                qss = 'on'
            elif quietstartup == 'on':
                qss = 'off'

            qs = open(str(home) + 'quietstartup.txt', "w")
            qs.write(qss)
            qs.close()

        if comd == 'ps1':
            if ps2 == 'simple':
                ps11 = 'full'
            elif ps2 == 'full':
                ps11 = 'simple'

            ps3 = open(str(home) + 'PS1.txt', "w")
            ps3.write(ps11)
            ps3.close()

        if comd == 'shut pc down':
            os.system("shutdown -s -t 1")





        hs = open(str(home) + 'ansh-history.txt', 'a')
        hs.write('\n' + str(comd))
        hs.close()


    while delte == 1:
        comd = input("[" + str(usrnm) + "@" + str(hostnm) + " (System Broky :( )]$ ")
        if comd == "exit":
            quit()

        else:
            print("Your System Broky :(")
        
    while arch == 1:
        _ = os.system('cls')
        print("Arch Linux 5.16.4-ARCH (tty1)")
        print("archiso login: root (automatic login)")
        cmd = input("root@archiso ~ # ")
        disk = 0
        if comd == "clear":
            _ = os.system('cls')

        if cmd.startswith("cfdisk") and "/dev/sda" in cmd:
            disk = 1
            print(disk)
        elif cmd.startswith("cfdisk") and "/dev/sda" not in cmd:
            print("Unknown disk")


cmdhandling()