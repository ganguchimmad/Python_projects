import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import os


class PersonalAssist:
    def __init__(self):
        pass
    
    def TakeCommand(self):
        Query = '';
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening')
            r.pause_threshold = 0.7
            audio = r.listen(source)
            try:
                print("recognizing")
                Query = r.recognize_google(audio, language='en-in')
                print("the command is printed=", Query)

            except Exception as e:
                print(e)
            # Speak("Sorry please say that again sir")
                # Speak("Sorry please say that again sir")
                
            return Query


    def Speak(self, audio):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1.6)
        engine.say(audio)
        engine.runAndWait()

    def NumberToString(self, number):
        number_dict = {1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen",20:"Twenty",	
                    21:"Twenty one",22:"Twenty two",23:"Twenty three",24:"Twenty four",25:"Twenty five",26:"Twenty six",27:"Twenty seven",28:"Twenty eight",29:"Twenty nine	",30:"Thirty",31:"Thirty one",32:"Thirty two",33:"Thirty three",34:"Thirty four",35:"Thirty five",36:"Thirty six",37:"Thirty seven",38:"Thirty eight",39:"Thirty nine",40:"Forty",			
                    41:"Forty-one",42:"Forty-two",43:"Forty-three",44:"Forty-four",45:"Forty-five",46:"Forty-six",47:"Forty-seven",48:"Forty-eight",49:"Forty-nine",50:"Fifty",51:"Fifty-one",52:"Fifty-two",53:"Fifty-three",54:"Fifty-four",55:"Fifty-five",56:"Fifty-six",57:"Fifty-seven",58:"Fifty-eight",59:"Fifty-nine",60:"Sixty",
                    2020:"two Thousand Twenty",2021:"two Thousand Twenty one",2022:"two Thousand Twenty two"
                    }
        return number_dict[number]

    def MonthList(month):
        month = {'01':'Janauary','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'December'}
        
    def TellDay(self):
        
        # This function is for telling the
        # day of the week
        day = datetime.datetime.today().weekday() + 1
        
        #this line tells us about the number
        # that will help us in telling the day
        Day_dict = {1: 'Monday', 2: 'Tuesday',
                    3: 'Wednesday', 4: 'Thursday',
                    5: 'Friday', 6: 'Saturday',
                    7: 'Sunday'}
        
        if day in Day_dict.keys():
            day_of_the_week = Day_dict[day]
            self.Speak("The day is " + day_of_the_week)


    def TellTime(self):
        # This method will give the time
        time = str(datetime.datetime.now())
        hour = int(time[11:13].lstrip("0"))
        if hour > 12: hour = hour -12
        hour = self.NumberToString(hour)
        min = self.NumberToString(int(time[14:16].lstrip("0")))
        self.Speak("The time is " + hour + "o'clock and" + min + "Minutes")	

    def TellDate(self):
        date = datetime.datetime.now()
        year = self.NumberToString(int(date.strftime("%Y")))
        month = date.strftime("%B")
        day = self.NumberToString(int(date.strftime("%d")))
        self.Speak("Today date is "+day+" "+month+" "+year)
        
        
    def Hello(self):
        time = str(datetime.datetime.now())
        hour = int(time[11:13].lstrip("0"))
        if hour >= 4 and hour < 12: message = "Good morning"
        elif hour >= 12 and hour < 16: message = "Good afternoon"
        elif hour >= 16 and hour < 20 : message = "Good evening"
        else: message = "Good night"
        self.Speak(message + "gaangu, tell me how may i help you")

    def TakeQuery(self, query):
        first_word = ''
        if query != '':
            first_word = str(query).split()[0]
            
        if first_word == "top":
            first_word = "stop"
            
        remove_first_word = query.replace(first_word, '').strip()
        if first_word == "search":
            webbrowser.open(query)
        
        elif first_word == "open":
            os.system("start "+remove_first_word)
        
        elif first_word == "stop" or first_word == "top" or first_word == "exit" or first_word == "quit" or first_word == "close":
            self.Speak(first_word+"ing")
            exit()
    
        elif "tell me the time" in query or "what is the time" in query or "siri time please" in query or "siri what is the time" in query or "what's time" in query:
            self.TellTime()
                
        elif "what is the date" in query or "what is the date today" in query or "siri date please" in query or "siri what is the date today" in query or "what's date" in query:
            self.TellDate()
            
        elif "which day it is" in query:
            self.TellDay()

        else:
            result = wikipedia.summary(remove_first_word, sentences=4)
            #Speak("According to wikipedia")
            self.Speak(result)
            
    def Start(self):
        active = False
        while(True):
            query = self.TakeCommand().lower()
            if query == "hey siri" or query == "siri" or query == "hi siri":
                active = True
                self.Hello()
            else:
                if active is True:
                    self.TakeQuery(query) 

obj = PersonalAssist()
obj.Start()