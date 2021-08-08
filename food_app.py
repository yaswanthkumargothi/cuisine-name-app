from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.camera import Camera
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
import food_predict
import tensorflow as tf
import cv2

#TESTTESTE:\freelance\kivy_app\cuisine-name-app\models\model.tflite
MODEL_PATH = "models\model.tflite"

labels=['Gulab jamun','Dhokla','Poori','Kathi roll','Idly','Meduvadai','Tandoori chicken',
 'Butternaan','Noodles','Vada pav','Biriyani','Ven pongal','Chaat','Halwa',
 'Upma','Bisibelebath','Samosa','Paniyaram','Chappati','Dosa']


# Load the TFLite model and allocate tensors.
interpreter = tf.lite.Interpreter(model_path = MODEL_PATH)
interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()



class TestNavigationDrawer(MDApp):
    def build(self):
        return Builder.load_file("appgui.kv")
       

class Cameraclick(MDBoxLayout):
    dialog = None
    def capture(self):
        camera=self.ids.camera1
        camera.export_to_png(f'food.png')
        #read image
        img_arr = cv2.imread("food.png")
        resized_arr = cv2.resize(img_arr, (256, 256))
        
        food_predict.set_input_tensor(interpreter, resized_arr)
        food_name = food_predict.classify_image(interpreter,labels, top_k=1)
        print(food_name)
        if not self.dialog:
            self.dialog = MDDialog(
                title=food_name[0][0],
                type="simple",
                buttons=[
            MDFlatButton(text="Close", on_release=self.closeDialog)],
            )
        self.dialog.open()

    def closeDialog(self,inst):
        self.dialog.dismiss()


TestNavigationDrawer().run()


        







