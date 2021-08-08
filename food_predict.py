import numpy as np
#set input tensor
def set_input_tensor(interpreter, image):
  tensor_index = interpreter.get_input_details()[0]['index']
  input_tensor = interpreter.tensor(tensor_index)()[0]
  input_tensor[:, :] = image

def classify_image(interpreter,labels, top_k=1):
    
    
    interpreter.invoke()

    output_details = interpreter.get_output_details()[0]
    output = np.squeeze(interpreter.get_tensor(output_details['index']))

    ordered = np.argpartition(-output, top_k)
    result=[(i, output[i]) for i in ordered[:top_k]]
    return [(labels[id], prob*100) for id, prob in result]
