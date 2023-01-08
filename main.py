import torch

print('')
print('A tensor from a list')
tensor1 = torch.tensor([1, 2, 3])
print(tensor1)

print('')
print('A tensor with a specific data type')
tensor2 = torch.tensor([1, 2, 3], dtype=torch.float32)
print(tensor2)

print('')
print('A tensor of ones')
tensor3 = torch.ones(2, 3)
print(tensor3)

print('')
print('A tensor of zeros')
tensor4 = torch.zeros(3, 2)
print(tensor4)

print('')
print('A tensor with random values')
tensor5 = torch.rand(2, 3)
print(tensor5)

print('')
print('A tensor with a specific shape and filled with a specific value')
tensor6 = torch.full((2, 3), fill_value=5)
print(tensor6)

print('')
print('A tensor with the same shape and data type as another tensor')
tensor7 = torch.empty_like(tensor5)
print(tensor7)

print('')
print('Shape of a tensor')
print(tensor5.shape)

print('')
print('Data type of a tensor')
print(tensor5.dtype)

print('')
print('Size of a tensor (number of elements)')
print(tensor5.size())

print('')
print('Number of dimensions of a tensor')
print(tensor5.dim())

print('')
print('Reshape a tensor')
tensor8 = tensor5.view(3, 2)
print(tensor8)