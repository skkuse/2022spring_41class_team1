import torch
import os
import os.path as p
import cv2
animal_data=[]
img_rows = 256
img_cols = 256

#주석처리부분이 사용자가 구현해야 할 부분
def example3_1(root_dir):
    # for animal in ('cats/', 'dogs/'):
    #     animal_dir=p.join(root_dir,animal)
    # os.chdir(animal_dir)
    # files = os.listdir(animal_dir)

    # for file in files:
    #     if '.jpg' in file: 
    #         f = cv2.imread(file, 0)
    #         f = torch.FloatTensor(cv2.resize(f, (img_rows, img_cols)))
    #     animal_data.append(f)
    
    return animal_data

def judge_3_1(root_dir,animal_data):
    answer_data=[]
    for animal in ('cats/', 'dogs/'):
        animal_dir=p.join(root_dir,animal)
    os.chdir(animal_dir)
    files = os.listdir(animal_dir)

    for file in files:
        if '.jpg' in file: 
            f = cv2.imread(file, 0)
            f = torch.FloatTensor(cv2.resize(f, (img_rows, img_cols)))
        answer_data.append(f)
    for i in range(len(answer_data)):
        if(torch.equal(answer_data[i],animal_data[i])):
            pass
        else:
            return False
    return True


if __name__ == "__main__":
    root_dir='C:/cd_classifier/Practice/Step3'
    animal_data = example3_1(root_dir)
    for i in animal_data:
        print(i)
        print(i.size())
    
    a=judge_3_1(root_dir,animal_data)
    print(a)


