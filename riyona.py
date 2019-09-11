from nltk.chat.util import Chat, reflections
from yahoo_weather.weather import YahooWeather
from yahoo_weather.config.units import Unit

weather = YahooWeather(APP_ID="bZfbp95i",
                     api_key="dj0yJmk9WlFYSnR2ZG5aTUcxJmQ9WVdrOVlscG1ZbkE1TldrbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PWJh",
                     api_secret="46d7dd26679a3d6bdfc8e59ccb392469c1027d5d")

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
     [
        r"what is your name ?",
        ["My name is Riyona. Thank You",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude\nSeriously you are asking me this?",]
        
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*) created ?",
        ["Bibith K Mathew, People call him Techy Bibi",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Chennai, Tamil Nadu',]
    ],
    [
        r"how is weather in (.*)?",
        [weather.get_yahoo_weather_by_city("%1", Unit.celsius),
        weather.condition.text,]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football",]
    ],
    [
        r"Bye",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
],
]

def riyona():
    print('---------------------------------------------')
    print('|HAI, I AM RIYONA 0.2.')
    print('---------------------------------------------')
    chat = Chat(pairs, reflections)
    chat.converse()
if __name__ == "__main__":
    riyona()
