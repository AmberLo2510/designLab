from cmu_graphics import *
from PIL import Image
import math  

def loadPilImage(path):
    return Image.open(path)

def loadTransparentPilImage(path):
    image = Image.open(path).convert('RGBA')
    for i in range(image.width):
      for j in range(image.height):
          pixel = image.getpixel((i, j))
          if pixel[3] == 0:
              image.putpixel((i, j), (0, 0, 0, 0))
    return image

def onAppStart(app):
    path = 'images/upload_icon.png' # https://www.creativefabrica.com/product/cloud-data-upload-icon/ 
    pilImage2 = loadTransparentPilImage(path)
    app.cmuImage2 = CMUImage(pilImage2)
    imageWidth, imageHeight = pilImage2.size
    pilImage3 = pilImage2.resize((imageWidth//3, imageHeight//3))
    app.uploadIcon = CMUImage(pilImage3)

    app.height = 1000 
    app.width =  1500

    app.labelWidth = 0.07 * (app.width) 
    app.labelHeight = 0.8 * app.height 
    app.tabs = 5
    app.selection = None
    app.labelLeft = 50 
    app.labelTop = 50


    app.viewLabelWidth =  0.07 * app.width
    app.viewLabelLeft = app.width - app.labelLeft - app.viewLabelWidth
    app.viewLabelTop = app.labelTop
    app.viewLabelHeight = app.height * 0.3
    app.viewTabs = 3
    app.viewSelection = None

def redrawAll(app):
    drawRect(0, 0, app.width, app.height, fill = 'whiteSmoke')

    drawRect(app.labelLeft, app.labelTop, app.labelWidth, app.labelHeight, fill='black')
    for tab in range(app.tabs):
        drawTabs(app, tab)
    drawRect(app.viewLabelLeft, app.viewLabelTop, app.viewLabelWidth, app.viewLabelHeight, fill = 'gray')
    for viewTab in range(app.viewTabs):
        drawViewTabs(app, viewTab)
    
    #icons
    iconX = app.labelLeft + (5 * app.labelWidth / 8) 
    tabHeight = getTabHeight(app)
    iconY = app.labelTop + (tabHeight / 2)
    drawImage(app.uploadIcon, iconX, iconY, align='center') 


def onMouseMove(app, mouseX, mouseY):
    if (app.labelLeft <= mouseX < app.labelWidth + app.labelLeft):
        selectedTab = getTab(app, mouseX, mouseY)
        if selectedTab != None:
            app.selection = selectedTab
    elif (app.viewLabelLeft <= mouseX < app.viewLabelWidth + app.viewLabelLeft): 
        selectedViewTab = getViewTab(app, mouseX, mouseY)
        if selectedViewTab != None:
            app.viewSelection = selectedViewTab
    else:
        app.viewSelection = None 
        app.selection = None


def drawTabs(app, tab):
    tabLeft, tabTop = getTabLeftTop(app, tab)
    tabHeight = getTabHeight(app)
    tabWidth = app.labelWidth
    if tab == app.selection:
        color = 'purple'
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

 #view     
def drawViewTabs(app, viewTab):
    viewTabLeft, viewTabTop = getViewTabLeftTop(app, viewTab)
    viewTabHeight = getViewTabHeight(app)
    viewTabWidth = app.viewLabelWidth
    if viewTab == app.viewSelection:
        color = 'cyan'
        borderCol = 'blue' 
    else:
        color = None
        borderCol = None
    drawRect(viewTabLeft, viewTabTop, viewTabWidth, viewTabHeight,
             fill=color, border=borderCol)
    
    
def getViewTabLeftTop(app, viewTab):
    viewTabHeight = getViewTabHeight(app)
    viewTabLeft = app.viewLabelLeft 
    viewTabTop = app.viewLabelTop + viewTab * viewTabHeight
    return (viewTabLeft, viewTabTop) 

def getViewTab(app, x, y):
    dy = y - app.viewLabelTop
    viewTabHeight = getViewTabHeight(app)
    viewTab = math.floor(dy / viewTabHeight)
    if ((0 <= viewTab < app.viewTabs) and 
        (app.viewLabelLeft <= x < app.viewLabelWidth + app.viewLabelLeft)): 
        return viewTab
    else:
      return None
    
def getViewTabHeight(app):
    viewTabHeight = app.viewLabelHeight/ app.viewTabs
    return (viewTabHeight)


runApp()

