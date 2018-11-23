import time
import requests

def read(url):
    return requests.get(url).text

class Hacker:
    def __init__(self, name, team):
        self.name = name
        self.team = team
        self.motivation = 0
        self.crying = True

    def stop_crying(self):
        self.crying = False

    def try_harder(self):
        self.motivation += 11

    @staticmethod
    def rtfm():
        read("https://0x00sec.org/")

    @staticmethod
    def enumerate(target):
        target.increase_progress(10)
        return "Run gobuster & nmap?"

    def hack(self, target):
        while not target.hacked:
            if self.motivation == 0:
                self.stop_crying()
                self.try_harder()
                self.rtfm()
            self.enumerate(target)
            time.sleep(0)
        print("???")
        print("Profit!")


class Target:
    def __init__(self, hostname):
        self.hostname = hostname
        self.hacked = False
        self.hacked_progress = 0

    def increase_progress(self, amount):
        if self.hacked_progress >= 100:
            self.hacked = True
        else:
            self.hacked_progress += amount


target = Target("https://hackthebox.eu/")
me = Hacker("pry0cc", "0x00sec")
me.hack(target)
