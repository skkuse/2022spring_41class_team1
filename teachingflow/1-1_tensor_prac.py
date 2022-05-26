
import torch

t1 = torch.FloatTensor([[[1., 2., 3.],
                       [4., 5., 6.]],
                       [[7., 8., 9.],
                       [10., 11., 12.]]]
                      )
t2=torch.FloatTensor([[[[1]]]])

print(t1.shape)
print(t2.shape)

