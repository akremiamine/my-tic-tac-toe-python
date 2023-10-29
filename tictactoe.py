import numpy as np
from utils import *




if __name__ == "__main__":

    while True:

        matriceV0 = []
        matrice = np.array(matriceV0)
        iAxisOfMatrix = int(input('iAxisOfMatrix : '))
        jAxisOfMatrix = int(input('jAxisOfMatrix : '))

        if ijAxisCheck(iAxisOfMatrix ,jAxisOfMatrix):
            print("This is not a number. Please enter a valid number")
            continue
        createMatrix (iAxisOfMatrix,jAxisOfMatrix,matriceV0)
        matrice = np.array(matriceV0)
        printmatrix(matrice)
        playersTurn = 'player'+input('1 or 2 : ')
        playersTurn

        while True:
            print(playersTurn, 'is your  turn')
            ax_I = int(input('Enter the row : '))
            ax_J = int(input('Enter the column : ' ))

            if testInvalidPositionInMatrix(ax_I, ax_J, iAxisOfMatrix, jAxisOfMatrix, matrice) :
                continue
            modifyMatrix(ax_I, ax_J, playersTurn, matrice)
            
            if  checkWinPlayer(matrice, ax_I, ax_J, iAxisOfMatrix, jAxisOfMatrix) :
                printmatrix(matrice)
                print(playersTurn ,' win')
                break
            

            printmatrix(matrice) 
            playersTurn = switchPlayersTurn(playersTurn)
            if not checkFordraw(matrice):
                break

