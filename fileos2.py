import sys
import os
import shutil
import subprocess
import chardet
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        #设置界面
        TabWidget.setObjectName("TabWidget")
        TabWidget.setEnabled(True)
        TabWidget.resize(1300, 800)
        TabWidget.setBaseSize(QtCore.QSize(2, 2))

        #添加一个成员变量获取文件图标：
        self.icon_provider = QFileIconProvider()

        #创建一个标签页
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.tab_large_icon_view = QtWidgets.QWidget()
        self.tab_large_icon_view.setObjectName("tab2")


        #获取调色板
        palette = QtGui.QPalette()
        #设置背景图片
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(QtGui.QPixmap('')))
        #应用到窗口上
        self.tab.setPalette(palette)
        #设置图片自适应窗口
        self.tab.setAutoFillBackground(True)

        #创建文件列表部件
        self.listWidget = QtWidgets.QListWidget(self.tab)
        self.listWidget.setGeometry(QtCore.QRect(30, 40, 371, 500))
        self.listWidget.setObjectName("listWidget")

        self.Title_2 = QtWidgets.QLabel(self.tab)
        self.Title_2.setGeometry(QtCore.QRect(950, 0, 81, 21))
        self.Title_2.setObjectName("Title")

        #创建文本编辑框
        self.textbox = QtWidgets.QTextEdit(self.tab)
        self.textbox.setGeometry(QtCore.QRect(820,40,371,500))
        self.textbox.setObjectName("textbox")

        #创建标题标签
        self.Title = QtWidgets.QLabel(self.tab)
        self.Title.setGeometry(QtCore.QRect(160, 0, 81, 21))
        self.Title.setObjectName("Title")

        #创建按钮
        self.list_file = QtWidgets.QPushButton(self.tab)
        self.list_file.setGeometry(QtCore.QRect(550, 50, 121, 41))
        self.list_file.setObjectName("list_file")

        self.touch = QtWidgets.QPushButton(self.tab)
        self.touch.setGeometry(QtCore.QRect(550, 120, 121, 41))
        self.touch.setObjectName("touch")

        self.dele = QtWidgets.QPushButton(self.tab)
        self.dele.setGeometry(QtCore.QRect(550, 190, 121, 41))
        self.dele.setObjectName("dele")

        self.open = QtWidgets.QPushButton(self.tab)
        self.open.setGeometry(QtCore.QRect(550, 260, 121, 41))
        self.open.setObjectName("open")

        self.move = QtWidgets.QPushButton(self.tab)
        self.move.setGeometry(QtCore.QRect(550,330,121,41))
        self.move.setObjectName("move")

        self.rename = QtWidgets.QPushButton(self.tab)
        self.rename.setGeometry(QtCore.QRect(550, 400, 121, 41))
        self.rename.setObjectName("rename")

        self.back = QtWidgets.QPushButton(self.tab)
        self.back.setGeometry(QtCore.QRect(500, 510, 75, 23))
        self.back.setObjectName("back")

        self.quit = QtWidgets.QPushButton(self.tab)
        self.quit.setGeometry(QtCore.QRect(600, 510, 75, 23))
        self.quit.setObjectName("quit")

        #将标签页添加到 TabWidget 中
        TabWidget.addTab(self.tab,"1")

        #连接按钮的点击事件到相应的处理函数
        self.list_file.clicked.connect(dispose.list)
        self.touch.clicked.connect(dispose.touch)
        self.dele.clicked.connect(dispose.delete)
        self.open.clicked.connect(dispose.open)
        self.move.clicked.connect(dispose.move)
        self.rename.clicked.connect(dispose.rename)
        self.back.clicked.connect(dispose.back)
        self.quit.clicked.connect(dispose.quit)

        self.listWidget.itemDoubleClicked.connect(dispose.open)

        #根据当前的语言设置重新加载并显示对应的翻译文本
        self.retranslateUi(TabWidget)
        #将当前的TabWidget的索引设置为0，这意味着它将显示第一个选项卡
        TabWidget.setCurrentIndex(0)

        #根据当前的语言设置重新加载并显示对应的翻译文本
        self.retranslateUi(TabWidget)

        #自动连接UI中的信号和槽
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    #重新翻译界面上的文本内容
    def retranslateUi(self, TabWidget):
        #将界面上的各个部件的文本内容重新翻译为特定的语言
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "文件管理系统"))
        self.Title.setText(_translate("TabWidget", "<html><head/><body><p><span style=\" font-size:13pt; font-weight:700;\">文件目录</span></p></body></html>"))
        self.Title_2.setText(_translate("TabWidget", "<html><head/><body><p><span style=\" font-size:13pt; font-weight:700;\">文本编辑</span></p></body></html>"))
        self.list_file.setText(_translate("TabWidget", "列出文件"))
        self.touch.setText(_translate("TabWidget", "创建文件"))
        self.dele.setText(_translate("TabWidget", "删除文件"))
        self.open.setText(_translate("TabWidget", "打开文件"))
        self.rename.setText(_translate("TabWidget", "重命名"))
        self.move.setText(_translate("TabWidget","移动文件"))
        self.back.setText(_translate("TabWidget","返回"))
        self.quit.setText(_translate("TabWidget", "退出"))
        self.textbox.setText(_translate("TabWidget",""))

    def get_file_icon(self, file_path):
        #使用 QFileIconProvider 获取文件图标
        icon = self.icon_provider.icon(QtCore.QFileInfo(file_path))
        return icon

class Ui_TabWidget2(object):
    def setupUi(self, TabWidget):
        #设置界面
        TabWidget.setObjectName("TabWidget")
        TabWidget.setEnabled(True)
        TabWidget.resize(1300, 800)
        TabWidget.setBaseSize(QtCore.QSize(2, 2))

        #添加一个成员变量获取文件图标：
        self.icon_provider = QFileIconProvider()

        #创建一个标签页
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab")

        #获取调色板
        palette = QtGui.QPalette()
        #设置背景图片
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(QtGui.QPixmap('')))
        #应用到窗口上
        self.tab1.setPalette(palette)
        #设置图片自适应窗口
        self.tab1.setAutoFillBackground(True)

        #创建文件列表部件
        self.listWidget1 = QtWidgets.QListWidget(self.tab1)
        self.listWidget1.setGeometry(QtCore.QRect(30, 40, 371, 500))
        self.listWidget1.setObjectName("listWidget")

        #将视图模式改为纵向三列显示
        self.listWidget1.setViewMode(QtWidgets.QListWidget.IconMode)
        self.listWidget1.setFlow(QtWidgets.QListWidget.LeftToRight)  #从左到右显示文件
        self.listWidget1.setIconSize(QtCore.QSize(24, 24))
        self.listWidget1.setResizeMode(QtWidgets.QListWidget.Adjust)
        self.listWidget1.setGridSize(QtCore.QSize(110, 50))  #设置每个网状单元格大小

        self.Title_21 = QtWidgets.QLabel(self.tab1)
        self.Title_21.setGeometry(QtCore.QRect(950, 0, 81, 21))
        self.Title_21.setObjectName("Title")

        #创建文本编辑框
        self.textbox1 = QtWidgets.QTextEdit(self.tab1)
        self.textbox1.setGeometry(QtCore.QRect(820,40,371,500))
        self.textbox1.setObjectName("textbox")

        #创建标题标签
        self.Title1 = QtWidgets.QLabel(self.tab1)
        self.Title1.setGeometry(QtCore.QRect(160, 0, 81, 21))
        self.Title1.setObjectName("Title")

        #创建按钮
        self.list_file1 = QtWidgets.QPushButton(self.tab1)
        self.list_file1.setGeometry(QtCore.QRect(550, 50, 121, 41))
        self.list_file1.setObjectName("list_file")

        self.touch1 = QtWidgets.QPushButton(self.tab1)
        self.touch1.setGeometry(QtCore.QRect(550, 120, 121, 41))
        self.touch1.setObjectName("touch")

        self.dele1 = QtWidgets.QPushButton(self.tab1)
        self.dele1.setGeometry(QtCore.QRect(550, 190, 121, 41))
        self.dele1.setObjectName("dele")

        self.open1 = QtWidgets.QPushButton(self.tab1)
        self.open1.setGeometry(QtCore.QRect(550, 260, 121, 41))
        self.open1.setObjectName("open")

        self.move1 = QtWidgets.QPushButton(self.tab1)
        self.move1.setGeometry(QtCore.QRect(550,330,121,41))
        self.move1.setObjectName("move")

        self.rename1 = QtWidgets.QPushButton(self.tab1)
        self.rename1.setGeometry(QtCore.QRect(550, 400, 121, 41))
        self.rename1.setObjectName("rename")

        self.back1 = QtWidgets.QPushButton(self.tab1)
        self.back1.setGeometry(QtCore.QRect(500, 510, 75, 23))
        self.back1.setObjectName("back")

        self.quit1 = QtWidgets.QPushButton(self.tab1)
        self.quit1.setGeometry(QtCore.QRect(600, 510, 75, 23))
        self.quit1.setObjectName("quit")

        #将标签页添加到 TabWidget 中
        TabWidget.addTab(self.tab1,"2")

        #连接按钮的点击事件到相应的处理函数
        self.list_file1.clicked.connect(DisposeTab2.list)
        self.touch1.clicked.connect(DisposeTab2.touch)
        self.dele1.clicked.connect(DisposeTab2.delete)
        self.open1.clicked.connect(DisposeTab2.open)
        self.move1.clicked.connect(DisposeTab2.move)
        self.rename1.clicked.connect(DisposeTab2.rename)
        self.back1.clicked.connect(DisposeTab2.back)
        self.quit1.clicked.connect(DisposeTab2.quit)

        self.listWidget1.itemDoubleClicked.connect(DisposeTab2.open)

        #根据当前的语言设置重新加载并显示对应的翻译文本
        self.retranslateUi(TabWidget)
        #将当前的TabWidget的索引设置为0，这意味着它将显示第一个选项卡
        TabWidget.setCurrentIndex(0)

        #根据当前的语言设置重新加载并显示对应的翻译文本
        self.retranslateUi(TabWidget)

        #自动连接UI中的信号和槽
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    #重新翻译界面上的文本内容
    def retranslateUi(self, TabWidget):
        #将界面上的各个部件的文本内容重新翻译为特定的语言
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "文件管理系统"))
        self.Title1.setText(_translate("TabWidget", "<html><head/><body><p><span style=\" font-size:13pt; font-weight:700;\">文件目录</span></p></body></html>"))
        self.Title_21.setText(_translate("TabWidget", "<html><head/><body><p><span style=\" font-size:13pt; font-weight:700;\">文本编辑</span></p></body></html>"))
        self.list_file1.setText(_translate("TabWidget", "列出文件"))
        self.touch1.setText(_translate("TabWidget", "创建文件"))
        self.dele1.setText(_translate("TabWidget", "删除文件"))
        self.open1.setText(_translate("TabWidget", "打开文件"))
        self.rename1.setText(_translate("TabWidget", "重命名"))
        self.move1.setText(_translate("TabWidget","移动文件"))
        self.back1.setText(_translate("TabWidget","返回"))
        self.quit1.setText(_translate("TabWidget", "退出"))
        self.textbox1.setText(_translate("TabWidget",""))

    def get_file_icon(self, file_path):
        #使用 QFileIconProvider 获取文件图标
        icon = self.icon_provider.icon(QtCore.QFileInfo(file_path))
        return icon

class Ui_TabWidget3(object):
    def setupUi(self, TabWidget):
        #设置界面
        TabWidget.setObjectName("TabWidget")
        TabWidget.setEnabled(True)
        TabWidget.resize(1300, 800)
        TabWidget.setBaseSize(QtCore.QSize(2, 2))

        #添加一个成员变量获取文件图标：
        self.icon_provider = QFileIconProvider()

        #创建一个标签页
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab")

        #获取调色板
        palette = QtGui.QPalette()
        #设置背景图片
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(QtGui.QPixmap('')))
        #应用到窗口上
        self.tab2.setPalette(palette)
        #设置图片自适应窗口
        self.tab2.setAutoFillBackground(True)

        #创建文件列表部件
        self.listWidget2 = QtWidgets.QListWidget(self.tab2)
        self.listWidget2.setGeometry(QtCore.QRect(30, 40, 371, 500))
        self.listWidget2.setObjectName("listWidget")

        self.Title_22 = QtWidgets.QLabel(self.tab2)
        self.Title_22.setGeometry(QtCore.QRect(950, 0, 81, 21))
        self.Title_22.setObjectName("Title")

        #创建文本编辑框
        self.textbox2 = QtWidgets.QTextEdit(self.tab2)
        self.textbox2.setGeometry(QtCore.QRect(820,40,371,500))
        self.textbox2.setObjectName("textbox")

        #创建标题标签
        self.Title2 = QtWidgets.QLabel(self.tab2)
        self.Title2.setGeometry(QtCore.QRect(160, 0, 81, 21))
        self.Title2.setObjectName("Title")

        #创建按钮
        self.list_file2 = QtWidgets.QPushButton(self.tab2)
        self.list_file2.setGeometry(QtCore.QRect(550, 50, 121, 41))
        self.list_file2.setObjectName("list_file")

        self.touch2 = QtWidgets.QPushButton(self.tab2)
        self.touch2.setGeometry(QtCore.QRect(550, 120, 121, 41))
        self.touch2.setObjectName("touch")

        self.dele2 = QtWidgets.QPushButton(self.tab2)
        self.dele2.setGeometry(QtCore.QRect(550, 190, 121, 41))
        self.dele2.setObjectName("dele")

        self.open2 = QtWidgets.QPushButton(self.tab2)
        self.open2.setGeometry(QtCore.QRect(550, 260, 121, 41))
        self.open2.setObjectName("open")

        self.move2 = QtWidgets.QPushButton(self.tab2)
        self.move2.setGeometry(QtCore.QRect(550,330,121,41))
        self.move2.setObjectName("move")

        self.rename2 = QtWidgets.QPushButton(self.tab2)
        self.rename2.setGeometry(QtCore.QRect(550, 400, 121, 41))
        self.rename2.setObjectName("rename")

        self.back2 = QtWidgets.QPushButton(self.tab2)
        self.back2.setGeometry(QtCore.QRect(500, 510, 75, 23))
        self.back2.setObjectName("back")

        self.quit2 = QtWidgets.QPushButton(self.tab2)
        self.quit2.setGeometry(QtCore.QRect(600, 510, 75, 23))
        self.quit2.setObjectName("quit")

        #将标签页添加到 TabWidget 中
        TabWidget.addTab(self.tab2,"3")

        #连接按钮的点击事件到相应的处理函数
        self.list_file2.clicked.connect(DisposeTab3.list)
        self.touch2.clicked.connect(DisposeTab3.touch)
        self.dele2.clicked.connect(DisposeTab3.delete)
        self.open2.clicked.connect(DisposeTab3.open)
        self.move2.clicked.connect(DisposeTab3.move)
        self.rename2.clicked.connect(DisposeTab3.rename)
        self.back2.clicked.connect(DisposeTab3.back)
        self.quit2.clicked.connect(DisposeTab3.quit)

        self.listWidget2.itemDoubleClicked.connect(DisposeTab3.open)

        #根据当前的语言设置重新加载并显示对应的翻译文本
        self.retranslateUi(TabWidget)
        #将当前的TabWidget的索引设置为0，这意味着它将显示第一个选项卡
        TabWidget.setCurrentIndex(0)

        #根据当前的语言设置重新加载并显示对应的翻译文本
        self.retranslateUi(TabWidget)

        #自动连接UI中的信号和槽
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    #重新翻译界面上的文本内容
    def retranslateUi(self, TabWidget):
        #将界面上的各个部件的文本内容重新翻译为特定的语言
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "文件管理系统"))
        self.Title2.setText(_translate("TabWidget", "<html><head/><body><p><span style=\" font-size:13pt; font-weight:700;\">文件目录</span></p></body></html>"))
        self.Title_22.setText(_translate("TabWidget", "<html><head/><body><p><span style=\" font-size:13pt; font-weight:700;\">文本编辑</span></p></body></html>"))
        self.list_file2.setText(_translate("TabWidget", "列出文件"))
        self.touch2.setText(_translate("TabWidget", "创建文件"))
        self.dele2.setText(_translate("TabWidget", "删除文件"))
        self.open2.setText(_translate("TabWidget", "打开文件"))
        self.rename2.setText(_translate("TabWidget", "重命名"))
        self.move2.setText(_translate("TabWidget","移动文件"))
        self.back2.setText(_translate("TabWidget","返回"))
        self.quit2.setText(_translate("TabWidget", "退出"))
        self.textbox2.setText(_translate("TabWidget",""))

    def get_file_icon(self, file_path):
        #使用 QFileIconProvider 获取文件图标
        icon = self.icon_provider.icon(QtCore.QFileInfo(file_path))
        return icon
    
class dispose(QtWidgets.QTabWidget):

    def __init__(self):
        super(dispose, self).__init__()
        self.ui = Ui_TabWidget()
        self.ui.setupUi(self)

    def list(self):     #打开文件夹
        ui.textbox.clear()
        ui.listWidget.clear()
        #QFileDialog.getExistingDirectory是一个方法，用于打开一个对话框，让用户选择一个文件夹。
        #参数None表示对话框的父窗口，'choose a file'是对话框的标题，'/'是对话框的默认路径，QFileDialog.ShowDirsOnly表示只显示文件夹而不显示文件。
        #这个方法会返回用户选择的文件夹的路径。
        global dir, file
        dir = QFileDialog.getExistingDirectory(None,'choose a file','/',QFileDialog.ShowDirsOnly)

        #检查用户是否点击了取消按钮或关闭了对话框
        if not dir:
            return

        #输出文件列表
        file = os.listdir(dir)
        for i in file:
            file_path = os.path.join(dir, i)
            item = QtWidgets.QListWidgetItem()
            item.setIcon(ui.get_file_icon(file_path))
            item.setText(i)
            ui.listWidget.addItem(item)
        

    def touch(self):  #创建文件或文件夹
        try:
            #检查文件列表是否为空
            if ui.listWidget.count() == 0: 
                QMessageBox.warning(None, "警告", "请先打开文件夹以创建文件或文件夹。", QMessageBox.Ok)
                return
            
            while True:
                #打开一个对话框，让用户输入文件或文件夹名称
                file_or_folder_name, ok_pressed = QInputDialog.getText(None, "创建文件或文件夹", "输入文件（文件夹）名称:")
                
                #如果用户点击了取消按钮或者未输入名称，退出循环
                if not ok_pressed or not file_or_folder_name:
                    break
                
                file_path = os.path.join(dir, file_or_folder_name)
                if '.' in file_or_folder_name:
                    reply = None
                    #检查文件是否已存在
                    if os.path.exists(file_path):  
                        #循环直到用户重新输入一个新的文件名或取消创建
                        while True:  
                            reply = QMessageBox.question(None, "警告", "文件已存在。是否要重新创建文件？", QMessageBox.Yes | QMessageBox.No)
                            #用户选择重新输入文件名，退出内层循环
                            if reply == QMessageBox.Yes:
                                break  
                            #用户选择取消创建，退出内层循环
                            elif reply == QMessageBox.No:
                                break  
                    #用户选择重新输入文件名，继续外层循环
                    if reply == QMessageBox.Yes:
                        continue 
                    #用户选择取消创建，退出外层循环
                    elif reply == QMessageBox.No:
                        break  
                    else:
                        #创建文件
                        with open(file_path, 'w') as file:
                            pass
                        file = os.listdir(dir)
                        for i in file:
                            file_path = os.path.join(dir, i)
                            item = QtWidgets.QListWidgetItem()
                            item.setIcon(ui.get_file_icon(file_path))
                            item.setText(i)
                            ui.listWidget.addItem(item)
                        #将新创建的文件名称添加到左侧的文件列表中
                        #文件创建成功，退出外层循环
                        break  
                else:
                    #检查文件夹是否已存在
                    if os.path.exists(file_path):  
                        QMessageBox.warning(None, "警告", "文件夹已存在。", QMessageBox.Ok)
                    else:
                        #创建文件夹
                        os.makedirs(file_path, exist_ok=True)
                        #将新创建的文件夹名称添加到左侧的文件列表中
                        file = os.listdir(dir)
                        for i in file:
                            file_path = os.path.join(dir, i)
                            item = QtWidgets.QListWidgetItem()
                            item.setIcon(ui.get_file_icon(file_path))
                            item.setText(i)
                            ui.listWidget.addItem(item)
                        break  
        except Exception as e:
            print(f"创建文件或文件夹时出现错误: {e}")

    def delete(self):   #删除文件（夹）
        try:
            #如果未选中文件，则弹出警示框
            current_item = ui.listWidget.currentItem()
            if current_item is None:
                QMessageBox.warning(None, "警告", "未选择任何文件!", QMessageBox.Ok)
                return
            
            #获取选中的文件
            file_name = current_item.text()
            #获取完整文件路径
            location = os.path.join(dir, file_name)

            if os.path.exists(location):
                confirmation = QMessageBox.question(None, "确认删除",f"你确定要删除 '{file_name}' 吗？",QMessageBox.Yes | QMessageBox.No)
                #删除操作
                if confirmation == QMessageBox.Yes:
                    #根据文件或文件夹进行相应的删除
                    if os.path.isfile(location):
                        os.remove(location)
                        ui.listWidget.takeItem(ui.listWidget.row(current_item))
                    elif os.path.isdir(location):
                        shutil.rmtree(location)
                        ui.listWidget.takeItem(ui.listWidget.row(current_item))
                #如果取消，则返回到主界面
                else:
                    return
            else:
                QMessageBox.warning(None, "警告", "路径不存在!", QMessageBox.Ok)
        except FileNotFoundError:
            QMessageBox.warning(None, "警告", "文件不存在!", QMessageBox.Ok)
        except PermissionError:
            QMessageBox.warning(None, "警告", "没有权限删除文件!", QMessageBox.Ok)

    def open(self):     #打开文件(夹)
        try:
            #告诉解释器在该函数内使用全局的 dir 变量
            global dir
            #获取当前选中的项目
            try:
                file_name = ui.listWidget.currentItem().text()
            except AttributeError:
                QMessageBox.warning(None, "警告", "请先选择一个文件(夹)!", QMessageBox.Ok)
                return
            position = dir + '/' + str(file_name)
            if os.path.isdir(position):
            #如果是文件夹，列出其内容
                #更新路径
                dir += '/' + str(file_name)
                ui.textbox.clear()
                ui.listWidget.clear()
                file_list = os.listdir(dir)
                for i in file_list:
                    file_path = os.path.join(dir, i)
                    item = QtWidgets.QListWidgetItem()
                    item.setIcon(ui.get_file_icon(file_path))
                    item.setText(i)
                    ui.listWidget.addItem(item)
            else:
                try:
                    subprocess.Popen(['xdg-open', position])
                except: 
                    try:
                        #使用 chardet 库检测文件编码
                        with open(position, 'rb') as f:
                            detector = chardet.universaldetector.UniversalDetector()
                            for line in f:
                                detector.feed(line)
                                if detector.done:
                                    break
                            detector.close()
                            encoding = detector.result['encoding']
                        #尝试使用检测到的编码重新打开文件
                        with open(position, 'r', encoding=encoding) as f:
                            ui.textbox.clear()
                            data = f.read()
                            ui.textbox.setText(data)
                    except UnicodeDecodeError:
                        QMessageBox.warning(None, "警告", "文件编码无法解析，尝试使用其他编码！", QMessageBox.Ok)
                    except FileNotFoundError:
                        QMessageBox.warning(None, "警告", "文件未找到！", QMessageBox.Ok)
                    except PermissionError:
                        QMessageBox.warning(None, "警告", "没有权限访问文件！", QMessageBox.Ok)
                    except Exception:
                        QMessageBox.warning(None, "警告", "发生未知错误！", QMessageBox.Ok)
        except Exception:
            QMessageBox.warning(None, "警告", "发生未知错误！", QMessageBox.Ok)

    def rename(self):   #重命名
        item = ui.listWidget.currentItem()

        if item is not None:
            current_name = item.text()

            new_name, ok_pressed = QInputDialog.getText(None, "Rename", "Enter new name:", QLineEdit.Normal, current_name)

            if ok_pressed and new_name != current_name:
                old_path = os.path.join(dir, current_name)
                new_path = os.path.join(dir, new_name)

                #如果新名称不包含文件后缀，发出警告
                if '.' not in new_name:
                    QMessageBox.warning(None, "警告", "新文件名缺少文件后缀，请添加后缀。", QMessageBox.Ok)
                    return

                #如果修改了文件后缀，更新文件格式
                if new_name.split('.')[-1] != current_name.split('.')[-1]:
                    try:
                        #获取文件内容
                        with open(old_path, 'r', encoding='utf-8') as file:
                            data = file.read()

                        #修改文件后缀
                        with open(new_path, 'w', encoding='utf-8') as file:
                            file.write(data)

                        #删除原文件
                        os.remove(old_path)
                        item.setText(new_name)
                    except Exception as e:
                        QMessageBox.warning(None, "警告", "修改文件格式失败！", QMessageBox.Ok)
                        return
                else:
                    try:
                        os.rename(old_path, new_path)
                        item.setText(new_name)
                        print(f"成功重命名为: {new_name}")
                    except Exception as e:
                        print(f"重命名失败: {e}")
                        QMessageBox.warning(None, "警告", "重命名失败！", QMessageBox.Ok)
        else:
            QMessageBox.warning(None, "警告", "请选择需要重命名的文件", QMessageBox.Ok)

    def move(self):  #移动文件
        try:
            if ui.listWidget.currentItem() is None:
                #如果用户没有选择任何文件，弹出提示
                QMessageBox.information(None, "提示", "请先选择要移动的文件。")
                return
            
            file_name = ui.listWidget.currentItem().text()
            source = str(dir) + '/' + str(file_name)

            #弹出文件对话框让用户选择目标文件夹
            destination = QFileDialog.getExistingDirectory(None, '选择目标文件夹', '/')

            if destination:  #如果用户选择了目标文件夹
                destination_path = os.path.join(destination, file_name)

                if os.path.exists(destination_path):
                    #如果目标文件已经存在，询问用户是否覆盖
                    reply = QMessageBox.question(None, '文件已存在', '目标文件夹已经存在同名文件，是否覆盖？',
                                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if reply == QMessageBox.Yes:
                        #覆盖已存在的文件
                        shutil.move(source, destination_path)
                    else:
                        #用户选择不覆盖，不执行移动操作
                        return
                else:
                    #目标文件夹不存在同名文件，正常移动
                    shutil.move(source, destination_path)

                #更新界面，从文件列表中移除已移动的文件
                ui.listWidget.takeItem(ui.listWidget.currentRow())
        except FileNotFoundError:
            QMessageBox.critical(None, "错误", "找不到文件或目录。")
        except PermissionError:
            QMessageBox.critical(None, "错误", "没有权限执行操作。")
        except Exception as e:
            #如果发生其他异常，弹出错误对话框显示错误信息
            QMessageBox.critical(None, "Error", f"移动文件时发生错误：{str(e)}")

    def back(self):
        #处理返回按钮的逻辑
        global dir
        current_dir = os.path.abspath(dir)
        parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

        if current_dir != parent_dir:
            # 如果当前目录不是根目录，返回上一级目录
            dir = parent_dir
            ui.textbox.clear()
            ui.listWidget.clear()

            file_list = os.listdir(dir)
            for i in file_list:
                file_path = os.path.join(dir, i)
                item = QtWidgets.QListWidgetItem()
                item.setIcon(ui.get_file_icon(file_path))
                item.setText(i)
                ui.listWidget.addItem(item)


    def quit(self):     # 退出软件
        # 退出时会有弹框提示用户是否确认退出
        reply = QMessageBox.question(None, '确认退出', '确定要退出吗？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            sys.exit(app.exec_())

class DisposeTab2(QtWidgets.QTabWidget):
    def __init__(self):
        super(DisposeTab2, self).__init__()
        self.ui1 = Ui_TabWidget2()
        self.ui1.setupUi(self)
    
    def list(self):     #打开文件夹
        ui1.textbox1.clear()
        ui1.listWidget1.clear()
        #QFileDialog.getExistingDirectory是一个方法，用于打开一个对话框，让用户选择一个文件夹。
        #参数None表示对话框的父窗口，'choose a file'是对话框的标题，'/'是对话框的默认路径，QFileDialog.ShowDirsOnly表示只显示文件夹而不显示文件。
        #这个方法会返回用户选择的文件夹的路径。
        global dir1,file1
        dir1 = QFileDialog.getExistingDirectory(None,'choose a file','/',QFileDialog.ShowDirsOnly)

        #检查用户是否点击了取消按钮或关闭了对话框
        if not dir1:
            return

        #输出文件列表
        file1 = os.listdir(dir1)
        for i in file1:
            file_path = os.path.join(dir1, i)
            item = QtWidgets.QListWidgetItem()
            item.setIcon(ui1.get_file_icon(file_path))
            item.setText(i)
            item.setToolTip(i)
            ui1.listWidget1.addItem(item)
        
            
            
        

    def touch(self):  #创建文件或文件夹
        try:
            #检查文件列表是否为空
            if ui1.listWidget1.count() == 0: 
                QMessageBox.warning(None, "警告", "请先打开文件夹以创建文件或文件夹。", QMessageBox.Ok)
                return
            
            while True:
                #打开一个对话框，让用户输入文件或文件夹名称
                file_or_folder_name, ok_pressed = QInputDialog.getText(None, "创建文件或文件夹", "输入文件（文件夹）名称:")
                
                #如果用户点击了取消按钮或者未输入名称，退出循环
                if not ok_pressed or not file_or_folder_name:
                    break
                
                file_path = os.path.join(dir1, file_or_folder_name)
                if '.' in file_or_folder_name:
                    reply = None
                    #检查文件是否已存在
                    if os.path.exists(file_path):  
                        #循环直到用户重新输入一个新的文件名或取消创建
                        while True:  
                            reply = QMessageBox.question(None, "警告", "文件已存在。是否要重新创建文件？", QMessageBox.Yes | QMessageBox.No)
                            #用户选择重新输入文件名，退出内层循环
                            if reply == QMessageBox.Yes:
                                break  
                            #用户选择取消创建，退出内层循环
                            elif reply == QMessageBox.No:
                                break  
                    #用户选择重新输入文件名，继续外层循环
                    if reply == QMessageBox.Yes:
                        continue 
                    #用户选择取消创建，退出外层循环
                    elif reply == QMessageBox.No:
                        break  
                    else:
                        #创建文件
                        with open(file_path, 'w') as file:
                            pass
                        file1 = os.listdir(dir1)
                        ui1.listWidget1.clear()
                        for i in file1:
                            file_path = os.path.join(dir1, i)
                            item = QtWidgets.QListWidgetItem()
                            item.setIcon(ui1.get_file_icon(file_path))
                            item.setText(i)
                            ui1.listWidget1.addItem(item)
                        #将新创建的文件名称添加到左侧的文件列表中
                        #文件创建成功，退出外层循环
                        break  
                else:
                    #检查文件夹是否已存在
                    if os.path.exists(file_path):  
                        QMessageBox.warning(None, "警告", "文件夹已存在。", QMessageBox.Ok)
                    else:
                        #创建文件夹
                        os.makedirs(file_path, exist_ok=True)
                        #将新创建的文件夹名称添加到左侧的文件列表中
                        file1 = os.listdir(dir1)
                        for i in file1:
                            file_path = os.path.join(dir1, i)
                            item = QtWidgets.QListWidgetItem()
                            item.setIcon(ui1.get_file_icon(file_path))
                            item.setText(i)
                            ui1.listWidget1.addItem(item)
                        break  
        except Exception as e:
            print(f"创建文件或文件夹时出现错误: {e}")

    def delete(self):   #删除文件（夹）
        try:
            #如果未选中文件，则弹出警示框
            current_item = ui1.listWidget1.currentItem()
            if current_item is None:
                QMessageBox.warning(None, "警告", "未选择任何文件!", QMessageBox.Ok)
                return
            
            #获取选中的文件
            file_name = current_item.text()
            #获取完整文件路径
            location = os.path.join(dir1, file_name)

            if os.path.exists(location):
                confirmation = QMessageBox.question(None, "确认删除",f"你确定要删除 '{file_name}' 吗？",QMessageBox.Yes | QMessageBox.No)
                #删除操作
                if confirmation == QMessageBox.Yes:
                    #根据文件或文件夹进行相应的删除
                    if os.path.isfile(location):
                        os.remove(location)
                        ui1.listWidget1.takeItem(ui.listWidget.row(current_item))
                    elif os.path.isdir(location):
                        shutil.rmtree(location)
                        ui1.listWidget1.takeItem(ui.listWidget.row(current_item))
                #如果取消，则返回到主界面
                else:
                    return
            else:
                QMessageBox.warning(None, "警告", "路径不存在!", QMessageBox.Ok)
        except FileNotFoundError:
            QMessageBox.warning(None, "警告", "文件不存在!", QMessageBox.Ok)
        except PermissionError:
            QMessageBox.warning(None, "警告", "没有权限删除文件!", QMessageBox.Ok)

    def open(self):     #打开文件(夹)
        try:
            #告诉解释器在该函数内使用全局的 dir 变量
            global dir1
            #获取当前选中的项目
            try:
                file_name = ui1.listWidget1.currentItem().text()
            except AttributeError:
                QMessageBox.warning(None, "警告", "请先选择一个文件(夹)!", QMessageBox.Ok)
                return
            position = dir1 + '/' + str(file_name)
            if os.path.isdir(position):
            #如果是文件夹，列出其内容
                #更新路径
                dir1 += '/' + str(file_name)
                ui1.textbox1.clear()
                ui1.listWidget1.clear()
                file_list = os.listdir(dir1)
                for i in file_list:
                    file_path = os.path.join(dir1, i)
                    item = QtWidgets.QListWidgetItem()
                    item.setIcon(ui1.get_file_icon(file_path))
                    item.setText(i)
                    ui1.listWidget1.addItem(item)
            else:
                try:
                    subprocess.Popen(['xdg-open', position])
                except: 
                    try:
                        #使用 chardet 库检测文件编码
                        with open(position, 'rb') as f:
                            detector = chardet.universaldetector.UniversalDetector()
                            for line in f:
                                detector.feed(line)
                                if detector.done:
                                    break
                            detector.close()
                            encoding = detector.result['encoding']
                        #尝试使用检测到的编码重新打开文件
                        with open(position, 'r', encoding=encoding) as f:
                            ui1.textbox1.clear()
                            data = f.read()
                            ui1.textbox1.setText(data)
                    except UnicodeDecodeError:
                        QMessageBox.warning(None, "警告", "文件编码无法解析，尝试使用其他编码！", QMessageBox.Ok)
                    except FileNotFoundError:
                        QMessageBox.warning(None, "警告", "文件未找到！", QMessageBox.Ok)
                    except PermissionError:
                        QMessageBox.warning(None, "警告", "没有权限访问文件！", QMessageBox.Ok)
                    except Exception:
                        QMessageBox.warning(None, "警告", "发生未知错误！", QMessageBox.Ok)
        except Exception:
            QMessageBox.warning(None, "警告", "发生未知错误！", QMessageBox.Ok)

    def rename(self):   #重命名
        item = ui1.listWidget1.currentItem()

        if item is not None:
            current_name = item.text()

            new_name, ok_pressed = QInputDialog.getText(None, "Rename", "Enter new name:", QLineEdit.Normal, current_name)

            if ok_pressed and new_name != current_name:
                old_path = os.path.join(dir, current_name)
                new_path = os.path.join(dir, new_name)

                #如果新名称不包含文件后缀，发出警告
                if '.' not in new_name:
                    QMessageBox.warning(None, "警告", "新文件名缺少文件后缀，请添加后缀。", QMessageBox.Ok)
                    return

                #如果修改了文件后缀，更新文件格式
                if new_name.split('.')[-1] != current_name.split('.')[-1]:
                    try:
                        #获取文件内容
                        with open(old_path, 'r', encoding='utf-8') as file:
                            data = file.read()

                        #修改文件后缀
                        with open(new_path, 'w', encoding='utf-8') as file:
                            file.write(data)

                        #删除原文件
                        os.remove(old_path)
                        item.setText(new_name)
                    except Exception as e:
                        QMessageBox.warning(None, "警告", "修改文件格式失败！", QMessageBox.Ok)
                        return
                else:
                    try:
                        os.rename(old_path, new_path)
                        item.setText(new_name)
                        print(f"成功重命名为: {new_name}")
                    except Exception as e:
                        print(f"重命名失败: {e}")
                        QMessageBox.warning(None, "警告", "重命名失败！", QMessageBox.Ok)
        else:
            QMessageBox.warning(None, "警告", "请选择需要重命名的文件", QMessageBox.Ok)

    def move(self):  #移动文件
        try:
            if ui1.listWidget1.currentItem() is None:
                #如果用户没有选择任何文件，弹出提示
                QMessageBox.information(None, "提示", "请先选择要移动的文件。")
                return
            
            file_name = ui1.listWidget1.currentItem().text()
            source = str(dir1) + '/' + str(file_name)

            #弹出文件对话框让用户选择目标文件夹
            destination = QFileDialog.getExistingDirectory(None, '选择目标文件夹', '/')

            if destination:  #如果用户选择了目标文件夹
                destination_path = os.path.join(destination, file_name)

                if os.path.exists(destination_path):
                    #如果目标文件已经存在，询问用户是否覆盖
                    reply = QMessageBox.question(None, '文件已存在', '目标文件夹已经存在同名文件，是否覆盖？',
                                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if reply == QMessageBox.Yes:
                        #覆盖已存在的文件
                        shutil.move(source, destination_path)
                    else:
                        #用户选择不覆盖，不执行移动操作
                        return
                else:
                    #目标文件夹不存在同名文件，正常移动
                    shutil.move(source, destination_path)

                #更新界面，从文件列表中移除已移动的文件
                ui1.listWidget1.takeItem(ui1.listWidget1.currentRow())
        except FileNotFoundError:
            QMessageBox.critical(None, "错误", "找不到文件或目录。")
        except PermissionError:
            QMessageBox.critical(None, "错误", "没有权限执行操作。")
        except Exception as e:
            #如果发生其他异常，弹出错误对话框显示错误信息
            QMessageBox.critical(None, "Error", f"移动文件时发生错误：{str(e)}")

    def back(self):
        #处理返回按钮的逻辑
        global dir1
        current_dir = os.path.abspath(dir1)
        parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

        if current_dir != parent_dir:
            # 如果当前目录不是根目录，返回上一级目录
            dir1 = parent_dir
            ui1.textbox1.clear()
            ui1.listWidget1.clear()

            file_list = os.listdir(dir1)
            for i in file_list:
                file_path = os.path.join(dir1, i)
                item = QtWidgets.QListWidgetItem()
                item.setIcon(ui1.get_file_icon(file_path))
                item.setText(i)
                ui1.listWidget1.addItem(item)


    def quit(self):     # 退出软件
        # 退出时会有弹框提示用户是否确认退出
        reply = QMessageBox.question(None, '确认退出', '确定要退出吗？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            sys.exit(app.exec_())
       
class DisposeTab3(QtWidgets.QTabWidget):
    def __init__(self):
        super(DisposeTab2, self).__init__()
        self.ui2 = Ui_TabWidget3()
        self.ui2.setupUi(self)
    
    def list(self):     #打开文件夹
        ui2.textbox2.clear()
        ui2.listWidget2.clear()
        #QFileDialog.getExistingDirectory是一个方法，用于打开一个对话框，让用户选择一个文件夹。
        #参数None表示对话框的父窗口，'choose a file'是对话框的标题，'/'是对话框的默认路径，QFileDialog.ShowDirsOnly表示只显示文件夹而不显示文件。
        #这个方法会返回用户选择的文件夹的路径。
        global dir2, file2
        dir2 = QFileDialog.getExistingDirectory(None,'choose a file','/',QFileDialog.ShowDirsOnly)

        #检查用户是否点击了取消按钮或关闭了对话框
        if not dir2:
            return

        #输出文件列表
        file2 = os.listdir(dir2)
        for i in file2:
            file_path = os.path.join(dir2, i)
            item = QtWidgets.QListWidgetItem()
            item.setIcon(ui2.get_file_icon(file_path))
            item.setText(i)
            ui2.listWidget2.addItem(item)
        

    def touch(self):  #创建文件或文件夹
        try:
            #检查文件列表是否为空
            if ui2.listWidget2.count() == 0: 
                QMessageBox.warning(None, "警告", "请先打开文件夹以创建文件或文件夹。", QMessageBox.Ok)
                return
            
            while True:
                #打开一个对话框，让用户输入文件或文件夹名称
                file_or_folder_name, ok_pressed = QInputDialog.getText(None, "创建文件或文件夹", "输入文件（文件夹）名称:")
                
                #如果用户点击了取消按钮或者未输入名称，退出循环
                if not ok_pressed or not file_or_folder_name:
                    break
                
                file_path = os.path.join(dir2, file_or_folder_name)
                if '.' in file_or_folder_name:
                    reply = None
                    #检查文件是否已存在
                    if os.path.exists(file_path):  
                        #循环直到用户重新输入一个新的文件名或取消创建
                        while True:  
                            reply = QMessageBox.question(None, "警告", "文件已存在。是否要重新创建文件？", QMessageBox.Yes | QMessageBox.No)
                            #用户选择重新输入文件名，退出内层循环
                            if reply == QMessageBox.Yes:
                                break  
                            #用户选择取消创建，退出内层循环
                            elif reply == QMessageBox.No:
                                break  
                    #用户选择重新输入文件名，继续外层循环
                    if reply == QMessageBox.Yes:
                        continue 
                    #用户选择取消创建，退出外层循环
                    elif reply == QMessageBox.No:
                        break  
                    else:
                        #创建文件
                        with open(file_path, 'w') as file:
                            pass
                        file2 = os.listdir(dir2)
                        for i in file2:
                            file_path = os.path.join(dir2, i)
                            item = QtWidgets.QListWidgetItem()
                            item.setIcon(ui2.get_file_icon(file_path))
                            item.setText(i)
                            ui2.listWidget2.addItem(item)
                        #将新创建的文件名称添加到左侧的文件列表中
                        #文件创建成功，退出外层循环
                        break  
                else:
                    #检查文件夹是否已存在
                    if os.path.exists(file_path):  
                        QMessageBox.warning(None, "警告", "文件夹已存在。", QMessageBox.Ok)
                    else:
                        #创建文件夹
                        os.makedirs(file_path, exist_ok=True)
                        #将新创建的文件夹名称添加到左侧的文件列表中
                        file2 = os.listdir(dir2)
                        ui2.listWidget2.clear()
                        for i in file2:
                            file_path = os.path.join(dir2, i)
                            item = QtWidgets.QListWidgetItem()
                            item.setIcon(ui2.get_file_icon(file_path))
                            item.setText(i)
                            ui2.listWidget2.addItem(item)
                        break  
        except Exception as e:
            print(f"创建文件或文件夹时出现错误: {e}")

    def delete(self):   #删除文件（夹）
        try:
            #如果未选中文件，则弹出警示框
            current_item = ui2.listWidget2.currentItem()
            if current_item is None:
                QMessageBox.warning(None, "警告", "未选择任何文件!", QMessageBox.Ok)
                return
            
            #获取选中的文件
            file_name = current_item.text()
            #获取完整文件路径
            location = os.path.join(dir2, file_name)

            if os.path.exists(location):
                confirmation = QMessageBox.question(None, "确认删除",f"你确定要删除 '{file_name}' 吗？",QMessageBox.Yes | QMessageBox.No)
                #删除操作
                if confirmation == QMessageBox.Yes:
                    #根据文件或文件夹进行相应的删除
                    if os.path.isfile(location):
                        os.remove(location)
                        ui2.listWidget2.takeItem(ui2.listWidget2.row(current_item))
                    elif os.path.isdir(location):
                        shutil.rmtree(location)
                        ui2.listWidget2.takeItem(ui2.listWidget2.row(current_item))
                #如果取消，则返回到主界面
                else:
                    return
            else:
                QMessageBox.warning(None, "警告", "路径不存在!", QMessageBox.Ok)
        except FileNotFoundError:
            QMessageBox.warning(None, "警告", "文件不存在!", QMessageBox.Ok)
        except PermissionError:
            QMessageBox.warning(None, "警告", "没有权限删除文件!", QMessageBox.Ok)

    def open(self):     #打开文件(夹)
        try:
            #告诉解释器在该函数内使用全局的 dir 变量
            global dir2
            #获取当前选中的项目
            try:
                file_name = ui2.listWidget2.currentItem().text()
            except AttributeError:
                QMessageBox.warning(None, "警告", "请先选择一个文件(夹)!", QMessageBox.Ok)
                return
            position = dir2 + '/' + str(file_name)
            if os.path.isdir(position):
            #如果是文件夹，列出其内容
                #更新路径
                dir2 += '/' + str(file_name)
                ui2.textbox2.clear()
                ui2.listWidget2.clear()
                file_list = os.listdir(dir2)
                for i in file_list:
                    file_path = os.path.join(dir2, i)
                    item = QtWidgets.QListWidgetItem()
                    item.setIcon(ui2.get_file_icon(file_path))
                    item.setText(i)
                    ui2.listWidget2.addItem(item)
            else:
                try:
                    subprocess.Popen(['xdg-open', position])
                except: 
                    try:
                        #使用 chardet 库检测文件编码
                        with open(position, 'rb') as f:
                            detector = chardet.universaldetector.UniversalDetector()
                            for line in f:
                                detector.feed(line)
                                if detector.done:
                                    break
                            detector.close()
                            encoding = detector.result['encoding']
                        #尝试使用检测到的编码重新打开文件
                        with open(position, 'r', encoding=encoding) as f:
                            ui2.textbox2.clear()
                            data = f.read()
                            ui2.textbox2.setText(data)
                    except UnicodeDecodeError:
                        QMessageBox.warning(None, "警告", "文件编码无法解析，尝试使用其他编码！", QMessageBox.Ok)
                    except FileNotFoundError:
                        QMessageBox.warning(None, "警告", "文件未找到！", QMessageBox.Ok)
                    except PermissionError:
                        QMessageBox.warning(None, "警告", "没有权限访问文件！", QMessageBox.Ok)
                    except Exception:
                        QMessageBox.warning(None, "警告", "发生未知错误！", QMessageBox.Ok)
        except Exception:
            QMessageBox.warning(None, "警告", "发生未知错误！", QMessageBox.Ok)

    def rename(self):   #重命名
        item = ui2.listWidget2.currentItem()

        if item is not None:
            current_name = item.text()

            new_name, ok_pressed = QInputDialog.getText(None, "Rename", "Enter new name:", QLineEdit.Normal, current_name)

            if ok_pressed and new_name != current_name:
                old_path = os.path.join(dir2, current_name)
                new_path = os.path.join(dir2, new_name)

                #如果新名称不包含文件后缀，发出警告
                if '.' not in new_name:
                    QMessageBox.warning(None, "警告", "新文件名缺少文件后缀，请添加后缀。", QMessageBox.Ok)
                    return

                #如果修改了文件后缀，更新文件格式
                if new_name.split('.')[-1] != current_name.split('.')[-1]:
                    try:
                        #获取文件内容
                        with open(old_path, 'r', encoding='utf-8') as file:
                            data = file.read()

                        #修改文件后缀
                        with open(new_path, 'w', encoding='utf-8') as file:
                            file.write(data)

                        #删除原文件
                        os.remove(old_path)
                        item.setText(new_name)
                    except Exception as e:
                        QMessageBox.warning(None, "警告", "修改文件格式失败！", QMessageBox.Ok)
                        return
                else:
                    try:
                        os.rename(old_path, new_path)
                        item.setText(new_name)
                        print(f"成功重命名为: {new_name}")
                    except Exception as e:
                        print(f"重命名失败: {e}")
                        QMessageBox.warning(None, "警告", "重命名失败！", QMessageBox.Ok)
        else:
            QMessageBox.warning(None, "警告", "请选择需要重命名的文件", QMessageBox.Ok)

    def move(self):  #移动文件
        try:
            if ui2.listWidget2.currentItem() is None:
                #如果用户没有选择任何文件，弹出提示
                QMessageBox.information(None, "提示", "请先选择要移动的文件。")
                return
            
            file_name = ui2.listWidget2.currentItem().text()
            source = str(dir2) + '/' + str(file_name)

            #弹出文件对话框让用户选择目标文件夹
            destination = QFileDialog.getExistingDirectory(None, '选择目标文件夹', '/')

            if destination:  #如果用户选择了目标文件夹
                destination_path = os.path.join(destination, file_name)

                if os.path.exists(destination_path):
                    #如果目标文件已经存在，询问用户是否覆盖
                    reply = QMessageBox.question(None, '文件已存在', '目标文件夹已经存在同名文件，是否覆盖？',
                                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if reply == QMessageBox.Yes:
                        #覆盖已存在的文件
                        shutil.move(source, destination_path)
                    else:
                        #用户选择不覆盖，不执行移动操作
                        return
                else:
                    #目标文件夹不存在同名文件，正常移动
                    shutil.move(source, destination_path)

                #更新界面，从文件列表中移除已移动的文件
                ui2.listWidget2.takeItem(ui1.listWidget1.currentRow())
        except FileNotFoundError:
            QMessageBox.critical(None, "错误", "找不到文件或目录。")
        except PermissionError:
            QMessageBox.critical(None, "错误", "没有权限执行操作。")
        except Exception as e:
            #如果发生其他异常，弹出错误对话框显示错误信息
            QMessageBox.critical(None, "Error", f"移动文件时发生错误：{str(e)}")

    def back(self):
        #处理返回按钮的逻辑
        global dir2
        current_dir = os.path.abspath(dir2)
        parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

        if current_dir != parent_dir:
            # 如果当前目录不是根目录，返回上一级目录
            dir2 = parent_dir
            ui2.textbox2.clear()
            ui2.listWidget2.clear()

            file_list = os.listdir(dir2)
            for i in file_list:
                file_path = os.path.join(dir2, i)
                item = QtWidgets.QListWidgetItem()
                item.setIcon(ui2.get_file_icon(file_path))
                item.setText(i)
                ui2.listWidget2.addItem(item)


    def quit(self):     # 退出软件
        # 退出时会有弹框提示用户是否确认退出
        reply = QMessageBox.question(None, '确认退出', '确定要退出吗？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            sys.exit(app.exec_())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    TabWidget = QtWidgets.QTabWidget()
    ui = Ui_TabWidget()
    ui.setupUi(TabWidget)
    ui1 = Ui_TabWidget2()
    ui1.setupUi(TabWidget)
    ui2 = Ui_TabWidget3()
    ui2.setupUi(TabWidget)

    TabWidget.show()

    sys.exit(app.exec_())
