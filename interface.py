import sys
import math
from ternary_search_tree import*
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QListWidgetItem, QMessageBox, QDialog, QScrollArea
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5 import QtCore

global tree
global conditionsdict
global datafilename
global movies
global fword
global freqdict
global ntree
global recmovies
global rectext

rectext = ''
recmovies = []
freqdict = {}
fword = ""
movies = []
tree = {'Root': None, 'Left': None, 'Middle': None, 'Right': None, 'Value': None, 'Data': None}
ntree = {'Root': None, 'Left': None, 'Middle': None, 'Right': None, 'Value': None, 'Data': None}
conditionsdict = {'year': 1, 'femalelead': 2, 'malelead': 3, 'genre': 4, 'rating': 5}
datafilename = r"D:\Salman\University\Semester 2\Data Structures & Algorithms\Project\Code\movielist.csv"

#Creating a class for each window that is to be displayed in the interface

class WelcomeWindow(QDialog):
    def __init__(self):
        super(WelcomeWindow, self).__init__()
        loadUi('welcomewindow.ui', self)
        self.continueButton.clicked.connect(self.gotoConditionWindow)   #Accesses the button, tells what to do when button clicked (Moves to the gotoConditionWindow function)
    
    def gotoConditionWindow(self):
        widget.setCurrentIndex(widget.currentIndex()+1)     #Moves to the next screen

class ConditionWindow(QDialog):
    def __init__(self):
        super(ConditionWindow, self).__init__()
        loadUi('conditionwindow.ui', self)
        self.genreButton.clicked.connect(self.gotoGenreWindow)
        self.yearButton.clicked.connect(self.gotoYearWindow)
        self.male_leadButton.clicked.connect(self.gotoMaleLeadWindow)
        self.female_leadButton.clicked.connect(self.gotoFemaleLeadWindow)
        self.allButton.clicked.connect(self.all)
    
    def gotoGenreWindow(self):
        widget.setCurrentIndex(widget.currentIndex()+1)     #Moves to the genre screen
        
    def gotoYearWindow(self):
        widget.setCurrentIndex(widget.currentIndex()+2)     #Moves to the year screen
        
    def gotoMaleLeadWindow(self):
        widget.setCurrentIndex(widget.currentIndex()+3)     #Moves to the malelead screen
        
    def gotoFemaleLeadWindow(self):
        widget.setCurrentIndex(widget.currentIndex()+4)     #Moves to the femalelead screen

    def all(self):
        # If a condition of all is selected, the function makes a ternary search tree using all the movies present in the csv file and moves to the search screen
        check = fileitems(datafilename, 'all', None, tree, conditionsdict)
        print(tree)
        widget.setCurrentIndex(widget.currentIndex()+5)

class GenreWindow(QDialog):
    def __init__(self):
        super(GenreWindow, self).__init__()
        loadUi('genrewindow.ui', self)
        self.romanceButton.clicked.connect(self.romance)
        self.actionButton.clicked.connect(self.action)
        self.dramaButton.clicked.connect(self.drama)
        self.comedyButton.clicked.connect(self.comedy)
        self.sportsButton.clicked.connect(self.sports)
        self.horrorButton.clicked.connect(self.horror)
        self.backButton.clicked.connect(self.back)

    #Creating ternary search tree depending on the genre selected

    def romance(self):
        check = fileitems(datafilename, 'genre', 'Romance', tree, conditionsdict)
        print(tree)
        if not check:
            print("Does not exist")
        else:
            widget.setCurrentIndex(widget.currentIndex()+4)

    def action(self):
        check = fileitems(datafilename, 'genre', 'Action', tree, conditionsdict)
        print(tree)
        if not check:
            print("Does not exist")
        else:
            widget.setCurrentIndex(widget.currentIndex()+4)

    def drama(self):
        check = fileitems(datafilename, 'genre', 'Drama', tree, conditionsdict)
        print(tree)
        if not check:
            print("Does not exist")
        else:
            widget.setCurrentIndex(widget.currentIndex()+4)
    
    def comedy(self):
        check = fileitems(datafilename, 'genre', 'Comedy', tree, conditionsdict)
        print(tree)
        if not check:
            print("Does not exist")
        else:
            widget.setCurrentIndex(widget.currentIndex()+4)
    
    def sports(self):
        check = fileitems(datafilename, 'genre', 'Sports', tree, conditionsdict)
        print(tree)
        if not check:
            print("Does not exist")
        else:
            widget.setCurrentIndex(widget.currentIndex()+4)

    def horror(self):
        check = fileitems(datafilename, 'genre', 'Horror', tree, conditionsdict)
        print(tree)
        if not check:
            print("Does not exist")
        else:
            widget.setCurrentIndex(widget.currentIndex()+4)

    def back(self):
        widget.setCurrentIndex(widget.currentIndex()-1)     #Moves to the conditions screen

class YearWindow(QDialog):
    def __init__(self):
        super(YearWindow, self).__init__()
        loadUi('yearwindow.ui', self)
        self.goButton.clicked.connect(self.year)
        self.backButton.clicked.connect(self.back)

    def year(self):
        #Creates ternary search tree depending on the year chosen
        content = self.comboBox.currentText()
        check = fileitems(datafilename, 'year', content, tree, conditionsdict)
        print(tree)
        if not check:
            print("Does not exist")
        else:
            widget.setCurrentIndex(widget.currentIndex()+3)
        
    def back(self):
        widget.setCurrentIndex(widget.currentIndex()-2)     #Moves to the conditions screen

class MaleLeadWindow(QDialog):
    def __init__(self):
        super(MaleLeadWindow, self).__init__()
        loadUi('maleleadwindow.ui', self)
        self.goButton.clicked.connect(self.malelead)
        self.backButton.clicked.connect(self.back)

    def malelead(self):
        #Creates ternary search tree depending on the male actor chosen
        content = self.comboBox.currentText()
        check = fileitems(datafilename, 'malelead', content, tree, conditionsdict)
        print(tree)
        if not check:
            print("Does not exist")
        else:
            widget.setCurrentIndex(widget.currentIndex()+2)

    def back(self):
        widget.setCurrentIndex(widget.currentIndex()-3)     #Moves to the conditions screen

class FemaleLeadWindow(QDialog):
    def __init__(self):
        super(FemaleLeadWindow, self).__init__()
        loadUi('femaleleadwindow.ui', self)
        self.goButton.clicked.connect(self.femalelead)
        self.backButton.clicked.connect(self.back)

    def femalelead(self):
        #Creates ternary search tree depending on the female actress chosen
        content = self.comboBox.currentText()
        check = fileitems(datafilename, 'femalelead', content, tree, conditionsdict)
        print(tree)
        if not check:
            print("Does not exist")
        else:
            widget.setCurrentIndex(widget.currentIndex()+1)

    def back(self):
        widget.setCurrentIndex(widget.currentIndex()-4)     #Moves to the conditions screen

class SearchWindow(QDialog):
    def __init__(self):
        super(SearchWindow, self).__init__()
        loadUi('searchwindow.ui', self)
        self.searchButton.clicked.connect(self.search)
        self.backButton.clicked.connect(self.back)

    def search(self):
        #Uses the search function of ternary search tree to find all the movies starting from the word input by the user
        global movies
        global fword
        content = self.lineEdit.text()
        fword = content
        movies = search(tree, content)
        # print(movies)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def back(self):
        global tree
        #Initialises tree to get rid of all values
        tree = {'Root': None, 'Left': None, 'Middle': None, 'Right': None, 'Value': None, 'Data': None}
        self.lineEdit.setText("")
        widget.setCurrentIndex(widget.currentIndex()-5)     #Moves to the conditions screen

class DisplayWindow(QDialog):
    def __init__(self):
        super(DisplayWindow, self).__init__()
        loadUi('displaywindow.ui', self)
        self.backButton.clicked.connect(self.back)
        searchwindow.searchButton.clicked.connect(self.display)

    def display(self):
        #Displays all the movies starting from the word input by the user
        global movies
        global fword
        global freqdict
        self.reclistWidget.clear()
        displaytxt = ""
        print(movies)
        if isinstance(movies, str):
            displaytxt = f" No movie exists in the database starting from '{fword}', try again!"
            self.movielistWidget.addItem(displaytxt)
        else:
            for i in movies:
                displaytxt = f" Movie Name: {i[0]} \n Year of Release: {i[1]} \n Cast: {i[2]} and {i[3]} \n Genre: {i[4]} \n Rating: {i[5]} \n" 
                if i[4] not in freqdict:
                    freqdict[i[4]] = 1
                else:
                    freqdict[i[4]] += 1
                self.movielistWidget.addItem(displaytxt)
        self.recommendationsButton.clicked.connect(self.rec)
        
    def rec(self):
        #If recommendations button clicked displays all movies from the most common genre of the movies shown
        global freqdict
        global movies
        global recmovies
        global rectext
        self.reclistWidget.clear()
        rectext = ''
        recmovies = []

        #Finds most common genre (if no movies displayed, common genre set to all)

        max = -(math.inf)
        maxgenre = 'all'
        if freqdict != {}:
            for x, y in freqdict.items():
                if y>max:
                    max = y
                    maxgenre = x
        headtxt = f" Movie Recommendations from {maxgenre} genre:\n"
        self.recheadLabel.setText(headtxt)
        print(maxgenre)
        print(freqdict)
        print(movies)

        if movies == 'Does not exist':
            fileitems(datafilename, 'all', None, ntree, conditionsdict)
            print(ntree)
            recmovies = []
            search_recursive_names(None, ntree, recmovies)
            print(recmovies)
            for i in recmovies:
                rectext = i[0] + '\n'
                self.reclistWidget.addItem(rectext)
        else:
            fileitems(datafilename, 'genre', maxgenre, ntree, conditionsdict)
            print(ntree)
            recmovies = []
            search_recursive_names(None, ntree, recmovies)
            print(recmovies)
            for i in recmovies:
                if i not in movies:
                    rectext = i[0] + '\n'
                    self.reclistWidget.addItem(rectext)

    def back(self):
        global recmovies
        global freqdict
        freqdict = {}
        global ntree
        rectext = ''
        #Initialises recommendations tree to get rid of previous values
        ntree = {'Root': None, 'Left': None, 'Middle': None, 'Right': None, 'Value': None, 'Data': None}
        recmovies = []
        self.reclistWidget.clear()
        self.movielistWidget.clear()
        self.recheadLabel.setText("")
        widget.setCurrentIndex(widget.currentIndex()-1)     #Moves to the search screen

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()

    welcomewindow = WelcomeWindow()
    conditionwindow = ConditionWindow()
    genrewindow = GenreWindow()
    yearwindow = YearWindow()
    maleleadwindow = MaleLeadWindow()
    femaleleadwindow = FemaleLeadWindow()
    searchwindow = SearchWindow()
    displaywindow = DisplayWindow()

    widget.addWidget(welcomewindow)
    widget.addWidget(conditionwindow)
    widget.addWidget(genrewindow)
    widget.addWidget(yearwindow)
    widget.addWidget(maleleadwindow)
    widget.addWidget(femaleleadwindow)
    widget.addWidget(searchwindow)
    widget.addWidget(displaywindow)
    widget.setFixedHeight(500)
    widget.setFixedWidth(700)
    widget.show()

    sys.exit(app.exec())