# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainQtGui.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1265, 864)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.visModeButton = QtWidgets.QPushButton(self.centralwidget)
        self.visModeButton.setObjectName("visModeButton")
        self.gridLayout.addWidget(self.visModeButton, 0, 3, 1, 2)
        self.infoWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infoWidget.sizePolicy().hasHeightForWidth())
        self.infoWidget.setSizePolicy(sizePolicy)
        self.infoWidget.setObjectName("infoWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.infoWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.selection1label = QtWidgets.QLabel(self.infoWidget)
        self.selection1label.setObjectName("selection1label")
        self.gridLayout_2.addWidget(self.selection1label, 0, 5, 1, 1)
        self.selection1 = QtWidgets.QLabel(self.infoWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selection1.sizePolicy().hasHeightForWidth())
        self.selection1.setSizePolicy(sizePolicy)
        self.selection1.setObjectName("selection1")
        self.gridLayout_2.addWidget(self.selection1, 0, 4, 1, 1)
        self.status = QtWidgets.QLabel(self.infoWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status.sizePolicy().hasHeightForWidth())
        self.status.setSizePolicy(sizePolicy)
        self.status.setObjectName("status")
        self.gridLayout_2.addWidget(self.status, 0, 0, 1, 1)
        self.selection2label = QtWidgets.QLabel(self.infoWidget)
        self.selection2label.setObjectName("selection2label")
        self.gridLayout_2.addWidget(self.selection2label, 0, 7, 1, 1)
        self.statusLabel = QtWidgets.QLabel(self.infoWidget)
        self.statusLabel.setObjectName("statusLabel")
        self.gridLayout_2.addWidget(self.statusLabel, 0, 1, 1, 1)
        self.selection2 = QtWidgets.QLabel(self.infoWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selection2.sizePolicy().hasHeightForWidth())
        self.selection2.setSizePolicy(sizePolicy)
        self.selection2.setObjectName("selection2")
        self.gridLayout_2.addWidget(self.selection2, 0, 6, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.infoWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMaximumSize(QtCore.QSize(150, 16777215))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 0, 2, 1, 1)
        self.line = QtWidgets.QFrame(self.infoWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.infoWidget, 3, 0, 1, 10)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 940, 708))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 2, 0, 1, 8)
        self.statisticsButton = QtWidgets.QPushButton(self.centralwidget)
        self.statisticsButton.setObjectName("statisticsButton")
        self.gridLayout.addWidget(self.statisticsButton, 0, 2, 1, 1)
        self.analysisButton = QtWidgets.QPushButton(self.centralwidget)
        self.analysisButton.setObjectName("analysisButton")
        self.gridLayout.addWidget(self.analysisButton, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 5, 1, 1)
        self.filterFrame = QtWidgets.QFrame(self.centralwidget)
        self.filterFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.filterFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.filterFrame.setObjectName("filterFrame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.filterFrame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.zoomSliderLabel = QtWidgets.QLabel(self.filterFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoomSliderLabel.sizePolicy().hasHeightForWidth())
        self.zoomSliderLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.zoomSliderLabel.setFont(font)
        self.zoomSliderLabel.setObjectName("zoomSliderLabel")
        self.gridLayout_3.addWidget(self.zoomSliderLabel, 0, 0, 1, 1)
        self.toLabel = QtWidgets.QLabel(self.filterFrame)
        self.toLabel.setMaximumSize(QtCore.QSize(25, 16777215))
        font = QtGui.QFont()
        font.setItalic(True)
        self.toLabel.setFont(font)
        self.toLabel.setObjectName("toLabel")
        self.gridLayout_3.addWidget(self.toLabel, 2, 2, 1, 1)
        self.rangeLabel = QtWidgets.QLabel(self.filterFrame)
        self.rangeLabel.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.rangeLabel.setFont(font)
        self.rangeLabel.setObjectName("rangeLabel")
        self.gridLayout_3.addWidget(self.rangeLabel, 2, 0, 1, 1)
        self.sepLine2 = QtWidgets.QFrame(self.filterFrame)
        self.sepLine2.setFrameShape(QtWidgets.QFrame.HLine)
        self.sepLine2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.sepLine2.setObjectName("sepLine2")
        self.gridLayout_3.addWidget(self.sepLine2, 4, 0, 1, 4)
        self.upperRangeField = QtWidgets.QLineEdit(self.filterFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upperRangeField.sizePolicy().hasHeightForWidth())
        self.upperRangeField.setSizePolicy(sizePolicy)
        self.upperRangeField.setMaximumSize(QtCore.QSize(50, 16777215))
        self.upperRangeField.setObjectName("upperRangeField")
        self.gridLayout_3.addWidget(self.upperRangeField, 2, 3, 1, 1)
        self.lowerRangeField = QtWidgets.QLineEdit(self.filterFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lowerRangeField.sizePolicy().hasHeightForWidth())
        self.lowerRangeField.setSizePolicy(sizePolicy)
        self.lowerRangeField.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lowerRangeField.setObjectName("lowerRangeField")
        self.gridLayout_3.addWidget(self.lowerRangeField, 2, 1, 1, 1)
        self.filterRangeCheckbox = QtWidgets.QCheckBox(self.filterFrame)
        self.filterRangeCheckbox.setObjectName("filterRangeCheckbox")
        self.gridLayout_3.addWidget(self.filterRangeCheckbox, 3, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.filterFrame)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 1, 0, 1, 4)
        self.widget_2 = QtWidgets.QWidget(self.filterFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 1, 0, 1, 1)
        self.atomAIndexField = QtWidgets.QLineEdit(self.widget_2)
        self.atomAIndexField.setMaximumSize(QtCore.QSize(75, 16777215))
        self.atomAIndexField.setObjectName("atomAIndexField")
        self.gridLayout_5.addWidget(self.atomAIndexField, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 5, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.widget_2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_5.addWidget(self.line_4, 3, 0, 1, 4)
        self.atomANameField = QtWidgets.QLineEdit(self.widget_2)
        self.atomANameField.setMaximumSize(QtCore.QSize(75, 16777215))
        self.atomANameField.setObjectName("atomANameField")
        self.gridLayout_5.addWidget(self.atomANameField, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget_2)
        self.label_8.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 2, 2, 1, 1)
        self.atomBNameField = QtWidgets.QLineEdit(self.widget_2)
        self.atomBNameField.setMaximumSize(QtCore.QSize(75, 16777215))
        self.atomBNameField.setObjectName("atomBNameField")
        self.gridLayout_5.addWidget(self.atomBNameField, 2, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        self.label_7.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 2, 0, 1, 1)
        self.atomBIndexField = QtWidgets.QLineEdit(self.widget_2)
        self.atomBIndexField.setMaximumSize(QtCore.QSize(75, 16777215))
        self.atomBIndexField.setObjectName("atomBIndexField")
        self.gridLayout_5.addWidget(self.atomBIndexField, 1, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 1, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 4, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.widget_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 5, 2, 1, 1)
        self.residBRangeField = QtWidgets.QLineEdit(self.widget_2)
        self.residBRangeField.setObjectName("residBRangeField")
        self.gridLayout_5.addWidget(self.residBRangeField, 5, 3, 1, 1)
        self.residARangeField = QtWidgets.QLineEdit(self.widget_2)
        self.residARangeField.setObjectName("residARangeField")
        self.gridLayout_5.addWidget(self.residARangeField, 5, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.widget_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 6, 0, 1, 1)
        self.residANameField = QtWidgets.QLineEdit(self.widget_2)
        self.residANameField.setObjectName("residANameField")
        self.gridLayout_5.addWidget(self.residANameField, 6, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.widget_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 6, 2, 1, 1)
        self.residBNameField = QtWidgets.QLineEdit(self.widget_2)
        self.residBNameField.setObjectName("residBNameField")
        self.gridLayout_5.addWidget(self.residBNameField, 6, 3, 1, 1)
        self.gridLayout_3.addWidget(self.widget_2, 7, 0, 1, 4)
        self.widget = QtWidgets.QWidget(self.filterFrame)
        self.widget.setObjectName("widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.compareTotalTimeDropdown = QtWidgets.QComboBox(self.widget)
        self.compareTotalTimeDropdown.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.compareTotalTimeDropdown.setFont(font)
        self.compareTotalTimeDropdown.setObjectName("compareTotalTimeDropdown")
        self.compareTotalTimeDropdown.addItem("")
        self.compareTotalTimeDropdown.addItem("")
        self.gridLayout_4.addWidget(self.compareTotalTimeDropdown, 0, 1, 1, 1)
        self.compareScoreDropdown = QtWidgets.QComboBox(self.widget)
        self.compareScoreDropdown.setMaximumSize(QtCore.QSize(90, 16777215))
        self.compareScoreDropdown.setObjectName("compareScoreDropdown")
        self.compareScoreDropdown.addItem("")
        self.compareScoreDropdown.addItem("")
        self.gridLayout_4.addWidget(self.compareScoreDropdown, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 2, 0, 1, 1)
        self.sortingOrderDropdown = QtWidgets.QComboBox(self.widget)
        self.sortingOrderDropdown.setMaximumSize(QtCore.QSize(75, 16777215))
        self.sortingOrderDropdown.setObjectName("sortingOrderDropdown")
        self.sortingOrderDropdown.addItem("")
        self.sortingOrderDropdown.addItem("")
        self.gridLayout_4.addWidget(self.sortingOrderDropdown, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setMaximumSize(QtCore.QSize(70, 16777215))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_4.addWidget(self.comboBox_2, 1, 0, 1, 1)
        self.scoreField = QtWidgets.QLineEdit(self.widget)
        self.scoreField.setMaximumSize(QtCore.QSize(75, 16777215))
        self.scoreField.setObjectName("scoreField")
        self.gridLayout_4.addWidget(self.scoreField, 1, 2, 1, 1)
        self.activeTotalTimeCheckbox = QtWidgets.QCheckBox(self.widget)
        self.activeTotalTimeCheckbox.setText("")
        self.activeTotalTimeCheckbox.setObjectName("activeTotalTimeCheckbox")
        self.gridLayout_4.addWidget(self.activeTotalTimeCheckbox, 0, 3, 1, 1)
        self.totalTimeField = QtWidgets.QLineEdit(self.widget)
        self.totalTimeField.setMaximumSize(QtCore.QSize(75, 16777215))
        self.totalTimeField.setObjectName("totalTimeField")
        self.gridLayout_4.addWidget(self.totalTimeField, 0, 2, 1, 1)
        self.activeScoreCheckbox = QtWidgets.QCheckBox(self.widget)
        self.activeScoreCheckbox.setText("")
        self.activeScoreCheckbox.setObjectName("activeScoreCheckbox")
        self.gridLayout_4.addWidget(self.activeScoreCheckbox, 1, 3, 1, 1)
        self.sortingKeyDropdown = QtWidgets.QComboBox(self.widget)
        self.sortingKeyDropdown.setMaximumSize(QtCore.QSize(90, 16777215))
        self.sortingKeyDropdown.setObjectName("sortingKeyDropdown")
        self.gridLayout_4.addWidget(self.sortingKeyDropdown, 2, 1, 1, 1)
        self.activeSortingBox = QtWidgets.QCheckBox(self.widget)
        self.activeSortingBox.setText("")
        self.activeSortingBox.setObjectName("activeSortingBox")
        self.gridLayout_4.addWidget(self.activeSortingBox, 2, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 3, 0, 1, 1)
        self.selectOnlyToolbox = QtWidgets.QComboBox(self.widget)
        self.selectOnlyToolbox.setObjectName("selectOnlyToolbox")
        self.gridLayout_4.addWidget(self.selectOnlyToolbox, 3, 1, 1, 2)
        self.onlyBoxActiveCheckbox = QtWidgets.QCheckBox(self.widget)
        self.onlyBoxActiveCheckbox.setText("")
        self.onlyBoxActiveCheckbox.setObjectName("onlyBoxActiveCheckbox")
        self.gridLayout_4.addWidget(self.onlyBoxActiveCheckbox, 3, 3, 1, 1)
        self.gridLayout_3.addWidget(self.widget, 5, 0, 1, 4)
        self.applyFilterButton = QtWidgets.QPushButton(self.filterFrame)
        self.applyFilterButton.setObjectName("applyFilterButton")
        self.gridLayout_3.addWidget(self.applyFilterButton, 9, 0, 1, 1)
        self.frameStrideField = QtWidgets.QLineEdit(self.filterFrame)
        self.frameStrideField.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frameStrideField.setObjectName("frameStrideField")
        self.gridLayout_3.addWidget(self.frameStrideField, 0, 1, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.filterFrame)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_3.addWidget(self.line_3, 6, 0, 1, 4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 8, 0, 1, 1)
        self.gridLayout.addWidget(self.filterFrame, 2, 8, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1265, 25))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionRun_VMD_contact_search = QtWidgets.QAction(MainWindow)
        self.actionRun_VMD_contact_search.setObjectName("actionRun_VMD_contact_search")
        self.actionLoad_Data = QtWidgets.QAction(MainWindow)
        self.actionLoad_Data.setObjectName("actionLoad_Data")
        self.actionImport_Session = QtWidgets.QAction(MainWindow)
        self.actionImport_Session.setObjectName("actionImport_Session")
        self.actionExport_Session = QtWidgets.QAction(MainWindow)
        self.actionExport_Session.setObjectName("actionExport_Session")
        self.actionDefault = QtWidgets.QAction(MainWindow)
        self.actionDefault.setObjectName("actionDefault")
        self.actionShow_Info = QtWidgets.QAction(MainWindow)
        self.actionShow_Info.setObjectName("actionShow_Info")
        self.actionExportData = QtWidgets.QAction(MainWindow)
        self.actionExportData.setCheckable(False)
        self.actionExportData.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionExportData.setObjectName("actionExportData")
        self.actionContact_Area_Calculations = QtWidgets.QAction(MainWindow)
        self.actionContact_Area_Calculations.setObjectName("actionContact_Area_Calculations")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionVMD_Remote_Control = QtWidgets.QAction(MainWindow)
        self.actionVMD_Remote_Control.setObjectName("actionVMD_Remote_Control")
        self.menuFile.addAction(self.actionLoad_Data)
        self.menuFile.addAction(self.actionImport_Session)
        self.menuFile.addAction(self.actionExport_Session)
        self.menuFile.addAction(self.actionDefault)
        self.menuAbout.addAction(self.actionShow_Info)
        self.menuTools.addAction(self.actionExportData)
        self.menuTools.addAction(self.actionContact_Area_Calculations)
        self.menuTools.addAction(self.actionVMD_Remote_Control)
        self.menuSettings.addAction(self.actionPreferences)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.scrollArea, self.lowerRangeField)
        MainWindow.setTabOrder(self.lowerRangeField, self.upperRangeField)
        MainWindow.setTabOrder(self.upperRangeField, self.filterRangeCheckbox)
        MainWindow.setTabOrder(self.filterRangeCheckbox, self.visModeButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.visModeButton.setText(_translate("MainWindow", "Vismode"))
        self.selection1label.setText(_translate("MainWindow", "-"))
        self.selection1.setText(_translate("MainWindow", "Selection 1:"))
        self.status.setText(_translate("MainWindow", "Status:"))
        self.selection2label.setText(_translate("MainWindow", "-"))
        self.statusLabel.setText(_translate("MainWindow", "-"))
        self.selection2.setText(_translate("MainWindow", "Selection 2:"))
        self.progressBar.setFormat(_translate("MainWindow", "%p%"))
        self.statisticsButton.setText(_translate("MainWindow", "Statistics"))
        self.analysisButton.setText(_translate("MainWindow", "Accumulate Scores"))
        self.zoomSliderLabel.setText(_translate("MainWindow", "Frame Stride:"))
        self.toLabel.setText(_translate("MainWindow", "to"))
        self.rangeLabel.setText(_translate("MainWindow", "Timeline Range:"))
        self.upperRangeField.setText(_translate("MainWindow", "end"))
        self.lowerRangeField.setText(_translate("MainWindow", "1"))
        self.filterRangeCheckbox.setText(_translate("MainWindow", "Filter Range"))
        self.label_4.setText(_translate("MainWindow", "idx 1:"))
        self.atomAIndexField.setText(_translate("MainWindow", "all"))
        self.label_10.setText(_translate("MainWindow", "resid 1:"))
        self.atomANameField.setText(_translate("MainWindow", "all"))
        self.label_8.setText(_translate("MainWindow", "name 2:"))
        self.atomBNameField.setText(_translate("MainWindow", "all"))
        self.label_6.setText(_translate("MainWindow", "Atoms:"))
        self.label_7.setText(_translate("MainWindow", "name 1:"))
        self.atomBIndexField.setText(_translate("MainWindow", "all"))
        self.label_5.setText(_translate("MainWindow", "idx 2:"))
        self.label_9.setText(_translate("MainWindow", "Residues:"))
        self.label_11.setText(_translate("MainWindow", "resid 2:"))
        self.residBRangeField.setText(_translate("MainWindow", "all"))
        self.residARangeField.setText(_translate("MainWindow", "all"))
        self.label_12.setText(_translate("MainWindow", "resn. 1:"))
        self.residANameField.setText(_translate("MainWindow", "all"))
        self.label_13.setText(_translate("MainWindow", "resn. 2"))
        self.residBNameField.setText(_translate("MainWindow", "all"))
        self.compareTotalTimeDropdown.setItemText(0, _translate("MainWindow", "greater"))
        self.compareTotalTimeDropdown.setItemText(1, _translate("MainWindow", "smaller"))
        self.compareScoreDropdown.setItemText(0, _translate("MainWindow", "greater"))
        self.compareScoreDropdown.setItemText(1, _translate("MainWindow", "smaller"))
        self.label_2.setText(_translate("MainWindow", "Sort by:"))
        self.sortingOrderDropdown.setItemText(0, _translate("MainWindow", "asc."))
        self.sortingOrderDropdown.setItemText(1, _translate("MainWindow", "desc."))
        self.label.setText(_translate("MainWindow", "Total Time:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Mean"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Median"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "HB %"))
        self.scoreField.setText(_translate("MainWindow", "0"))
        self.totalTimeField.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "Show Only:"))
        self.applyFilterButton.setText(_translate("MainWindow", "Apply"))
        self.frameStrideField.setText(_translate("MainWindow", "1"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionExport.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionRun_VMD_contact_search.setText(_translate("MainWindow", "Run VMD contact search"))
        self.actionLoad_Data.setText(_translate("MainWindow", "Load Trajectory Data"))
        self.actionLoad_Data.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actionImport_Session.setText(_translate("MainWindow", "Import Session"))
        self.actionImport_Session.setShortcut(_translate("MainWindow", "Ctrl+Shift+I"))
        self.actionExport_Session.setText(_translate("MainWindow", "Export Session"))
        self.actionExport_Session.setShortcut(_translate("MainWindow", "Ctrl+Shift+E"))
        self.actionDefault.setText(_translate("MainWindow", "Default"))
        self.actionDefault.setShortcut(_translate("MainWindow", "Ctrl+Shift+D"))
        self.actionShow_Info.setText(_translate("MainWindow", "Developer Info"))
        self.actionExportData.setText(_translate("MainWindow", "Export Contact Data"))
        self.actionExportData.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionContact_Area_Calculations.setText(_translate("MainWindow", "Contact Area Calculation"))
        self.actionContact_Area_Calculations.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))
        self.actionPreferences.setShortcut(_translate("MainWindow", "Ctrl+,"))
        self.actionVMD_Remote_Control.setText(_translate("MainWindow", "VMD Remote Control"))
        self.actionVMD_Remote_Control.setShortcut(_translate("MainWindow", "Ctrl+V"))

