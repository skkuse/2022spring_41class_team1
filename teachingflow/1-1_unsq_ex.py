import torch
t = torch.FloatTensor([[1., 2., 3.],
                       [4., 5., 6.],
                       [7., 8., 9.],
                       [10., 11., 12.]]
                      )
t = t.unsqueeze(0)
print(t)
print(t.shape)
t=t.squeeze()
print(t.shape)
