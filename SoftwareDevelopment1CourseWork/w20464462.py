# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w20464462
# Date: 11/11/2023

from graphics import *   

file = open("ResultsFile.txt", "w")   #creates or wipes text file to write into
fileRead = open("ResultsFile.txt", "r")   #allows the text file to be read from

allScores = []   # Global variable that will keep a record of all valid scores entered

outcomes = {"[120, 0, 0]": "Progress",
             "[100, 20, 0]": "Progress(module trailer)",
             "[100, 0, 20]": "Progress(module trailer)",
            "[80, 40, 0]": "Do not Progress – module retriever",
            "[80, 20, 20]": "Do not Progress – module retriever",
            "[80, 0, 40]": "Do not Progress – module retriever",
            "[60, 60, 0]": "Do not Progress – module retriever",
            "[60, 40, 20]": "Do not Progress – module retriever",
            "[60, 20, 40]": "Do not Progress – module retriever",
            "[60, 0, 60]": "Do not Progress – module retriever",
            "[40, 80, 0]": "Do not Progress – module retriever",
            "[40, 60, 20]": "Do not Progress – module retriever",
            "[40, 40, 40]": "Do not Progress – module retriever",
            "[40, 20, 60]": "Do not Progress – module retriever",
            "[40, 0, 80]": "Excluded",
            "[20, 100, 0]": "Do not Progress – module retriever",
            "[20, 80, 20]": "Do not Progress – module retriever",
            "[20, 60, 40]": "Do not Progress – module retriever",
            "[20, 40, 60]": "Do not Progress – module retriever",
            "[20, 20, 80]": "Excluded",
            "[20, 0, 100]": "Excluded",
            "[0, 120, 0]": "Do not Progress – module retriever",
            "[0, 100, 20]": "Do not Progress – module retriever",
            "[0, 80, 40]": "Do not Progress – module retriever",
            "[0, 60, 60]": "Do not Progress – module retriever",
            "[0, 40, 80]": "Excluded",
            "[0, 20, 100]": "Excluded",
            "[0, 0, 120]": "Excluded"}   # a dictionary where the keys are all possible credits and the values are all progression outcomes. Created so I can compare the credit scores entered to keys and output the value(the progression outcomes).

def menu(): 
    menuQuit = False   # allows the code to loop until 'q' is entered for menuA where the program ends. 
    while menuQuit != True:
        menuA = input("""Would you like to enter another set of data?
Enter 'y' for yes or 'q' to quit and view results: """)    
        print("")
        menuA = menuA.lower()   # converts any character entered to lower case making the program more user friendly
        if menuA == 'y':
            scores()   # calls scores function
        elif menuA == 'q':   # when q is entered the program should display the scores entered, hisotgram and then shut down
            print("Part 2:")
            for i in range(len(allScores)):
                print(str(allScores[i][3]), "- " +str(allScores[i][0])+", " +str(allScores[i][1])+", " + str(allScores[i][2]))   # displays the data inputted in the same format as the example in the coursework doc
            WriteTextFile()   # calls function to input all data entered into text file
            file.close()   # closes the file so the changes save so that it can be read from
            drawHistogram()   # calls function to draw histogram
            ReadTextFile()   # calls function to read from text file the scores inputted them and display them in python
            print("")
            print("Thank you for using my program. Goodbye!")
            menuQuit = True   # sets menuQuit to True so the main program loop stops
        else:   # if any other key is pressed other than 'y' or 'q' the program displays an error message and then loops back to ask for another input instead of crashing.
            print("Invalid Choice.")
            print("")
            
def scores():
    inRange = False   
    score = []   # empty list created to store the current scores being entered
    while inRange != True:   # if the values entered are valid inputs the code will continue. If the values entered are not valid the program will break out of current loop and go back to menu() loop.
        passCredit = creditP()   # passCredit is set to the value returned from function creditP().
        if passCredit == 1:
            break   # if passCredit is 1 this means in the function creditP() it was discovered that the value entered by user was invalid so the function returned 1 so the program can break out the loop and go back to menu() loop.
        else:
            pass
        deferCredit = creditD()
        if deferCredit == 1:   # same as what happens with passCredit except for it is with deferCredit
            break
        else:
            pass
        failCredit = creditF()
        if failCredit == 1:   # same as what happens with passCredit except for it is with failCredit
            break
        else:
            inRange = True   
        if passCredit + deferCredit + failCredit == 120:   # checks if the data entered adds up to a total of 120 otherwise incorrect data was inputted.
            score.append(passCredit)# appends the credits entered to the list score
            score.append(deferCredit)
            score.append(failCredit)
            score.append(outcomes.get(str(score)))   # uses the get() method for dictionary to get the corresponding the value associated with the key that is the same as the credits stored in score
            allScores.append(score)   # appends the score and outcomes to list allScores(nested list)
            print(score[3])   # print the element at index 3 which is the progression outcome.
            print("")
        else:
            print("Total incorrect.")
            print("")
              
def creditP():
    passCredit = input("Enter your total PASS credits: ")   # asks user to enter pass credits.
    try:
        passCredit = int(passCredit)   # checks if the user entered an integer.
    except ValueError:
        print("Integer required.")   # if the user entered a non-integer program will display error message and this function will return 1. 
        print("")
        return 1
    if passCredit == 0 or passCredit == 20 or passCredit == 40 or passCredit == 60 or passCredit == 80 or passCredit == 100 or passCredit == 120 :   # This conditional statement checks if the value entered by user is within the accepted range.
        return passCredit    # returns the value entered by user
    else:
        print("Out of range.")   # If the value isn't in the accepted range and error message is displayed and the program returns 1.
        print("")
        return 1    

def creditD():
    deferCredit = input("Enter your total DEFER credits: ")   # same as creditP except its for defer credits
    try:
        deferCredit = int(deferCredit)
    except ValueError:
         print("Integer required.")
         print("")
         return 1
    if deferCredit == 0 or deferCredit == 20 or deferCredit == 40 or deferCredit == 60 or deferCredit == 80 or deferCredit == 100 or deferCredit == 120 :
        return deferCredit
    else:
        print("Out of range.")
        print("")
        return 1

def creditF():
    failCredit = input("Enter your total FAIL credits: ")   # same as creditP except its for fail credits
    try:
        failCredit = int(failCredit)
    except ValueError:
        print("Integer required.")
        print("")
        return 1
    if failCredit == 0 or failCredit == 20 or failCredit == 40 or failCredit == 60 or failCredit == 80 or failCredit == 100 or failCredit == 120 :
        return failCredit
    else:
        print("Out of range.")
        print("")
        return 1            

def drawHistogram():
    win = GraphWin("Histogram", 1200, 750)   # window size
    win.setBackground("gray90")   # background colour
    
    header = Text(Point(250,50), "Histogram Results")   # coordinates and text to mirror demo
    header.setSize(25)   # font size
    header.draw(win)   # actually displays text in the window
    
    numbOfOutcomes = Text(Point(300,700), f"{len(allScores)} Outcomes in total.")   # uses f string to print number of outcomes entered
    numbOfOutcomes.setSize(25)
    numbOfOutcomes.draw(win)

    line = Rectangle(Point(50,600), Point(1150,600))   # the line which acts as the base for the histograms
    line.draw(win)
    
    histogramProgress = Text(Point(200,625), "Progressed")   # name on the x axis to show which bar in the histogram represents which outcome
    histogramProgress.setSize(20)
    histogramProgress.draw(win)
    histogramProgressBar = Rectangle(Point(100,600), Point(300,(600 - HistogramSizeProgressed())))   # sets the size of the histogram by minusing the amount found in the function HistogramSizeProgressed() from 600 which is where the line is.
    histogramProgressBar.setFill("chartreuse3")
    histogramProgressBar.setOutline("black")
    histogramProgressBar.draw(win)
    histogramProgressNumber = Text(Point(200,(550 - HistogramSizeProgressed())), HistogramProgressNumber())   # to display the number of students (calculated by the function HistogramProgressNumber()) with this outcome above the bar. to display it above the bar i subtracted the same amount found for histogram bar size from a slightly higher coordinate to ensure the number is always above the histogram bar
    histogramProgressNumber.setSize(20)
    histogramProgressNumber.draw(win)

    histogramTrailer = Text(Point(450,625), "Trailer")   # same as above
    histogramTrailer.setSize(20)
    histogramTrailer.draw(win)
    histogramTrailerBar = Rectangle(Point(350,600), Point(550,(600 - HistogramSizeTrailer())))
    histogramTrailerBar.setFill("dark cyan")
    histogramTrailerBar.setOutline("black")
    histogramTrailerBar.draw(win)
    histogramTrailerNumber = Text(Point(450,(550 - HistogramSizeTrailer())), HistogramTrailerNumber())
    histogramTrailerNumber.setSize(20)
    histogramTrailerNumber.draw(win)

    histogramRetreiver = Text(Point(700,625), "Retreiver")    # same as above
    histogramRetreiver.setSize(20)
    histogramRetreiver.draw(win)
    histogramRetreiverBar = Rectangle(Point(600,600), Point(800,(600 - HistogramSizeRetreiver())))
    histogramRetreiverBar.setFill("forest green")
    histogramRetreiverBar.setOutline("black")
    histogramRetreiverBar.draw(win)
    histogramRetreiverNumber = Text(Point(700,(550 - HistogramSizeRetreiver())), HistogramRetreiverNumber())
    histogramRetreiverNumber.setSize(20)
    histogramRetreiverNumber.draw(win)

    histogramExcluded = Text(Point(950,625), "Excluded")   # same as above
    histogramExcluded.setSize(20)
    histogramExcluded.draw(win)
    histogramExcludedBar = Rectangle(Point(850,600), Point(1050,(600 - HistogramSizeExcluded())))
    histogramExcludedBar.setFill("maroon")
    histogramExcludedBar.setOutline("black")
    histogramExcludedBar.draw(win)
    histogramExcludedNumber = Text(Point(950,(550 - HistogramSizeExcluded())), HistogramExcludedNumber())
    histogramExcludedNumber.setSize(20)
    histogramExcludedNumber.draw(win)

def HistogramSizeProgressed():
    progressed = 0
    for i in range(len(allScores)):   # iterates through the nested list allScores and for every outcome that is 'Progress' increases histogram size
        if allScores[i][3] == "Progress":
            progressed = progressed + (450/ len(allScores))   # uses this formula so that the histogram bar is limited to a max size that it can never exceed ensuring the histogram is accurate and not broken when no or lots of data has been entered.
        else:
            pass
    return progressed

def HistogramProgressNumber():
    students = 0
    for i  in range(len(allScores)):
        if allScores[i][3] == "Progress":   # keeps track of number of students who got the outcome 'Progress' to display on the distogram
            students = students + 1
        else:
            pass
    return students

def HistogramSizeTrailer():   # same as above
    trailer = 0
    for i  in range(len(allScores)):
        if allScores[i][3] == "Progress(module trailer)":
            trailer = trailer + (450/ len(allScores))
        else:
            pass
    return trailer

def HistogramTrailerNumber():   # same as above
    students = 0
    for i  in range(len(allScores)):
        if allScores[i][3] == "Progress(module trailer)":
            students = students + 1
        else:
            pass
    return students

def HistogramSizeRetreiver():   # same as above
    retriever = 0
    for i  in range(len(allScores)):
        if allScores[i][3] == "Do not Progress – module retriever":
            retriever = retriever + (450/ len(allScores))
        else:
            pass
    return retriever

def HistogramRetreiverNumber():    # same as above
    students = 0
    for i  in range(len(allScores)):
        if allScores[i][3] == "Do not Progress – module retriever":
            students = students + 1
        else:
            pass
    return students

def HistogramSizeExcluded():    # same as above
    excluded = 0
    for i  in range(len(allScores)):
        if allScores[i][3] == "Excluded":
            excluded = excluded + (450/ len(allScores))
        else:
            pass
    return excluded

def HistogramExcludedNumber():   # same as above
    students = 0
    for i  in range(len(allScores)):
        if allScores[i][3] == "Excluded":
            students = students + 1
        else:
            pass
    return students

def WriteTextFile(): # I used a tutorial by: Le MasterTech titled: How to Write to a text .txt file in Python! Processing Lists, and Outputting Data!
    for i in range(len(allScores)):
        entry = allScores[i][3] + " - "  + str(allScores[i][0]) + ", " +str(allScores[i][1]) + ", " + str(allScores[i][2]) + "\n"   # inputs into text file so that the outcome is displayed first followed by the test scores to mirror example in coursework doc
        file.write(entry)
        
def ReadTextFile(): # I used a tutorial by: Le MasterTech titled: How to Read from a text .txt file in Python! Pulling in data and filtering and modifying the info!
    modified = []   
    results = ""
    print("")
    print("Part 3:")
    read = fileRead.readlines()   # returns as a list
    for line in read:
        if line[-1] == "\n":
            modified.append(line[:-1])   # as python sees \n as a character this removes it from the list for each element
        else:
            modified.append(line)   # final element won't have \n so prevents code from bugging out 
    for i in range(len(modified)):
        results = results + str(modified[i]) + "\n"   # converts it to the format shown as an example in coursework doc  
    print(results)   # prints what is read from the text file

         
menu()
