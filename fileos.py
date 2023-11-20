import sys
import re
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

        #创建一个标签页
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

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

        self.quit = QtWidgets.QPushButton(self.tab)
        self.quit.setGeometry(QtCore.QRect(600, 510, 75, 23))
        self.quit.setObjectName("quit")

        #将标签页添加到 TabWidget 中
        TabWidget.addTab(self.tab,"")

        #连接按钮的点击事件到相应的处理函数
        self.list_file.clicked.connect(dispose.list)
        self.touch.clicked.connect(dispose.touch)
        self.dele.clicked.connect(dispose.delete)
        self.open.clicked.connect(dispose.open)
        self.move.clicked.connect(dispose.move)
        self.rename.clicked.connect(dispose.rename)
        self.quit.clicked.connect(dispose.quit)

        self.listWidget.itemDoubleClicked.connect(dispose.open)

        #根据当前的语言设置重新加载并显示对应的翻译文本
        self.retranslateUi(TabWidget)
        #将当前的TabWidget的索引设置为0，这意味着它将显示第一个选项卡
        TabWidget.setCurrentIndex(0)
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
        self.quit.setText(_translate("TabWidget", "退出"))
        self.textbox.setText(_translate("TabWidget",""))

class dispose(QtWidgets.QTabWidget):

    def __init__(self):
        super(dispose, self).__init__()
        self.ui = Ui_TabWidget()
        self.ui.setupUi(self)

    def list(self):     #打开文件夹
        ui.textbox.clear()
        ui.listWidget.clear()
        #QFileDialog.getExistingDirectory是一个方法，用于打开一个对话框，让用户选择一个文件夹。
        #参数None表示对话框的父窗口，'choose a file'是对话框的标题，'E:/'是对话框的默认路径，QFileDialog.ShowDirsOnly表示只显示文件夹而不显示文件。
        #这个方法会返回用户选择的文件夹的路径。
        global dir, file
        dir = QFileDialog.getExistingDirectory(None,'choose a file','E:/',QFileDialog.ShowDirsOnly)
        file = os.listdir(dir)
        for i in file:
            ui.listWidget.addItem(i)

    def touch(self):  # 创建文件或文件夹
        try:
            # 获取最后打开的文件夹路径
            last_opened_directory = os.path.dirname(dir) if 'dir' in globals() else ''
            # 打开一个对话框，让用户输入文件或文件夹名称
            file_or_folder_name, ok_pressed = QInputDialog.getText(None, "创建文件或文件夹", "输入文件（文件夹）名称:")
        
            # 如果用户点击了对话框的OK按钮并且输入了名称
            if ok_pressed and file_or_folder_name:
                file_path = os.path.join(dir, file_or_folder_name)
                if '.' in file_or_folder_name:
                    # 创建文件
                    with open(file_path, 'w') as file:
                        pass  # 在这里进行文件操作，比如写入内容
                    print(f"文件 '{file_path}' 创建成功。")
                else:
                    # 创建文件夹
                    os.makedirs(file_path, exist_ok=True)
                    print(f"文件夹 '{file_path}' 创建成功。")
            
                # 将新创建的文件或文件夹名称添加到左侧的文件列表中
                ui.listWidget.addItem(file_or_folder_name)
        except Exception as e:
            print(f"创建文件或文件夹时出现错误: {e}")
            
    def delete(self):   #删除文件
        row = ui.listWidget.currentRow()
        file_name = ui.listWidget.currentItem().text()
        os.remove(str(dir) + "/" + str(file_name))
        ui.listWidget.takeItem(row)

    def open(self):     #打开文件(夹)
        try:
            # 告诉解释器在该函数内使用全局的 dir 变量
            global dir
            # 获取当前选中的项目
            try:
                file_name = ui.listWidget.currentItem().text()
            except AttributeError:
                QMessageBox.warning(None, "警告", "请先选择一个文件(夹)!", QMessageBox.Ok)
                return
            position = dir + '/' + str(file_name)
            if os.path.isdir(position):
            # 如果是文件夹，列出其内容
                # 更新路径
                dir += '/' + str(file_name)
                ui.textbox.clear()
                ui.listWidget.clear()
                file_list = os.listdir(dir)
                for i in file_list:
                    ui.listWidget.addItem(i)
            else:
                try:
                    subprocess.Popen(['xdg-open', position])
                except:
                    try:
                        # 使用 chardet 库检测文件编码
                        with open(position, 'rb') as f:
                            detector = chardet.universaldetector.UniversalDetector()
                            for line in f:
                                detector.feed(line)
                                if detector.done:
                                    break
                            detector.close()
                            encoding = detector.result['encoding']
                        # 尝试使用检测到的编码重新打开文件
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

    def rename(self):
        item = ui.listWidget.currentItem()

        if item is not None:
            current_name = item.text()

            new_name, ok_pressed = QInputDialog.getText(None, "Rename", "Enter new name:", QLineEdit.Normal, current_name)

            if ok_pressed and new_name != current_name:
                old_path = os.path.join(dir, current_name)
                new_path = os.path.join(dir, new_name)

                try:
                    os.rename(old_path, new_path)
                    item.setText(new_name)
                    print(f"成功重命名为: {new_name}")
                except Exception as e:
                    print(f"重命名失败: {e}")
        else:
            QMessageBox.warning(None, "警告", "请选择需要重命名的文件", QMessageBox.Ok)

    def move(self):  # 移动文件
        try:
            if ui.listWidget.currentItem() is None:
                # 如果用户没有选择任何文件，弹出提示
                QMessageBox.information(None, "提示", "请先选择要移动的文件。")
                return
            
            file_name = ui.listWidget.currentItem().text()
            source = str(dir) + '/' + str(file_name)

            # 弹出文件对话框让用户选择目标文件夹
            destination = QFileDialog.getExistingDirectory(None, '选择目标文件夹', 'C:/')

            if destination:  # 如果用户选择了目标文件夹
                destination_path = os.path.join(destination, file_name)

                if os.path.exists(destination_path):
                    # 如果目标文件已经存在，询问用户是否覆盖
                    reply = QMessageBox.question(None, '文件已存在', '目标文件夹已经存在同名文件，是否覆盖？',
                                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if reply == QMessageBox.Yes:
                        # 覆盖已存在的文件
                        shutil.move(source, destination_path)
                    else:
                        # 用户选择不覆盖，不执行移动操作
                        return
                else:
                    # 目标文件夹不存在同名文件，正常移动
                    shutil.move(source, destination_path)

                # 更新界面，从文件列表中移除已移动的文件
                ui.listWidget.takeItem(ui.listWidget.currentRow())
        except FileNotFoundError:
            QMessageBox.critical(None, "错误", "找不到文件或目录。")
        except PermissionError:
            QMessageBox.critical(None, "错误", "没有权限执行操作。")
        except Exception as e:
            # 如果发生其他异常，弹出错误对话框显示错误信息
            QMessageBox.critical(None, "Error", f"移动文件时发生错误：{str(e)}")

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
    TabWidget.show()
    sys.exit(app.exec_())
