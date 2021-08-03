import kivy 
from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatButton
import time

#TESTTEST


kv = '''
CameraClick:
    orientation: 'vertical'
    Camera:
        id: camera
        #resolution: (640, 480)
        play: True
    MDFillRoundFlatButton:
        text: 'Capture'
        #size_hint_y: None
        #height: '48dp'
        pos_hint: {"center_x": .5, "center_y": .4}
        on_release: root.capture()
        #background_normal: ""
        md_bg_color: (173/255,252/255,3/255,0.7)
'''

class CameraClick(BoxLayout):
    def capture(self):
        camera = self.ids.camera
        time_str = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png(f'IMG_{time_str}.png')
        print("Captured")


class TestCamera(MDApp):
    def build(self):
        return Builder.load_string(kv)


    
if __name__ =="__main__":
    TestCamera().run()






