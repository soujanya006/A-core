import torch
import torch.nn as nn
import torch.nn.functional as F

# Updated input image (6x6) based on your provided values
input_image = torch.tensor([
    [0.1, 0.2,  0.3,  0.4,  0.5,  0.6],
    [0.7,  0.8,  0.9,  0.9,  0.10, 0.10],
    [0.13, 0.14, 0.15, 0.14, 0.15, 0.15],
    [0.19, 0.2, 0.21, 0.19, 0.20, 0.20],
    [0.25, 0.26, 0.27, 0.24, 0.25, 0.25],
    [0.31, 0.32, 0.33, 0.24, 0.25, 0.25]
], dtype=torch.float32).unsqueeze(0).unsqueeze(0)  # Shape: [1, 1, 6, 6]

# New filter (3x3) based on your provided values
filter = torch.tensor([
    [1, 0, -1],
    [1, 0, -1],
    [1, 0, -1]
], dtype=torch.float32).unsqueeze(0).unsqueeze(0)  # Shape: [1, 1, 3, 3]

# Define the convolution operation with the new filter size
convolution = nn.Conv2d(in_channels=1, out_channels=1, kernel_size=3, stride=1, padding=0, bias=False)

# Manually set the filter weights to the convolution layer
convolution.weight.data = filter

# Apply convolution to the input image
output = convolution(input_image)

print(output)
