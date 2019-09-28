#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow_datasets as tfds


# In[177]:


mnist_dataset, mnist_info = tfds.load(name='mnist', with_info=True, as_supervised=True)


# In[178]:


mnist_train, mnist_test = mnist_dataset['train'], mnist_dataset['test']


# In[179]:


num_validation_samples = 0.1 * mnist_info.splits['train'].num_examples
num_validation_samples = tf.cast(num_validation_samples, tf.int64)


num_test_samples = mnist_info.splits['test'].num_examples
num_test_samples = tf.cast(num_validation_samples, tf.int64)


# In[180]:


def scale(image, label):
    image = tf.cast(image, tf.float32)
    image /= 255.
    return image, label


# In[181]:


scaled_train_and_validation = mnist_train.map(scale)
test_data = mnist_test.map(scale)


# In[182]:


BUFFER_SIZE = 10000
shuffled_train_and_validation = scaled_train_and_validation
validation_data = shuffled_train_and_validation.take(num_validation_samples)
train_data = shuffled_train_and_validation.skip(num_validation_samples)


# In[183]:


BATCH_SIZE = 100

validation_data = validation_data.batch(BATCH_SIZE)
train_data = train_data.batch(BATCH_SIZE)
test_data = test_data.batch(BATCH_SIZE)

validation_inputs, validation_targets = next(iter(validation_data))


# In[184]:


input_size = 784
output_size = 10
hidden_layer_size = 200


# In[63]:


model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape = (28,28,1)),
    tf.keras.layers.Dense(hidden_layer_size,activation = 'relu'),
    tf.keras.layers.Dense(hidden_layer_size,activation = 'relu'),
    tf.keras.layers.Dense(output_size, activation = 'softmax')
])

model.compile(optimazer = 'Adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])


# In[64]:


NUM_EPOCHS = 5
STEPS = num_validation_samples/BATCH_SIZE
model.fit(train_data, epochs = NUM_EPOCHS, validation_data=(validation_inputs, validation_targets), validation_steps=STEPS, verbose = 2)
        


# In[65]:


test_loss, test_accuracy = model.evaluate(test_data)


# In[66]:


print('Test loss: {0:.2f}. Test accuracy: {1:.2f}%'.format(test_loss, test_accuracy*100.))


# In[185]:


validation_inputs = tf.Variable(validation_inputs)


# In[191]:


validation_input = tf.reshape(validation_inputs[12], (1,28, 28,1))

pred = model.predict(validation_input)

val_input = tf.reshape(validation_inputs[12], (28,28))

plt.imshow(val_input,cmap='Greys')
print(pred.argmax())


# In[ ]:




