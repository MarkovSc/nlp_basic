from keras.layers import Layer
from keras import backend as K
from keras.models import Sequential, Model
from keras.layers import BatchNormalization, Input, Embedding, SpatialDropout1D, concatenate, Conv2D, Reshape, Conv1D
from keras.layers import MaxPool2D, PReLU, AvgPool2D, MaxPooling1D
from keras.layers.core import Flatten, Dense, Dropout, Lambda
from keras.optimizers import Adam



class MyLayer(Layer):
	def __init__(self, output_dim, **kwargs):
		self.output_dim = output_dim
		super(MyLayer, self).__init__(**kwargs)

	def build(self, input_shape):
		print(type(input_shape))
		self.kernel = self.add_weight(name='kernel',
						shape = (input_shape[-1], self.output_dim),
						initializer = 'uniform',
						trainable = True)
		super(MyLayer, self).build(input_shape)
	
	def call(self, x):
		print("invoke call")
		#assert isinstance(input_shape, list)
		return [K.dot(x, self.kernel)]

inp = Input(shape=(10,), name="test") 
output = MyLayer(10)(inp)
model = Model(inputs=inp, outputs=output)
model.summary()
