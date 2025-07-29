from cmu_graphics import *
import math 
from customize import onAppStart
def redrawAll(app):
    drawRect(app.viewLabelLeft, app.viewLabelTop, app.viewLabelWidth, app.viewLabelHeight, fill = 'gray')
    for viewTab in range(app.viewTabs):
        drawTabs(app, viewTab)

def onMousePress(app, mouseX, mouseY):
    selectedTab = getTab(app, mouseX, mouseY)
    if selectedTab != None:
      if selectedTab == app.selection:
          app.selection = None
      else:
          app.selection = selectedTab

def drawTabs(app, viewTab):
    viewTabLeft, viewTabTop = getTabLeftTop(app, viewTab)
    viewTabHeight = getTabHeight(app)
    viewTabWidth = app.viewLabelWidth
    if viewTab == app.selection:
        color = 'cyan'
        borderCol = 'blue' 
    else:
        color = None
        borderCol = None
    drawRect(viewTabLeft, viewTabTop, viewTabWidth, viewTabHeight,
             fill=color, border=borderCol)
    
    
def getTabLeftTop(app, viewTab):
    viewTabHeight = getTabHeight(app)
    viewTabLeft = app.viewLabelLeft 
    viewTabTop = app.viewLabelTop + viewTab * viewTabHeight
    return (viewTabLeft, viewTabTop) 

def getTab(app, x, y):
    dy = y - app.viewLabelTop
    viewTabHeight = getTabHeight(app)
    viewTab = math.floor(dy / viewTabHeight)
    if ((0 <= viewTab < app.viewTabs) and 
        (app.viewLabelLeft <= x < app.viewLabelWidth + app.viewLabelLeft)): 

      return viewTab
    else:
      return None
    
def getTabHeight(app):
    viewTabHeight = (app.viewLabelHeight * 0.6) / app.viewTabs
    return (viewTabHeight)

runApp()

