import requests
class Hue:
    def __init__(self, user, ip, lamp):
        self.user = user
        self.ip = ip
        self.lamp = lamp
        self.url = 'http://{}/api//lights/{}/state/'.format(self.ip, self.user, self.lamp)
        
    def set_lamp(self, is_on):
        data = {'on' : is_on}
        requests.put(self.url, json=data)
        
    def set_color(self, color):
        if color =="ORANGE":
            data = {"on" : True, "sat" : 254, "bri" : 254, "hue" : 10880}
        elif color == "GREEN":
            data = {"on" : True, "sat" : 254, "bri" : 254, "hue" : 21760}
        elif color == "WHITE":
            data = {"on" : True, "sat" : 254, "bri" : 254, "hue" : 32640}
        elif color == "BLUE":
            data = {"on" : True, "sat" : 254, "bri" : 254, "hue" : 43520}
        elif color == "PINK":
            data = {"on" : True, "sat" : 254, "bri" : 254, "hue" : 54400}
        elif color == "RED":
            data = {"on" : True, "sat" : 254, "bri" : 254, "hue" : 65280}
        requests.put(self.url, json=data)
    
if __name__ == "__main__":
    hue = Hue('xxxxx-xxxxx', '192.168.2.127', '3') # Usercode, Adresse der Bridge, Lampennummer
    #while (command := input("Kommando: ")) != "X": #Befehl mit Walrossoperator
    command = input("Kommando: ")
    while command != "X":
        command = input("Kommando: ")
    
        if command == "ON":
            hue.set_lamp(True)
        elif command == "OFF":
            hue.set_lamp(False)
        else:
            hue.set_color(command)
                


            