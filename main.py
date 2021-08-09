import sys
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon
from process import Searched


class HomePage(QDialog):
    def __init__(self):
        super(HomePage,self).__init__()
        loadUi("HomePage.ui", self)
        self.SearchButton.clicked.connect(self.CheckSearch)

    
    def CheckSearch(self):
        if self.InputSearch.text() == "":
            self.Warning.setText("Please Enter Job")
        else:
            self.Warning.setText("")
            self.SearchButton.clicked.connect(self.Searched1)
            self.SearchButton.clicked.connect(self.GoToResultsPage)

    def GoToResultsPage(self):
        Rp = ResultsPage(self.Company_name,self.location,self.job_title,self.career_level,self.date_posted,self.links,self.NumberOfResults)
        widget.addWidget(Rp)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def Searched1(self):
        text = self.InputSearch.text()
        self.Company_name,self.location,self.job_title,self.career_level,self.date_posted,self.links,self.NumberOfResults = Searched(text)
        

class ResultsPage(QDialog):
    def __init__(self,company_name,location,job_title,career_level,date_posted,links,NumberOfResults):
        super(ResultsPage,self).__init__()
        loadUi("ResultsPage.ui", self)
        
        self.company_name = company_name
        self.location = location
        self.job_title = job_title
        self.career_level = career_level
        self.date_posted = date_posted
        self.links = links
        self.NumberOfResults = NumberOfResults
        
        self.ResultsCount.setText(f"Showing: {self.NumberOfResults}")
        
        self.resultLables = [self.FirstResult_0,self.FirstResult_1,self.FirstResult_2,self.FirstResult_3,self.FirstResult_4,self.FirstResult_5,self.FirstResult_6,self.FirstResult_7
                                        ,self.FirstResult_8,self.FirstResult_9,self.FirstResult_10,self.FirstResult_11,self.FirstResult_12,self.FirstResult_13,self.FirstResult_14,self.FirstResult_15
                                        ,self.FirstResult_16,self.FirstResult_17,self.FirstResult_18,self.FirstResult_19,self.FirstResult_20,self.FirstResult_21,self.FirstResult_22,self.FirstResult_23
                                        ,self.FirstResult_24]

        
        i = 0
        for count  in range(len(self.company_name)):
            self.resultLables[count].setOpenExternalLinks(True)
            link = self.links[i]
            self.resultLables[count].setText(f"<a href=\"https://www.akhtaboot.com/{link}\">Job Description Page</a> <br> <br>"+"Company: "+self.company_name[i]
                                                    +"<br> <br>\nLocation: "+self.location[i]+"<br> <br>\nJob: "+self.job_title[i]+"<br> <br>\nJob Career: "
                                                    +self.career_level[i]+"<br><br>\n\nDate Posted"+self.date_posted[i][1])
            i+=1
        

        for count in range(len(self.resultLables)):
            if self.resultLables[count].text() == "":
                self.resultLables[count].hide()   

        self.company_name.clear()
        self.location.clear()
        self.job_title.clear()
        self.career_level.clear()
        self.date_posted.clear()

        self.Backbutton.clicked.connect(self.BackToHome)

    def BackToHome(self):
        print("cleared")
        home = HomePage()
        widget.addWidget(home)
        for count  in range(len(self.company_name)):
            self.resultLables[count].clear()
            
        widget.setCurrentIndex(widget.currentIndex()+1)



if __name__ == '__main__':
    app= QApplication(sys.argv)
    mainWindow =HomePage()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainWindow)
    widget.setWindowTitle("Job Finder")
    widget.setWindowIcon(QIcon('find.png'))
    widget.setFixedHeight(800)
    widget.setFixedWidth(500)
    widget.show()
    app.exec_()
