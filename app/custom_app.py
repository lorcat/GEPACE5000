from app.load import *

class CustomApplication(qtgui.QApplication, Tester):
    def __init__(self, *args, **kwargs):
        qtgui.QApplication.__init__(self, *args, **kwargs)
        Tester.__init__(self)

    def notify(self, obj, event):
        try:
            return qtgui.QApplication.notify(self, obj, event)
        except Exception as e:
            self.error("Exception on the application level ({})".format(e))
        return False