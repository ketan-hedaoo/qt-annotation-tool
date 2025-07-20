
from PySide6 import QtWidgets
from abc import abstractmethod

class BaseWindow(QtWidgets.QMainWindow):
    param ={}
    window = None

    @abstractmethod
    def onResume(self):
        pass

    @abstractmethod
    def onPause(self):
        pass

    @abstractmethod
    def setClickCallback(self):
        pass

    @abstractmethod
    def onBackClicked(self):
        pass
    
    @abstractmethod
    def setStyles(self):
        pass

    def getParam(self, _key):
        return self.param.get(_key) 

    def setParam(self, _param):
        self.param = _param
    



    