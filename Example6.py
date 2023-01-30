from PyQt6 import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class yakitHesaplayicisi (QDialog):
    def __init__(self, parent=None):
        super(yakitHesaplayicisi,self).__init__(parent)
        # ızgarayı oluştur:
        izgara = QGridLayout()
        # widgetları tek tek ekle (gui jpgsindeki tasarıma göre)
        izgara.addWidget(QLabel ('Gideceğiniz Yol (km):'),0,0,1,1)
        self.gidilenYol = QLineEdit() # QlineEdit metin kutusu oluşturur
        self.gidilenYol.setInputMask('0000000000') # text giriş formatını netleştirir.
        izgara.addWidget(self.gidilenYol,0,1,1,1)
        
        izgara.addWidget(QLabel ('Yakıtın Litre Fiyatı:'),1,0,1,1)
        self.yakitFiyati = QLineEdit() # QlineEdit edit edilebilir metin kutusu oluşturur
        self.yakitFiyati.setInputMask('00.00') # text giriş formatını netleştirir.
        izgara.addWidget(self.yakitFiyati,1,1,1,1)
        
        izgara.addWidget(QLabel ("100km'de Tüketilen Yakıt:" ),2,0,1,1)
        self.yakitTuketimi = QLineEdit() # QlineEdit edit edilebilir metin kutusu oluşturur
        self.yakitTuketimi.setInputMask('0.0') # text giriş formatını netleştirir.
        izgara.addWidget(self.yakitTuketimi,2,1,1,1)
        
        
        izgara.addWidget(QLabel ("Toplam Tutar:" ),3,0,1,1)
        self.tutar = (QLabel('<i> KM Giriniz</i>')) 
        izgara.addWidget(self.tutar,3,1,1,1)
        
        
        self.hesaplaDugmesi = QPushButton("Hesapla")
        self.hesaplaDugmesi.clicked.connect(self.yakitHesapla)
        izgara.addWidget(self.hesaplaDugmesi,4,0,1,2)
        
        
        self.setLayout(izgara)
        self.setWindowTitle('Yakıt Hesaplayıcısı')
        
        
    def yakitHesapla (self):
        yol = 0
        try: yol = int(self.gidilenYol.text())
        except: pass
    
        fiyat = 0
        try: fiyat = float(self.yakitFiyati.text())
        except: pass
    
        tuketim = 0
        try: tuketim = float(self.yakitTuketimi.text())
        except: pass
    
    
        if not yol :
            self.tutar.setText('<font color ="red"><i> KM giriniz</i></font>')
            self.gidilenYol.setFocus()    
        elif not fiyat:
            self.tutar.setText('<font color ="red"><i> Fiyat Giriniz</i></font>')
            self.yakitFiyati.setFocus()
        elif not tuketim:
            self.tutar.setText('<font color ="red"><i> Tuketim Giriniz</i></font>')
            self.yakitTuketimi.setFocus()
            
        else: 
            tutar = fiyat*((yol*tuketim)/100)
            self.tutar.setText('<font color ="black"><b>%0.2f</b></font>' % tutar)
            
            
    
uyg = QApplication([]) 
pencere = yakitHesaplayicisi()   
pencere.show()
uyg.exec()
