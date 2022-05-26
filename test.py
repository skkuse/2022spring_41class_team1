import subprocess


p = subprocess.Popen(['python3', 'asd.py','''def practice1_1():
    t1 = torch.FloatTensor([[[1., 2., 3.],
                       [4., 5., 6.]],
                       [[7., 8., 9.],
                       [10., 11., 12.]]]
                      )
    t2=torch.FloatTensor([[[[1]]]])
    return t1, t2'''], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = p.communicate()
print('out', out)
print('err', err)
print('returncode', p.returncode)
print('EXIT')