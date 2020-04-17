import os
import random
from shutil import copyfile


# Given SOURCE which is directory of our data, we copy the data randomly to the train set and test set directory
def split_data(SOURCE, TRAINING, TESTING, SPLIT_SIZE=0.8):
    dataset = []

    for unitData in os.listdir(SOURCE):
        data = SOURCE + unitData
        if os.path.getsize(data) > 0:
            dataset.append(unitData)
        else:
            print('Skipped ' + unitData)
            print('Invalid file size! i.e Zero length.')

    train_data_length = int(len(dataset) * SPLIT_SIZE)
    test_data_length = int(len(dataset) - train_data_length)

    shuffled_set = random.sample(dataset, len(dataset))
    train_set = shuffled_set[0:train_data_length]
    test_set = shuffled_set[-test_data_length:]

    for unitData in train_set:
        copyfile(SOURCE + unitData, TRAINING + unitData)

    for unitData in test_set:
        copyfile(SOURCE + unitData, TESTING + unitData)

# Returns path of the folder of source data
def init_source(bitNo, type=''):
    if bitNo != 64 or bitNo != 128 or bitNo != 256:
        print('Error! \nBit no must be 64,128 or 256')
    if type != 'bw' or type != 'gray' or type != '':
        print('Error! \nType must be blank( for rgb) bw (for bitwise) or gray!')
    return './Dataset/Hey-Waldo/' + bitNo + '-' + type


# Returns path of the folders of training data and test data
def init_folder(folderName, className1, className2):
    try:
        os.mkdir('/tmp/'+ folderName + '/')
        os.mkdir('/tmp/' + folderName + '/training')
        os.mkdir('/tmp/' + folderName + '/testing')
        os.mkdir('/tmp/' + folderName + '/training/' + className1)
        os.mkdir('/tmp/' + folderName + '/testing/' + className1)
        os.mkdir('/tmp/' + folderName + '/training' + className2)
        os.mkdir('/tmp/' + folderName + '/testing' + className2)
    except OSError:
        pass

    return '/tmp/' + folderName + '/training', '/tmp/' + folderName + '/testing'