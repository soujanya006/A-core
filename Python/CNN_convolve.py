import torch
import torch.nn as nn
import torch.nn.functional as F

# Hardcoded input image (6x6)
input_image = torch.tensor([[1, 2, 3, 4, 5, 6],
                            [7, 8, 9, 10, 11, 12],
                            [13, 14, 15, 16, 17, 18],
                            [19, 20, 21, 22, 23, 24],
                            [25, 26, 27, 28, 29, 30],
                            [31, 32, 33, 34, 35, 36]], dtype=torch.float32)
                            

# Reshape input image to (batch_size, channels, height, width)
input_image = input_image.unsqueeze(0).unsqueeze(0)  # Shape: [1, 1, 6, 6]

# Hardcoded filter (4x4)
filter = torch.tensor([[1, 0, -1, 0],
                       [1, 0, -1, 0],
                       [1, 0, -1, 0],
                       [1, 0, -1, 0]], dtype=torch.float32)

# Reshape filter to (out_channels, in_channels, height, width)
filter = filter.unsqueeze(0).unsqueeze(0)  # Shape: [1, 1, 4, 4]

# Define the convolution operation
convolution = nn.Conv2d(in_channels=1, out_channels=1, kernel_size=4, stride=1, padding=0, bias=False)

# Manually set the filter weights
convolution.weight.data = filter

# Apply convolution
output = convolution(input_image)

print(output)
