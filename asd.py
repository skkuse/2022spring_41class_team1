import torch
import sys

def judge_1_1(t1,t2):
    answer_t1 = torch.FloatTensor([[[1., 2., 3.],
                        [4., 5., 6.]],
                        [[7., 8., 9.],
                        [10., 11., 12.]]]
                      )
    answer_t2=torch.FloatTensor([[[[1]]]])
    
    t=torch.FloatTensor([0])
    if(type(t1)==type(answer_t1))&(type(t2)==type(answer_t2)):
        pass
    else:
        return False
    if(t1.shape==answer_t1.shape)&(t2.shape==answer_t2.shape):
        return True
    else:
        return False

if __name__=="__main__":
    code = sys.argv[1]
    exec(code,)
    t1,t2=practice1_1()
    #사용자가 봐야할 t1,t2의 결과
    print(t1.shape)
    print(t2.shape)
    print(judge_1_1(t1,t2))