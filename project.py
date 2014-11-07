#############################################################################
# Miguel & Esteban
# project.py
# Checkers Game
#############################################################################

from graphics import*


class CheckerBoard:
    def __init__(self, player1, player2):
        # these are all the instance variables that we are using 
        self.player1 = player1
        self.player2 = player2
        self.pieces = []
        self.king1 = []
        self.pieces2 = []
        self.king2 = []
        self.onepiece = 0
        self.onepiece2 = 0
        self.legalMoves = [(150,350),(350,350),(550,350),(750,350),(50,450),(250,450),(450,450),(650,450)]
        
        self.KingMoves = [(150,350),(350,350),(550,350),(750,350),(50,450),(250,450),(450,450),(650,450)]

        self.topRow = [(50,50),(250,50),(450,50),(650,50)]
        self.bottomRow = [(150,750),(350,750),(550,750),(750,750)]
        
        # this code opens a window with the graphics and displays the intro of
        # the game and the names of each player along with their assinged pieces
        self.win = GraphWin('Checkers', 1400, 800)
        #self.win.setBackground('darkBlue')
        # Makes Players one's name
        '''Txt =Text(Point(950,180), str(self.player1))
        Txt.setFace('arial')
        Txt.setSize(20)
        Txt.setStyle('bold')
        Txt.setTextColor('green')
        Txt.draw(self.win)
        # Makes Players two's name
        Txt2 =Text(Point(1250,180), str(self.player2))
        Txt2.setFace('arial')
        Txt2.setSize(20)
        Txt2.setStyle('bold')
        Txt2.setTextColor('green')
        Txt2.draw(self.win)'''
        Image(Point(1100,100), 'checkers.gif').draw(self.win)
        Image(Point(1000,250), 'black.gif').draw(self.win)
        Image(Point(900,250), 'king1.gif').draw(self.win)
        Image(Point(1200,250), 'smallcircle.gif').draw(self.win)
        Image(Point(1300,250), 'king2.gif').draw(self.win)
        Image(Point(1100,350), 'rules.gif').draw(self.win)
        Image(Point(1320,760), 'exit.gif').draw(self.win)
        Image(Point(1100,550), 'rule.gif').draw(self.win)
        
        # this nested for loop is the loop the creates the checkers board and 
        # colors it with white and black according to the code
        for i in range(0, 800, 100):
            for j in range(0, 801, 100):
                if (i // 100) % 2 == 0 and (j // 100) % 2 == 0:
                    square = Rectangle(Point(i, j),Point(i+100, j+100))
                    square.setFill('white')
                    square.draw(self.win)
                else:
                    square = Rectangle(Point(i, j), Point(i+100, j+200))
                    square.setFill('black')
                    square.draw(self.win)
                if (i // 100) % 2 == 1 and (j // 100) % 2 == 1:
                    square = Rectangle(Point(i+100, j+100), Point(i, j))
                    square.setFill('white')
                    square.draw(self.win)
        
    
    def Player1Piece(self):
        # This function uses a similar method as the loop that creates the board
        # to create player one's puzzle pieces
        pieceCounter = 0
        for i in range(0, 800, 100):
            for j in range(0, 301, 200):
                if (i // 100) % 2 == 0 and (j // 100) % 2 == 0:
                    center = Point(50+i, 50+j)
                    self.pieces.append(Image(center,'black.gif'))
                    self.pieces[pieceCounter].draw(self.win)
                    pieceCounter += 1

        for i in range(100, 801, 200):
            for j in range(0, 300, 100):
                if (i // 100) % 2 == 1 and (j // 100) % 2 == 1:
                    center = Point(i+50, j+50)
                    self.pieces.append(Image(center,'black.gif'))
                    self.pieces[pieceCounter].draw(self.win)
                    pieceCounter += 1

        
    def Player2Piece(self):
        # This function uses a similar method as the loop that creates the board
        # to create player two's puzzle pieces
        pieceCounter = 0 
        for i in range(100, 801, 200):
            for j in range(500, 800, 100):
                if (i // 100) % 2 == 1 and (j // 100) % 2 == 1:
                    center = Point(50+i, 50+j)
                    self.pieces2.append(Image(center,'smallcircle.gif'))
                    self.pieces2[pieceCounter].draw(self.win)
                    pieceCounter += 1
                    
                if (i // 100) % 2 == 1 and (j // 100) % 2 == 0:
                    center = Point(i-50, j+50)
                    self.pieces2.append(Image(center,'smallcircle.gif'))
                    self.pieces2[pieceCounter].draw(self.win)
                    pieceCounter += 1

                                        
    def getcenter(self):
        # this function allows the user to use the mouse to click on the piece
        # he/she wants to move and then calculates the center of where that 
        # piece is located and then stores the chosen piece in a variable
        m = self.win.getMouse()
        x = 0
        y = 0
        for i in range(0, 801, 100):
            for j in range(0, 801, 100):
                if i <= m.getX() <= i+100 and j<= m.getY() <= j+100:
                    x = (i+i+100) // 2 
                    y = (j+j+100) // 2
                
           
        for i in range(len(self.pieces)-1):
            if (x,y) == (self.pieces[i].getAnchor().getX(), self.pieces[i].getAnchor().getY()):
                 self.onepiece = i
                 self.getNewCenter()
        for i in range(len(self.king1)):
            if (x,y) ==(self.king1[i].getAnchor().getX(),self.king1[i].getAnchor().getY()):
                self.onepiece = i
                self.getKingCenter()
        
           

    def getNewCenter(self):
        # this function also allows the user to use the mouse to click on the 
        # space that he/she wants to move and then calls on the get center
        # function to move the chosen piece a differenc between the center
        # calculated by the get center function and the get New Center function
        e = self.win.getMouse()
        for i in range(0, 801, 100):
            for j in range(0, 801, 100):
                if i <= e.getX() <= i+100 and j <= e.getY() <= j+100:
                    newX = (i+i+100) // 2
                    newY = (j+j+100) // 2
                    
                    oldX = self.pieces[self.onepiece].getAnchor().getX()
                    oldY = self.pieces[self.onepiece].getAnchor().getY()
                    
                    # using the new center it compares it to the list of legal
                    # moves and caries on the following operation. This also
                    # implements the jumping method and king method
                    if (newX,newY) in self.legalMoves and ((oldX+100,oldY+100) == (newX,newY) or (oldX-100,oldY+100)== (newX,newY)):
                        self.pieces[self.onepiece].move(newX-oldX,newY-oldY)
                        self.legalMoves.remove((newX,newY))
                        self.KingMoves.remove((newX,newY))
                        self.legalMoves.append((oldX,oldY))
                        self.KingMoves.append((oldX,oldY))
                        
                    
                   
                    
                    # allows for player one's pieces to eat to the right
                    elif (newX,newY) not in self.legalMoves and (newX+100,newY+100) in self.legalMoves :
                        for item in self.pieces2:
                            x = item.getAnchor().getX()
                            y = item.getAnchor().getY()
                            if (x,y) == (newX,newY) and newX+100 <= 800 and newY+100<=0:
                                item.undraw()
                                self.pieces2.remove(item)
                                self.legalMoves.append((oldX,oldY))
                                self.legalMoves.append((newX,newY))
                                self.KingMoves.append((oldX,oldY))
                                self.KingMoves.append((newX,newY))
                                self.pieces[self.onepiece].move(200,200)
                                self.legalMoves.remove((newX+100, newY+100))
                                self.KingMoves.remove((newX+100, newY+100))
                                
                    # allows for player one's pieces to eat to the left 
                    elif (newX,newY) not in self.legalMoves and (newX-100,newY+100) in self.legalMoves:
                        for item in self.pieces2:
                            x = item.getAnchor().getX()
                            y = item.getAnchor().getY()
                            if (x,y) == (newX,newY) and newX+100 >=0 and newY +100>=0:
                                item.undraw()
                                self.pieces2.remove(item)
                                self.legalMoves.append((oldX,oldY))
                                self.legalMoves.append((newX,newY))
                                self.KingMoves.append((oldX,oldY))
                                self.KingMoves.append((newX,newY))
                                self.legalMoves.append((newX-100,newY+100))
                                self.pieces[self.onepiece].move(-200,200)
                                self.legalMoves.remove((newX-100,newY+100))
                                self.KingMoves.remove((newX-100,newY+100))
                                
                                
                    else:
                        print('Not a Valid Move')
                        self.getcenter()
                        self.getNewCenter()
                            
                    # checks if a piece1 becomes king
                    if (newX,newY) in self.bottomRow:
                          self.pieces[self.onepiece].undraw()
                          self.pieces.remove(self.pieces[self.onepiece])
                          self.king1.append(Image(Point(newX,newY),'king1.gif'))
                          self.king1[-1].draw(self.win)
                          print(self.king1)


    



    def getKingCenter(self):
        # This fucntion implements the legal moves of the king and when it can 
        # eat another piece
        e = self.win.getMouse()

        for i in range(0, 801, 100):
            for j in range(0, 801, 100):
                if i <= e.getX() <= i+100 and j <= e.getY() <= j+100:
                    newX = (i+i+100) // 2
                    newY = (j+j+100) // 2
                    print(newX,newY)
                    oldX = self.king1[self.onepiece].getAnchor().getX()
                    oldY = self.king1[self.onepiece].getAnchor().getY()
        
                    # with this code the king moves normally down right or left     
                    if (newX,newY) in self.KingMoves and ((oldX+100,oldY+100) == (newX,newY) or (oldX-100,oldY+100)== (newX,newY)):
                        
                        self.king1[self.onepiece].move(newX-oldX,newY-oldY)
                        self.KingMoves.remove((newX,newY))
                        self.KingMoves.append((oldX,oldY))

                    # with this code the king moves normally up left or right  
                    elif (newX,newY) in self.KingMoves and ((oldX-100,oldY-100) == (newX,newY) or (oldX+100,oldY-100)== (newX,newY)):
                        
                        self.king1[self.onepiece].move(newX-oldX,newY-oldY)
                        self.KingMoves.remove((newX,newY))
                        self.KingMoves.append((oldX,oldY))
                        
                        
                    # allows for player one's king to eat to the right going 
                    # down
                    elif (newX,newY) not in self.KingMoves and (newX+100,newY+100) in self.KingMoves :
                        for item in self.pieces2:
                            # checks if one of the pieces that it wants to eat 
                            # is from the opponent
                            x = item.getAnchor().getX()
                            y = item.getAnchor().getY()
                            if (x,y) == (newX,newY) and newX+100 <=800 and newY+100 <=800:
                                item.undraw()
                                self.pieces2.remove(item)
                                self.legalMoves.append((oldX,oldY))
                                self.legalMoves.append((newX,newY))
                                self.KingMoves.append((oldX,oldY))
                                self.KingMoves.append((newX,newY))
                                self.king1[self.onepiece].move(200,200)
                                
                                self.legalMoves.remove((newX+100,newY+100))
                                self.KingMoves.remove((newX+100,newY+100))
                        
                        for item in self.king2:
                            # checks if one of the pieces that it wants to eat 
                            # is from the opponent
                            x = item.getAnchor().getX()
                            y = item.getAnchor().getY()
                            if (x,y) == (newX,newY) and newX+100 <=800 and newY+100 <=800:
                                item.undraw()
                                self.king2.remove(item)
                                self.legalMoves.append((oldX,oldY))
                                self.legalMoves.append((newX,newY))
                                self.KingMoves.append((oldX,oldY))
                                self.KingMoves.append((newX,newY))
                                self.king1[self.onepiece].move(200,200)
                                
                                self.legalMoves.remove((newX+100,newY+100))
                                self.KingMoves.remove((newX+100,newY+100))
                            
                        
                                
                    # allows for player one's king to eat to the left down
                    elif (newX,newY) not in self.KingMoves and (newX-100,newY+100) in self.KingMoves:
                        for item in self.pieces2:
                            # checks if one of the pieces that it wants to eat 
                            # is from the opponent
                            x = item.getAnchor().getX()
                            y = item.getAnchor().getY()
                            if (x,y) == (newX,newY) and newX-100 >= 0 and newY+100>=0:
                                item.undraw()
                                self.pieces2.remove(item)
                                self.legalMoves.append((oldX,oldY))
                                self.legalMoves.append((newX,newY))
                                self.KingMoves.append((oldX,oldY))
                                self.KingMoves.append((newX,newY))
                                self.king1[self.onepiece].move(-200,200)
                                
                                self.legalMoves.remove((newX-100,newY+100))
                                self.KingMoves.remove((newX-100,newY+100))
                                
                        for item in self.king2:
                            # checks if one of the pieces that it wants to eat 
                            # is from the opponent
                            x = item.getAnchor().getX()
                            y = item.getAnchor().getY()
                            if (x,y) == (newX,newY) and newX-100 >= 0 and newY+100>=0:
                                item.undraw()
                                self.king2.remove(item)
                                self.legalMoves.append((oldX,oldY))
                                self.legalMoves.append((newX,newY))
                                self.KingMoves.append((oldX,oldY))
                                self.KingMoves.append((newX,newY))
                                self.king1[self.onepiece].move(200,200)
                                
                                self.legalMoves.remove((newX+100,newY+100))
                                self.KingMoves.remove((newX+100,newY+100))
                    
                     # allows for player one's pieces to eat to the right going
                    # up
                    elif (newX,newY) not in self.KingMoves and (newX+100,newY-100) in self.KingMoves:
                        for item in self.pieces2:
                            # checks if one of the pieces that it wants to eat 
                            # is from the opponent
                            x = item.getAnchor().getX()
                            y = item.getAnchor().getY()
                            if (x,y) == (newX,newY) and newX+100 <=800 and newY-100 <=800:
                                item.undraw()
                                self.pieces2.remove(item)
                                self.legalMoves.append((newX,newY))
                                self.legalMoves.append((oldX,oldY))
                                self.KingMoves.append((newX,newY))
                                self.KingMoves.append((oldX,oldY))
                                self.king1[self.onepiece].move(200,-200)
                                
                                self.legalMoves.remove((newX+100,newY-100))
                                self.KingMoves.remove((newX+100,newY-100))
                                
                        for item in self.king2:
                            # checks if one of the pieces that it wants to eat 
                            # is from the opponent
                            x = item.getAnchor().getX()
                            y = item.getAnchor().getY()
                            if (x,y) == (newX,newY) and newX+100 <=800 and newY-100 <=800:
                                item.undraw()
                                self.king2.remove(item)
                                self.legalMoves.append((newX,newY))
                                self.legalMoves.append((oldX,oldY))
                                self.KingMoves.append((newX,newY))
                                self.KingMoves.append((oldX,oldY))
                                self.king1[self.onepiece].move(200,-200)
                                
                                self.legalMoves.remove((newX+100,newY-100))
                                self.KingMoves.remove((newX+100,newY-100))
                               
                               
                    # allows for player one's pieces to eat to the left up
                    elif (newX,newY) not in self.KingMoves and (newX-100,newY-100) in self.KingMoves:
                        for item in self.pieces2:
                            # checks if one of the pieces that it wants to eat 
                            # is from the opponent
                            x = item.getAnchor().getX()
                            y = item.getAnchor().getY()
                            if (x,y) == (newX,newY) and newX-100>=0 and newY-100>=0:
                                item.undraw()
                                self.pieces2.remove(item)
                                self.legalMoves.append((oldX,oldY))
                                self.legalMoves.append((newX,newY))
                                self.KingMoves.append((oldX,oldY))
                                self.KingMoves.append((newX,newY))
                                self.king1[self.onepiece].move(-200,-200)
                                
                                self.legalMoves.remove((newX-100,newY-100))
                                self.KingMoves.remove((newX-100,newY-100))
                        for item in self.king2:
                            # checks if one of the pieces that it wants to eat 
                            # is from the opponent
                            x = item.getAnchor().getX()
                            y = item.getAnchor().getY()
                            if (x,y) == (newX,newY) and newX-100>=0 and newY-100>=0:
                                item.undraw()
                                self.king2.remove(item)
                                self.legalMoves.append((oldX,oldY))
                                self.legalMoves.append((newX,newY))
                                self.KingMoves.append((oldX,oldY))
                                self.KingMoves.append((newX,newY))
                                self.king1[self.onepiece].move(-200,-200)
                                
                                self.legalMoves.remove((newX-100,newY-100))
                                self.KingMoves.remove((newX-100,newY-100))       
                        
                            


                            
                    

    def getcenter2(self):
        # this function allows the user to use the mouse to click on the piece
        # he/she wants to move and then calculates the center of where that 
        # piece is located and then stores the chosen piece in a variable
        m = self.win.getMouse()
        for i in range(0, 801, 100):
            for j in range(0, 801, 100):
                if i <= m.getX() <= i+100 and j<= m.getY() <= j+100:
                    x = (i+i+100) // 2 
                    y = (j+j+100) // 2
                    
        for i in range(len(self.pieces2)-1):
            if (x,y) == (self.pieces2[i].getAnchor().getX(),self.pieces2[i].getAnchor().getY()):
                self.onepiece2 = i
                self.getNewCenter2()
        for i in range(len(self.king2)):
            if (x,y) ==(self.king2[i].getAnchor().getX(),self.king2[i].getAnchor().getY()):
                self.onepiece2 = i
                self.getKingCenter2()

    




    def getNewCenter2(self):
        # this function also allows the user to use the mouse to click on the 
        # space that he/she wants to move and then calls on the get center
        # function to move the chosen piece a differenc between the center
        # calculated by the get center function and the get New Center function
        e = self.win.getMouse()
        for i in range(0, 801, 100):
            for j in range(0, 801, 100):
                if i <= e.getX() <= i+100 and j<= e.getY() <= j+100:
                    newX = (i+i+100) // 2 
                    newY = (j+j+100) // 2
                    oldX = self.pieces2[self.onepiece2].getAnchor().getX()
                    oldY = self.pieces2[self.onepiece2].getAnchor().getY()
                    
                    if (newX,newY) in self.legalMoves and ((oldX-100,oldY-100) == (newX,newY) or (oldX+100,oldY-100)== (newX,newY)):
                        
                        self.pieces2[self.onepiece2].move(newX-oldX,newY-oldY)
                        self.legalMoves.remove((newX,newY))
                        self.legalMoves.append((oldX,oldY))
                        self.KingMoves.remove((newX,newY))
                        self.KingMoves.append((oldX,oldY))
                        
                   
                    
                    # allows for player two's pieces to eat to the right
                    elif (newX,newY) not in self.legalMoves and (oldX+200,oldY-200) in self.legalMoves:
                        for item in self.pieces:
                            # checks if one of the pieces that it wants to eat 
                            # is from the opponent
                            x = item.getAnchor().getX()
                            y = item.getAnchor().getY()
                            if (x,y) == (newX,newY) and newX+100 <= 800 and newY-100 <=800:
                                item.undraw()
                                self.pieces.remove(item)
                                self.legalMoves.append((newX,newY))
                                self.legalMoves.append((oldX,oldY))
                                self.KingMoves.append((newX,newY))
                                self.KingMoves.append((oldX,oldY))
                        
                                self.pieces2[self.onepiece2].move(200,-200)
                                self.legalMoves.remove((newX+100,newY-100))
                                self.KingMoves.remove((newX+100,newY-100))
                               
                               
                    # allows for player two's pieces to eat to the left
                    elif (newX,newY) not in self.legalMoves and (oldX-200,oldY-200) in self.legalMoves:
                        for item in self.pieces:
                            x = item.getAnchor().getX()
                            y = item.getAnchor().getY()
                            if (x,y) == (newX,newY) and newX-100>=0 and newY-100>=0:
                                item.undraw()
                                self.pieces.remove(item)
                                self.legalMoves.append((oldX,oldY))
                                self.legalMoves.append((newX,newY))
                                self.KingMoves.append((oldX,oldY))
                                self.KingMoves.append((newX,newY))
                            
                                self.pieces2[self.onepiece2].move(-200,-200)
                                self.legalMoves.remove((newX-100,newY-100))
                                self.KingMoves.remove((newX-100,newY-100))
                     # checks if a piece has become king    
                    if (newX,newY) in self.topRow:
                          self.pieces2[self.onepiece2].undraw()
                          self.pieces2.remove(self.pieces2[self.onepiece2])
                          self.king2.append(Image(Point(newX,newY),'king2.gif'))
                          self.king2[-1].draw(self.win)



    def getKingCenter2(self):
        e = self.win.getMouse()
        for i in range(0, 801, 100):
            for j in range(0, 801, 100):
                if i <= e.getX() <= i+100 and j <= e.getY() <= j+100:
                    newX = (i+i+100) // 2
                    newY = (j+j+100) // 2
                    
                    oldX = self.king2[self.onepiece2].getAnchor().getX()
                    oldY = self.king2[self.onepiece2].getAnchor().getY()
        
                    # allows for the king to move right or left down      
                    if (newX,newY) in self.KingMoves and ((oldX+100,oldY+100) == (newX,newY) or (oldX-100,oldY+100)== (newX,newY)):
                        self.king2[self.onepiece2].move(newX-oldX,newY-oldY)
                        self.KingMoves.remove((newX,newY))
                        self.KingMoves.append((oldX,oldY))
                    # allows for the king to move right or left up    
                    if (newX,newY) in self.KingMoves and ((oldX-100,oldY-100) == (newX,newY) or (oldX+100,oldY-100)== (newX,newY)):
                        
                        self.king2[self.onepiece2].move(newX-oldX,newY-oldY)
                        self.KingMoves.remove((newX,newY))
                        self.KingMoves.append((oldX,oldY))
                        
                        
                    # allows for player two's king to eat to the right down
                    elif (newX,newY) not in self.KingMoves and (newX+100,newY+100) in self.KingMoves :
                        for item in self.pieces:
                            # checks if one of the pieces that it wants to eat 
                            # is from the opponent
                            x = item.getAnchor().getX()
                            y = item.getAnchor().getY()
                            if (x,y) == (newX,newY) and newX+100 <=800 and newY+100<=800:
                                item.undraw()
                                self.pieces.remove(item)
                                self.legalMoves.append((oldX,oldY))
                                self.legalMoves.append((newX,newY))
                                self.KingMoves.append((oldX,oldY))
                                self.KingMoves.append((newX,newY))
                                self.king2[self.onepiece2].move(200,200)
                                
                                self.legalMoves.remove((newX+100,newY+100))
                                self.KingMoves.remove((newX+100,newY+100))
                                
                        
                        for item in self.king1:
                            # checks if one of the pieces that it wants to eat 
                            # is from the opponent
                            x = item.getAnchor().getX()
                            y = item.getAnchor().getY()
                            if (x,y) == (newX,newY) and newX+100 <=800 and newY+100<=800:
                                item.undraw()
                                self.king1.remove(item)
                                self.legalMoves.append((oldX,oldY))
                                self.legalMoves.append((newX,newY))
                                self.KingMoves.append((oldX,oldY))
                                self.KingMoves.append((newX,newY))
                                self.king2[self.onepiece2].move(200,200)
                                
                                self.legalMoves.remove((newX+100,newY+100))
                                self.KingMoves.remove((newX+100,newY+100))
                                
                    # allows for player two's king to eat to the left down
                    elif (newX,newY) not in self.KingMoves and (newX-100,newY+100) in self.KingMoves:
                        for item in self.pieces:
                            # checks if one of the pieces that it wants to eat 
                            # is from the opponent
                            x = item.getAnchor().getX()
                            y = item.getAnchor().getY()
                            if (x,y) == (newX,newY) and newX-100>=0 and newY+100>=0:
                                item.undraw()
                                self.pieces.remove(item)
                                self.legalMoves.append((oldX,oldY))
                                self.legalMoves.append((newX,newY))
                                self.KingMoves.append((oldX,oldY))
                                self.KingMoves.append((newX,newY))
                                self.king2[self.onepiece2].move(-200,200)
                                
                                self.legalMoves.remove((newX-100,newY+100))
                                self.KingMoves.remove((newX-100,newY+100))
                                
                        for item in self.king1:
                            # checks if one of the pieces that it wants to eat 
                            # is from the opponent
                            x = item.getAnchor().getX()
                            y = item.getAnchor().getY()
                            if (x,y) == (newX,newY) and newX-100>=0 and newY+100>=0:
                                item.undraw()
                                self.king1.remove(item)
                                self.legalMoves.append((oldX,oldY))
                                self.legalMoves.append((newX,newY))
                                self.KingMoves.append((oldX,oldY))
                                self.KingMoves.append((newX,newY))
                                self.king2[self.onepiece2].move(-200,200)
                                
                                self.legalMoves.remove((newX-100,newY+100))
                                self.KingMoves.remove((newX-100,newY+100))
                    
                     # allows for player two's king to eat to the right up
                    elif (newX,newY) not in self.KingMoves and (newX+100,newY-100) in self.KingMoves:
                        for item in self.pieces:
                            # checks if one of the pieces that it wants to eat 
                            # is from the opponent
                            x = item.getAnchor().getX()
                            y = item.getAnchor().getY()
                            if (x,y) == (newX,newY) and newX+100>=800 and newY>=100:
                                item.undraw()
                                self.pieces.remove(item)
                                self.legalMoves.append((newX,newY))
                                self.legalMoves.append((oldX,oldY))
                                self.KingMoves.append((newX,newY))
                                self.KingMoves.append((oldX,oldY))
                                self.king2[self.onepiece2].move(200,-200)

                                self.legalMoves.remove((newX+100,newY-100))
                                self.KingMoves.remove((newX+100,newY-100))

                        for item in self.king1:
                            # checks if one of the pieces that it wants to eat 
                            # is from the opponent
                            x = item.getAnchor().getX()
                            y = item.getAnchor().getY()
                            if (x,y) == (newX,newY) and newX+100>=800 and newY>=100:
                                item.undraw()
                                self.king1.remove(item)
                                self.legalMoves.append((newX,newY))
                                self.legalMoves.append((oldX,oldY))
                                self.KingMoves.append((newX,newY))
                                self.KingMoves.append((oldX,oldY))
                                self.king2[self.onepiece2].move(200,-200)

                                self.legalMoves.remove((newX+100,newY-100))
                                self.KingMoves.remove((newX+100,newY-100))
                               
                               
                    # allows for player two's king to eat to the left up
                    elif (newX,newY) not in self.KingMoves and (newX-100,newY-100) in self.KingMoves:
                        for item in self.pieces:
                            # checks if one of the pieces that it wants to eat 
                            # is from the opponent
                            x = item.getAnchor().getX()
                            y = item.getAnchor().getY()
                            if (x,y) == (newX,newY) and newX-100>=0 and newY-100>=0:
                                item.undraw()
                                self.pieces.remove(item)
                                self.legalMoves.append((oldX,oldY))
                                self.legalMoves.append((newX,newY))
                                self.KingMoves.append((oldX,oldY))
                                self.KingMoves.append((newX,newY))
                                self.king2[self.onepiece2].move(-200,-200)
                                
                                self.legalMoves.remove((newX-100,newY-100))
                                self.KingMoves.remove((newX-100,newY-100))
                                
                        for item in self.king1:
                            # checks if one of the pieces that it wants to eat 
                            # is from the opponent
                            x = item.getAnchor().getX()
                            y = item.getAnchor().getY()
                            if (x,y) == (newX,newY) and newX-100>=0 and newY-100>=0:
                                item.undraw()
                                self.king1.remove(item)
                                self.legalMoves.append((oldX,oldY))
                                self.legalMoves.append((newX,newY))
                                self.KingMoves.append((oldX,oldY))
                                self.KingMoves.append((newX,newY))
                                self.king2[self.onepiece2].move(-200,-200)
                                
                                self.legalMoves.remove((newX-100,newY-100))
                                self.KingMoves.remove((newX-100,newY-100))
                    
            
                   
                                        
    



    def getPlayer1(self):
        # return name of player 1
        return self.player1


    def getPlayer2(self):
        # return name of player 2
        return self.player2


    def getPieces1(self):
        # return the length of player one's list
        return len(self.pieces)


    def getPieces2(self):
        # return the length of player two's list
        return len(self.pieces2)


    def isOver(self):
        #checks if the game is over and announces a winner
        if self.getPieces1() == 0:
            text = Text(Point(400,400), str(self.getPlayer1()))
            text.draw(self.win)
        
        if self.getPieces2() == 0:
            text = Text(Point(400,400), str(self.getPlayer2()))
            text.draw(self.win)
        

    def exitOnClick(self):
        #allows for the display window to close when the exit button is clicked
        click = self.win.getMouse()
        if 1320 <= click.getX <= 1400 and 760 <= click.getY() <= 800:
            self.win.close()


        
       
                

        
        
