from cmu_graphics import *
from viewer import onAppStart
import math
onAppStart()

def onMousePress(app, mouseX, mouseY):
    selectedTab = getTab(app, mouseX, mouseY)
    if selectedTab != None:
      if selectedTab == app.selection:
          app.selection = None
      else:
          app.selection = selectedTab

