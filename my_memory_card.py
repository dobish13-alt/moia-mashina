
import random
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel , QButtonGroup)
from random import *
class ques():
    def __init__(self,question1 , right_answer_text  , wrong1_text, wrong2_text, wrong3_text):
        self.question2 = question1
        self.right_answer1 = right_answer_text
        self.wrong1 = wrong1_text
        self.wrong2 = wrong2_text
        self.wrong3 = wrong3_text
app = QApplication([])

my_win = QWidget()
my_win.resize(400,200)
my_win.setWindowTitle('Тест на знание Counter - Strike')
 
question = QLabel('Самый сложный вопрос в мире!')
answer = QPushButton('Ответить')
Radiogroupbox = QGroupBox('Варианты ответов')
answer1 = QRadioButton()
answer2 = QRadioButton()
answer3 = QRadioButton()
answer4 = QRadioButton()
QGroup = QButtonGroup()
QGroup.addButton(answer1)
QGroup.addButton(answer2)
QGroup.addButton(answer3)
QGroup.addButton(answer4)
layoutV1 = QVBoxLayout()

layoutV1.addWidget(answer1)
layoutV1.addWidget(answer2)

layoutV2 = QVBoxLayout()

layoutV2.addWidget(answer3)
layoutV2.addWidget(answer4)

layout = QHBoxLayout()
layout.addLayout(layoutV1)
layout.addLayout(layoutV2)
Radiogroupbox.setLayout(layout)

ansgroupbox = QGroupBox('Результаты теста')
is_coreect = QLabel('правильно/неправильно')
answer_text = QLabel('Правильный ответ')

Layout_ans = QVBoxLayout()
Layout_ans.addWidget(is_coreect, alignment = (Qt.AlignLeft|Qt.AlignTop))
Layout_ans.addWidget(answer_text, alignment = Qt.AlignCenter)
ansgroupbox.setLayout(Layout_ans)




layout_main = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH1.addWidget(question, alignment = (Qt.AlignHCenter|Qt.AlignVCenter))
layoutH2.addWidget(Radiogroupbox)
layoutH2.addWidget(ansgroupbox)
layoutH3.addStretch(1)
layoutH3.addWidget(answer, stretch=3)
layoutH3.addStretch(1)













layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)
layout_main.setSpacing(20)



def show_result():
    Radiogroupbox.hide()
    ansgroupbox.show()
    answer.setText('Следующий вопрос')
def show_question():
    ansgroupbox.hide()
    Radiogroupbox.show()
    answer.setText('Ответить')
    QGroup.setExclusive(False)
    answer1.setChecked(False)
    answer2.setChecked(False)
    answer3.setChecked(False)
    answer4.setChecked(False)
    QGroup.setExclusive(True)



an = [answer1,answer2,answer3,answer4]
ansgroupbox.hide()
def ask(q:ques):
    shuffle(an)
    an[0].setText(q.right_answer1)
    an[1].setText(q.wrong1)
    an[2].setText(q.wrong2)
    an[3].setText(q.wrong3)
    answer_text.setText(q.right_answer1)
    question.setText(q.question2)
    show_question()

def check_answer():
    if an[0].isChecked():
        show_correct('Правильно!')
        my_win.score += 1
    elif (an[1].isChecked() or an[2].isChecked() or an[3].isChecked()):
        show_correct('Неверно!')
    print('Статистика')
    print(' - Верно отвечено:', my_win.score)
    print('- Общее количество вопросов:', my_win.total)
    print('Рейтинг -', my_win.score / my_win.total * 100,'%')
def show_correct(res):
     is_coreect.setText(res)
     show_result()

def next_question():
    my_win.total += 1
    cur_question = randint(0, len(questions_list) - 1)

    ask(questions_list[cur_question])
    print('Статистика')
    print(' - Верно отвечено:', my_win.score)
    print('- Общее количество вопросов:', my_win.total)
    
def click_ok():
    if answer.text() == 'Ответить':
        check_answer()
    else:
        next_question()
answer.clicked.connect(click_ok)


questions_list = []
questions_list.append(ques('В каком году вышла кс2?','2023',
    '2021', '2022', '2024')

)
questions_list.append(
    ques('В каком году вышла ксго?',
    '2012',
    '2014','2016','2013'))
questions_list.append(
    ques('Победитель 1 - го мейджора в кс го?',
    'fnatic',
    'NIP','VeryGames','LDLC'))
questions_list.append(
    ques('топ 1 хлтв(ксго) 2018?',
    's1mple',
    'dev1ce','niko','guardian'))   
questions_list.append(
    ques('MVP ESL ONE COLOGNE 2016?',
    'coldzera',
    's1mple','fallen','guardian'))   
questions_list.append(
    ques('Первый трофей s1mple - а?',
    'ESL ONE NEW YORK 2016',
    'ESL ONE KATOWICE 2016','MLG COLUMBUS 2016','ESL PRO LEAGUE SEASON 3 FINALS'))
questions_list.append(
    ques('Чемпион DREAMHACK OPEN CLUJ - NAPOCA 2015?',
    'Envy',
    'NAVI','G2','Fnatic'))   
questions_list.append(
    ques('В каком году прошел ELEAGUE BOSTON MAJOR?',
    '2018',
    '2019','2021','2017'))
questions_list.append(
    ques('Кто не прошел в play - off PGL MAJOR STOCKHOLM 2021?',
    'Faze clan',
    'NAVI','Gambit Esports','NIP'))   
      
   







my_win.setLayout(layout_main)
my_win.total = 0
my_win.score = 0
next_question()
my_win.show()
app.exec_()


#создай приложение для запоминания информации