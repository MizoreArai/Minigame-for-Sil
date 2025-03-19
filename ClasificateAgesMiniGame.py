# Minor&OfAge[MiniGame] - Dedicated to deerest Sil
# Create a project that asks the user for their age 
# Then displays the message "You are of age", or "You are not of age"
# Depending on whether the user is of age or not.
# if---if/else---if/elif/else statements:
entrance = print ("How old are you?") # entrance shiets are fine anyways (no need 'def stuff' here)
# Here we come with da lists
y = ['Yes', 'yes', 'y', 'Aye', 'aye', 'Yep', 'yep', 'Yesh', 'yesh', 'Yeah', 'yeah'] 
n = ['No', 'no', 'n', 'Nah', 'nah', 'Nah ah', 'nah ah', 'Nope', 'nope', 'Niet', 'niet']
yeno = ['Who knows?', 'who knows?', 'Maybe', 'maybe', 'I do not know', 'Could be', 'could be']
s = ['Ye ye', 'ye ye', 'Yeye', 'yeye', 'Mayhaps', 'mayhaps', 'I am Sil', 'Sil', 'sil', 'S', 's']
d = ['Nuh uh', 'nuh uh', 'Meh', 'meh', 'Nein', 'nein', 'i am sil', 'Deer', 'Deer Moma', 'deer moma']
expectedAnswer = ['25th of October', '25th of october', '25th Oct', '25th oct', '25 Oct', '25 oct', 'October 25', 'october 25', 'Oct 25', 'oct 25']
one = ['One', 'one', '1', 'First', 'first', 'The first one']
two = ['Two', 'two', '2', 'Second', 'second', 'The second one']
three = ['Three', 'three', '3', 'Third', 'third', 'The third one']
Silber = 'Deer Moma'
while True:
    try:
        x = int (input ()) # input is needed to give da users a chance to interact with da programme
        # int: converts the user input to an integer
        # if/elif/else statements
        if x < 0:
            print ("Either you are dead as fack or you do not even existed yet, buddy.")
            print ("Thankyu for spending time with me. Wish ya a marvelous day!")
            break
        elif x >= 0 and x < 18:
            print ("Ew, a minor!")
            print ("Haha jk jk. Thank you so much for being here. Please have a terrific day!")
            break
        elif x == 18:
            print ("Please enter your birth date:")
# Noice, here comes the lmao part
            while True:
                a = input()
                if a in expectedAnswer:
                    print ("You are here, Deer Moma!")
                    print ("Wanna take a peek at a heart?")
                    # Turtle Graphics (draw heart)
                    while True:
                        b = input()
                        if b in y or b in s:
                            import turtle # import turtle library
                            bg = turtle.Screen()
                            bg.bgcolor("light purple")
                            bg.title ("Sil thing")
                            pen = turtle.Turtle()
                            def curve(): # Use[def x():---x()] to define a function (seems useful but still)
                                for k in range (200):
                                    pen.right (1)
                                    pen.forward (1)
                            def heart():
                                pen.fillcolor ('light blue')
                                pen.begin_fill()
                                pen.left (140)
                                pen.forward (133)
                                curve()
                                pen.forward (112)
                                pen.end_fill()
                            def txt():
                                pen.up()
                                pen.setpos (-68, 95)
                                pen.down()
                                pen.color ('light pink') # Now, lemme add a bit of cuteness into your life
                                pen.write ("ϯλρρψ β√-1Γ⊥ϯәλψ 2 µ", font=("Segoe Print", 12, "cursive"))
                                heart() # Happy Birthday!!!
                                txt()
                                pen.ht()
                            break
                        elif b in n or b in d:
                            print ("Okay, I do not wanna show ya a heart either...")
                            print ("So, would ya like to listen to some musics instead?")
# And here, da music part. I took a look at those pieces we had mentioned sometimes thinking you might wanna listen to 'em again haha xD
                            while True:
                                cb = input()
                                if cb in y or cb in s:
                                    print ("They are all old tracks so just choose one and chill out.")
                                    print ("1. Violin Concerto in B Minor, Op. 35: 3rd Mov [Oskar Rieding]")
                                    print ("2. La Campanella [Niccòlo Paganini]")
                                    print ("3. Eden Roc [Ludovico Einaudi]")
                                    while True:
                                        cb1 = input()
                                    # Open link using html file.example (shiet doesn't work since I don't have the required library lol)
                                        #if cb1 in one:
                                            #print ("")
                                            #open("link.html", "w").write('<a href="WHERE DA LINK GOES"< Link </a>')
                                            #break
                                    # Same stuff using webbrowser commmand
                                        if cb1 in one:
# Doubting hard whether Spotify or YouTube is better to copy links
                                            import webbrowser
                                            webbrowser.open ("https://open.spotify.com/embed/track/7rRdxmennBB1z4dgv8k518?utm_source=generator")
                                            break
                                        elif cb1 in two:
                                            import webbrowser
                                            webbrowser.open ("https://open.spotify.com/embed/track/1IRqLBc1JAKIsLcOKwIMyY?utm_source=generator")
                                            break
                                        elif cb1 in three:
                                            import webbrowser
                                            webbrowser.open ("https://open.spotify.com/embed/track/7mwE7apWsU1dNwReYOdDis?utm_source=generator")
                                            break
                                        else:
                                            print ("Are you blind or wat? Choose an option from 1 to 3!")
                                        continue
                                    break
                                elif cb in n or cb in d:
                                    print ("Oh, maybe the next time then. Wanna play something else?")
                                    print ("Like, rolling dice and guessing numbers?")
# Here come da Mini Guessing Games!!! Starts with A SIX SIDES DICE.
                                    while True:
                                        ak = input()
                                        if ak in y or ak in s:
                                        # Roll_Dice programme: Gives you an error if you enter an invalid integer (other than the ones in the dice)
                                        # how the user about the error and do not enter a character that is not an integer
                                            import random
                                            number = random.randint(1, 6)
                                            if number == 1:
                                                side = '1'
                                            elif number == 2:
                                                side = '2'
                                            elif number == 3:
                                                side = '3'
                                            elif number == 4:
                                                side = '4'
                                            elif number == 5:
                                                side = '5'
                                            elif number == 6:
                                                side = '6'
                                            entrance = print (Silber, 'are you gonna choose 1, 2, 3, 4, 5 or 6?', sep=', ')
                                            # Give an answer and let's see how lucky you are
                                            while True:
                                                try:
                                                    answer = int(input())
                                                    if answer == number:
                                                        print ('Well done '+Silber+', it is '+side+', I am so proud of you kiddo haha.')
                                                        break
                                                    # Show 'error' of integers other than the dice number        
                                                    elif 0 >= answer or answer > 6:
                                                        print ("ERROR: Silly goosberry! A dice only has 6 sides!!!")
                                                        print ("Choose a number from 1 to 6, omaghosh!!!")
                                                        continue
                                                    else:
                                                        print ('Ah, nooo... '+Silber+', it is '+side+', such a tragedyyyy!!!')
                                                        break
# I could add more trash here and there but I'm dead as fack now so the code would stay as it is
# Okay, last check and Imma sleep sleep
                                                # Gives a "ValueError" error if you type a letter instead of a number.
                                                except:
                                                    print ("ERROR: Something went wrong. Lil shiet do ya know?")
                                                    print ("Only intergers are allowed!!! Try again!")
                                                    continue
                                            print ("Mah, hope you at least had a lil good time here.")
                                            print ("Take care a lot and have a great day. Much love!")
                                            break
                                        elif ak in n or ak in d:
                                            print ("Oh well, maybe you would like to play Head/Tail game better?")
                                            while True:
# Following by COIN FLIP. I guess OWO (a Discord bot) also has this kind of tossing game. But classified as gambling stuff, lmfao.
                                                sb = input()
                                                if sb in y or sb in s:
                                                    import random
                                                    number = random.randint(1, 2)
                                                    if number == 1:
                                                        side = 'head'
                                                    elif number == 2:
                                                        side = 'tail'
                                                    # Guess head or tail (of a coin) game: Using if/else, while, try/except/finally.
                                                    entrance = print ('Oh, are chu gonna choose head or tail?', sep=', ')
                                                    ans = input()
                                                    if ans == side:
                                                        print ('Luckyyy!!! It is '+side+', you have just won da game yayyy!')
                                                    elif ans != side:
                                                        print ('Uwahhh... It is '+side+' tho... Sadge, you got [Lucky]: -1')
                                                    break
                                                elif sb in n or sb in d:
                                                    print ("Okey, we'll just finish here then.")
                                                    break
                                                else:
                                                    print ("Aghhhhh... You goofy! Type 'yes' or 'no'!!!")
                                                    continue
                                            print ("Wateva, danke für deine Zeit, Sil! Ich hoffe, du hattest Spaß.")
                                            print ("Wünsche dir heute alles Gute!")
                                            print ("Viel Liebe!")
                                            break
                                        else:
# Really wanna scream out loud when I got to this part cuz shiet, I gotta use 'print' to make it looks good
# But Holy Crab, I'm running out of ideas to invent new non-repetitive txts...
                                            print ("Really tho... Wat part of 'Yes/No question' that you don't understand???")
                                            print ("TRY IT AGAINNNNNNN!!!")
                                            continue        
                                    break
                                else:
                                    print ("You forgot something? It is a Yes/No question tho. Try again!")
                                    continue
                        else:
                            print ("Blueberry shiet, type 'yes' or 'no'!")
                            continue
                        break
                elif a != expectedAnswer:
                    print ("Oh, I did not expected that, wateva you are really a wonderful adult!")
                    print ("I'm so glad you're here with me. Wish ya a magical day!")
                    break 
                break
            break
        elif x > 18 and x <= 150:
            print ("Wow, such a gorgeous adult!")
            print ("Love to see you roamming around. Please have a super-duper day!")
            break
        else:
# Alien theory is coming pfft
            print ("Ugh... that is not a human lifespan possible.")
            entrance = print ("Are you an alien? Yes/No:") # print, of course, to print a message
            # while/break/continue (loop stuffs)
            while True:
                k = input()
                if k in y: # 'in' operator: check (for membership) if da 'input' value is either of the items in da list
                    print ("Wat da hell? Please return to your planet!")
                    print ("Just kidding haha. Thanks for your attention, hope you have a sweet day!")
                    break
                elif k in n:
                    print ("Think you can lie? Nah ah, return to your planet!")
                    print ("Lol, nah, that was just a joke. Thanks for being here deer, please have a comfy day!")
                    break
                elif k in yeno:
                    print ("Noice, you dumb shiet do not even know who you are...")
                    print ("Joking joking. Thank you for accompany me. Wish ya a thrilling day!")
                    break
                elif k in s or k in d:
# Sil's typical responses are added to identify him as an extraterrestre xDDDD
# I'm such a facking genius invented this shiet. Lord help me my stomach hurts so much hahahahah
                    print ("Pfft, morgen Deer Moma!")
                    print ("Do ya wanna see a heart?")
                    # Turtle Graphics (draw heart)
                    while True:
                        l = input()
                        if l in y or l in s:
# This parts basically repeats da heart and da list of music (some pop songs) with some modificatoins. And yeah, that's all.
                            import turtle # import turtle library
                            bg = turtle.Screen()
                            bg.bgcolor("light yellow")
                            bg.title ("Sil thing")
                            pen = turtle.Turtle()
                            def curve(): # Use[def x():---x()] to define a function (seems useful but still)
                                for k in range (200):
                                    pen.right (1)
                                    pen.forward (1)
                            def heart():
                                pen.fillcolor ('lavander')
                                pen.begin_fill()
                                pen.left (140)
                                pen.forward (133)
                                curve()
                                pen.forward (112)
                                pen.end_fill()
                            def txt():
                                pen.up()
                                pen.setpos (-68, 95)
                                pen.down()
                                pen.color ('light blue') # Now, lemme add a bit of depression into your life
                                pen.write ("tan(x^2+y^2)=1", font=("Mathematica6", 12, "cursive"))
                                heart() # Dat is da function of "Work smart, not hard!" lol
                                txt()
                                pen.ht()
                            break
                        elif l in n or l in d:
                            print ("Okay, I do not wanna give ya a heart either...")
                            print ("Maybe some nice melodies instead?")
                            while True:
                                ck = input()
                                if ck in y or ck in s:
                                    print ("There are three options tho. Choose one please.")
                                    print ("1. Deliah [Mikolas Josef & Mark Neve]")
                                    print ("2. 3 Sum [Mark Dohner]")
                                    print ("3. Yes, I am a mess [AJR]")
                                    while True:
                                        ck1 = input()
                                        # Open link using webbrowser commmand
                                        if ck1 in one:
                                            import webbrowser
                                            webbrowser.open ("https://open.spotify.com/embed/track/60O0CjviBowszlKb9R4Xjm?utm_source=generator")
                                            break
                                        elif ck1 in two:
                                            import webbrowser
                                            webbrowser.open ("https://open.spotify.com/embed/track/0QWe786CWm4PVKRdaehQoB?utm_source=generator")
                                            break
                                        elif ck1 in three:
                                            import webbrowser
                                            webbrowser.open ("https://open.spotify.com/embed/track/4Yrt54xR4T8PPOZ7yf9kyT?utm_source=generator")
                                            break
                                        else:
                                            print ("You have a serious problem tho. Please choose an option from 1 to 3!")
                                        continue
                                    break
                                elif ck in n or ck in d:
                                    print ("Oh, maybe the next time then. Wish ya a great day!")
                                    break
                                else:
                                    print ("Blueberry shiet, type 'yes' or 'no'!")
                                    continue
                            break
                        else:
                            print ("You stoopid, it is a Yes/No question! Type 'yes' or 'no'!!!")
                            continue
                    print ("Thank you so much for spending time with me. Take care, have a terrific day and see ya around!!!")
                    break
                else:
                    print ("You illiterate shiet. Type 'yes' or 'no'!")
                    continue
# Feels so good, here comes the very last lines.
        break
    except ValueError:
        print ("Oh well, variable is not defined sweetie.")
        print ("Means only intergers are allowed. Type a number please!")

# Finally... shiet is killing me ngl, I should have mastered on shiet after all of this lol
# Again, HAPPY BIRTHDAY late and yep, enjoy your time. Work hard but don't be stressed so much, you can do everything good anyways.