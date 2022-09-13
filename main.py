import subprocess
import os
import appscript
import time as TT
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import smtplib
import keyring
from email.message import EmailMessage
from playsound import playsound
import wikipedia
import pyjokes
from selenium import webdriver
import face_recognition
import cv2
import numpy as np
import wget
import requests
import ast
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import shutil
from textblob import TextBlob

server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
server.starttls()
server.login("namannanda5657@gmail.com",keyring.get_password("mail", "namannanda5657"))
def wha_do_u_feel(text):
    tell = TextBlob(text)
    tell1 = tell.sentiment.polarity
    if tell1 >= 0.6:
        tts(" i think you are a really good person, i like you and i think you will do something really good in future")
    elif tell1 <= 0.59 and tell1 >= 0:
        tts("i think you are a nice and positive person")
    elif tell1 <=0 and tell1 >= -0.3:
        tts("you can be a little more better person")
    elif tell1 <= -0.31:
        tts("i think you really are a bad person and you shouldn't talk with me")        


def pd():
    print(os.getcwd())
def tts(to_speak):

    engine.say(to_speak)
    engine.runAndWait()
def change_wallpaper():
    TT.sleep(2)
    tts("changing wallpaper ,sir")
    url = "https://api.nasa.gov/planetary/apod?api_key=lyeVRtd1d7YWl9NB5k2yxbff793dcM4jwAKkiX7v"
    TT.sleep(2)
    tts("getting the wallpaper from nasa ,sir")
    r = requests.get(url)
    data = ast.literal_eval(r.content.decode('utf-8'))
    print(data["url"])
    TT.sleep(2)
    tts("downloading the wallpaper,sir")
    wget.download(data["url"], "./wallpaper_prev.jpg") 

    img = plt.imread("wallpaper_prev.jpg")
    plt.imshow(img)
    plt.show()
    
    c1 = input("y for yes and n for no")
    
    if "y" in c1:
        shutil.move("./wallpaper_prev.jpg","/Users/jarvis/wallpapers/current_wallpaper.jpg")
        from appscript import app, mactypes
        app('Finder').desktop_picture.set(mactypes.File('/Users/jarvis/wallpapers/current_wallpaper.jpg'))
        TT.sleep(2)
        tts("wallpaper updated ,sir")
    else:
        os.remove('./wallpaper_prev.jpg')
        TT.sleep(2)
        tts("wallpaper not updated, sir")       
def sendmsg(reciever, subject, message):
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From'] = "namannanda5657@yahoo.com"
    msg['To'] = reciever
    server.send_message(msg)
    server.quit()
def mail():
    mails_to_name = {"naman": "lifelovesnaman@gmail.com"}
    TT.sleep(2)
    tts("what is the mail address, sir")
    print("what is the mail address?, sir")
    inp3 = listen_say()
    if inp3 in mails_to_name:
        inp8 = mails_to_name[inp3]
    else:
        inp8 = inp3
    print(inp8)
    TT.sleep(2)
    tts("what is the subject, sir")
    print("what is the subject? ,sir ")
    inp4 = listen_say()
    print(inp4)
    TT.sleep(2)
    tts("what is the text you want to send ,sir ")
    print("what is the text you want to send? ,sir")
    inp2 = listen_say()
    print(inp2)
    TT.sleep(2)
    tts("would you like to see the mail before sending , sir ")
    print("would you like to see the mail before sending ?, sir ")
    b1 = listen_say()
    if "yes" in b1:
        print("mail id: " + inp8)
        print("subject: " + inp4)
        print("body: " + inp2)
        TT.sleep(2)
        tts("would you like to send this , sir ")
        print("would you like to send this? , sir ")
        c1 = listen_say()
        if "yes" in c1:
            sendmsg(inp8, inp4, inp2)
        else:
            quit
    else:
        sendmsg(inp8, inp4, inp2)
    print("DONE!!")
def alarms():
    TT.sleep(2)
    tts("at what time will you like me to notify you , sir ")
    print("at what time will you like me to notify you ?, sir")
    l1 = listen_say()
    a2, a3 = l1.split(":")
    alarm_hour = a2
    alarm_min = a3[0:2]
    q, w, e = a3[3:7].split(".")
    alarm_period = q+w
    TT.sleep(2)
    tts("alarm set for {}".format(l1))
    print("alarm set for {}".format(l1))
    while True:
        now = datetime.datetime.now()

        current_hour = now.strftime("%I")
        current_min = now.strftime("%M")
        current_period1 = now.strftime("%p")
        current_period = current_period1.lower()

        if alarm_period == current_period:
            if alarm_hour == current_hour:
                if alarm_min == current_min:
                    print("Wake Up!")
                    # playsound("/Users/jarvis/mycod/facial_recon/sbeep.mp3")
                    TT.sleep(2)
                    tts("sir its {}".format(current_hour+current_min+current_period))
def times():
    time = datetime.datetime.now().strftime(
        "%I:%M %p")      # %H:%M for 24 hr format
    TT.sleep(2)
    tts(" current time is " + time)
    print(time)
def plays():
    song = a1.replace('play', '')
    TT.sleep(2)
    tts("playing" + song)
    pywhatkit.playonyt(song)
    print(song)
def intros():
    TT.sleep(2)
    tts("okay sir,here we go")
    TT.sleep(3)
    tts("i am an artificial intelligence system who thinks on his own and works on your commands , also known as ramu kaka ,always here to help you like your virtual assistant ")
def sleeps():
    TT.sleep(2)
    tts("okay ,sir , going to sleep . see you later")
    subprocess.call(['osascript', '-e', 'tell app "System Events" to sleep'])
def searchs():
    person = a1.replace("search for ", "")
    info = wikipedia.summary(person, 1)
    print(info)
    TT.sleep(2)
    tts(info)
def howru():
    TT.sleep(2)
    tts("i am good , thanks for asking , how are you doing ,sir")
def dies():
    TT.sleep(2)
    tts("as you wish ,i am dead ,sir")
    playsound("/Users/jarvis/pymycod/123adhm.mp3")
def sub_processs(oc,in123):
    if oc =="open":
        TT.sleep(2)
        tts("{} is opened sir".format(in123))
    elif oc =="close":
        TT.sleep(2)
        tts("{} is closed sir".format(in123))
def jokess():
    s1 = pyjokes.get_joke(language="en", category="all")
    print(s1)
    TT.sleep(2)
    tts(s1)
    tts("hahaha")
def welcome():
    print("My pleasure sir")
    TT.sleep(2)
    tts("My pleasure sir, always happy to help you")
def face_recon():
    TT.sleep(2)
    tts("turning face recognition on ,sir")

    # Get a reference to webcam #0 (the default one)
    video_capture = cv2.VideoCapture(0)

    # faces to be recognised


    naman = face_recognition.load_image_file("/Users/jarvis/mycod/facial_recon/known_ppl/naman.jpeg")
    naman_face_encoding = face_recognition.face_encodings(naman)[0]

    garv = face_recognition.load_image_file("/Users/jarvis/mycod/facial_recon/known_ppl/garv.jpg")
    garv_face_encoding = face_recognition.face_encodings(garv)[0]

    seema = face_recognition.load_image_file("/Users/jarvis/mycod/facial_recon/known_ppl/seema.jpeg")
    seema_face_encoding = face_recognition.face_encodings(seema)[0]

    dadu = face_recognition.load_image_file("/Users/jarvis/mycod/facial_recon/known_ppl/dadu.jpeg")
    dadu_face_encoding = face_recognition.face_encodings(dadu)[0]

    chachu = face_recognition.load_image_file("/Users/jarvis/mycod/facial_recon/known_ppl/chachu.jpeg")
    chachu_face_encoding = face_recognition.face_encodings(chachu)[0]

    chachi = face_recognition.load_image_file("/Users/jarvis/mycod/facial_recon/known_ppl/chachi.jpeg")
    chachi_face_encoding = face_recognition.face_encodings(chachi)[0]

    sachi = face_recognition.load_image_file("/Users/jarvis/mycod/facial_recon/known_ppl/sachi.jpeg")
    sachi_face_encoding = face_recognition.face_encodings(sachi)[0]


    # Create arrays of known face encodings and their names

    known_face_encodings = [
        naman_face_encoding,
        garv_face_encoding,
        seema_face_encoding,
        dadu_face_encoding,
        chachu_face_encoding,
        chachi_face_encoding,
        sachi_face_encoding


    ]

    known_face_names = [
        "naman ",
        "garv",
        "seema",
        "dadu",
        "chachu",
        "chachi",
        "sachi"


    ]

    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.45)
                name = "Unknown"

                # # If a match was found in known_face_encodings, just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(
                known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)

                for item in known_face_names:
                    for item2 in face_names:
                        if item == item2:
                            print("known person detected")
                            # playsound("/Users/jarvis/mycod/facial_recon/sbeep.mp3")

        process_this_frame = not process_this_frame

        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35),
                        (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6),
                        font, 1.0, (255, 255, 255), 1)

        # Display the resulting image

        cv2.imshow('face recon - enabled , video output ', frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(10) == ord('q'):
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()
def listen_say():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        process = r.recognize(audio)
        process = process.lower()
        print(process)
        if "jarvis" in process:
            process = process.replace("jarvis", "")
            print(process)
            exit
    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return process
engine = pyttsx3.init(driverName='nsss')
get_voice = engine.getProperty("voices")
engine.setProperty("rate", 185)
engine.setProperty("voice", get_voice[0].id)
tts("Hi , i am jarvis ,,at your command ")
def command():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        process = r.recognize(audio)
        process = process.lower()
        print(process)
        if "jarvis" in process:
            process = process.replace("jarvis", "")
            print(process)
            exit
    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return process
while True:

    a1 = command()
    if "chrome" in a1:
        if "open" in a1:
            subprocess.call(['osascript', '-e', 'tell app "Google Chrome" to open'])
            sub_processs("open","Google Chrome")
        elif "close" in a1:
            subprocess.call(['osascript', '-e', 'tell app "Google Chrome" to quit'])
            sub_processs("close","Google Chrome")
    elif "whatsapp" in a1:
        if "open" in a1:
            subprocess.call(['osascript', '-e', 'tell app "Whatsapp" to open'])
            sub_processs("open","Whatsapp")
        elif "close" in a1:
            subprocess.call(['osascript', '-e', 'tell app "Whatsapp" to quit'])
            sub_processs("close","Whatsapp")
    elif "youtube" in a1:
        web = webdriver.Chrome('/Users/jarvis/mycod/chromedriver')
        web.get("https://www.youtube.com")
        sub_processs("open","youtube")
    elif "amazon" in a1:
        web = webdriver.Chrome('/Users/jarvis/mycod/chromedriver')
        web.get("https://www.amazon.in")
        sub_processs("open","amazon")
    elif "study" in a1:
        web = webdriver.Chrome('/Users/jarvis/mycod/chromedriver')
        web.get("https://online.vidyamandir.com/user/login")
        roll = "j2spr000007"
        a1 = web.find_element_by_xpath('//*[@id="edit-name-1"]')
        a1.send_keys(roll)
        key = keyring.get_password("vmc", "j2spr000007")
        a2 = web.find_element_by_xpath('//*[@id="edit-pass-1"]')
        a2.send_keys(key)
        b1 = web.find_element_by_xpath('//*[@id="edit-submit-1"]')
        b1.click()
        sub_processs("open","vmc")
    elif "die" in a1:
        dies()
        break
    elif "kill" in a1:
        dies()
        break
    elif "search" in a1:
        searchs()
    elif "sleep" in a1:
        sleeps()
    elif "introduce" in a1:
        intros()
    elif "play" in a1:
        plays()
    elif "time" in a1:
        times()
    elif "mail" in a1:
        mail()
    elif "alarm" in a1:
        alarms()
    elif "sad" in a1:
        jokess()
    elif "joke" in a1:
        jokess()
    elif "thank you" in a1:
        welcome()
    elif "funny" in a1:
        welcome()
    elif "face" in a1:
        face_recon() 
    elif "wallpaper" in a1:
        change_wallpaper()
    elif "how are you" in a1:
        howru()  
    elif "do you feel" in a1:
        wha_do_u_feel(a1)
    elif "your name" in a1:
        TT.sleep(2)
        tts("my name is jarvis because the person who made me liked the name jarvis , duh , ,who kept your name?")         
    elif "quit" in a1:
        break
    
    else:
        TT.sleep(2)
        tts("ohh, good for you")
