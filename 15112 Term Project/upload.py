from cmu_graphics import *
import math

def onMousePress(app, mouseX, mouseY):
    selectedTab = getTab(app, mouseX, mouseY)
    if selectedTab != None:
      if selectedTab == app.selection:
          app.selection = None
      else:
          app.selection = selectedTab

