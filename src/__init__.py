
from __future__ import print_function
import re
import random
import time as tyme
try:
    import codes as __codes__
except ImportError:
    from . import codes as __codes__
import webbrowser

class flames(object):

    def __init__(self, name=None, crush=None):

        if name == None or crush == None:
            raise SyntaxError("Enter two names for FLAMES calculation")
        if type(name) == int:
            self.name = str(name)
        if type(crush) == int:
            self.crush = str(crush)
        if type(name) == str:
            self.name = name.lower()
        if type(crush) == str:
            self.crush = crush.lower()
        if type(name) == list or type(name) == tuple or type(name) == dict:
            raise TypeError("Input only strings or numbers")
        if type(crush) == list or type(crush) == tuple or type(crush) == dict:
            raise TypeError("Input only strings or numbers")

        self.__common = []
        Name = list(re.sub("\W", "", self.name))
        Crush = list(re.sub("\W", "", self.crush))
        for flag in range(len(Name)+len(Crush)):
            for i in Name:
                if i in Crush:
                    Name.remove(i)
                    Crush.remove(i)
                    self.__common.append(i)

        count = len(Name) + len(Crush)
        flag = count
        FLAMES = ['.'] + list("FLAMES" * count)
        self.__order = []

        for i in range(5):

            element = FLAMES[count]
            temp = FLAMES.index(element)
            self.__order.append(element)
            while element in FLAMES:
                FLAMES.remove(element)
            count = flag + temp -1

        self.__FULL = {'F':'FRIENDSHIP',
                       'L':'LOVE',
                       'A':'AFFECTION',
                       'M':'MARRIAGE',
                       'E':'ENEMY',
                       'S':'SIBLINGS'}
        self.__count = flag
        self.__FLAMES = FLAMES
        self.__percentage = str(random.randint(20, 100))
        self.value = self.__FULL[self.__FLAMES[1]]

    def __repr__(self):

        return "<-{0}:FLAMES:{1}->".format(self.name, self.crush)

    def result(self, no=1, time=0.09):

        fword = self.__FULL[self.__FLAMES[1]]
        word = self.__FLAMES[1]
        codes = {'F':__codes__.FRIENDS,
                 'L':__codes__.LOVE,
                 'A':__codes__.AFFECTION,
                 'M':__codes__.MARRIAGE,
                 'E':__codes__.ENEMY,
                 'S':__codes__.SIBLINGS
                }
        length = len(codes[word])-1
        if length == 1:
            statement = "{0} has only {1} design".format(fword, length)
        else:
            statement = "{0} has only {1} designs".format(fword, length)
        if no == "LOVE" and time == "YES":
            for i in __codes__.__gettrattr__:
                for j in i: print(j)
            return
        if no <= 0:
            raise IndexError("The Starting number is 1 or it can be leftout")
        if no > len(codes[word]):
            raise IndexError(statement)
        else:
            for line in codes[word][no]:
                print(line)
                tyme.sleep(time)

    def info(self):

        print()
        print("Name                     :", self.name)
        print("Crush                    :", self.crush)
        print("Result                   :", self.value)
        print("FLAMES Count             :", self.__count)
        print("Common Letters           :", ", ".join(self.__common))
        print("Order                    :", ", ".join(self.__order))
        print("Relationship Percentage  :", self.__percentage)
        print()

    def getinfo(self):

        return {'Name' : self.name,
                'Crush': self.crush,
                'Result': self.value,
                'FLAMES Count':self.__count,
                'Common Letters' : self.__common,
                'Order' : self.__order,
                'Relationship Percentage' : self.__percentage,
               }

def about():

    print(r'''
    FLAMES : Friend Love Affection Marriage Enemy Siblings

    We all love to play this game during our childhood days.
    Putting FLAMES with your name and our crush name and getting L, M or A
    will be the most happiest moment of our time.
    Or even Worse..! we will be teased by our friend if we get S or E...

    Now you can do this in python with ease and get your
    Relationship percentage also..

    >>> import flames
    >>> i = flames.flames("YourName", "YourCrushName")
    >>> i.info()

    Name                     : yourname
    Crush                    : yourcrushname
    Result                   : F
    FLAMES Count             : 5
    Common Letters           : y, u, n, m, o, a, r, e
    Order                    : E, M, S, L, A
    Relationship Percentage  : 30

    And... Hold on.. This is boring and more didatic. Where's the fun ?
    Use i.result() for yourself and feel the fun...
    Also you can change the design and speed for i.result
    i.result(no=<num>, time=<speed>)  # This is really fun..!!

    Developed with love by Vaasu Devan S.
    To view his github page, just call flames.github()

    He also developed easy-to-use cowsay module and also
    the Periodic elements properties.
    pip install cowsay periodicelements
    ''')

def github():

    webbrowser.open("https://www.github.com/VaasuDevanS")

if __name__ == "__main__":
    print("Success..You can import the flames module without any error")
