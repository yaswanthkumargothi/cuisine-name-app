import kivy 
from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatButton
import time
import food_predict
import tensorflow as tf
import cv2

#TESTTEST
MODEL_PATH = "cuisine-name-app\models\model.tflite"

labels=['gulab jamun','dhokla','poori','kathi roll','idly','meduvadai','tandoori chicken',
 'butternaan','noodles','vada pav','biriyani','ven pongal','chaat','halwa',
 'upma','bisibelebath','samosa','paniyaram','chappati','dosa']


# Load the TFLite model and allocate tensors.
interpreter = tf.lite.Interpreter(model_path = MODEL_PATH)
interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()



##
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
        food_image = camera.export_to_png(f'IMG_{time_str}.png')
        #read image
        img_arr = cv2.imread(food_image, cv2.IMREAD_UNCHANGED) #[...,::-1] #convert BGR to RGB format #optional
        resized_arr = cv2.resize(img_arr, (256, 256))
        
        food_predict.set_input_tensor(interpreter, resized_arr)
        food_name = food_predict.classify_image(interpreter, food_image, top_k=1)

        
        
        print(food_name)


class TestCamera(MDApp):
    def build(self):
        return Builder.load_string(kv)


    
if __name__ =="__main__":
    TestCamera().run()






