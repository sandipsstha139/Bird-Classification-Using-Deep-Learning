import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import os

# Disable GPU usage
tf.config.set_visible_devices([], 'GPU')


# # Provide the path to your saved model
print("Current working directory:", os.getcwd())

model_path = 'home/bird_classification_model.h5'
model = load_model(model_path)


class_labels=['Abbott’s Babbler',
 'Black Bittern',
 'Blue-eared Kingfisher',
 'Blue-naped Pitta',
 'Broad-billed Warbler',
 'Cheer Pheasant',
 'Chestnut Munia',
 'Cinereous Vulture',
 'Golden Babbler',
 'Goulds Shortwing ',
 'Great Bittern',
 'Great Hornbill',
 'Great Slaty Woodpecker',
 'Ibisbill',
 'Indian Courser',
 'Indian Grassbird',
 'Indian Nightjar',
 'Knob-billed Duck',
 'Northern Pintail',
 'Painted Stork',
 'Purple Cochoa',
 'Red-headed Trogon',
 'Red-headed Vulture ',
 'Red-necked Falcon',
 'Ruby-cheeked Sunbird',
 'Rusty-fronted',
 'Saker Falcon',
 'Silver-eared Mesia',
 'Slaty-legged Crake',
 'Spot-bellied Eagle Owl',
 'Sultan Tit',
 'Swamp Francolin ',
 'Tawny-bellied Babbler',
 'Thick-billed Green Pigeon ',
 'White-throated Bulbul',
 'White-throated Bushchat',
 'Yellow-rumped Honeyguide',
 'Yellow-vented Warbler']

# class_labels=['Abbott’s Babbler Malacocincla abbotti',
#  'Black Bittern (Dupetor flavicollis)',
#  'Blue-eared Kingfisher Alcedo meninting',
#  'Blue-naped Pitta Pitta nipalensis',
#  'Broad-billed Warbler Tickellia hodgsoni',
#  'Cheer Pheasant (Catreus wallichii)',
#  'Chestnut Munia Lonchura atricapilla',
#  'Cinereous Vulture Aegypius monachus',
#  'Golden Babbler Stachyris chrysaea',
#  'Goulds Shortwing Brachypteryx stellata',
#  'Great Bittern Botaurus stellaris',
#  'Great Hornbill (Buceros bicornis)',
#  'Great Slaty Woodpecker Mulleripicus pulverulentus',
#  'Ibisbill Ibidorhyncha struthersii',
#  'Indian Courser Cursorius coromandelicus',
#  'Indian Grassbird - Graminicola bengalensis',
#  'Indian Nightjar Caprimulgus asiaticus',
#  'Knob-billed Duck Sarkidiornis melanotos',
#  'Northern Pintail Anas acuta',
#  'Painted Stork Mycteria leucocephala',
#  'Purple Cochoa Cochoa purpurea',
#  'Red-headed Trogon Harpactes erythrocephalus',
#  'Red-headed Vulture Sarcogyps calvus',
#  'Red-necked Falcon Falco chicquera',
#  'Ruby-cheeked Sunbird Anthreptes singalensis',
#  'Rusty-fronted Barwing Actinodura egertoni',
#  'Saker Falcon Falco cherrug',
#  'Silver-eared Mesia Leiothrix argentauris',
#  'Slaty-legged Crake Rallina eurizonoides',
#  'Spot-bellied Eagle Owl Bubo nipalensis',
#  'Sultan Tit Melanochlora sultanea',
#  'Swamp Francolin Francolinus gularis',
#  'Tawny-bellied Babbler Dumetia hyperythra',
#  'Thick-billed Green Pigeon Treron curvirostra',
#  'White-throated Bulbul Alophoixus flaveolus',
#  'White-throated Bushchat Saxicola insignis',
#  'Yellow-rumped Honeyguide - Indicator xanthonotus',
#  'Yellow-vented Warbler Phylloscopus cantator']


from PIL import Image

def predictClassLabel(image, threshold = 0.4):
    # Load and preprocess the image
    img = Image.open(image)
    img = img.resize((224, 224)) 

    # Convert the image to an array
    img_array = np.array(img) / 255.0  
    img_array = np.expand_dims(img_array, axis=0)  

    # Make predictions
    predictions = model.predict(img_array)

    predicted_class_index = np.argmax(predictions)

  
    predicted_class_label = class_labels[predicted_class_index]

    predicted_probability = predictions[0][predicted_class_index]
    if predicted_probability >= threshold:
        predicted_class_label = class_labels[predicted_class_index]
        print("Predicted Class Label:", predicted_class_label)
        return predicted_class_label
    else:
        print("Prediction probability below threshold. Model not confident.")
        return None

    # print("Predicted Class Label:", predicted_class_label)
    # return predicted_class_label

#to prevent the model loading when I am learning an API i have commented the above code with a dummy function

# the following code is just a dummy
# def predictClassLabel(image):
#     return "Dummy text"

