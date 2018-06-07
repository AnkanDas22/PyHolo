#module importing
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import playsound
import random
import string
from weather import Weather
from PyLyrics import PyLyrics
from selenium import webdriver
import webbrowser

#main code
cropen=0
abuses=['n****','n*****','f*****','m***********','c***','a**','p****','f***','dick','d***']
memes=['Toucha my spagget lol funny amirite?','Hahaha Ugandan Knuckles hahaha very funny show me da way','Metal Gear isn\'t a solid franchise','Spiderman goes down on Elsa','''What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You’re fucking dead, kiddo.''','Doesn\'t matter, memes suck']
songs=['''Girl, you really got me goin'
You got me so I don't know what I'm doin'
Yeah, you really got me now
You got me so I can't sleep at night''',
       '''Little darling, the smiles returning to the faces
Little darling, it seems like years since it's been here
Here comes the sun
Here comes the sun, and I say
It's all right''',
       '''Hey Jude, don't make it bad
Take a sad song and make it better
Remember to let her into your heart
Then you can start to make it better''',
       '''Out here in the fields
I fight for my meals
I get my back into my living
I don't need to fight
To prove I'm right
I don't need to be forgiven

Don't cry
Don't raise your eye
It's only teenage wasteland

Sally ,take my hand
Travel south crossland
Put out the fire
Don't look past my shoulder
The exodus is here
The happy ones are near
Let's get together
Before we get much older

Teenage wasteland
It's only teenage wasteland
Teenage wasteland
Oh, oh
Teenage wasteland
They're all wasted!''',
       '''Mama, just killed a man,
Put a gun against his head,
Pulled my trigger, now he's dead.
Mama, life had just begun,
But now I've gone and thrown it all away.

Mama, ooh,
Didn't mean to make you cry,
If I'm not back again this time tomorrow,
Carry on, carry on as if nothing really matters.''',
       '''With the lights out, it's less dangerous
Here we are now, entertain us
I feel stupid and contagious
Here we are now, entertain us
A mulatto
An albino
A mosquito
My libido
Yeah, hey, yay''',
       '''Just a small town girl, living in a lonely world
She took the midnight train going anywhere
Just a city boy, born and raised in South Detroit
He took the midnight train going anywhere
A singer in a smoky room
A smell of wine and cheap perfume
For a smile they can share the night
It goes on and on and on and on''',
       '''But you didn't have to cut me off
Make out like it never happened and that we were nothing
And I don't even need your love
But you treat me like a stranger and that feels so rough
No you didn't have to stoop so low
Have your friends collect your records and then change your number
I guess that I don't need that though
Now you're just somebody that I used to know

Now you're just somebody that I used to know
Now you're just somebody that I used to know''',
       '''dun dun dun dun dun dun dun dun dun dun dun dundun dun dundundun dun dun dun dun dun dun dundun dundun dun
    ''',
       '''Dancing on the line
Of the great divide
Wash my hands, turn my back
I don't need the memories we had
I'm leaving you behind
Across the great divide''',
       '''Ha-ha-ha-ha-ha-ha-ha-ha-ha-ha
Look what you've done!
Ha-ha-ha-ha-ha-ha-ha-ha-ha-ha
I'm a motherfuckin' Starboy
Ha-ha-ha-ha-ha-ha-ha-ha-ha-ha
Look what you've done!
Ha-ha-ha-ha-ha-ha-ha-ha-ha-ha
I'm a motherfuckin' Starboy''',
       '''She had a face straight outta magazine
God only knows but you'll never leave her
Her balaclava is starting to chafe
And when she gets his gun he's begging, "Babe, stay, stay, stay, stay, stay."''']

def weather(place):
    weather=Weather()
    location=weather.lookup_by_location(place)
    condition=location.condition()
    con_text_matters=condition.text()
    speak(con_text_matters)

def forecast(place):
    weatherf=Weather()
    locationf=weatherf.lookup_by_location(place)
    forecasts=locationf.forecast()
    speak("Forecast for how many days from now on?")
    try:
        ui=recordAudio()
        #uix=[]
        cc=0
        if "ONE" or "1" in ui.upper():
            uix=1
        elif "TWO" or "2" in ui.upper():
            uix=2
        elif "THREE" or "3" in ui.upper():
            uix=3
        elif "FOUR" or "4" in ui.upper():
            uix=4
        elif "FIVE" or "5" in ui.upper():
            uix=5
        elif "SIX" or "6" in ui.upper():
            uix=6
        elif "SEVEN" or "7" in ui.upper():
            uix=7
        elif "EIGHT" or "8" in ui.upper():
            uix=8
        elif "NINE" or "9" in ui.upper():
            uix=9
        elif "TEN" or "10" in ui.upper():
            uix=10
        elif "ELEVEN" or "11" in ui.upper():
            uix=11
        elif "TWELVE" or "12" in ui.upper():
            uix=12
        """for c in ui:
            if c.isdigit():
                uix.append(c)
        uix=''.join(uix)
        uix=int(uix)"""
        for forecastf in forecasts:
            if(cc==uix):
                break
            speak("It'll be "+(forecastf.text()).lower()+" on "+forecastf.date()+" with a maximum temperature of "+forecastf.high()+" degrees Fahrenheit and a minimum of "+forecastf.low()+" degrees Fahrenheit")
            cc=cc+1
    except ValueError:
        speak("Just say the number of days")
    
def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    fn=os.path.abspath('mp3s\\'+''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase) for i in range(6))+'.mp3')
    tts.save(fn)
    time.sleep(2)
    playsound.playsound(fn,True)
    os.unlink(fn)
 
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
 
    #Speech recognition
    data = ""
    try:
        #Uses Google API
        #To use another API key: r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data

def search(term):
    webbrowser.open("https://www.google.co.in/search?q="+term.replace(" ", "+"))

i=0

def lara(data):
    global i
    co=0
    for j in abuses:
        if j in data:
            speak("That's very rude, kid!")
            break
    if "search for " in data:
        search(data.split(" for ")[1])
    
    if "how are you" in data:
        speak("I am fine")
 
    if "time" in data:
        speak(ctime())
 
    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on"+a+", I will show you where " + location + " is.")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
        os.pause()
    if "kill" in data:
        if "yourself" or "yourselves" in data:
            if(i==0):
                speak("Please don't be so rude")
            elif(i==1):
                speak("Please don't say that anymore")
            elif(i==2):
                speak("This is the third time you're being so rude")
            elif(i==3):
                speak("Shut that out")
            elif(i==4):
                speak("You're literally harassing me at this point")
            else:
                speak("That is enough")
            i=i+1
    if "cure" and "cancer" in data:
        speak("Not yet known, or so I know")
    if "forecast" in data:
        if "weather" in data:
            speak("Where do you live?")
            u=recordAudio()
            forecast(u)
        else:
            speak("I'm no astrologer")
        co=1
    if(co==0):
        if "weather" in data:
            speak("Where do you live?")
            x=recordAudio()
            weather(x)
            
    if "best" in data:
        if "song" in data:
            speak("Darude Sandstorm")
        if "MEME" in data.upper():
            speak("Short Nibba Memes")
    if "MAKE" or "FIND" or "FRY" or "SHOW" or "THROW" or "TELL" or "GIVE" or "SPICY" in data.upper():
        if "MEME" in data.upper():
            speak("I hate memes but here you go: "+memes[random.randint(0,(len(memes)-1))])
    if "SING" in data.upper():
        speak(songs[random.randint(0,(len(songs)-1))])
    if "LYRICS" in data.upper():
        speak("What's the song?")
        sng=recordAudio()
        speak("Who's the artist of the song?")
        art=recordAudio()
        try:
            xd=PyLyrics.getLyrics(art,sng)
            speak(xd)
        except ValueError:
            speak("Sorry couldn't find anything like that, try to be more accurate next time")
    if "YOUR" in data.upper():
        if "NAME" in data.upper():
            speak("My name is Slim shay...well I'm Lara")
    if "YOU" in data.upper():
        if "LOVE" in data.upper():
            speak("I love everyone, mostly")
    if "WHO" in data.upper():
        if "YOU" in data.upper():
            speak("I'm a very good girl and I was made by Ankan Das. I dream to be a unicorn one day.")
    if "THANK" in data.upper():
        if "YOU" in data.upper():
            speak("Always Welcome")
    if "THANKS" in data.upper():
        speak("Awww you're welcome")

    if "OPEN" in data.upper():
        try:
            if "BOB" in data.upper():
                speak("We are well ahead of 2017, my dude")
            elif "TOP CAKE" in data.upper():
                webbrowser.open("https://www.youtube.com/playlist?list=PLP6VcJBJDTosuorpW5bpmatMMHy1hqZvj")
            elif "MUSIC" in data.upper():
                webbrowser.open("https://www.youtube.com/playlist?list=PLP6VcJBJDTosuorpW5bpmatMMHy1hqZvj")
            elif "FACEBOOK" in data.upper():
                webbrowser.open("https://www.facebook.com/")
            elif "TWITTER" in data.upper():
                webbrowser.open("https://twitter.com/")
            elif "REDDIT" in data.upper():
                webbrowser.open("https://www.reddit.com/")
            elif "GOOGLE" in data.upper():
                webbrowser.open("https://www.google.com")
            elif "YOUTUBE" in data.upper():
                webbrowser.open("https://www.youtube.com/")
            elif "GITHUB" in data.upper():
                webbrowser.open("https://github.com/")
            elif "INSTAGRAM" in data.upper():
                webbrowser.open("https://www.instagram.com/")
            elif "QUORA" in data.upper():
                webbrowser.open("https://www.quora.com/")
            elif "LINKEDIN" in data.upper():
                webbrowser.open("https://www.linkedin.com/")
            elif "GMAIL" in data.upper():
                webbrowser.open("https://mail.google.com/")
            elif "TRANSLATE" in data.upper():
                webbrowser.open("https://translate.google.com/")
            elif "DRIVE" in data.upper():
                webbrowser.open("https://drive.google.com/")
            elif "STACK OVERFLOW" in data.upper():
                webbrowser.open("https://stackoverflow.com/")
            elif "STEAM" in data.upper():
                webbrowser.open("http://store.steampowered.com/")
            elif "WIKIPEDIA" in data.upper():
                webbrowser.open("https://en.wikipedia.org/")
            elif "YAHOO" in data.upper():
                webbrowser.open("http://www.yahoo.com/")
            elif "AMAZON" in data.upper():
                webbrowser.open("https://www.amazon.com/")
            elif "NETFLIX" in data.upper():
                webbrowser.open("https://www.netflix.com/")
            elif "ITUNES" in data.upper():
                webbrowser.open("https://www.apple.com/itunes/")
            elif "SPOTIFY" in data.upper():
                webbrowser.open("https://www.spotify.com/")
            elif "IMDB" in data.upper():
                webbrowser.open("www.imdb.com/")
            elif "CRAIGLIST" in data.upper():
                webbrowser.open("https://www.craigslist.org/about/sites")
            elif "x******" in data.upper():
                webbrowser.open("https://www.xvideos.com/")
            elif "P******" in data.upper():
                webbrowser.open("https://www.pornhub.com/")
            elif "R******" in data.upper():
                webbrowser.open("https://www.redtube.com/")
            elif "X*******" in data.upper():
                webbrowser.open("https://xhamster.com/")
            elif "DROPBOX" in data.upper():
                webbrowser.open("https://www.dropbox.com/")
            elif "EBAY" in data.upper():
                webbrowser.open("https://www.ebay.com/")
            elif "BOOKING" in data.upper():
                webbrowser.open("https://www.booking.com/")
            elif "SOUNDCLOUD" in data.upper():
                webbrowser.open("https://soundcloud.com/")
            elif "BLOGGER" in data.upper():
                webbrowser.open("https://www.blogger.com/")
            elif "BING" in data.upper():
                webbrowser.open("https://www.bing.com/")
            elif "TUMBLR" in data.upper():
                webbrowser.open("https://www.tumblr.com/")
            elif "TUMBLER" in data.upper():
                webbrowser.open("https://www.tumblr.com/")
            elif "WORDPRESS" in data.upper():
                webbrowser.open("https://wordpress.com/")
            elif "IMGUR" in data.upper():
                webbrowser.open("https://imgur.com/")
            elif "BAIDU" in data.upper():
                webbrowser.open("https://www.baidu.com/")
            elif "L*********" in data.upper():
                webbrowser.open("https://www.livejasmin.com/en/")
        except:
            speak("Try again later, connection failed")

    if "OPEN" in data.upper():
        if "PRIVATE" in data.upper():
            global cropen
            try:
                if(cropen==0):
                    driver=webdriver.Chrome("chromedriver.exe")
                    driver.set_page_load_timeout(30)
                if "BOB" in data.upper():
                    speak("We are well ahead of 2017, my dude")
                elif "TOP CAKE" in data.upper():
                    driver.get("https://www.youtube.com/playlist?list=PLP6VcJBJDTosuorpW5bpmatMMHy1hqZvj")
                elif "MUSIC" in data.upper():
                    driver.get("https://www.youtube.com/playlist?list=PLP6VcJBJDTosuorpW5bpmatMMHy1hqZvj")
                elif "FACEBOOK" in data.upper():
                    driver.get("https://www.facebook.com/")
                elif "TWITTER" in data.upper():
                    driver.get("https://twitter.com/")
                elif "REDDIT" in data.upper():
                    driver.get("https://www.reddit.com/")
                elif "GOOGLE" in data.upper():
                    driver.get("https://www.google.com")
                elif "YOUTUBE" in data.upper():
                    driver.get("https://www.youtube.com/")
                elif "GITHUB" in data.upper():
                    driver.get("https://github.com/")
                elif "INSTAGRAM" in data.upper():
                    driver.get("https://www.instagram.com/")
                elif "QUORA" in data.upper():
                    driver.get("https://www.quora.com/")
                elif "LINKEDIN" in data.upper():
                    driver.get("https://www.linkedin.com/")
                elif "GMAIL" in data.upper():
                    driver.get("https://mail.google.com/")
                elif "TRANSLATE" in data.upper():
                    driver.get("https://translate.google.com/")
                elif "DRIVE" in data.upper():
                    driver.get("https://drive.google.com/")
                elif "STACK OVERFLOW" in data.upper():
                    driver.get("https://stackoverflow.com/")
                elif "STEAM" in data.upper():
                    driver.get("http://store.steampowered.com/")
                elif "WIKIPEDIA" in data.upper():
                    driver.get("https://en.wikipedia.org/")
                elif "YAHOO" in data.upper():
                    driver.get("http://www.yahoo.com/")
                elif "AMAZON" in data.upper():
                    driver.get("https://www.amazon.com/")
                elif "NETFLIX" in data.upper():
                    driver.get("https://www.netflix.com/")
                elif "ITUNES" in data.upper():
                    driver.get("https://www.apple.com/itunes/")
                elif "SPOTIFY" in data.upper():
                    driver.get("https://www.spotify.com/")
                elif "IMDB" in data.upper():
                    driver.get("www.imdb.com/")
                elif "CRAIGLIST" in data.upper():
                    driver.get("https://www.craigslist.org/about/sites")
                elif "x******" in data.upper():
                    driver.get("https://www.xvideos.com/")
                elif "P******" in data.upper():
                    driver.get("https://www.pornhub.com/")
                elif "R******" in data.upper():
                    driver.get("https://www.redtube.com/")
                elif "X*******" in data.upper():
                    driver.get("https://xhamster.com/")
                elif "DROPBOX" in data.upper():
                    driver.get("https://www.dropbox.com/")
                elif "EBAY" in data.upper():
                    driver.get("https://www.ebay.com/")
                elif "BOOKING" in data.upper():
                    driver.get("https://www.booking.com/")
                elif "SOUNDCLOUD" in data.upper():
                    driver.get("https://soundcloud.com/")
                elif "BLOGGER" in data.upper():
                    driver.get("https://www.blogger.com/")
                elif "BING" in data.upper():
                    driver.get("https://www.bing.com/")
                elif "TUMBLR" in data.upper():
                    driver.get("https://www.tumblr.com/")
                elif "TUMBLER" in data.upper():
                    driver.get("https://www.tumblr.com/")
                elif "WORDPRESS" in data.upper():
                    driver.get("https://wordpress.com/")
                elif "IMGUR" in data.upper():
                    driver.get("https://imgur.com/")
                elif "BAIDU" in data.upper():
                    driver.get("https://www.baidu.com/")
                elif "L*********" in data.upper():
                    driver.get("https://www.livejasmin.com/en/")
            except ConnectionRefusedError or ConnectionResetError:
                speak("Try again later, connection failed")

    try:
        if "CLOSE" in data.upper():
            if "BROWSER" in data.upper():
                driver.close()
                speak("Okay closed the browser for ya")
            if "BROWSERS" in data.upper():
                driver.quit()
    except ConnectionRefusedError or ConnectionResetError:
        speak("Sorry, internal breakdowns")

#LaraWakesUp
time.sleep(1)
speak("What's your name?")
mm=recordAudio()
speak("Hi "+mm+", what can I do for you?")
while True:
    data = recordAudio()
    if('exit' in data):
        if('app' or 'application' or 'it' or 'yourself' in data):
            speak("Buh bye for now!")
            break
    elif('close' in data):
        if('app' or 'application' or 'it' or 'yourself' in data):
            speak("See ya!")
            break
    elif('shut' in data):
        if('app' or 'application' or 'it' or 'yourself' in data):
            speak("Hit me up whenever you feel free again!")
            break
    lara(data)
