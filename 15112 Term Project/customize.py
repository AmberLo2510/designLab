from cmu_graphics import *
import math 
import customize
# import tkinter as tk
# #https://www.geeksforgeeks.org/python/getting-screens-height-and-width-using-tkinter-python/
# root = tk.Tk()
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight() #button? today's Lecture

def onAppStart(app):
    app.height = 1000 #how do i set app size to be the size of the moniter
    app.width =  1500
    app.labelWidth = 0.07 * (app.width) 
    app.labelHeight = 0.8 * app.height 
    app.tabs = 5
    app.selection = None
    app.labelLeft = 50 
    app.labelTop = 50
    app.viewLabelWidth = 0.08 * app.width
    app.viewLabelLeft = app.width - app.labelLeft - app.viewLabelWidth
    app.viewLabelTop = app.labelTop
    app.viewLabelHeight = app.height * 0.3
    app.viewTabs = 3

def redrawAll(app):
    drawRect(app.labelLeft, app.labelTop, app.labelWidth, app.labelHeight, fill='black')
    for tab in range(app.tabs):
        drawTabs(app, tab)
    drawRect(app.viewLabelLeft, app.viewLabelTop, app.viewLabelWidth, app.viewLabelHeight, fill = 'gray')

def onMousePress(app, mouseX, mouseY):
    selectedTab = getTab(app, mouseX, mouseY)
    if selectedTab != None:
      if selectedTab == app.selection:
          app.selection = None
      else:
          app.selection = selectedTab

def drawTabs(app, tab):
    tabLeft, tabTop = getTabLeftTop(app, tab)
    tabHeight = getTabHeight(app)
    tabWidth = app.labelWidth
    if tab == app.selection:
        color = 'cyan'
        borderCol = 'blue' 
    else:
        color = None
        borderCol = None
    drawRect(tabLeft, tabTop, tabWidth, tabHeight,
             fill=color, border=borderCol)
    
    
def getTabLeftTop(app, tab):
    tabHeight = getTabHeight(app)
    tabLeft = app.labelLeft 
    tabTop = app.labelTop + tab * tabHeight
    return (tabLeft, tabTop) 

def getTab(app, x, y):
    dy = y - app.labelTop
    tabHeight = getTabHeight(app)
    tab = math.floor(dy / tabHeight)
    if ((0 <= tab < app.tabs) and 
        (app.labelLeft <= x < app.labelWidth + app.labelLeft)): 

      return tab
    else:
      return None
    
def getTabHeight(app):
    tabHeight = (app.labelHeight * 0.6) / app.tabs
    return (tabHeight)
customize()
runApp()

