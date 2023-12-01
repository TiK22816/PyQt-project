import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTableWidget, \
    QTableWidgetItem, QDialog, QMessageBox
from PyQt5 import QtGui
import sqlite3

class AuthorizationWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('1903172.png'))
        self.setStyleSheet("background-image: url(123.jpg);")
        self.setWindowTitle("Авторизация")
        self.setGeometry(200, 200, 300, 150)
        self.username_label = QLabel("Имя пользовотеля:")
        self.username_label.setStyleSheet("""
                                        QLabel{
                                            font-style: classic;
                                            font-weight: bold;
                                            color: white;
                                            background-color: black;
                                        }
                                        """)
        self.username_input = QLineEdit()
        self.username_input.setStyleSheet("""
                QLineEdit{
                    font-style: classic;
                    font-weight: bold;
                    border: 3px solid white;
                    border-radius: 15px;
                    color: white;
                    background-color: black;
                }
                """)
        self.password_label = QLabel("Пароль:")
        self.password_label.setStyleSheet("""
                                QLabel{
                                    font-style: classic;
                                    font-weight: bold;
                                    color: white;
                                    background-color: black;
                                }
                                """)
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet("""
                        QLineEdit{
                            font-style: classic;
                            font-weight: bold;
                            border: 3px solid white;
                            border-radius: 15px;
                            color: white;
                            background-color: black;
                        }
                        """)

        self.login_button = QPushButton("Войти")
        self.login_button.clicked.connect(self.login)

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        self.setLayout(layout)

        self.login_button.setStyleSheet("""
                QPushButton{
                    font-style: classic;
                    font-weight: bold;
                    border: 3px solid red;
                    border-radius: 15px;
                    color: #1DA1F2;
                    background-color: black;
                }
                """)


        self.status = None
        self.group = None
        self.user_name = None

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        conn = sqlite3.connect('pairs_users.db')
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM users WHERE username='{username}' AND password='{password}'")
        user = cursor.fetchone()
        conn.close()

        if user:
            self.status = user[3]
            self.group = user[4]
            self.user_name = user[1]
            self.accept()
        else:
            err = ErrorWin()
            err.exec()


class ErrorWin(QDialog):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-image: url(123.jpg);")
        self.setWindowIcon(QtGui.QIcon('1903172.png'))
        self.setWindowTitle("Ошибочка вышла")
        self.setFixedSize(333,150)

        self.subject_label = QLabel("Неправильное имя пользователя или пароль!")
        self.subject_label.setStyleSheet("""
                                        QLabel{
                                            font-style: classic;
                                            font-weight: bold;
                                            color: white;
                                            background-color: black;
                                        }
                                        """)

        self.submit_button = QPushButton("Назад")
        self.submit_button.setStyleSheet("""
                        QPushButton{
                            font-style: classic;
                            font-weight: bold;
                            border: 3px solid red;
                            border-radius: 15px;
                            color: #1DA1F2;
                            background-color: black;
                        }
                        """)
        self.submit_button.clicked.connect(self.go_to_login1)

        layout = QVBoxLayout()
        layout.addWidget(self.subject_label)
        layout.addWidget(self.submit_button)
        self.setLayout(layout)

    def go_to_login1(self):
        while True:
            self.close()
            break

class AddPairWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-image: url(123.jpg);")
        self.setWindowIcon(QtGui.QIcon('1903172.png'))

        self.setWindowTitle("Добавить пару")
        self.setGeometry(200, 200, 400, 200)

        self.date_label = QLabel("Дата:")
        self.date_label.setStyleSheet("""
                                                QLabel{
                                                    font-style: classic;
                                                    font-weight: bold;
                                                    color: white;
                                                    background-color: black;
                                                }
                                                """)
        self.date_input = QLineEdit()
        self.date_input.setStyleSheet("""
                        QLineEdit{
                            font-style: classic;
                            font-weight: bold;
                            border: 3px solid white;
                            border-radius: 15px;
                            color: white;
                            background-color: black;
                        }
                        """)



        self.teacher_label = QLabel("Преподаватель:")
        self.teacher_label.setStyleSheet("""
                                                QLabel{
                                                    font-style: classic;
                                                    font-weight: bold;
                                                    color: white;
                                                    background-color: black;
                                                }
                                                """)
        self.teacher_input = QLineEdit()
        self.teacher_input.setStyleSheet("""
                        QLineEdit{
                            font-style: classic;
                            font-weight: bold;
                            border: 3px solid white;
                            border-radius: 15px;
                            color: white;
                            background-color: black;
                        }
                        """)

        self.group_label = QLabel("Группа:")
        self.group_label.setStyleSheet("""
                                                QLabel{
                                                    font-style: classic;
                                                    font-weight: bold;
                                                    color: white;
                                                    background-color: black;
                                                }
                                                """)
        self.group_input = QLineEdit()
        self.group_input.setStyleSheet("""
                        QLineEdit{
                            font-style: classic;
                            font-weight: bold;
                            border: 3px solid white;
                            border-radius: 15px;
                            color: white;
                            background-color: black;
                        }
                        """)
        self.group_input.setStyleSheet("""
                        QLineEdit{
                            font-style: classic;
                            font-weight: bold;
                            border: 3px solid white;
                            border-radius: 15px;
                            color: white;
                            background-color: black;
                        }
                        """)

        self.subject_label = QLabel("Предмет:")
        self.subject_label.setStyleSheet("""
                                                QLabel{
                                                    font-style: classic;
                                                    font-weight: bold;
                                                    color: white;
                                                    background-color: black;
                                                }
                                                """)
        self.subject_input = QLineEdit()
        self.subject_input.setStyleSheet("""
                        QLineEdit{
                            font-style: classic;
                            font-weight: bold;
                            border: 3px solid white;
                            border-radius: 15px;
                            color: white;
                            background-color: black;
                        }
                        """)

        self.submit_button = QPushButton("Добавить пару")
        self.submit_button.setStyleSheet("""
                                QPushButton{
                                    font-style: classic;
                                    font-weight: bold;
                                    border: 3px solid red;
                                    border-radius: 15px;
                                    color: #1DA1F2;
                                    background-color: black;
                                }
                                """)
        self.submit_button.clicked.connect(self.add_pair)

        layout = QVBoxLayout()
        layout.addWidget(self.date_label)
        layout.addWidget(self.date_input)
        layout.addWidget(self.teacher_label)
        layout.addWidget(self.teacher_input)
        layout.addWidget(self.group_label)
        layout.addWidget(self.group_input)
        layout.addWidget(self.subject_label)
        layout.addWidget(self.subject_input)
        layout.addWidget(self.submit_button)
        self.setLayout(layout)

    def add_pair(self):
        date = self.date_input.text()
        teacher = self.teacher_input.text()
        group = self.group_input.text()
        subject = self.subject_input.text()

        conn = sqlite3.connect('pairs_users.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pairs (date, teacher, group_name, subject) VALUES (?, ?, ?, ?)",
                       (date, teacher, group, subject))
        conn.commit()
        conn.close()

        self.close()


class ScheduleWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-image: url(123.jpg);")
        self.setWindowIcon(QtGui.QIcon('1903172.png'))
        self.setWindowTitle("Расписание")
        self.setGeometry(200, 200, 600, 400)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Дата", "Преподаватель", "Группа", "Предмет"])

        self.table.setStyleSheet("""
                                                    QTableWidget{
                                                        font-style: classic;
                                                        font-weight: bold;
                                                        color: white;
                                                        background-color: black;
                                                    }
                                                    """)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)

    def load_schedule(self):
        conn = sqlite3.connect('pairs_users.db')
        cursor = conn.cursor()
        group = authorization_window.group
        if group:
            cursor.execute(f"SELECT * FROM pairs WHERE group_name = '{group}'")
        else:
            cursor.execute(f"SELECT * FROM pairs")
        pairs = cursor.fetchall()
        conn.close()
        self.table.setRowCount(0)  # Clear existing rows

        for row_num, pair in enumerate(pairs):
            self.table.insertRow(row_num)
            for col_num, data in enumerate(pair):
                self.table.setItem(row_num, col_num - 1, QTableWidgetItem(str(data)))


class StudentAssessmentWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-image: url(123.jpg);")
        self.setWindowIcon(QtGui.QIcon('1903172.png'))
        self.setWindowTitle("Оценки учащихся")
        self.setGeometry(200, 200, 600, 400)


        self.assessment_table = QTableWidget()
        self.assessment_table.setColumnCount(4)
        self.assessment_table.setHorizontalHeaderLabels(["Фио студента", "Предмет", "Оценка", "Коментарий"])

        self.assessment_table.setStyleSheet("""
                                            QTableWidget{
                                                font-style: classic;
                                                font-weight: bold;
                                                color: white;
                                                background-color: black;
                                            }
                                            """)

        layout = QVBoxLayout()
        layout.addWidget(self.assessment_table)
        self.setLayout(layout)

    def view_assessments(self):
        conn = sqlite3.connect('pairs_users.db')
        cursor = conn.cursor()

        user_type = authorization_window.status
        if user_type:
            cursor.execute(f"SELECT * FROM assessments WHERE student_name = '{authorization_window.user_name}'")
        else:
            cursor.execute(f"SELECT * FROM assessments")
        assessments = cursor.fetchall()
        conn.close()
        self.assessment_table.setRowCount(0)
        for row_num, assessment in enumerate(assessments):
            self.assessment_table.insertRow(row_num)
            for col_num, data in enumerate(assessment):
                self.assessment_table.setItem(row_num, col_num - 1, QTableWidgetItem(str(data)))







class StudentWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-image: url(123.jpg);")
        self.setWindowIcon(QtGui.QIcon('1903172.png'))
        self.setWindowTitle("Зарегестрировать студента")
        self.setGeometry(200, 200, 600, 400)

        self.setWindowTitle("Регистрация")
        self.setGeometry(200, 200, 300, 150)
        self.group_label = QLabel("Группа:")
        self.group_label.setStyleSheet("""
                                                QLabel{
                                                    font-style: classic;
                                                    font-weight: bold;
                                                    color: white;
                                                    background-color: black;
                                                }
                                                """)
        self.group_input = QLineEdit()
        self.group_input.setStyleSheet("""
                        QLineEdit{
                            font-style: classic;
                            font-weight: bold;
                            border: 3px solid white;
                            border-radius: 15px;
                            color: white;
                            background-color: black;
                        }
                        """)
        self.user_label = QLabel("Логин студента:")
        self.user_label.setStyleSheet("""
                                                QLabel{
                                                    font-style: classic;
                                                    font-weight: bold;
                                                    color: white;
                                                    background-color: black;
                                                }
                                                """)
        self.user_input = QLineEdit()
        self.user_input.setStyleSheet("""
                        QLineEdit{
                            font-style: classic;
                            font-weight: bold;
                            border: 3px solid white;
                            border-radius: 15px;
                            color: white;
                            background-color: black;
                        }
                        """)
        self.passw_label = QLabel("Пароль:")
        self.passw_label.setStyleSheet("""
                                                QLabel{
                                                    font-style: classic;
                                                    font-weight: bold;
                                                    color: white;
                                                    background-color: black;
                                                }
                                                """)
        self.passw_input = QLineEdit()
        self.passw_input.setStyleSheet("""
                        QLineEdit{
                            font-style: classic;
                            font-weight: bold;
                            border: 3px solid white;
                            border-radius: 15px;
                            color: white;
                            background-color: black;
                        }
                        """)
        self.passw_input.setEchoMode(QLineEdit.Password)

        self.reg_button = QPushButton("Зарегестрировать")
        self.reg_button.setStyleSheet("""
                                QPushButton{
                                    font-style: classic;
                                    font-weight: bold;
                                    border: 3px solid red;
                                    border-radius: 15px;
                                    color: #1DA1F2;
                                    background-color: black;
                                }
                                """)
        self.reg_button.clicked.connect(self.register)

        layout = QVBoxLayout()
        layout.addWidget(self.group_label)
        layout.addWidget(self.group_input)
        layout.addWidget(self.user_label)
        layout.addWidget(self.user_input)
        layout.addWidget(self.passw_label)
        layout.addWidget(self.passw_input)
        layout.addWidget(self.reg_button)
        self.setLayout(layout)

        layout = QVBoxLayout()
        self.setLayout(layout)

    def register(self):
        group = self.group_input.text()
        username = self.user_input.text()
        password = self.passw_input.text()
        usertype = "student"

        conn = sqlite3.connect('pairs_users.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password, user_type, group_name) VALUES (?, ?, ?, ?)",
                       (username, password, usertype, group))
        conn.commit()
        conn.close()

        self.close()


class StudentdeleteWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-image: url(123.jpg);")
        self.setWindowIcon(QtGui.QIcon('1903172.png'))
        self.setWindowTitle("Удалить студента")
        self.setGeometry(200, 200, 600, 400)

        self.setWindowTitle("Удаление")
        self.setGeometry(200, 200, 300, 150)
        self.user_label = QLabel("ID студента:")
        self.user_label.setStyleSheet("""
                                                QLabel{
                                                    font-style: classic;
                                                    font-weight: bold;
                                                    color: white;
                                                    background-color: black;
                                                }
                                                """)
        self.user_input = QLineEdit()
        self.user_input.setStyleSheet("""
                        QLineEdit{
                            font-style: classic;
                            font-weight: bold;
                            border: 3px solid white;
                            border-radius: 15px;
                            color: white;
                            background-color: black;
                        }
                        """)
        self.del_button = QPushButton("Удалить")
        self.del_button.setStyleSheet("""
                                QPushButton{
                                    font-style: classic;
                                    font-weight: bold;
                                    border: 3px solid red;
                                    border-radius: 15px;
                                    color: #1DA1F2;
                                    background-color: black;
                                }
                                """)
        self.del_button.clicked.connect(self.delete)

        layout = QVBoxLayout()
        layout.addWidget(self.user_label)
        layout.addWidget(self.user_input)
        layout.addWidget(self.del_button)
        self.setLayout(layout)

        layout = QVBoxLayout()
        self.setLayout(layout)

    def delete(self):
        id = self.user_input.text()
        conn = sqlite3.connect('pairs_users.db')
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM users WHERE id = '{id}'")
        conn.commit()
        conn.close()

        self.close()

class DeletePair(QDialog):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-image: url(123.jpg);")
        self.setWindowIcon(QtGui.QIcon('1903172.png'))
        self.setWindowTitle("Удалить пару")
        self.setGeometry(200, 200, 600, 400)

        self.setWindowTitle("Удаление")
        self.setGeometry(200, 200, 300, 150)
        self.user_label = QLabel("ID пары:")
        self.user_label.setStyleSheet("""
                                                QLabel{
                                                    font-style: classic;
                                                    font-weight: bold;
                                                    color: white;
                                                    background-color: black;
                                                }
                                                """)
        self.user_input = QLineEdit()
        self.user_input.setStyleSheet("""
                        QLineEdit{
                            font-style: classic;
                            font-weight: bold;
                            border: 3px solid white;
                            border-radius: 15px;
                            color: white;
                            background-color: black;
                        }
                        """)
        self.del_button = QPushButton("Удалить")
        self.del_button.setStyleSheet("""
                                QPushButton{
                                    font-style: classic;
                                    font-weight: bold;
                                    border: 3px solid red;
                                    border-radius: 15px;
                                    color: #1DA1F2;
                                    background-color: black;
                                }
                                """)
        self.del_button.clicked.connect(self.del_pair)

        layout = QVBoxLayout()
        layout.addWidget(self.user_label)
        layout.addWidget(self.user_input)
        layout.addWidget(self.del_button)
        self.setLayout(layout)

        layout = QVBoxLayout()
        self.setLayout(layout)

    def del_pair(self):
        id = self.user_input.text()
        conn = sqlite3.connect('pairs_users.db')
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM pairs WHERE id = '{id}'")
        conn.commit()
        conn.close()

        self.close()


class DeleteAssessments(QDialog):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-image: url(123.jpg);")
        self.setWindowIcon(QtGui.QIcon('1903172.png'))
        self.setWindowTitle("Удалить оценку")
        self.setGeometry(200, 200, 600, 400)

        self.setWindowTitle("Удаление")
        self.setGeometry(200, 200, 300, 150)
        self.user_label = QLabel("ID оценки:")
        self.user_label.setStyleSheet("""
                                                QLabel{
                                                    font-style: classic;
                                                    font-weight: bold;
                                                    color: white;
                                                    background-color: black;
                                                }
                                                """)
        self.user_input = QLineEdit()
        self.user_input.setStyleSheet("""
                        QLineEdit{
                            font-style: classic;
                            font-weight: bold;
                            border: 3px solid white;
                            border-radius: 15px;
                            color: white;
                            background-color: black;
                        }
                        """)
        self.del_button = QPushButton("Удалить")
        self.del_button.setStyleSheet("""
                                QPushButton{
                                    font-style: classic;
                                    font-weight: bold;
                                    border: 3px solid red;
                                    border-radius: 15px;
                                    color: #1DA1F2;
                                    background-color: black;
                                }
                                """)
        self.del_button.clicked.connect(self.del_ass)

        layout = QVBoxLayout()
        layout.addWidget(self.user_label)
        layout.addWidget(self.user_input)
        layout.addWidget(self.del_button)
        self.setLayout(layout)

        layout = QVBoxLayout()
        self.setLayout(layout)
    def del_ass(self):
        id = self.user_input.text()
        conn = sqlite3.connect('pairs_users.db')
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM assessments WHERE id = '{id}'")
        conn.commit()
        conn.close()

        self.close()



class TeacherApp(QDialog):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-image: url(image.png);")
        self.setWindowIcon(QtGui.QIcon('1903172.png'))
        self.setWindowTitle("Успеваемость")
        self.setFixedSize(900,800)


        self.go_to_login_button = QPushButton("Назад")
        self.go_to_login_button.setStyleSheet("""
                                QPushButton{
                                    font-style: classic;
                                    font-weight: bold;
                                    border: 3px solid red;
                                    border-radius: 15px;
                                    color: #1DA1F2;
                                    background-color: black;
                                }
                                """)
        self.go_to_login_button.setFixedSize(150, 35)
        self.go_to_login_button.clicked.connect(self.go_to_login1)

        self.add_pair_button = QPushButton("Добавить пару")
        self.add_pair_button.setStyleSheet("""
                                QPushButton{
                                    font-style: classic;
                                    font-weight: bold;
                                    border: 3px solid red;
                                    border-radius: 15px;
                                    color: #1DA1F2;
                                    background-color: black;
                                }
                                """)
        self.add_pair_button.setFixedSize(500, 35)
        self.add_pair_button.clicked.connect(self.open_add_pair_window)

        self.del_pair_button = QPushButton("Удалить пару")
        self.del_pair_button.setStyleSheet("""
                                QPushButton{
                                    font-style: classic;
                                    font-weight: bold;
                                    border: 3px solid red;
                                    border-radius: 15px;
                                    color: #1DA1F2;
                                    background-color: black;
                                }
                                """)
        self.del_pair_button.setFixedSize(500, 35)
        self.del_pair_button.clicked.connect(self.delete_pair)

        self.add_assessment_button = QPushButton("Добавить оценку")
        self.add_assessment_button.setStyleSheet("""
                                QPushButton{
                                    font-style: classic;
                                    font-weight: bold;
                                    border: 3px solid red;
                                    border-radius: 15px;
                                    color: #1DA1F2;
                                    background-color: black;
                                }
                                """)
        self.add_assessment_button.setFixedSize(500, 35)
        self.add_assessment_button.clicked.connect(self.open_add_assessment_window)

        self.del_assessment_button = QPushButton("Удалить оценку")
        self.del_assessment_button.setStyleSheet("""
                                QPushButton{
                                    font-style: classic;
                                    font-weight: bold;
                                    border: 3px solid red;
                                    border-radius: 15px;
                                    color: #1DA1F2;
                                    background-color: black;
                                }
                                """)
        self.del_assessment_button.setFixedSize(500, 35)
        self.del_assessment_button.clicked.connect(self.delete_assessment)

        self.view_schedule_button = QPushButton("Посмотреть расписание")
        self.view_schedule_button.setStyleSheet("""
                                QPushButton{
                                    font-style: classic;
                                    font-weight: bold;
                                    border: 3px solid red;
                                    border-radius: 15px;
                                    color: #1DA1F2;
                                    background-color: black;
                                }
                                """)
        self.view_schedule_button.setFixedSize(500,35)
        self.view_schedule_button.clicked.connect(self.open_schedule_window)

        self.view_assessment_button = QPushButton("Посмотреть оценки")
        self.view_assessment_button.setStyleSheet("""
                                QPushButton{
                                    font-style: classic;
                                    font-weight: bold;
                                    border: 3px solid red;
                                    border-radius: 15px;
                                    color: #1DA1F2;
                                    background-color: black;
                                }
                                """)
        self.view_assessment_button.setFixedSize(500, 35)
        self.view_assessment_button.clicked.connect(self.open_assessment_window)


        self.new_child_button = QPushButton("Записать нового ученика")
        self.new_child_button.setStyleSheet("""
                                QPushButton{
                                    font-style: classic;
                                    font-weight: bold;
                                    border: 3px solid red;
                                    border-radius: 15px;
                                    color: #1DA1F2;
                                    background-color: black;
                                }
                                """)
        self.new_child_button.setFixedSize(500, 35)
        self.new_child_button.clicked.connect(self.new_child)

        self.del_child_button = QPushButton("Удалить ученика")
        self.del_child_button.setStyleSheet("""
                                QPushButton{
                                    font-style: classic;
                                    font-weight: bold;
                                    border: 3px solid red;
                                    border-radius: 15px;
                                    color: #1DA1F2;
                                    background-color: black;
                                }
                                """)
        self.del_child_button.setFixedSize(500, 35)
        self.del_child_button.clicked.connect(self.del_child)

        layout = QVBoxLayout()
        layout.addWidget(self.go_to_login_button)
        layout.addWidget(self.add_pair_button)
        layout.addWidget(self.del_pair_button)
        layout.addWidget(self.add_assessment_button)
        layout.addWidget(self.del_assessment_button)
        layout.addWidget(self.view_schedule_button)
        layout.addWidget(self.view_assessment_button)
        layout.addWidget(self.new_child_button)
        layout.addWidget(self.del_child_button)

        self.schedule_window = ScheduleWindow()
        layout.addWidget(self.schedule_window)


        self.assessment_window = StudentAssessmentWindow()
        layout.addWidget(self.assessment_window)




        self.setLayout(layout)


    def delete_pair(self):
        del_p_win = DeletePair()
        del_p_win.exec()

    def delete_assessment(self):
        del_ass_win = DeleteAssessments()
        del_ass_win.exec()


    def new_child(self):
        add_stud_window = StudentWindow()
        add_stud_window.exec()


    def del_child(self):
        del_win = StudentdeleteWindow()
        del_win.exec()

    def open_add_pair_window(self):
        add_pair_window = AddPairWindow()
        add_pair_window.exec()

    def open_add_assessment_window(self):
        add_pair_window = AddAssessmentWindow()
        add_pair_window.exec()

    def open_schedule_window(self):
        self.schedule_window.load_schedule()

    def open_assessment_window(self):
        self.assessment_window.view_assessments()

    def go_to_login1(self):
        while True:
            self.close()
            os.system("python main.py")
            break




class StudentApp(QDialog):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-image: url(image.png);")
        self.setWindowIcon(QtGui.QIcon('1903172.png'))
        self.setWindowTitle("Планировщик пар")
        self.setFixedSize(600,600)

        self.view_schedule_button = QPushButton("Посмотреть расписание")
        self.view_schedule_button.setStyleSheet("""
                                QPushButton{
                                    font-style: classic;
                                    font-weight: bold;
                                    border: 3px solid red;
                                    border-radius: 15px;
                                    color: #1DA1F2;
                                    background-color: red;
                                }
                                """)
        self.view_schedule_button.clicked.connect(self.open_schedule_window)

        self.view_assessment_button = QPushButton("Посмотреть оценки")
        self.view_assessment_button.setStyleSheet("""
                                QPushButton{
                                    font-style: classic;
                                    font-weight: bold;
                                    border: 3px solid red;
                                    border-radius: 15px;
                                    color: #1DA1F2;
                                    background-color: red;
                                }
                                """)
        self.view_assessment_button.clicked.connect(self.open_assessment_window)

        self.go_back_button = QPushButton("Назад")
        self.go_back_button.setStyleSheet("""
                                QPushButton{
                                    font-style: classic;
                                    font-weight: bold;
                                    border: 3px solid red;
                                    border-radius: 15px;
                                    color: #1DA1F2;
                                    background-color: black;
                                }
                                """)
        self.go_back_button.clicked.connect(self.go_to_login2)

        layout = QVBoxLayout()
        layout.addWidget(self.go_back_button)
        layout.addWidget(self.view_schedule_button)
        layout.addWidget(self.view_assessment_button)

        self.schedule_window = ScheduleWindow()
        layout.addWidget(self.schedule_window)

        self.assessment_window = StudentAssessmentWindow()
        layout.addWidget(self.assessment_window)

        self.setLayout(layout)

    def open_schedule_window(self):
        self.schedule_window.load_schedule()

    def open_assessment_window(self):
        self.assessment_window.view_assessments()

    def go_to_login2(self):
        while True:
            self.close()
            os.system("python main.py")
            break


class AddAssessmentWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-image: url(123.jpg);")
        self.setWindowIcon(QtGui.QIcon('1903172.png'))
        self.setWindowTitle("Добавить оценку")
        self.setGeometry(200, 200, 400, 200)

        self.student_label = QLabel("Фио студента:")
        self.student_label.setStyleSheet("""
                                                QLabel{
                                                    font-style: classic;
                                                    font-weight: bold;
                                                    color: white;
                                                    background-color: black;
                                                }
                                                """)
        self.student_input = QLineEdit()
        self.student_input.setStyleSheet("""
                        QLineEdit{
                            font-style: classic;
                            font-weight: bold;
                            border: 3px solid white;
                            border-radius: 15px;
                            color: white;
                            background-color: black;
                        }
                        """)

        self.subject_label = QLabel("Предмет:")
        self.subject_label.setStyleSheet("""
                                                QLabel{
                                                    font-style: classic;
                                                    font-weight: bold;
                                                    color: white;
                                                    background-color: black;
                                                }
                                                """)
        self.subject_input = QLineEdit()
        self.subject_input.setStyleSheet("""
                        QLineEdit{
                            font-style: classic;
                            font-weight: bold;
                            border: 3px solid white;
                            border-radius: 15px;
                            color: white;
                            background-color: black;
                        }
                        """)

        self.grade_label = QLabel("Оценка:")
        self.grade_label.setStyleSheet("""
                                                QLabel{
                                                    font-style: classic;
                                                    font-weight: bold;
                                                    color: white;
                                                    background-color: black;
                                                }
                                                """)
        self.grade_input = QLineEdit()
        self.grade_input.setStyleSheet("""
                        QLineEdit{
                            font-style: classic;
                            font-weight: bold;
                            border: 3px solid white;
                            border-radius: 15px;
                            color: white;
                            background-color: black;
                        }
                        """)

        self.comments_label = QLabel("Комментарий:")
        self.comments_label.setStyleSheet("""
                                                QLabel{
                                                    font-style: classic;
                                                    font-weight: bold;
                                                    color: white;
                                                    background-color: black;
                                                }
                                                """)
        self.comments_input = QLineEdit()
        self.comments_input.setStyleSheet("""
                        QLineEdit{
                            font-style: classic;
                            font-weight: bold;
                            border: 3px solid white;
                            border-radius: 15px;
                            color: white;
                            background-color: black;
                        }
                        """)

        self.submit_button = QPushButton("Добавить оценку")
        self.submit_button.setStyleSheet("""
                                QPushButton{
                                    font-style: classic;
                                    font-weight: bold;
                                    border: 3px solid red;
                                    border-radius: 15px;
                                    color: #1DA1F2;
                                    background-color: black;
                                }
                                """)
        self.submit_button.clicked.connect(self.add_assessment)

        layout = QVBoxLayout()
        layout.addWidget(self.student_label)
        layout.addWidget(self.student_input)
        layout.addWidget(self.subject_label)
        layout.addWidget(self.subject_input)
        layout.addWidget(self.grade_label)
        layout.addWidget(self.grade_input)
        layout.addWidget(self.comments_label)
        layout.addWidget(self.comments_input)
        layout.addWidget(self.submit_button)
        self.setLayout(layout)

    def add_assessment(self):
        student_name = self.student_input.text()
        subject = self.subject_input.text()
        grade = self.grade_input.text()
        comments = self.comments_input.text()

        conn = sqlite3.connect('pairs_users.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO assessments (student_name, subject, grade, comments) VALUES (?, ?, ?, ?)",
                       (student_name, subject, grade, comments))
        conn.commit()
        conn.close()

        self.close()

if __name__ == '__main__':

    conn = sqlite3.connect('pairs_users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE,
                    password TEXT,
                    user_type TEXT,
                    group_name TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS pairs
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT,
                    teacher TEXT,
                    group_name TEXT,
                    subject TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS assessments
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_name TEXT,
                    subject TEXT,
                    grade TEXT,
                    comments TEXT)''')

    conn.commit()
    conn.close()


    app = QApplication(sys.argv)
    mainapp = None
    authorization_window = AuthorizationWindow()
    if authorization_window.exec() == QDialog.Accepted:
        if authorization_window.status == 'student':
            mainapp = StudentApp()
        else:
            mainapp = TeacherApp()

    mainapp.show()
    sys.exit(app.exec())