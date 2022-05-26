import torch
import os
import os.path as p
import cv2
from torch.utils.data import TensorDataset


animal_data=[]
data_labels=[]
img_rows = 256
img_cols = 256
def practice3_2(root_dir):
    animal_data=[]
    data_labels=[]
    #주석처리부분이 사용자가 구현해야 할 부분
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
    dataset=TensorDataset(animal_data, data_labels)
    
    return dataset

def judge_3_2(root_dir,dataset):
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
    answer_data=torch.stack(answer_data)
    answer_data=answer_data.unsqueeze(1)
    answer_labels=torch.LongTensor(answer_labels)
    answerset=TensorDataset(answer_data, answer_labels)

    for i in range(len(answer_data)):
        if(torch.equal(answerset[i][0],dataset[i][0])):
            pass
        else:
            return False
        if(torch.equal(answerset[i][1],dataset[i][1])):
            pass
        else:
            return False
    return True

if __name__ == "__main__":
    root_dir='C:/cd_classifier/Practice/Step3'
    dataset=practice3_2(root_dir)
    for i in dataset:
        print(i)
    
    a=judge_3_2(root_dir,dataset)
    print(a)

