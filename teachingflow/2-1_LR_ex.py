import torch
x_train = torch.FloatTensor([[1], [2], [3]])
y_train = torch.FloatTensor([[2], [4], [6]])
# 가중치 W를 0으로 초기화하고 학습을 통해 값이 변경되는 변수임을 명시합니다
W=torch.zeros(1, requires_grad=True)
# 편향 b를 0으로 초기화하고 학습을 통해 값이 변경되는 변수임을 명시합니다
b=torch.zeros(1, requires_grad=True)

# H(x)
hypothesis = x_train * W + b
# cost
cost = torch.mean((hypothesis - y_train) ** 2 )


print(W, b)
print(hypothesis)
print(cost)
