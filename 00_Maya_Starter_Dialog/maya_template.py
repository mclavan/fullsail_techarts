'''
Maya Dialog Starter
maya_template.py

Description:
	This a interface starter script for pyside.  
	The main interface is inherited from the maya_gui.py file.  
	This file get generated when you compile the QtDesigner ui file.  
	This file just adds on top of the original maya_gui file. 

How to Run:

# Place the two gui files in your script folder, 
#    then run the code below.

import maya_template
reload(maya_template)
maya_template.gui()   # Dockable 
# maya_template.gui(False) # Not Dockable 

# * Note
# Remember any change to the orginal ui files require the 
# 	ui file to be recompiled. 

'''

from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
from PySide.QtGui import *
from PySide.QtCore import *

# Interface Import
import maya_gui
reload(maya_gui)



class MainDialog(QDialog, maya_gui.Ui_Dialog):
	def __init__(self, parent=None):
		super(MainDialog, self).__init__(parent)
		self.setupUi(self)

	# 	self.connect(self.pushButton, SIGNAL('clicked()'), self.button_pressed)

	# def button_pressed(self):
	# 	print 'Button has been pressed.'


class MyDockableWindow(MayaQWidgetDockableMixin, MainDialog):
    def __init__(self, parent=None):
        super(MyDockableWindow, self).__init__(parent=parent)




def gui(dock=True):
	button = MyDockableWindow()
	button.show(dockable=dock)    
	print('# ' + button.showRepr())	

	