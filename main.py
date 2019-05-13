# Work by Fabien AUBRET <fabien.aubret@gadzarts.org>
# For Arts et Metiers engineering school
# Published under Open Source License

import re
import numpy as np
from dictionary import *

from keras.models import Sequential
from keras.layers import Dense, Activation

# This is to eliminate punctuation in future messages
Punctuation = [',', ':', '.', '?', '!', ';', '-', '(', ')']

message_list = []                           # This will store the list of message AND their labels
dataset_file = open('dataset.txt', 'r')     # This is our dataset file
type_regex = r"(.+)\.\s([0-1])"             # This is a regex that will be used to identify labels in messages

# We will gather our messages by iterating over the dataset file
for line in dataset_file.readlines():
    matches = re.finditer(type_regex, line)
    for matchNum, match in enumerate(matches, start=1):
        message_list.append([match.group(1), match.group(2)])

labels = []
for entry in message_list:
    labels.append([int(entry[1])])
# Our labels are ready


# Let's create our dictionary
# We're not removing non-sense words (such as 'the', 'a', 'in') because
# statistically speaking, the AI model will not care about them later

dictionary = Dictionary()
words = []
splitted_msg = []
for msg in message_list:
    current_msg = msg[0]
    current_msg_split = current_msg.split(' ')
    splitted_msg.append([])
    for word in current_msg_split:
        for p in Punctuation:
            word = word.replace(p, '')
        if word not in dictionary:
            dictionary.push(word)
        words.append(word)
        splitted_msg[-1].append(word)

# dictionary = dictionary.reduce(words, 500)

# Our dictionary is ready, let's build our input vectors
input_vectors = []
for msg in splitted_msg:
    # msg_vector = np.zeros((len(dictionary), 1))
    msg_vector = [0 for k in range(len(dictionary))]
    for word in msg:
        word_index = dictionary.get_by_element(word)
        msg_vector[word_index] += 1
    input_vectors.append(msg_vector)

train_test_limit = 2 * (len(input_vectors) // 3)
train_features = np.array(input_vectors[0:train_test_limit])
train_labels = np.array(labels[0:train_test_limit])             # This is just a reminder, now we know the name of our vars for AI model

test_features = np.array(input_vectors[train_test_limit::])
test_labels = np.array(labels[train_test_limit::])

# print(labels)

# Let's implement it
model = Sequential()
model.add(Dense(500, input_dim=len(dictionary)))
model.add(Activation('relu'))
model.add(Dense(500, input_dim=len(dictionary)))
model.add(Activation('relu'))
model.add(Dense(500, input_dim=len(dictionary)))
model.add(Activation('relu'))
model.add(Dense(500, input_dim=len(dictionary)))
model.add(Activation('relu'))
model.add(Dense(1, input_dim=len(dictionary)))
model.add(Activation('relu'))

model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(train_features, train_labels, epochs=50, batch_size=10)

errors = 0
for k in range(len(test_features)):
    input_vec = [[test_features[k][i] for i in range(test_features.shape[1])]]
    # print(np.round(model.predict(np.array(input_vec))))
    if np.round(model.predict(np.array(input_vec))) != test_labels[k]:
        errors += 1

print("Accuracy: "+str(int((errors / len(test_features)) * 1000)/10)+'%')

# print(dictionary.show_elements())
# print(dictionary.show_indexes())
# print(splitted_msg)
# print(input_vectors)
# print(labels)
