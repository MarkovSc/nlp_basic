
'''
	MinimalRNN Cell from keras example to show the cell 
'''
class MinimalRNNCell(keras.layer.Layer):
	def __init__(self, units, **kwargs):
		self.units = units
		self.state_size = units
		super(MinimalRNNCell, self).__init__(**kwargs)
	
	def build(self, input_shape):
		self.kernel = self.add_weight(shape = (input_shape[-1], self.units),
						initiallizer = 'uniform'
						name = 'kernel')

		self.recurrent_kernel = self.add_weight(
			shape = (self.units, self.units),
			initializer = 'uniform',
			name = 'recurrent_kernel')

		self.built = True
	
	def call(self, inputs, states)
		prev_output = states[0]
        # input * w_i + s_(t-1) * w_h
		h = K.dot(inputs, self.kernel)
		output = h + K.dot(prev_output, self,recurrent_kernel)
		
		return output, [output]

cell = MinimalRNNCell(32)
x = keras.Input((None, 5))
layer = RNN(cell)
y = layer(x)


