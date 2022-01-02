import time
import counter
import sqlite3
import pyttsx3

engine = pyttsx3.init()

st = "Welcome to Kahoot Quiz Board"
engine.say(st)
engine.runAndWait()

admin1 = ""
admin2 = ""
count = 0

con = sqlite3.connect('logins.db')
cur = con.cursor()

# Create table
# cur.execute('''CREATE TABLE users2(f_name text, l_name text,u_name text, p_word text)''')

q = True

class Login:
    def __init__(self, id, pas):
        self.id = id
        self.pas = pas

    def check(self, id, pas):
        print(f" Hi {self.id}")
        if self.id == id and self.pas == pas:
            print("Login success!")
        else:
            print("login failed")


log = Login(admin1, admin2)


while q == True:
    print("\n++++++ Welcome to Kahoot Quiz Board ++++++\n")
    #engine.say("Welcome to Kahoot Quiz Board")
    print("[Choice 1: For Registration  ]")
    print("[Choice 2: For Registered User]")
    print("[Choice 3: Create Quiz Room]")
    print("[Choice 4: Play Kahoot(SQS) game]")

    x = int(input("Enter a choice: "))
    if x == 1:
        f_name = input("Enter first name:")
        l_name = input("Enter Last name:")
        u_name = input("Enter User name:")
        p_word = input("Enter password: ")

        # Insert a row of data
        # cur.execute("INSERT INTO users2 VALUES (?,?,?,?)", lang_list)
        cur.execute("INSERT INTO users2 VALUES ('" + f_name + "','" + l_name + "','" + u_name + "','" + p_word + "')")
        print("Registration complete")

    elif x == 2:
        uname = input("Enter Login ID:")
        password = input("Enter password: ")
        log.check(uname, password)

    elif x == 3:
         #cur.execute('''CREATE TABLE subject(Question text, option1 text, option2 text, option3 text,option4 text,
         # ans text, code int,topic text)''')

        q_number = int(input("enter the total question to be created"))
        for x in range(q_number):
            code = input("enter the code ")
            topic = input(" enter the Topic ")
            Question = input("Enter Question:")
            option1 = input("Enter Option1:")
            option2 = input("Enter option2:")
            option3 = input("Enter Option3")
            option4 = input("Enter Option4: ")
            ans = input("Enter the correct answer: ")
            cur.execute("INSERT INTO subject VALUES ('" + Question + "','" + option1 + "','" + option2 + "',"
                                                                                          "'" + option3 + "',"
                                                                                                                  "'" +
                    option4 + "','" + ans + "','" + code + "','" + topic + "')")
        con.commit()


    elif x == 4:
          #print("hello")
        for row in cur.execute("SELECT Question,option1,option2,option3,option4,ans FROM subject "):
            q1 = row[0]
            q2 = row[1]
            q3 = row[2]
            q4 = row[3]
            q5 = row[4]
            a6 = row[5]
            print("QUESTION  :-", q1)
            print("OPTION1:-", q2)
            print("OPTION2:-", q3)
            print("OPTION3:-", q4)
            print("OPTION4:-", q5)
            print("Enter You Answer Choice:")
            #counter.stopwatch(60)
            tic = time.perf_counter()
            gamer_ans = input()
            toc = time.perf_counter()
            tim = toc - tic
            print(f" Your answered the question  in {tim:0.2f} seconds")
            if a6 == gamer_ans:
                print("you answer is correct")
                count = count + 1
        print("total correct answers:", count)

    else:
        print("Thank you,Welcome  Again")
        sx = "Thank you,Welcome  Again"

        engine.say(sx)
        engine.runAndWait()
        q = False

#print("total correct answers:", count)

con.close()
