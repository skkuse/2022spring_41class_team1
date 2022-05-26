import torch
import os
import os.path as p
import cv2
from torch.utils.data import TensorDataset

root_dir='C:/cd_classifier/Practice/Step3'
animal_data=[]
data_labels=[]
img_rows = 256
img_cols = 256
#주석처리부분이 사용자가 구현해야 할 부분
# # Get animal data
# print("Get data...")
# for animal in ('cats/', 'dogs/'):
#     animal_dir=p.join(root_dir,animal)
#     os.chdir(animal_dir)
#     files = os.listdir(animal_dir)

#     for file in files:
#         if '.jpg' in file: 
#             f = cv2.imread(file, 0)
#             f = torch.FloatTensor(cv2.resize(f, (img_rows, img_cols)))
        
#         animal_data.append(f)
#         if animal == "cats/":
#             data_labels.append(1)
#         else:
#             data_labels.append(0)
# animal_data=torch.stack(animal_data)
# animal_data=animal_data.unsqueeze(1)
# data_labels=torch.LongTensor(data_labels)
# dataset=TensorDataset(animal_data, data_labels)
# print(dataset[0])
# print(dataset[10])

# for j in data_labels:
#     print(j, end=' ')    