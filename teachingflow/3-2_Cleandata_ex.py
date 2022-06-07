import torch
import cv2
animal_data=[]
data_labels=[]
img_rows = 256
img_cols = 256
root_dir='C:/cd_classifier/Practice/Step3'
#data loading => files에 있다고 가정
for file in files:
    if '.jpg' in file: 
        f = cv2.imread(file, 0)
        f = torch.FloatTensor(cv2.resize(f, (img_rows, img_cols)))
    animal_data.append(f)
    if animal == "cats/":
        data_labels.append(1)
    else:
        data_labels.append(0)
print(animal_data[0])
for i in animal_data:
    print(i.shape)
for j in data_labels:
    print(j, end=' ')
