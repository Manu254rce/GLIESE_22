import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random
import pandas as pd
import os, wget
 
# from sklearn.model_selection import train_test_split
from keras import layers, Model
from keras.preprocessing.image import ImageDataGenerator
# from keras.utils import img_to_array, load_img
from keras.optimizers import RMSprop
# from keras.losses import categorical_crossentropy
from keras.applications.inception_v3 import InceptionV3

url = 'https://storage.googleapis.com/mledu-datasets/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5'

if not os.path.exists('./inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5'):
    wget.download(url, './inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5')

local_weights_file = './inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5'

pre_trained_model = InceptionV3(input_shape=(150, 150, 3), include_top=False, weights=None)  # type: ignore
pre_trained_model.load_weights(local_weights_file)

for layer in pre_trained_model.layers:
    layer.trainable = False

last_layer = pre_trained_model.get_layer('mixed7')
print('last layer output shape: ', last_layer.output_shape)
last_output = last_layer.output

stars = pd.read_csv('./data/Datasets/HYG_Catalogue.csv')

data_ngcic = pd.read_excel('./data/Datasets/DSO-NGCIC Classification.xlsx', sheet_name='NGCIC Classification')
data_dso = pd.read_excel('./data/Datasets/DSO-NGCIC Classification.xlsx', sheet_name='DSO Classification')
print('Messier Objects:', data_dso.shape)
print('NGCIC Objects:', data_ngcic.shape)
print('Data shape: ', data_ngcic.shape, data_dso.shape)
print('Details: ', data_ngcic.columns, data_dso.columns)

data_ngcic['float ra'] = data_ngcic['ra hr'] + data_ngcic['ra min']/60 + data_ngcic['ra sec']/3600
data_ngcic['float dec'] = data_ngcic['dec deg '] + data_ngcic['dec min']/60 + data_ngcic['dec sec']/3600

plt.figure(figsize=(30, 10))
plt.ylim(-90, 90)
plt.xlabel('Right Ascension')
plt.ylabel('Declination')
plt.xticks(np.arange(0, 24, 1), labels=['0h', '1h', '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h',
                                        '10h', '11h', '12h', '13h', '14h', '15h', '16h', '17h', '18h',
                                        '19h', '20h', '21h', '22h', '23h'])
plt.yticks(np.arange(-90, 90, 10), labels=['-90deg', '-80deg', '-70deg', '-60deg', '-50deg', '-40deg', '-30deg',
                                           '-20deg', '-10deg', '0deg', '10deg', '20deg', '30deg', '40deg', '50deg',
                                           '60deg', '70deg', '80deg'])
plt.title('Plot for NGCIC Objects in the Sky', fontsize=20, fontweight='bold')
plt.scatter(data_ngcic['float ra'], data_ngcic['float dec'], s=0.09, c='red')
plt.scatter(stars['ra'], stars['dec'], s=0.01, c='blue')
plt.legend(['NGCIC Objects', 'Stars'], loc='upper right', fontsize=16, markerscale=10)
plt.show()

base_dir = './data/Images'

train_dir = os.path.join( base_dir, 'training_set')
validation_dir = os.path.join( base_dir, 'validation_set')

train_diffuse_nebula_dir = os.path.join(train_dir, 'dark_nebula') 
train_diffuse_nebula_dir = os.path.join(train_dir, 'diffuse_nebula') 
train_diffuse_nebula_dir = os.path.join(train_dir, 'dwarf_elliptical') 
train_diffuse_nebula_dir = os.path.join(train_dir, 'elliptical_galaxy') 
train_diffuse_nebula_dir = os.path.join(train_dir, 'globular_cluster') 
train_diffuse_nebula_dir = os.path.join(train_dir, 'interacting_galaxy') 
train_diffuse_nebula_dir = os.path.join(train_dir, 'irregular_galaxy') 
train_diffuse_nebula_dir = os.path.join(train_dir, 'open_cluster') 
train_diffuse_nebula_dir = os.path.join(train_dir, 'planetary_nebula') 
train_diffuse_nebula_dir = os.path.join(train_dir, 'spiral_galaxy') 
train_diffuse_nebula_dir = os.path.join(train_dir, 'supernova_rem') 

validation_diffuse_nebula_dir = os.path.join(validation_dir, 'dark_nebula')
validation_diffuse_nebula_dir = os.path.join(validation_dir, 'diffuse_nebula')
validation_diffuse_nebula_dir = os.path.join(validation_dir, 'dwarf_elliptical')
validation_diffuse_nebula_dir = os.path.join(validation_dir, 'elliptical_galaxy')
validation_diffuse_nebula_dir = os.path.join(validation_dir, 'globular_cluster')
validation_diffuse_nebula_dir = os.path.join(validation_dir, 'interacting_galaxy')
validation_diffuse_nebula_dir = os.path.join(validation_dir, 'irregular_galaxy')
validation_diffuse_nebula_dir = os.path.join(validation_dir, 'open_cluster')
validation_diffuse_nebula_dir = os.path.join(validation_dir, 'planetary_nebula')
validation_diffuse_nebula_dir = os.path.join(validation_dir, 'spiral_galaxy')
validation_diffuse_nebula_dir = os.path.join(validation_dir, 'supernova_rem')

# Add our data-augmentation parameters to ImageDataGenerator
train_datagen = ImageDataGenerator(rescale = 1./255.,
                                   rotation_range = 40,
                                   width_shift_range = 0.2,
                                   height_shift_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

# Note that the validation data should not be augmented!
test_datagen = ImageDataGenerator( rescale = 1.0/255. )

# Flow training images in batches of 20 using train_datagen generator
train_generator = train_datagen.flow_from_directory(train_dir,
                                                    batch_size = 20,
                                                    class_mode = 'categorical', 
                                                    target_size = (150, 150))     

# Flow validation images in batches of 20 using test_datagen generator
validation_generator =  test_datagen.flow_from_directory( validation_dir,
                                                          batch_size  = 20,
                                                          class_mode  = 'categorical', 
                                                          target_size = (150, 150))


x = layers.Flatten()(last_output)
x = layers.Dense(1024, activation='relu')(x)
x = layers.Dropout(0.2)(x)                  
x = layers.Dense  (11, activation='softmax')(x)           
model = Model(pre_trained_model.input, x) 

model.compile(optimizer = RMSprop(learning_rate=0.0001), 
              loss = 'categorical_crossentropy', 
              metrics = ['accuracy'])

history = model.fit(
            train_generator,
            validation_data = validation_generator,
            # steps_per_epoch = 100,
            epochs = 20,
            # validation_steps = 50
            )

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(len(acc))

plt.figure(figsize=(20, 10))
plt.plot(epochs, acc, 'r', label='Training accuracy')
plt.plot(epochs, val_acc, 'b', label='Validation accuracy')
plt.title('Training and validation accuracy')
plt.legend(loc='lower right')
plt.figure()

plt.show()