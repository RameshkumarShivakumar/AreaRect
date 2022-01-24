from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivy.lang import Builder
from kivy.core.window import Window
Window.size=(350,600)
class India(MDFloatLayout):
    def resulting(self,*args):
        make1=self.ids.a1.text
        make2=self.ids.a2.text
        make3=int(make1)*int(make2)
        make4=[]
        make4.append(str(make3))
        for a in make4:
            self.ids.stylish1.text=a
    def rating(self,*args):
        ma1=self.ids.aa1.text
        ma2=self.ids.bb1.text
        ma3=self.ids.cc1.text
        ma4=int(ma1)+int(ma2)+int(ma3)/2
        ma5=[]
        ma5.append(str(ma4))
        for a in ma5:
            self.ids.stylish2.text=a
class Shorts(MDApp):
    def build(self):
        return India()
Shorts().run()