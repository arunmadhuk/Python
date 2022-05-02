# -*- coding: utf-8 -*-

################################################################################
##
##
## Plugin JSON Manager
##
##
################################################################################
import os
import json
import PySide2
import sys
# import maya.cmds as cmds

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.classifiedObjects = {}
        self.tempDict = {}
        self.objSelected = None

        self.setMinimumSize(500, 450)
        # self.resize(500, 450)
        self.windowTitle = u"QC Classifier"
        self.setWindowIcon(QIcon('hierarchy.png'))
        self.setWindowTitle(self.windowTitle)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")

        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setSizeIncrement(QSize(0, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 534, 640))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        # Add Object Button
        self.addButton = QPushButton(self.scrollAreaWidgetContents)
        self.addButton.setObjectName(u"addButton")
        self.addButton.clicked.connect(self.addSelectedObject)
        # self.addButton.setEnabled(False)
        self.addButton.setText(u"Add")

        # Remove Object Button
        self.removeButton = QPushButton(self.scrollAreaWidgetContents)
        self.removeButton.setObjectName(u"removeButton")
        self.removeButton.clicked.connect(self.removeSelectedObject)
        self.removeButton.setEnabled(False)
        self.removeButton.setText(u"Remove")

        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        self.objectListWidget = QListWidget(self.scrollAreaWidgetContents)
        self.objectListWidget.setObjectName(u"objectListWidget")
        sizePolicy.setHeightForWidth(self.objectListWidget.sizePolicy().hasHeightForWidth())
        self.objectListWidget.setSizePolicy(sizePolicy)
        self.objectListWidget.itemClicked.connect(self.objectListWidgetSelection)

        self.setGroupListWidget = QListWidget(self.scrollAreaWidgetContents)
        self.setGroupListWidget.setObjectName(u"categoryListWidget")
        sizePolicy.setHeightForWidth(self.setGroupListWidget.sizePolicy().hasHeightForWidth())
        self.setGroupListWidget.setSizePolicy(sizePolicy)
        self.setGroupListWidget.setFocusPolicy(Qt.NoFocus)
        self.setGroupListWidget.itemClicked.connect(self.categorySelection)

        self.horizontalSpacer_6 = QSpacerItem(10, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.verticalSpacer_2 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_2.addWidget(self.objectListWidget, 0, 2, 1, 2)
        self.gridLayout_2.addItem(self.verticalSpacer_2, 1, 2, 1, 1)
        self.gridLayout_2.addItem(self.horizontalSpacer_6, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.addButton, 2, 2, 1, 1)
        self.gridLayout_2.addWidget(self.removeButton, 2, 3, 1, 1)
        self.gridLayout_2.addWidget(self.setGroupListWidget, 0, 0, 3, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(15)
        sizePolicy1.setVerticalStretch(2)

        # Start Process
        self.updateButton = QPushButton(self.centralwidget)
        self.updateButton.setObjectName(u"updateButton")
        # self.updateButton.clicked.connect(self.createSets)
        sizePolicy1.setHeightForWidth(self.updateButton.sizePolicy().hasHeightForWidth())
        self.updateButton.setSizePolicy(sizePolicy1)
        self.updateButton.setText(u"Update Set")

        # Cancel Process
        self.cancelButton = QPushButton(self.centralwidget)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.clicked.connect(self.cancelProcess)
        sizePolicy1.setHeightForWidth(self.cancelButton.sizePolicy().hasHeightForWidth())
        self.cancelButton.setSizePolicy(sizePolicy1)
        self.cancelButton.setText(u"Cancel")

        self.bottom_horizontalSpacer_1 = QSpacerItem(120, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.bottom_horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.bottom_horizontalSpacer_3 = QSpacerItem(120, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.bottom_horizontalSpacer_1)
        self.horizontalLayout_2.addWidget(self.updateButton)
        self.horizontalLayout_2.addItem(self.bottom_horizontalSpacer_2)
        self.horizontalLayout_2.addWidget(self.cancelButton)
        self.horizontalLayout_2.addItem(self.bottom_horizontalSpacer_3)

        self.verticalSpacer = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.verticalSpacer_4 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)
        self.gridLayout.addItem(self.verticalSpacer_3, 4, 0, 1, 1)
        self.gridLayout.addItem(self.verticalSpacer_4, 0, 0, 1, 1)

        self.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)

        QWidget.setTabOrder(self.scrollArea, self.setGroupListWidget)
        QWidget.setTabOrder(self.setGroupListWidget, self.objectListWidget)
        QWidget.setTabOrder(self.objectListWidget, self.addButton)
        QWidget.setTabOrder(self.addButton, self.removeButton)

        self.classifiers = None
        self.groupSet = None
        self.setName = None

        self.load_classifier_json()

        self.initializeUI()

        # QMetaObject.connectSlotsByName(self)


    def objectListWidgetSelection(self):
        self.removeButton.setEnabled(True)

    def addSelectedObject(self):
        objectsList = []
        if self.setName in self.classifiedObjects:
            self.classifiedObjects.pop(self.setName)

        

    def removeSelectedObject(self):
        index = self.objectListWidget.currentRow()
        value = self.objectListWidget.currentItem().text()

        if index >= 0:
            self.objectListWidget.takeItem(index)
            self.classifiedObjects[self.setName].remove(value)

            if self.objectListWidget.count() == 0:
                self.removeButton.setEnabled(False)

    def cancelProcess(self):
        self.classifiedObjects = {}
        self.load_existing_sets()
        self.initializeUI()

    def categorySelection(self, item):
        self.objectListWidget.clear()
        self.setName = item.text()
        keys = self.classifiedObjects.keys()
        if self.setName in keys:
            values = self.classifiedObjects[self.setName]
            for value in values:
                self.objectListWidget.addItem(QListWidgetItem(value))
        else:
            return

    def load_classifier_json(self):
        """
        Loads the "classifier.json" file from the environment variable "OPENPYPE_PLUGINS_DIR"
        """
        print("load json")
        # plugin_env = os.getenv("OPENPYPE_PLUGINS_DIR")
        # plugin_dir = plugin_env.replace("\openpype\plugins", "")
        plugin_dir = "D:/Python/Plugin_JSON"
        json_file_path = os.path.join(plugin_dir, "classifier.json")
        json_file = open(json_file_path)
        self.classifiers = json.load(json_file)
        json_file.close()

    def initializeUI(self):
        self.setGroupListWidget.clear()
        self.objectListWidget.clear()
        # if self.classifiers is not None:
        #     for item in self.classifiers.keys():
        #         self.setGroupListWidget.addItem(QListWidgetItem(item))
        #
        #     first_key = self.classifiers.keys()[0]
        #     # print first_key
        #     if first_key in self.classifiedObjects.keys():
        #         values = self.classifiedObjects[first_key]
        #         # print item , " --- ", values
        #         for value in values:
        #             self.objectListWidget.addItem(QListWidgetItem(value))
   


if __name__ == '__main__':
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    fb = MainWindow()
    fb.show()
