import datetime
import re
import subprocess
import sys
import webbrowser
from discord_webhook import DiscordEmbed, DiscordWebhook
import websocket
import threading
import aiohttp, asyncio, json, os, time, uuid, socket
from itertools import islice, cycle
import pyperclip
class sniper:
    def __init__(self):
        self.shutIT = True
        self.threadit = True
        self.dontrest = 0
        self.items = []
        with open('itsconfig.json', 'r') as file: 
            content = json.load(file)
            self.token = content["token"]
        def send_json_request(ws,request):
            ws.send(json.dumps(request))
        def recieve_json_response(ws):
            response = ws.recv()
            if response:
                return json.loads(response)
        def heartbeat(interval,ws):
            print ('BROKEN CODES WATCHER: BY STRONK')
            print('WATCHING...')
            while self.threadit:
                time.sleep(interval)
                heartbeatJSON = {
                    "op": 1,
                    "d": "null"
                }
                send_json_request(ws,heartbeatJSON)
                self.dontrest += 1
                print("Restarting")
                if self.dontrest == 15:
                    self.restart_program()
                    break
        ws = websocket.WebSocket()
        ws.connect('wss://gateway.discord.gg/?v=6&encording=json')
        event = recieve_json_response(ws)
        heartbeat_interval = event['d']['heartbeat_interval'] / 1000
        threading._start_new_thread(heartbeat,(heartbeat_interval,ws)) # type: ignore
        token = self.token
        payload = {
            'op':2,
            "d":{
                "token":token,
                "properties":{
                    "$os":"windows",
                    "$browser":"chrome",
                    "$device": 'pc'
                }
            }
        }
        send_json_request(ws,payload)
        keywords = ['thundyundez.#0','BrokenCodesBot#0870','ayumiswift#0','justcallmekie#0','zbrush#0','.enbro#0','flakies#0','effyessias#0','rookvanguard#0','surfer#0','fouled.anchors#0','exoticdev#0','yuveiin#0','mihq#0','valkenheim#0','harht#0','milkware#0','augc#0','ash_#0','ebuh#0','coldbe#0','sebee#0','yasinsamsuddin#0','alpkurt#0','anareloux#0','xenonic_778#0','sziczi#0','aerialsabove#0','pointmelon#0','bunnexh#0','ydebbi#0','redlegenddev#0','melecody#0','duckxander#0','adaptkhoi#0','builder_boy#0','koob85#0','empyror#0','zeemane#0','caska0.1#0','devvincis#0','typedummy#0','wh1m.#0','dipybrick#0','junozy#0','astrra#0','zdragonx#0','kingerman89#0','fakerup#0','waffletrades#0','UGC Limited Notifier#0098','sharkingaround#0','divstudio#0']
        while self.threadit:
            event = recieve_json_response(ws)
            try:
                self.dontrest = 0
                if event is not None and isinstance(event, dict): 
                    current_time = datetime.datetime.now().strftime("%I:%M:%S.%f %p")
                    
                    if 'author' in event['d'] and 'content' in event['d']:
                        text = f"{event['d']['author']['username']}#{event['d']['author']['discriminator']}: {event['d']['content']}"
                        texts = f"{event['d']['embeds']}"
                        for keyword in keywords:
                            match = re.search(keyword, text)
                            matches = re.search(r'\|\|([^\n]+)\|\|', text)
                            length = len("n795etwbavzexz")
                            pattern = r'\b\w{%d}\b' % length
                            typedummy = re.search(pattern, text)
                            urls = re.search(r'Arial_80:([^\s/]+)',texts)
                            if match:
                                if typedummy:
                                    print('TypeDummy: ')
                                    result = typedummy.group(0)
                                    pyperclip.copy(result) 
                                    print(result)
                                if matches:
                                    print('Broken Codes: ')
                                    result = matches.group(1)
                                    pyperclip.copy(result) 
                                    print(result)
                                if urls:
                                    code_text = urls[0][9:23] 
                                    pyperclip.copy(code_text) 
                                    print('Broken Codes:')
                                    print(code_text)
                        op_code = event.get('op')
                        if op_code == 11:
                            print('heartbeat received')
            except Exception as e:
                string = str(e)
                if string == "argument of type 'NoneType' is not iterable":
                    print(f"")
                else:
                    self.restart_program()
                continue
    def restart_program(self):
        python = sys.executable
        self.items = []
        subprocess.call([python, __file__])
        exit(1)
bot = sniper()
bot.__init__()