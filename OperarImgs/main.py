'''
Created on 10/4/2015

@author: rodrigo
'''
from PyQt4.QtGui import QApplication, QMainWindow, QGraphicsScene, QFileDialog, \
    QImage, QPixmap, QGraphicsPixmapItem
import sys

from mainwin import Ui_MainWindow


class Ventana(Ui_MainWindow, QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)        
        self.actionOpenImgA.triggered.connect(self.cargarImgA)
        self.actionOpenImgB.triggered.connect(self.cargarImgB)
        self.actionOperate.triggered.connect(self.operar)
        
        self.escenaA = QGraphicsScene()
        self.imgA.setScene(self.escenaA)
        
        self.escenaB = QGraphicsScene()
        self.imgB.setScene(self.escenaB)
        
        self.escenaC = QGraphicsScene()
        self.imgC.setScene(self.escenaC)
        
        self.operacion.addItem("suma")
        self.operacion.addItem("multiplicacion")
        self.operacion.addItem("promedio")
    
    def cargarImgA(self):
        self.imagenA = self.cargarImg(self.escenaA)
        
    def cargarImgB(self):
        self.imagenB = self.cargarImg(self.escenaB)
    
    def cargarImg(self, escena):
        ruta =QFileDialog.getOpenFileName(parent=self, caption="Archivo")
        imagen = QImage()
        imagen.load(ruta)
        pixmap = QPixmap(imagen)
        escena.addItem(QGraphicsPixmapItem(pixmap))
        return imagen

    def operar(self):
        ancho = min(self.imagenA.width(), self.imagenB.width())
        alto  = min(self.imagenA.height(), self.imagenB.height())
        
        oper = getattr(self,str(self.operacion.currentText()))
        
        self.imagenC = QImage(ancho, alto, QImage.Format_RGB32 )
        
        for i in range(ancho):
            for j in range(alto):
                pix = oper(self.imagenA.pixel(i,j), self.imagenB.pixel(i,j))
                self.imagenC.setPixel(i, j, pix)
        
        pixmap = QPixmap(self.imagenC)
        self.escenaC.addItem(QGraphicsPixmapItem(pixmap))
        
    def suma(self, pixA, pixB):
        return pixA + pixB
    
    def multiplicacion(self, pixA, pixB):
        return pixA * pixB
    
    def promedio(self, pixA, pixB):
        return (pixA + pixB) / 2
             

def main():
    app = QApplication(sys.argv)
    win = Ventana()
    win.show()
    return app.exec_()


if __name__ == '__main__':
    main()