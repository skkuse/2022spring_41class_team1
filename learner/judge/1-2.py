import torch
import sys

#주석처리부분이 사용자가 구현해야 할 부분
def practice1_2():
    t1 = torch.FloatTensor([[1., 2., 3.],
                        [4., 5., 6.],
                        [7., 8., 9.],
                        [10., 11., 12.]]
                      )
    t2=torch.FloatTensor([[1]])
    t1 = t1.unsqueeze(1).unsqueeze(0)
    t2 = t2.squeeze(0).squeeze(0)
    return t1, t2

#judge is_answer => True or False
def judge_1_2(t1,t2):
    answer_t1=torch.FloatTensor([[[[ 1.,  2.,  3.]],
          [[ 4.,  5.,  6.]],
          [[ 7.,  8.,  9.]],
          [[10., 11., 12.]]]])
    answer_t2=torch.FloatTensor([1.]).squeeze(0)
    
    t=torch.FloatTensor([0])
    if(type(t1)==type(t)):
        pass
    else:
        return False
    if(t1.shape==answer_t1.shape)&(t2.shape==answer_t2.shape):
        return True
    else:
        return False

if __name__=="__main__":
    code = sys.argv[1]
    exec(code)
    t1,t2=practice1_2()
    #사용자가 봐야할 t1,t2의 결과
    print(t1)
    print(t2)
    
    if judge_1_2(t1,t2):    
        sys.exit(0)
    sys.exit(-1)