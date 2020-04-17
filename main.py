from manageData import split_data
from manageData import init_source
from manageData import init_folder
from model import model
from plot import plot

SPLIT_SIZE = 0.9 # Split the data as %90 training set, %10 test set


train_path, test_path = init_folder('FindWaldo', 'Waldo', 'NotWaldo')
source_path = init_source(64)

split_data(source_path, train_path, test_path, SPLIT_SIZE)

# Training ve testing ayrımı yapılacak ama waldo nonwaldo sınıflandırılması için iki kere mi split data kullanılacak çözülemedi!