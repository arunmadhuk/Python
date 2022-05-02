# -*- coding: utf-8 -*-
"""
A Simple GUI tool to read the TMS Logs efficiently with filtering options.
"""
import os
import sys
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class LogReaderUI(QMainWindow):

    log_types = ["AssetLibrary","GDC TMS","IngestDaemon","IntegratedReport", "Prometheus",
                 "Template", "TmsConnect", "TmsService", "TransferService", "WebService"]
    user_log_filter_options = ["-----------", "Automator", "AutoSPL Backup", "POS", "TM"]

    def __init__(self):
        super(LogReaderUI, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("LogReaderUI")
        self.resize(1178, 853)
        self.setWindowIcon(QIcon('Logo_bw.png'))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 1161, 821))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(613, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.tbl_log = QtWidgets.QTableView(self.layoutWidget)
        self.tbl_log.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tbl_log.setObjectName("tbl_log")
        self.verticalLayout.addWidget(self.tbl_log)
        self.gridLayout.addLayout(self.verticalLayout, 4, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_filter_option = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_filter_option.sizePolicy().hasHeightForWidth())
        self.lbl_filter_option.setSizePolicy(sizePolicy)
        self.lbl_filter_option.setObjectName("lbl_filter_option")
        self.horizontalLayout.addWidget(self.lbl_filter_option)
        self.cmbbx_filter_option = QtWidgets.QComboBox(self.layoutWidget)
        self.cmbbx_filter_option.setObjectName("cmbbx_filter_option")
        self.horizontalLayout.addWidget(self.cmbbx_filter_option)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.lbl_start_date = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_start_date.sizePolicy().hasHeightForWidth())
        self.lbl_start_date.setSizePolicy(sizePolicy)
        self.lbl_start_date.setObjectName("lbl_start_date")
        self.horizontalLayout.addWidget(self.lbl_start_date)
        self.dt_start_date = QtWidgets.QDateEdit(self.layoutWidget, calendarPopup=True)
        # self.dt_start_date.calendarPopup(self,True)
        self.dt_start_date.setObjectName("dt_start_date")
        self.dt_start_date.setDate(datetime.now().date())
        self.dt_start_date.setDisplayFormat("dd MMM yyyy")
        self.horizontalLayout.addWidget(self.dt_start_date)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.lbl_end_date = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_end_date.sizePolicy().hasHeightForWidth())
        self.lbl_end_date.setSizePolicy(sizePolicy)
        self.lbl_end_date.setObjectName("lbl_end_date")
        self.horizontalLayout.addWidget(self.lbl_end_date)
        self.dt_end_date = QtWidgets.QDateEdit(self.layoutWidget, calendarPopup=True)
        self.dt_end_date.setDate(datetime.now().date())
        self.dt_end_date.setObjectName("dt_end_date")
        self.dt_end_date.setDisplayFormat("dd MMM yyyy")
        self.horizontalLayout.addWidget(self.dt_end_date)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.btn_apply = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_apply.setObjectName("btn_apply")
        self.horizontalLayout.addWidget(self.btn_apply)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_filter_option_2 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_filter_option_2.sizePolicy().hasHeightForWidth())
        self.lbl_filter_option_2.setSizePolicy(sizePolicy)
        self.lbl_filter_option_2.setObjectName("lbl_filter_option_2")
        self.horizontalLayout_2.addWidget(self.lbl_filter_option_2)
        self.le_folder_path = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_folder_path.sizePolicy().hasHeightForWidth())
        self.le_folder_path.setSizePolicy(sizePolicy)
        self.le_folder_path.setObjectName("le_folder_path")
        self.horizontalLayout_2.addWidget(self.le_folder_path)
        self.btn_folder_browse = QtWidgets.QToolButton(self.layoutWidget)
        self.btn_folder_browse.setObjectName("btn_folder_browse")
        self.horizontalLayout_2.addWidget(self.btn_folder_browse)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.lbl_filter_option_3 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_filter_option_3.sizePolicy().hasHeightForWidth())
        self.lbl_filter_option_3.setSizePolicy(sizePolicy)
        self.lbl_filter_option_3.setObjectName("lbl_filter_option_3")
        self.horizontalLayout_2.addWidget(self.lbl_filter_option_3)
        self.cmbbx_log_types = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbbx_log_types.sizePolicy().hasHeightForWidth())
        self.cmbbx_log_types.setSizePolicy(sizePolicy)
        self.cmbbx_log_types.setObjectName("cmbbx_log_types")
        self.cmbbx_log_types.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.horizontalLayout_2.addWidget(self.cmbbx_log_types)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)

        self.btn_folder_browse.clicked.connect(self.browse_log_files)
        self.cmbbx_log_types.currentTextChanged.connect(self.selected_log_type_filter)
        self.retranslateUi()
        # QtCore.QMetaObject.connectSlotsByName(LogReaderUI)
        self.update_filter_options(self.user_log_filter_options)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("LogReaderUI", "TMS Log Reader"))
        self.lbl_filter_option.setText(_translate("LogReaderUI", "Select Option:"))
        self.lbl_start_date.setText(_translate("LogReaderUI", "Select Start Date:"))
        self.lbl_end_date.setText(_translate("LogReaderUI", "Select End Date:"))
        self.btn_apply.setText(_translate("LogReaderUI", "Apply"))
        self.lbl_filter_option_2.setText(_translate("LogReaderUI", "Select Log Path:"))
        self.btn_folder_browse.setText(_translate("LogReaderUI", "..."))
        self.lbl_filter_option_3.setText(_translate("LogReaderUI", "Select Logs:"))

    def update_filter_options(self, filter_options):
        self.cmbbx_filter_option.addItems(filter_options)

    def set_start_and_end_date(self, dates):
        start_date = datetime.strptime(dates[0], '%Y-%m-%d').date()
        end_date = datetime.strptime(dates[-1], '%Y-%m-%d').date()
        print("qstart_date {}".format(start_date))
        print("qend_date {}".format(end_date))
        self.dt_start_date.setDate(start_date)
        self.dt_start_date.setDateRange(start_date, end_date)
        self.dt_end_date.setDate(end_date)
        self.dt_end_date.setDateRange(start_date, end_date)

    def show_dialog_box(self, setIcon, setText, setWindowTitle, setStandardButtons):
        msg_box = QMessageBox()
        msg_box.setIcon(setIcon)
        msg_box.setText(setText)
        msg_box.setWindowTitle(setWindowTitle)
        msg_box.setStandardButtons(setStandardButtons)
        msg_box.exec_()

    def selected_log_type_filter(self, selected_log_type):
        print(selected_log_type)


    def browse_log_files(self):
        log_folder_path = QFileDialog.getExistingDirectory(self, "Choose TMS Log Path", "D:\\Logs\\Malaysia")
        print("selected path --- {}".format(log_folder_path))
        if self.is_tms_log_folder(log_folder_path):
            self.le_folder_path.setText(log_folder_path)
        else:
            setIcon = QMessageBox.Information
            setText = "Selcted folder doesnt seems to be valid TMS Logs folder"
            setWindowTitle ="Invalid Fodler"
            setStandardButtons = QMessageBox.Ok | QMessageBox.Cancel
            self.show_dialog_box(setIcon, setText, setWindowTitle, setStandardButtons)

    def is_tms_log_folder(self, selected_path):
        child_directories = [f.name for f in os.scandir(selected_path) if f.is_dir()]
        check = any(item in self.log_types for item in child_directories)
        if check:
            if "GDC TMS" in child_directories:
                child_directories.remove("GDC TMS")
                tms_log_path = os.path.join(selected_path, "GDC TMS")
                grand_childs = [s.name for s in os.scandir(tms_log_path) if s.is_dir()]
                print(grand_childs)
                for grand_child in grand_childs:
                    child_directories.append("GDC TMS - " + grand_child)

            self.cmbbx_log_types.addItem("----------")
            self.cmbbx_log_types.addItems(child_directories)
            # self.cmbbx_log_types.setCurrentIndex(-1)
            self.cmbbx_log_types.model().sort(0)
            return True
        else:
            return False

    def initialize_log_reader(self, log_file_path):
        year = datetime.now().year
        # log_file_path = "D:/Logs/Malaysia/Dadi Cinema/Dadi Pavilion 15-04-22/TmsLogsExport_20220415104013"
        gdc_tms_log_folder = "GDC TMS\\log\\{}".format(year)
        gdc_tms_user_log_folder = "GDC TMS\\UserLogs\\{}".format(year)
        gdc_tms_log_path = os.path.join(log_file_path, gdc_tms_log_folder)
        print("gdc_tms_log_folder {}".format(gdc_tms_log_path))
        log_files, self.log_dates = self.get_log_files(gdc_tms_log_path)
        self.set_start_and_end_date(self.log_dates)

        print("log_files  {} ".format(log_files))

        gdc_tms_user_log_path = os.path.join(log_file_path, gdc_tms_user_log_folder)
        print("gdc_tms_user_log_folder {}".format(gdc_tms_user_log_path))
        usr_log_files, usr_log_dates = self.get_log_files(gdc_tms_user_log_path)

        print("usr_log_files  {} ".format(usr_log_files))
        print("usr_log_files start date -- {}".format(usr_log_dates[0]))
        print("usr_log_files End date -- {}".format(usr_log_dates[-1]))

    def get_log_files(self, log_path):
        dates = []
        if os.path.exists(log_path):
            logs = os.listdir(log_path)
            for log_file in logs:
                log_date = log_file.split(".log")[0]
                dates.append(log_date)
                # log_datetime= datetime.strptime(log_date,"%Y-%m-%d")
                # print("log_datetime --- {}".format(log_datetime))
                # print("log_datetime month --- {}".format(log_datetime.month))
        else:
            raise Exception("The path {} doesn't exists".format(log_path))

        return logs, dates


if __name__ == '__main__':
    app = QApplication([])
    ex = LogReaderUI()
    log_file_path = "D:\\Python\\tms_log\\TmsLogsExport_20220426013813"
    ex.initialize_log_reader(log_file_path)
    ex.show()
    app.exec_()
