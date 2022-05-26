import torch
import os
import os.path as p
import cv2
from torch.utils.data import TensorDataset

img_rows = 256
img_cols = 256

def example3_2(root_dir):
    animal_data=[]
    data_labels=[]
    for animal in ('cats/', 'dogs/'):
        animal_dir=p.join(root_dir,animal)
        os.chdir(animal_dir)
        files = os.listdir(animal_dir)
    #주석처리부분이 사용자가 구현해야 할 부분
        # for file in files:
        #     if '.jpg' in file: 
        #         f = cv2.imread(file, 0)
        #         f = torch.FloatTensor(cv2.resize(f, (img_rows, img_cols)))
        #     animal_data.append(f)

        #     if animal == "cats/":
        #         data_labels.append(1)
        #     else:
        #         data_labels.append(0)
    
    return animal_data, data_labels

def judge_3_2(root_dir,animal_data,data_labels):
    answer_data=[]
    answer_labels=[]
    for animal in ('cats/', 'dogs/'):
        animal_dir=p.join(root_dir,animal)
        os.chdir(animal_dir)
        files = os.listdir(animal_dir)

        for file in files:
            if '.jpg' in file: 
                f = cv2.imread(file, 0)
                f = torch.FloatTensor(cv2.resize(f, (img_rows, img_cols)))
            answer_data.append(f)
            if animal == "cats/":
                answer_labels.append(1)
            else:
                answer_labels.append(0)

    for i in range(len(answer_data)):
        if(torch.equal(answer_data[i],animal_data[i])):
            pass
        else:
            return False
        if(answer_labels[i]==data_labels[i]):
            pass
        else:
            return False
    return True

if __name__ == "__main__":
    root_dir='C:/cd_classifier/Practice/Step3'
    animal_data,data_labels = example3_2(root_dir)
    for i in animal_data:
        print(i)
        print(i.size())
    for j in data_labels:
        print(j)
    
    a=judge_3_2(root_dir,animal_data,data_labels)
    print(a)



