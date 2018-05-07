import torch
import numpy as np
from conv import Conv2D
from PIL import Image
from skimage import color
from skimage import io
import torch



image = color.rgb2gray(io.imread('cartoon.jpg'))
t_image = torch.from_numpy(image)

conv = Conv2D(in_channel=3, o_channel=1, kernel_size=3, stride=1, mode='known')
(operation_count, filtered_image) = conv.forward(t_image)
print (filtered_image.size()== (720, 1280))

conv = Conv2D(in_channel=3, o_channel=1, kernel_size=3, stride=2, mode='rand')
(operation_count, filtered_image) = conv.forward(t_image)
print (filtered_image[0].size()== (360, 640))
