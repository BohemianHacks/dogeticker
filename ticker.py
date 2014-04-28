import json
import urllib2
import curses
import curses.ascii
import time

DogeChainUrl = 'https://dogechain.info/chain/Dogecoin/q/addressbalance/'
ExchangeUrl = 'https://www.dogeapi.com/wow/?a=get_current_price&convert_to=USD&amount_doge=1'
address = 'DN395oxmaPTKFoB5fWUh8cD7qrx3HAM3UP'
interval = 30.0
ExitButtons = [curses.ascii.ESC, curses.ascii.ascii('q')]

def getExchangeRate():
    try:
        data = float(json.loads(urllib2.urlopen(ExchangeUrl).read())['data']['amount'])
    except:
        data = 0.0
    return data

def getBalance(address):
    try:
        data = float(urllib2.urlopen(DogeChainUrl+address).read())
    except:
        data = 0.0
    return data

win = curses.initscr()
win.addstr("Loading...")
win.refresh()
win.nodelay(1)
curses.cbreak()
curses.noecho()
curses.curs_set(0)
key = win.getch()
last = time.time()

while not (key in ExitButtons):
    balance = "$" + str(getBalance(address) * getExchangeRate())
    win.clear()
    win.addstr(balance)
    win.refresh()

    while time.time() - last < interval and not (key in ExitButtons):
        curses.napms(200)
        key = win.getch()

    last = time.time()

curses.nocbreak()
curses.echo()
curses.curs_set(1)
curses.endwin()
