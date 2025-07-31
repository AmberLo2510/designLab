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


class Buttons:
    def __init__(self, left, top, width, height, function):
        self.left = left
        self.top = top 
        self.width = width 
        self.height = height
        self.function = function

    def respondToPress(self, app, mx, my):
        if self.isPressed(mx, my):
            self.function(app)


    def isPressed(self, mx, my):
        left = self.left
        top = self.top
        right = left + self.width
        bottom = top + self.height
        return left<=mx<=right and top<=my<=bottom     




def onAppStart(app):

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

    app.popupWidth = 400
    app.popupHeight = app.labelHeight
    app.popup = False

    app.front = True

    app.showArtworkList = False
    app.text = False
    app.font = (['arial', 'monospace', 'caveat', 'cinzel', 'montserrat','grenze', 'sacramento', 'orbitron'])
    app.fontSelection = None
    app.fontLeft = 302.5
    app.fontTop = app.labelTop
    app.fontWidth = 300
    app.customFont = 'arial'
    app.fontSize = 20
    app.fontColor = 'black'
    app.textX = 302.5
    app.textY = app.labelTop + 50
    app.shirtLeft = 895 
    app.shirtTop = app.height / 2
    

   


    path1 = 'images/upload_icon.png' # https://www.creativefabrica.com/product/cloud-data-upload-icon/ 
    pilImage1 = loadTransparentPilImage(path1)
    uploadWidth, uploadHeight = pilImage1.size
    uploadImage = pilImage1.resize((uploadWidth//5, uploadHeight//5))
    app.uploadIcon = CMUImage(uploadImage)


    path2 = 'images/x_icon.png' # https://icon-icons.com/icon/x/173468 
    pilImage2 = loadTransparentPilImage(path2)
    exitWidth, exitHeight = pilImage2.size
    pilImage2 = pilImage2.resize((exitWidth//25, exitHeight//25))
    app.exitIcon = CMUImage(pilImage2)

    path3 = 'images/text_icon.png' # https://pngtree.com/freepng/text-icon-cursor-abstract-black_8287456.html 
    pilImage3 = loadTransparentPilImage(path3)
    textWidth, textHeight = pilImage3.size
    pilImage3 = pilImage3.resize((textWidth// 7, textHeight// 7))
    app.textIcon = CMUImage(pilImage3)


    path4 = 'images/front.png' # https://shop.companycasuals.com/p/3985_AquaticBl
    pilImage4 = loadTransparentPilImage(path4)
    frontWidth, frontHeight = pilImage4.size
    pilImage4 = pilImage4.resize(((frontWidth * 3)// 2, (frontHeight * 3)// 2))
    app.shirtFront = CMUImage(pilImage4)

    
    path5 = 'images/frontIcon.png' # https://shop.companycasuals.com/p/3985_AquaticBl 
    pilImage5 = loadTransparentPilImage(path5)
    frontIconWidth, frontIconHeight = pilImage5.size
    pilImage5 = pilImage5.resize((frontIconWidth // 9, frontIconHeight // 9))
    app.shirtFrontIcon = CMUImage(pilImage5)

    path6 = 'images/backIcon.png' # https://shop.companycasuals.com/p/3985_AquaticBl
    pilImage6 = loadTransparentPilImage(path6)
    backIconWidth, backIconHeight = pilImage5.size
    pilImage6 = pilImage6.resize((backIconWidth, backIconHeight))
    app.shirtBackIcon = CMUImage(pilImage6)

    path7 = 'images/back.png' # https://shop.companycasuals.com/p/3985_AquaticBl
    pilImage7 = loadTransparentPilImage(path7)
    backWidth, backHeight = pilImage7.size
    pilImage7 = pilImage7.resize(((backWidth * 3)// 2, (backHeight * 3)// 2))
    app.shirtBack = CMUImage(pilImage7)

    path8 = 'images/artwork_icon.png' # https://icons8.com/icons/set/picture--white
    pilImage8 = loadTransparentPilImage(path8)
    artworkWidth, artworkHeight = pilImage8.size
    pilImage8 = pilImage8.resize((artworkWidth // 11, artworkHeight // 11))
    app.artworkIcon = CMUImage(pilImage8)

    path9 = 'charityLogos/redCross_logo.png' #https://en.m.wikipedia.org/wiki/File:American_Red_Cross_logo.svg
    pilImage9 = loadTransparentPilImage(path9)
    redCrossWidth, redCrossHeight = pilImage9.size
    pilImage9 = pilImage9.resize((redCrossWidth // 11, redCrossHeight // 11))
    
    path10 = 'charityLogos/breast_cancer.png' #https://www.citypng.com/photo/18104/png-breast-cancer-awareness-ribbon-clipart
    pilImage10 = loadTransparentPilImage(path10)
    breastCancerWidth, breastCancerHeight = pilImage10.size
    pilImage10 = pilImage10.resize((breastCancerWidth // 11, 
                                    breastCancerHeight // 11))

    path11 = 'images/undo_icon.png' #https://www.shutterstock.com/image-vector/undo-button-icon-1153185847
    pilImage11 = loadTransparentPilImage(path11)
    artworkWidth, artworkHeight = pilImage11.size
    pilImage11 = pilImage11.resize((artworkWidth // 11, artworkHeight // 11))
    app.undoIcon = CMUImage(pilImage11)
    
    
    app.artworkCols = 2 
    app.artworkRows = 1 #for now 
    app.artSelected = None 
    app.cx = app.shirtLeft + 100
    app.cy = app.shirtTop + 200
    app.drawLogo = False

    app.charityPath = [pilImage9, pilImage10]
    app.artworkList = ['charityLogos', 'sports']
    app.logoList = [ ]

    app.buttonList = [Buttons(50, 50, 105, 96, uploadFunction),
                      Buttons(400, 40, 40, 60, exitFunction),
                      Buttons(1340, 50, 195, 100, frontFunction),
                      Buttons(1345, 150, 1950, 100, backFunction),
                      Buttons(50, 146, 105, 96, textFunction),
                      Buttons(50, 242, 105, 96, artworkFunction),
                      Buttons(450, 50, 40, 40, undoFunction)]
                    #   Buttons(450, 90, 40, 40, redoFunction)

    app.boundLeft = 730
    app.boundTop = 260
    app.boundWidth = 339
    app.boundHeight = 585
    app. drawBounds = False


def redrawAll(app):
    drawRect(0, 0, app.width, app.height, fill = 'gainsboro')
    drawRect(app.labelLeft, app.labelTop, app.popupWidth, 
             app.popupHeight, fill = 'whitesmoke')
    

    #popup tab
    if app.popup == True:
        #exit
        drawImage(app.exitIcon, 420, 80, align = 'center')


    drawRect(app.labelLeft, app.labelTop, app.labelWidth, 
             app.labelHeight, fill='black')
    for tab in range(app.tabs):
        drawTabs(app, tab)

    
    drawRect(app.viewLabelLeft, app.viewLabelTop, app.viewLabelWidth, 
             app.viewLabelHeight, fill = 'whitesmoke')
    for viewTab in range(app.viewTabs):
        drawViewTabs(app, viewTab)

    #text
    if app.text == True:
        # text = input("Add Text: ") # need to fix how to integrate user input onto cmu graph
        drawLabel('text', app.textX, app.textY, font = f'{app.customFont}',
                  size = app.fontSize, fill = app.fontColor)

    #artwork
    if app.showArtworkList == True:
        for row in range(app.artworkRows):
            for col in range(app.artworkCols):
                for i in range(len(app.charityPath)):    
                    if Index(row, col) == i:
                        drawArtwork(app, row, col, i)

  


    #icons

    #upload
    drawImage(app.uploadIcon, 112, 95, align='center') 

    #text
    drawImage(app.textIcon, 102, 196, align='center') 
    
    #artwork
    drawImage(app.artworkIcon, 102, 290, align='center') 

    #undo
    drawImage(app.undoIcon, 450, 50) 
    
    #shirt
    if app.front == True:
        drawImage(app.shirtFront, app.shirtLeft, app.shirtTop, align='center') 
    else:
        drawImage(app.shirtBack, app.shirtLeft, app.shirtTop, align='center') 
    
    #front and back icons
    drawImage(app.shirtFrontIcon, 1397.5, 90, align='center') 
    drawLabel("Front", 1397.5, 130, align='center', font='montserrat', size = 15)

    drawImage(app.shirtBackIcon, 1397.5, 190, align='center') 
    drawLabel("Back", 1397.5, 230, align='center', font='montserrat', size = 15)

    if app.drawBounds == True:
        drawRect(app.boundLeft, app.boundTop, app.boundWidth, app.boundHeight, 
                 border='gray', borderWidth=4, dashes = True, fill = None)

    if app.drawLogo == True:
        for i in app.logoList:
            logo = CMUImage(app.charityPath[i])
            drawImage(logo, app.cx, app.cy, align = 'center')
    
# def drawOutFonts(app):
#     for fontIndex in range(len(app.font)):
#             drawFonts(app, fontIndex)

def undoFunction(app):
    if len(app.logoList) != 0:
        app.logoList.pop()


def uploadFunction(app): #draws a separate tab
    app.popup = True
    app.text = False

def textFunction(app):
    app.popup = True
    app.text = True


def artworkFunction(app):
    app.popup = True
    app.showArtworkList = True
    app.text = False

def exitFunction(app):
    app.popup = False
    app.text = False
    app.showArtworkList = False

def frontFunction(app):
    app.front = True

def backFunction(app):
    app.front = False

def onMouseMove(app, mouseX, mouseY):
    if (app.labelLeft <= mouseX < app.labelWidth + app.labelLeft):
        selectedTab = getTab(app, mouseX, mouseY)
        if selectedTab != None:
            app.selection = selectedTab
    elif (app.viewLabelLeft <= mouseX < app.viewLabelWidth + app.viewLabelLeft): 
        selectedViewTab = getViewTab(app, mouseX, mouseY)
        if selectedViewTab != None:
            app.viewSelection = selectedViewTab
    
    elif (app.fontLeft <= mouseX < app.fontLeft + (app.fontWidth//2)): 
        selectedFont = getFont(app, mouseX, mouseY)
        if selectedFont != None:
            app.fontSelection = selectedFont

    elif 155 < mouseX < 450 and app.showArtworkList == True:
        for i in range(len(app.charityPath)):
            selectedArt = getArt(app, mouseX, mouseY, i)
            if selectedArt != None:
                app.artSelected = selectedArt

    else:
        app.viewSelection = None 
        app.selection = None
        app.artSelected = None
def onMouseRelease(app, mx, my):
    app.drawBounds = False

def Index(row, col):
    if (row, col) == (0, 0): return 0
    elif (row, col) == (0, 1): return 1
    elif (row, col) ==(1, 0): return 2
    elif (row, col) == (1, 1): return 3
    elif (row, col) ==(2, 0): return 4
    elif (row, col) == (2, 1): return 5
    elif (row, col) ==(3, 0): return 6
    elif (row, col) == (3, 1): return 7

def onMousePress(app, mx, my):
    for button in app.buttonList:
        button.respondToPress(app, mx, my)
    
    if app.fontSelection != None:
        selectedFontInd = getFont(app, mx, my)
        if selectedFontInd != None:
            app.customFont = app.font[selectedFontInd]
    
    if app.artSelected != None:  
        row, col = getArtPressed(app, mx,my)
        app.logoList.append(Index(row, col))
        app.drawLogo = True


def getArtPressed(app, mx, my): 
    dx = mx - 170
    dy = my - 220
    row = math.floor(dy / 50)
    col = math.floor(dx / 120)
    if (0 <= row < app.artworkRows) and (0 <= col < app.artworkCols):
        return (row, col)
    else:
        return None
    
def onMouseDrag(app, mx, my):
    if app.showArtworkList == True:
        app.drawBounds = True
        if (app.boundLeft < mx < app.boundLeft + app.boundWidth and 
            app.boundTop < my < app.boundTop + app.boundHeight):
            app.cx = mx
            app.cy = my


#artwork



def drawArtwork(app, row, col, i):
    image = app.charityPath[i]
    artLeft, artTop = getArtLeftTop(app, row, col, i)
    artWidth, artHeight = image.size
    artCX = artLeft + 70 + (artWidth // 2) * col
    artCY = artTop + 100 + (artHeight // 2) * row  
    if (row,col) == app.artSelected: 
        border = 'blue'
    else:
        border = None
    logo = CMUImage(image)
    drawImage(logo, artCX, artCY, border = border, align = 'center')

def getArtLeftTop(app, row, col, i):
    image = app.charityPath[i]
    artWidth, artHeight = image.size
    artLeft = 170 + col * (artWidth + 50)
    artTop = 150 + row  * (artHeight + 30) 
    return artLeft, artTop


def getArt(app, mx, my, i): #might have to change this
    dx = mx - 170
    dy = my - 220
    image = app.charityPath[i]
    artWidth, artHeight = image.size
    row = math.floor(dy / artHeight)
    col = math.floor(dx / 120)
    if (0 <= row < app.artworkRows) and (0 <= col < app.artworkCols):
        return (row, col)
    else:
        return None


#fonts
def drawFonts(app, fontIndex):
    fontLeft, fontTop = getFontLeftTop(app, fontIndex)
    fontHeight = getFontHeight(app)
    if fontIndex == app.fontSelection:
        color = 'blue'
    else:
        color = None
    drawLabel(f'{app.font[fontIndex]}', fontLeft, 
              fontTop + (fontHeight//2), font = f'{app.font[fontIndex]}',
               fill = color, size = 30)
    
    
def getFontLeftTop(app, font):
    fontHeight = getFontHeight(app)
    fontLeft = app.fontLeft 
    tabTop = app.fontTop + font * fontHeight
    return (fontLeft, tabTop) 

def getFont(app, x, y):
    dy = y - app.fontTop
    fontHeight = getFontHeight(app)
    fontInd = math.floor(dy / fontHeight)
    if ((0 <= fontInd < len(app.font)) and 
        (app.fontLeft <= x < app.fontWidth + app.fontLeft)): 
      return fontInd
    else:
        return None
    
def getFontHeight(app):
    fontHeight = app.labelHeight / len(app.font)
    return (fontHeight)



#tabs
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

