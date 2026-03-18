import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit
import os
import smtplib

engine=pyttsx3.init('sapi5') # well its used to take inbuilt voices 
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices',voices[1].id)

rate = 185 # Decrease this value to slow down the speech engine.
engine.setProperty('rate', rate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning!!')
    elif hour>=12 and hour<18:
        speak('good afternoon!!')
    elif hour>=18:
        speak('Good evening')
    else :
        speak('night night')

    speak('im Morgan miss ,how may i help you??')
    

def takecommand():
        # takes input rom microphone n returs in string foramat
        r=sr.Recognizer() 
        print('hearing....')

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,duration=1)
            r.energy_threshold=10000
            r.pause_threshold= 1
            print("say anything : ")
            audio= r.listen(source)
        try:
            query= r.recognize_google(audio,language='en-in')
            print(query)
            
        except:
            print("sorry, could not recognise")
            return 'none'          
        return query

def sendEmail(to,content):
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.ehlo
        server.login('muttinswati9@gmail.com','swats13195')
        server.sendmail('muttinswati9@gmail.com',to,content)
        server.close()

if __name__=="__main__" :
        wishMe()
        while True:
            query=takecommand().lower()
            if 'morgan' in query:
                print('yes maam!')
                speak('yes maam!')
            
            elif "who are you" in query:
                print('im Morgan')
                speak('im Morgan')
                print('i can do everything that my creator programmed me for ')
                speak('i can do everything that my creator programmed me for ')
            
            elif "who created you" in query:
                print('i was built by Swats in vs code')
                speak('i was built by Swats in vs code')


            # logics for taskin 
            elif 'wikipedia' in query:
                    speak('searching wikipedia')
                    query=query.replace('wikipedia','')
                    result=wikipedia.summary(query,sentences=2)
                    speak('According to wikipedia')
                    print(result)
                    speak(result)
            
            elif "open youtube" in query:
                print('launching yt')
                # webbrowser.open('youtube.com')
                chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                urL='https://www.google.com'
                webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
                webbrowser.get('chrome').open_new_tab("www.youtube.com")
            
            elif "play" in query:
                song=query.replace("play"," ")
                speak("playing" +song)
                pywhatkit.playonyt(song)
            
            # elif "search in youtube" in query:
            #     speak('what u wanna watch?')
            #     qr=query.replace('search in youtube'," ")
            #     webbrowser.open(f"www.youtube.com/results?seach_query={qr}")
            
            
            elif "open google" in query:
                # webbrowser.open('stackoverflow.com')
                # browser= webbrowser.get('chrome')
                # browser.open_new("peeet")
                chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                urL='https://www.google.com'
                webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
                webbrowser.get('chrome').open_new_tab("www.google.com")

            # elif "search in google" in query:
            #     speak('what should i search for?')
            #     chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            #     # urL='https://www.google.com'
            #     webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
            #     query=takecommand().lower()
            #     webbrowser.get('chrome').open_new_tab(f"{query}")
            #     # webbrowser.open(f"{qr}")
            #     #  well check this shiiii out its fasinating'
            #     res=wikipedia.summary(query,sentences=1)
            #     speak(res)


            elif " open brave" in query:
                chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                urL='https://www.google.com'
                webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
                webbrowser.get('chrome').open_new_tab("www.brave.com")
                # webbrowser.open('www.brave.com')
            
            # elif 'close browser' in query:
            #     os.system('taskkill/f/im brave.exe')
            
            elif 'the time' in query:
                strTime=datetime.datetime.now().strftime('%H:%M:%S')
                speak(f'miss the time is {strTime}') 
            
            elif 'open code' in query:
                codepath="C:\\Users\\mutti\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
                os.startfile(codepath)  

            elif 'close code' in query:
                os.system('taskkill/im code.exe/t /f')
            
            # elif 'open SnippingTool' in query:
            #     codepath="C:\\WINDOWS\\system32\\SnippingTool.exe"
            #     os.startfile(codepath)
            
            # elif 'close SnippingTool' in query:
            #     os.system('taskkill/f/im SnippingTool.exe')
            
            elif 'open notepad' in query:
                codepath="C:\\Windows\\notepad.exe"
                os.startfile(codepath)
            
            # elif 'close  notepad' in query:
            #     os.system('taskkill/f/im notepad.exe')

            elif 'open project recommendation' in query:
                speak('INCOMING project recommendation')
                codepath="C://MY Files//Swati Academics//sem 3//projects//dvp//dvp.py"
                os.startfile(codepath)
            
            elif 'send email' in query:
                # for i in eid:
                    try:
                        speak('what shall i write?')
                        print('what shall i write?')
                        content=takecommand()
                        to='erenmika009@gmail.com'
                        sendEmail(to,content)
                        speak('email has been sent')
                    except Exception as e:
                        speak('sorry email cant be sent!!:(')

            elif "shutdown the system Morgan" in query:
                os.system('shutdown /s /t 5')
                # os.system("shutdown /p")
            
            elif "restart the system" in query:
                os.system('shutdown /r /t 5')
            
            elif 'go to sleep Morgan' in query:
                os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
            
            # elif "lock the system" in query:
            #     os.system("rund1132.exe powrprof.d11,setsuspendstate 0,1,0")
                    

                        
            
            