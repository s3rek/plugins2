# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tableManagerUi.ui'
#
# Created: Wed Sep 21 22:37:22 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setEnabled(True)
        Dialog.resize(627, 490)
        Dialog.setFocusPolicy(QtCore.Qt.NoFocus)
        Dialog.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/tableManager/icons/tableManagerIcon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        self.gridlayout = QtGui.QGridLayout(self.tab_1)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.fieldsTable = QtGui.QTableWidget(self.tab_1)
        self.fieldsTable.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldsTable.sizePolicy().hasHeightForWidth())
        self.fieldsTable.setSizePolicy(sizePolicy)
        self.fieldsTable.setMinimumSize(QtCore.QSize(0, 280))
        self.fieldsTable.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.fieldsTable.setEditTriggers(QtGui.QAbstractItemView.AnyKeyPressed|QtGui.QAbstractItemView.DoubleClicked|QtGui.QAbstractItemView.EditKeyPressed)
        self.fieldsTable.setDragDropMode(QtGui.QAbstractItemView.NoDragDrop)
        self.fieldsTable.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.fieldsTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.fieldsTable.setGridStyle(QtCore.Qt.DotLine)
        self.fieldsTable.setWordWrap(False)
        self.fieldsTable.setCornerButtonEnabled(False)
        self.fieldsTable.setRowCount(0)
        self.fieldsTable.setColumnCount(2)
        self.fieldsTable.setObjectName(_fromUtf8("fieldsTable"))
        item = QtGui.QTableWidgetItem()
        self.fieldsTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.fieldsTable.setHorizontalHeaderItem(1, item)
        self.gridlayout.addWidget(self.fieldsTable, 0, 0, 1, 1)
        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.butUp = QtGui.QToolButton(self.tab_1)
        self.butUp.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butUp.sizePolicy().hasHeightForWidth())
        self.butUp.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/tableManager/dialog/icons/crystalsvg_1uparrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butUp.setIcon(icon1)
        self.butUp.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.butUp.setObjectName(_fromUtf8("butUp"))
        self.vboxlayout.addWidget(self.butUp)
        self.butDown = QtGui.QToolButton(self.tab_1)
        self.butDown.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butDown.sizePolicy().hasHeightForWidth())
        self.butDown.setSizePolicy(sizePolicy)
        self.butDown.setMinimumSize(QtCore.QSize(120, 0))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/tableManager/dialog/icons/crystalsvg_1downarrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butDown.setIcon(icon2)
        self.butDown.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.butDown.setObjectName(_fromUtf8("butDown"))
        self.vboxlayout.addWidget(self.butDown)
        self.butRename = QtGui.QToolButton(self.tab_1)
        self.butRename.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butRename.sizePolicy().hasHeightForWidth())
        self.butRename.setSizePolicy(sizePolicy)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/tableManager/dialog/icons/tableManagerIcon3.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butRename.setIcon(icon3)
        self.butRename.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.butRename.setObjectName(_fromUtf8("butRename"))
        self.vboxlayout.addWidget(self.butRename)
        self.butIns = QtGui.QToolButton(self.tab_1)
        self.butIns.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butIns.sizePolicy().hasHeightForWidth())
        self.butIns.setSizePolicy(sizePolicy)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/tableManager/dialog/icons/mActionNewAttribute.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butIns.setIcon(icon4)
        self.butIns.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.butIns.setObjectName(_fromUtf8("butIns"))
        self.vboxlayout.addWidget(self.butIns)
        self.butClone = QtGui.QToolButton(self.tab_1)
        self.butClone.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butClone.sizePolicy().hasHeightForWidth())
        self.butClone.setSizePolicy(sizePolicy)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/tableManager/dialog/icons/mActionCopySelected.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butClone.setIcon(icon5)
        self.butClone.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.butClone.setObjectName(_fromUtf8("butClone"))
        self.vboxlayout.addWidget(self.butClone)
        spacerItem = QtGui.QSpacerItem(20, 24, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.vboxlayout.addItem(spacerItem)
        self.butDel = QtGui.QToolButton(self.tab_1)
        self.butDel.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butDel.sizePolicy().hasHeightForWidth())
        self.butDel.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 147, 145))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.butDel.setPalette(palette)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/tableManager/dialog/icons/mActionDeleteAttribute.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butDel.setIcon(icon6)
        self.butDel.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.butDel.setObjectName(_fromUtf8("butDel"))
        self.vboxlayout.addWidget(self.butDel)
        spacerItem1 = QtGui.QSpacerItem(120, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem1)
        self.gridlayout.addLayout(self.vboxlayout, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridlayout1 = QtGui.QGridLayout(self.tab_2)
        self.gridlayout1.setObjectName(_fromUtf8("gridlayout1"))
        self.dataTable = QtGui.QTableWidget(self.tab_2)
        self.dataTable.setEnabled(True)
        self.dataTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.dataTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectColumns)
        self.dataTable.setGridStyle(QtCore.Qt.DotLine)
        self.dataTable.setWordWrap(False)
        self.dataTable.setCornerButtonEnabled(False)
        self.dataTable.setObjectName(_fromUtf8("dataTable"))
        self.dataTable.setColumnCount(0)
        self.dataTable.setRowCount(0)
        self.gridlayout1.addWidget(self.dataTable, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.label = QtGui.QLabel(self.tab_3)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        spacerItem3 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem3)
        self.label_2 = QtGui.QLabel(self.tab_3)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        spacerItem4 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem4)
        self.cbWarning = QtGui.QCheckBox(self.tab_3)
        self.cbWarning.setChecked(True)
        self.cbWarning.setObjectName(_fromUtf8("cbWarning"))
        self.verticalLayout_2.addWidget(self.cbWarning)
        spacerItem5 = QtGui.QSpacerItem(20, 272, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        spacerItem6 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem6)
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setEnabled(True)
        self.progressBar.setAlignment(QtCore.Qt.AlignHCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.progressBar.setFormat(_fromUtf8(""))
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.hboxlayout.addWidget(self.progressBar)
        spacerItem7 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem7)
        self.butSave = QtGui.QPushButton(Dialog)
        self.butSave.setEnabled(False)
        self.butSave.setMinimumSize(QtCore.QSize(0, 32))
        palette = QtGui.QPalette()
        self.butSave.setPalette(palette)
        self.butSave.setStatusTip(_fromUtf8(""))
        self.butSave.setWhatsThis(_fromUtf8(""))
        self.butSave.setAccessibleDescription(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/tableManager/dialog/icons/mActionFileSave.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butSave.setIcon(icon7)
        self.butSave.setObjectName(_fromUtf8("butSave"))
        self.hboxlayout.addWidget(self.butSave)
        self.butSaveAs = QtGui.QPushButton(Dialog)
        self.butSaveAs.setEnabled(False)
        self.butSaveAs.setMinimumSize(QtCore.QSize(0, 32))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/tableManager/dialog/icons/mActionFileSaveAs.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butSaveAs.setIcon(icon8)
        self.butSaveAs.setObjectName(_fromUtf8("butSaveAs"))
        self.hboxlayout.addWidget(self.butSaveAs)
        spacerItem8 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem8)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setMinimumSize(QtCore.QSize(0, 32))
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.hboxlayout.addWidget(self.buttonBox)
        spacerItem9 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.hboxlayout)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.buttonBox, self.tabWidget)
        Dialog.setTabOrder(self.tabWidget, self.fieldsTable)
        Dialog.setTabOrder(self.fieldsTable, self.butUp)
        Dialog.setTabOrder(self.butUp, self.butDown)
        Dialog.setTabOrder(self.butDown, self.butRename)
        Dialog.setTabOrder(self.butRename, self.butIns)
        Dialog.setTabOrder(self.butIns, self.butClone)
        Dialog.setTabOrder(self.butClone, self.butDel)
        Dialog.setTabOrder(self.butDel, self.dataTable)
        Dialog.setTabOrder(self.dataTable, self.butSaveAs)
        Dialog.setTabOrder(self.butSaveAs, self.butSave)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Table Manager", None))
        item = self.fieldsTable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Name", None))
        item = self.fieldsTable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Type", None))
        self.butUp.setToolTip(_translate("Dialog", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Move selected field up</p></body></html>", None))
        self.butUp.setText(_translate("Dialog", "Move Up", None))
        self.butDown.setToolTip(_translate("Dialog", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Move selected field down</p></body></html>", None))
        self.butDown.setText(_translate("Dialog", "Move Down", None))
        self.butRename.setToolTip(_translate("Dialog", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Rename selected field</p></body></html>", None))
        self.butRename.setText(_translate("Dialog", "Rename", None))
        self.butIns.setToolTip(_translate("Dialog", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Insert new field</p></body></html>", None))
        self.butIns.setText(_translate("Dialog", "Insert", None))
        self.butClone.setToolTip(_translate("Dialog", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Clone selected field</p></body></html>", None))
        self.butClone.setText(_translate("Dialog", "Clone", None))
        self.butDel.setToolTip(_translate("Dialog", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Remove selected field</p></body></html>", None))
        self.butDel.setText(_translate("Dialog", "Delete", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("Dialog", "Fields", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Table preview", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#c00000;\">WARNING</span></p><p align=\"center\"><span style=\" color:#c00000;\">This plugin is discontinued and </span><span style=\" font-weight:600; color:#c00000;\">may corrupt your data.</span></p><p align=\"center\"><span style=\" color:#c00000;\">Please use the </span><span style=\" font-weight:600; font-style:italic; color:#c00000;\">Refactor Fields</span><span style=\" color:#c00000;\"> Processing algorithm instead.</span></p></body></html>", None))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p>Now, when QGIS is able to process attribute tables internally, it\'s time to discontinue Table Manager. Please note it doesn\'t work well with recent QGIS (and GDAL) versions and <span style=\" font-weight:600;\">several data corruptions were reported</span>. For that reason please ensure you always have a backup copy of your data and be aware there are no plans for releasing any further versions (especially for the upcoming QGIS 3).</p><p>You are highly recommended to use the <span style=\" font-style:italic;\">Refactor Fields</span> algorithm available in the <span style=\" font-style:italic;\">Processing</span> toolbox instead. If you can\'t find it on the algorithm tree, you may need to switch to the <span style=\" font-style:italic;\">Advanced Interface</span> mode. If you\'re not sure how to use the <span style=\" font-style:italic;\">Refactor Fields</span>, try to double click the field names, types etc.</p></body></html>", None))
        self.cbWarning.setText(_translate("Dialog", "Always show this tab on startup", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "About", None))
        self.butSave.setToolTip(_translate("Dialog", "Save changes (available only for Shapefiles) ", None))
        self.butSave.setText(_translate("Dialog", "Save", None))
        self.butSaveAs.setToolTip(_translate("Dialog", "Save changes to a new layer", None))
        self.butSaveAs.setText(_translate("Dialog", "Save as...", None))

import resources_rc