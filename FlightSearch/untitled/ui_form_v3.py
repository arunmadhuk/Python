# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGroupBox,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_FlightSearch(object):
    def setupUi(self, FlightSearch):
        if not FlightSearch.objectName():
            FlightSearch.setObjectName(u"FlightSearch")
        FlightSearch.resize(510, 550)
        FlightSearch.setMinimumSize(QSize(510, 550))
        FlightSearch.setMaximumSize(QSize(510, 550))
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(12)
        FlightSearch.setFont(font)
        icon = QIcon()
        icon.addFile(u"flight.png", QSize(), QIcon.Normal, QIcon.Off)
        FlightSearch.setWindowIcon(icon)
        self.centralwidget = QWidget(FlightSearch)
        self.centralwidget.setObjectName(u"centralwidget")
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setPointSize(10)
        self.centralwidget.setFont(font1)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(0, -30, 511, 561))
        self.widget = QWidget(self.groupBox_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 310, 491, 166))
        self.horizontalLayout_7 = QHBoxLayout(self.widget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.groupBox_passengers = QGroupBox(self.widget)
        self.groupBox_passengers.setObjectName(u"groupBox_passengers")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_passengers.sizePolicy().hasHeightForWidth())
        self.groupBox_passengers.setSizePolicy(sizePolicy)
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_passengers)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(self.groupBox_passengers)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(self.groupBox_passengers)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.label_6)

        self.label_7 = QLabel(self.groupBox_passengers)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.sb_adults = QSpinBox(self.groupBox_passengers)
        self.sb_adults.setObjectName(u"sb_adults")

        self.verticalLayout_3.addWidget(self.sb_adults)

        self.sb_childrens = QSpinBox(self.groupBox_passengers)
        self.sb_childrens.setObjectName(u"sb_childrens")

        self.verticalLayout_3.addWidget(self.sb_childrens)

        self.sb_infants = QSpinBox(self.groupBox_passengers)
        self.sb_infants.setObjectName(u"sb_infants")

        self.verticalLayout_3.addWidget(self.sb_infants)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)


        self.horizontalLayout_7.addWidget(self.groupBox_passengers)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.groupBox_5 = QGroupBox(self.widget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.rb_economy = QRadioButton(self.groupBox_5)
        self.rb_economy.setObjectName(u"rb_economy")
        self.rb_economy.setChecked(True)

        self.verticalLayout_2.addWidget(self.rb_economy)

        self.rb_business = QRadioButton(self.groupBox_5)
        self.rb_business.setObjectName(u"rb_business")

        self.verticalLayout_2.addWidget(self.rb_business)

        self.rb_firstclass = QRadioButton(self.groupBox_5)
        self.rb_firstclass.setObjectName(u"rb_firstclass")

        self.verticalLayout_2.addWidget(self.rb_firstclass)


        self.horizontalLayout_7.addWidget(self.groupBox_5)

        self.widget1 = QWidget(self.groupBox_2)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(20, 500, 461, 35))
        self.horizontalLayout_6 = QHBoxLayout(self.widget1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_reset = QPushButton(self.widget1)
        self.btn_reset.setObjectName(u"btn_reset")

        self.horizontalLayout_6.addWidget(self.btn_reset)

        self.horizontalSpacer_9 = QSpacerItem(138, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)

        self.btn_generate = QPushButton(self.widget1)
        self.btn_generate.setObjectName(u"btn_generate")

        self.horizontalLayout_6.addWidget(self.btn_generate)

        self.widget2 = QWidget(self.groupBox_2)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(10, 130, 491, 91))
        self.horizontalLayout = QHBoxLayout(self.widget2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox_departure = QGroupBox(self.widget2)
        self.groupBox_departure.setObjectName(u"groupBox_departure")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_departure.sizePolicy().hasHeightForWidth())
        self.groupBox_departure.setSizePolicy(sizePolicy2)
        self.cmb_departure = QComboBox(self.groupBox_departure)
        self.cmb_departure.setObjectName(u"cmb_departure")
        self.cmb_departure.setGeometry(QRect(14, 41, 200, 32))
        sizePolicy2.setHeightForWidth(self.cmb_departure.sizePolicy().hasHeightForWidth())
        self.cmb_departure.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.groupBox_departure)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.groupBox_destination = QGroupBox(self.widget2)
        self.groupBox_destination.setObjectName(u"groupBox_destination")
        sizePolicy2.setHeightForWidth(self.groupBox_destination.sizePolicy().hasHeightForWidth())
        self.groupBox_destination.setSizePolicy(sizePolicy2)
        self.cmb_destination = QComboBox(self.groupBox_destination)
        self.cmb_destination.setObjectName(u"cmb_destination")
        self.cmb_destination.setGeometry(QRect(14, 41, 200, 32))

        self.horizontalLayout.addWidget(self.groupBox_destination)

        self.widget3 = QWidget(self.groupBox_2)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(10, 41, 491, 83))
        self.horizontalLayout_3 = QHBoxLayout(self.widget3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.groupBox_journey = QGroupBox(self.widget3)
        self.groupBox_journey.setObjectName(u"groupBox_journey")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_journey.sizePolicy().hasHeightForWidth())
        self.groupBox_journey.setSizePolicy(sizePolicy3)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_journey)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.rb_oneway = QRadioButton(self.groupBox_journey)
        self.rb_oneway.setObjectName(u"rb_oneway")
        self.rb_oneway.setChecked(True)

        self.horizontalLayout_2.addWidget(self.rb_oneway)

        self.rb_roundtrip = QRadioButton(self.groupBox_journey)
        self.rb_roundtrip.setObjectName(u"rb_roundtrip")

        self.horizontalLayout_2.addWidget(self.rb_roundtrip)

        self.rb_multicity = QRadioButton(self.groupBox_journey)
        self.rb_multicity.setObjectName(u"rb_multicity")

        self.horizontalLayout_2.addWidget(self.rb_multicity)


        self.horizontalLayout_3.addWidget(self.groupBox_journey)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.widget4 = QWidget(self.groupBox_2)
        self.widget4.setObjectName(u"widget4")
        self.widget4.setGeometry(QRect(10, 220, 491, 91))
        self.horizontalLayout_4 = QHBoxLayout(self.widget4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.groupBox_date = QGroupBox(self.widget4)
        self.groupBox_date.setObjectName(u"groupBox_date")
        sizePolicy2.setHeightForWidth(self.groupBox_date.sizePolicy().hasHeightForWidth())
        self.groupBox_date.setSizePolicy(sizePolicy2)
        self.groupBox_date.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.dt_departure = QDateEdit(self.groupBox_date)
        self.dt_departure.setObjectName(u"dt_departure")
        self.dt_departure.setGeometry(QRect(30, 40, 150, 33))

        self.horizontalLayout_4.addWidget(self.groupBox_date)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.groupBox = QGroupBox(self.widget4)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.dt_return = QDateEdit(self.groupBox)
        self.dt_return.setObjectName(u"dt_return")
        self.dt_return.setGeometry(QRect(40, 40, 150, 33))

        self.horizontalLayout_4.addWidget(self.groupBox)

        FlightSearch.setCentralWidget(self.centralwidget)
        self.groupBox_2.raise_()
        self.statusbar = QStatusBar(FlightSearch)
        self.statusbar.setObjectName(u"statusbar")
        FlightSearch.setStatusBar(self.statusbar)

        self.retranslateUi(FlightSearch)

        QMetaObject.connectSlotsByName(FlightSearch)
    # setupUi

    def retranslateUi(self, FlightSearch):
        FlightSearch.setWindowTitle(QCoreApplication.translate("FlightSearch", u"Flight Search JSON Report Generator", None))
        self.groupBox_2.setTitle("")
        self.groupBox_passengers.setTitle(QCoreApplication.translate("FlightSearch", u"Passengers", None))
        self.label_5.setText(QCoreApplication.translate("FlightSearch", u"Adults", None))
        self.label_6.setText(QCoreApplication.translate("FlightSearch", u"Childrens", None))
        self.label_7.setText(QCoreApplication.translate("FlightSearch", u"Infants", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("FlightSearch", u"Cabin Type", None))
        self.rb_economy.setText(QCoreApplication.translate("FlightSearch", u"Economy", None))
        self.rb_business.setText(QCoreApplication.translate("FlightSearch", u"Business", None))
        self.rb_firstclass.setText(QCoreApplication.translate("FlightSearch", u"First Class", None))
        self.btn_reset.setText(QCoreApplication.translate("FlightSearch", u"Reset", None))
        self.btn_generate.setText(QCoreApplication.translate("FlightSearch", u"Generate", None))
        self.groupBox_departure.setTitle(QCoreApplication.translate("FlightSearch", u"Departure", None))
        self.groupBox_destination.setTitle(QCoreApplication.translate("FlightSearch", u"Destination", None))
        self.groupBox_journey.setTitle(QCoreApplication.translate("FlightSearch", u"Journey Type", None))
        self.rb_oneway.setText(QCoreApplication.translate("FlightSearch", u"One Way", None))
        self.rb_roundtrip.setText(QCoreApplication.translate("FlightSearch", u"Round Trip", None))
        self.rb_multicity.setText(QCoreApplication.translate("FlightSearch", u"Multi City", None))
        self.groupBox_date.setTitle(QCoreApplication.translate("FlightSearch", u"Departure", None))
        self.groupBox.setTitle(QCoreApplication.translate("FlightSearch", u"Return", None))
    # retranslateUi

