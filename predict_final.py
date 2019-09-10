import h5py
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

model = load_model('model/model.h5')
print(model.summary())
text = input("enter the post content: ")
text = text.replace('\d+', '')
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
from keras.preprocessing.sequence import pad_sequences
seq = tokenizer.texts_to_sequences(text)
padded = pad_sequences(seq, maxlen=max_sequence_len)
pred = model.predict(padded)
pred = np.mean(pred, axis=0)
labels = ['Politics','[R]eddiquette','Non-Political','AskIndia','Policy/Economy','Business/Finance','Science/Technology','Sports','Photography','AMA']
print(labels[np.argmax(pred)])