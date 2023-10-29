def createMatrix(iAxisOfMatrix,jAxisOfMatrix,matriceV0):
    for i in range(iAxisOfMatrix):
        matriceV0.append([]) 
        for j in range(jAxisOfMatrix):
            matriceV0[i].append(0)

def ijAxisCheck(iAxisOfMatrix ,jAxisOfMatrix):
    if  iAxisOfMatrix == 0 or iAxisOfMatrix > 9 or  jAxisOfMatrix == 0 or jAxisOfMatrix > 9:
        return True  

def ax_iax_jCheck(ax_I ,ax_J):

        return False  


def printmatrix(matrice):
    print(matrice)
    print('*' * 50)


def switchPlayersTurn(player):
    if player == 'player1' :
        return 'player2'
    else:
        return 'player1'



def modifyMatrix(ax_I,ax_J , playersTurn,matrice) :
    if playersTurn == 'player1' :
        matrice[ax_I][ax_J] = 1
    else:
        matrice[ax_I][ax_J] = 2


def testInvalidPositionInMatrix(ax_I, ax_J, iAxisOfMatrix, jAxisOfMatrix, matrice):
    if ax_I > iAxisOfMatrix  or ax_I < 0 or ax_J < 0 or ax_J > jAxisOfMatrix :
        return False  #out of bounds
    elif matrice[ax_I][ax_J] == 0:
        return False  # already taken
    else:
        return True  # Valid position





def checkTopLeftCorner(matrice, ax_I , ax_J):
    # pour( ax_I = 0 , ax_J = 0)
     return (matrice[ax_I][ax_J] == matrice[ax_I][ax_J+1]  == matrice[ax_I][ax_J+2]  !=0  or  matrice[ax_I][ax_J] == matrice[ax_I+1][ax_J] == matrice[ax_I+2][ax_J]  !=0  or  matrice[ax_I][ax_J] == matrice[ax_I+1][ax_J+1] == matrice[ax_I+2][ax_J+2]  !=0)
        
def checkTopRightCorner(matrice, ax_I , ax_J):
    #pour(0,N)
    return (matrice[ax_I][ax_J] == matrice[ax_I][ax_J-1] == matrice[ax_I][ax_J-2]  !=0  or matrice[ax_I][ax_J] == matrice[ax_I+1][ax_J] == matrice[ax_I+2][ax_J]  !=0  or matrice[ax_I][ax_J] == matrice[ax_I-1][ax_J+1] == matrice[ax_I-2][ax_J+2]  !=0  ) 

def checkBottomLeftCorner(matrice, ax_I , ax_J):
    #pour(N,0)
    return (matrice[ax_I][ax_J] == matrice[ax_I-1][ax_J] == matrice[ax_I-2][ax_J]  !=0  or matrice[ax_I][ax_J] == matrice[ax_I][ax_J-1] == matrice[ax_I][ax_J-2]  !=0  or matrice[ax_I][ax_J] == matrice[ax_I-1][ax_J+1] == matrice[ax_I-2][ax_J+2]  !=0 ) 

def checkBottomRightCorner(matrice, ax_I , ax_J):
   #pour(N,N)
    return (matrice[ax_I][ax_J] == matrice[ax_I-1][ax_J] == matrice[ax_I-1][ax_J]  !=0  or matrice[ax_I][ax_J] == matrice[ax_I][ax_J-1] == matrice[ax_I][ax_J-2]  !=0  or matrice[ax_I][ax_J] == matrice[ax_I-1][ax_J-1] == matrice[ax_I-2][ax_J-2]  !=0)  
    

    
def checkCenter(matrice, ax_I , ax_J):
    #pour centre
    return (matrice[ax_I][ax_J] == matrice[ax_I-1][ax_J] == matrice[ax_I+1][ax_J]  !=0  
            or matrice[ax_I][ax_J] == matrice[ax_I][ax_J-1] == matrice[ax_I][ax_J+1]  !=0  
            or matrice[ax_I][ax_J] == matrice[ax_I-1][ax_J-1] == matrice[ax_I+1][ax_J+1]  !=0    
            or matrice[ax_I][ax_J] == matrice[ax_I-1][ax_J+1] == matrice[ax_I+1][ax_J-1]  !=0  
             )


def checkTopLine(matrice, ax_I , ax_J):
    #i >0 and i< -1 and j =0
    return (matrice[ax_I][ax_J] == matrice[ax_I][ax_J+1] == matrice[ax_I][ax_J+2]  !=0  
            or matrice[ax_I][ax_J] == matrice[ax_I][ax_J-1] == matrice[ax_I][ax_J-2]  !=0
            or matrice[ax_I][ax_J] == matrice[ax_I+1][ax_J] == matrice[ax_I+2][ax_J]  !=0
            or matrice[ax_I][ax_J] == matrice[ax_I][ax_J+1] == matrice[ax_I][ax_J-1]  !=0 ) 
def checkBottomLine(matrice, ax_I , ax_J):
    #i >0 and i< -1 and j = -1
    return (matrice[ax_I][ax_J] == matrice[ax_I][ax_J-1] == matrice[ax_I][ax_J+1]  !=0  
            or matrice[ax_I][ax_J] == matrice[ax_I-1][ax_J] == matrice[ax_I-2][ax_J]  !=0
            or matrice[ax_I][ax_J] == matrice[ax_I][ax_J+1] == matrice[ax_I][ax_J+2]  !=0
            or matrice[ax_I][ax_J] == matrice[ax_I][ax_J-1] == matrice[ax_I][ax_J-2]  !=0 ) 
def checkLeftLine(matrice, ax_I , ax_J):
    # j>0 and j< -1 and i = 0
    return (matrice[ax_I][ax_J] == matrice[ax_I+1][ax_J] == matrice[ax_I+2][ax_J]  !=0 
            or matrice[ax_I][ax_J] == matrice[ax_I-1][ax_J] == matrice[ax_I-2][ax_J]  !=0 
            or matrice[ax_I][ax_J] == matrice[ax_I][ax_J+1] == matrice[ax_I][ax_J+2]  !=0
            or matrice[ax_I][ax_J] == matrice[ax_I+1][ax_J] == matrice[ax_I+2][ax_J]  !=0
) 
def checkRighLine(matrice, ax_I , ax_J):
    # j>0 and j< -1 and i = -1
    return (matrice[ax_I][ax_J] == matrice[ax_I+1][ax_J] == matrice[ax_I+2][ax_J]  !=0  
            or matrice[ax_I][ax_J] == matrice[ax_I-1][ax_J] == matrice[ax_I-2][ax_J]  !=0
            or matrice[ax_I][ax_J] == matrice[ax_I+1][ax_J] == matrice[ax_I-1][ax_J]  !=0
            or matrice[ax_I][ax_J] == matrice[ax_I][ax_J-1] == matrice[ax_I][ax_J-2]  !=0
 ) 

def checkFordraw(matrice):
    if 0 not in matrice:
        return False  # Stop 
    return True  # Continue 


def checkWinPlayer(matrice, ax_I, ax_J, iAxisOfMatrix, jAxisOfMatrix):

    if ax_I == 0 and ax_J == 0 and checkTopLeftCorner(matrice, ax_I, ax_J):
        return True

    elif ax_I == 0 and ax_J == jAxisOfMatrix -1 and checkTopRightCorner(matrice, ax_I, ax_J):
        return True

    elif ax_I == iAxisOfMatrix -1 and ax_J == 0  and checkBottomLeftCorner(matrice, ax_I, ax_J):
        return True


    elif ax_I == iAxisOfMatrix -1 and ax_J == jAxisOfMatrix -1  and checkBottomRightCorner(matrice, ax_I, ax_J):
        return True
        
    elif ax_I > 0 and ax_I < iAxisOfMatrix -1 and ax_J == 0 and checkTopLine(matrice, ax_I, ax_J):
        return True

    elif ax_I > 0 and ax_I < iAxisOfMatrix -1 and ax_J == -1 and checkBottomLine(matrice, ax_I, ax_J):
        return True

    elif ax_J > 0 and ax_J < jAxisOfMatrix-1 and ax_I == 0 and checkLeftLine(matrice, ax_I, ax_J):
        return True

    elif ax_J > 0 and ax_J < jAxisOfMatrix -1 and ax_I == -1 and checkLeftLine(matrice, ax_I, ax_J):
        return True













