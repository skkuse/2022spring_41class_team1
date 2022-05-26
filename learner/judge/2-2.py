import torch
import sys

#주석처리부분이 사용자가 구현해야 할 부분

def practice_2_2(x_train,y_train):

    # # 모델 초기화
    # W = torch.zeros(1, requires_grad=True)
    # b = torch.zeros(1, requires_grad=True)
    # # optimizer 설정
    # optimizer = torch.optim.SGD([W, b], lr=0.0001)

    # nb_epochs = 100 # 원하는만큼 경사 하강법을 반복
    # for epoch in range(nb_epochs + 1):
    #     # H(x) 계산
    #     hypothesis = x_train * W + b
    #     # cost 계산
    #     cost = torch.mean((hypothesis - y_train) ** 2)
    #     # cost로 H(x) 개선
    #     optimizer.zero_grad()
    #     cost.backward()
    #     optimizer.step()
    #     # 100번마다 로그 출력
    #     if epoch % 10 == 0:
    #         print('Epoch {:4d}/{} W: {:.3f}, b: {:.3f} Cost: {:.6f}'.format(
    #             epoch, nb_epochs, W.item(), b.item(), cost.item()))

    return hypothesis, cost, W, b

def judge2_2(cost,W,b):
    if(cost.item()<30):
        pass
    else:
        return False
    if(0<b<0.1)&(2.9<W<3.1):
        return True
    else:
        return False

if __name__=="__main__":

    code = sys.argv[1]
    exec(code)
    
    x_train = torch.FloatTensor([[25], [50], [42],[61],[80]])
    y_train = torch.FloatTensor([[81], [159], [130],[180],[244]])

    hypothesis, cost, W, b = practice_2_2(x_train,y_train)
    
    print(hypothesis)
    print(cost)
    print(W)
    print(b)
    
    if judge2_2(cost,W,b):    
        sys.exit(0)
    sys.exit(-1)