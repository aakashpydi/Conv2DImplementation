import torch
from skimage import color
from skimage import io
from conv import Conv2D
from PIL import Image
import numpy as np
import math
import time
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def normalize(filtered_image):
    return (filtered_image[:,:] - filtered_image[:,:].min())/ filtered_image.ptp() # value - min/max-min

## Read Image as a NUMPY array
input_image_1 = color.rgb2gray(io.imread('cartoon.jpg'))
input_image_2 = color.rgb2gray(io.imread('checker.jpg'))

##convert to TORCH TENSOR.
t_input_image_1 = torch.from_numpy(input_image_1)
t_input_image_2 = torch.from_numpy(input_image_2)

############################# PART A ##############################
# ## TASK #1
conv = Conv2D(in_channel=3, o_channel=1, kernel_size=3, stride=1, mode='known')
(operation_count, filtered_image) = conv.forward(t_input_image_1)
print "Operation Count: " + str(operation_count)
f_image = Image.fromarray(filtered_image.numpy() * 255).convert('RGB')
# f_image.save('output_cartoon_k1_task_1.png')
f_image.show()

(operation_count, filtered_image) = conv.forward(t_input_image_2)
print "Operation Count: " + str(operation_count)
f_image = Image.fromarray(filtered_image.numpy() * 255).convert('RGB')
# f_image.save('output_checker_k1_task_1.png')
f_image.show()

#TASK #2
conv = Conv2D(in_channel=3, o_channel=2, kernel_size=5, stride=1, mode='known')
(operation_count, filtered_images) = conv.forward(t_input_image_2)
f_image_1 = Image.fromarray(filtered_images[0].numpy() * 255).convert('RGB')
f_image_2 = Image.fromarray(filtered_images[1].numpy() * 255).convert('RGB')
f_image_1.show()
# f_image_1.save('output_checker_k4_task_2.png')
f_image_2.show()
# f_image_2.save('output_checker_k5_task_2.png')

##TASK#3
conv = Conv2D(in_channel=3, o_channel=3, kernel_size=3, stride=2, mode='known')
(operation_count, filtered_images) = conv.forward(t_input_image_1)
f_image_1 = Image.fromarray(filtered_images[0].numpy() * 255).convert('RGB')
f_image_2 = Image.fromarray(filtered_images[1].numpy() * 255).convert('RGB')
f_image_3 = Image.fromarray(filtered_images[2].numpy() * 255).convert('RGB')
f_image_1.show()
# f_image_1.save('output_checker_k1_task_3.png')
f_image_2.show()
# f_image_2.save('output_checker_k2_task_3.png')
f_image_3.show()
# f_image_3.save('output_checker_k3_task_3.png')

############################# PART B #########################
# i_values = [0, 1, 2, 3, 4, 5, 6, 7, 8] #USING EXTRAPOLATION FOR i=9,10
# time_taken = []
# for i in i_values:
#     o_channel_val = int(math.pow(2, i))
#     conv2d = Conv2D(in_channel=3, o_channel=o_channel_val, kernel_size=3, stride=1, mode='rand')
#     start_time = time.time()
#     (operation_count, filtered_image) = conv2d.forward(t_input_image_2)
#     time_taken.append(time.time()-start_time)
#     print time_taken
# extrapolation = np.polyfit(i_values, time_taken, 3)
# extrapolater = np.poly1d(extrapolation)
#
# time_9 = extrapolater(9)
# i_values.append(9)
# time_taken.append(time_9)
#
# time_10 = extrapolater(10)
# i_values.append(10)
# time_taken.append(time_10)
#
#
# plt.plot(i_values, time_taken, 'ro')
# plt.ylabel('Time Taken for forward()')
# plt.xlabel('i Value')
# plt.title('HW1 Part B: Time Taken for Convolution vs i Value (where 2^i = no. of out channels)')
# plt.grid(True)
# plt.show()

############################# PART C #########################
# kernel_sizes = [3, 5, 7, 9, 11]
# operation_counts = []
#
# for k in kernel_sizes:
#     conv2d = Conv2D(in_channel=3, o_channel=2, kernel_size=k, stride=1, mode='rand')
#     (operation_count, filtered_image) = conv2d.forward(t_input_image_2)
#     operation_counts.append(operation_count)
#     print operation_counts
#
# plt.plot(kernel_sizes, operation_counts, 'ro')
# plt.ylabel('Number of Operations in Convolution')
# plt.xlabel('Kernel Size')
# plt.title('HW1 Part C: Number of Operations in Convolution vs Kernel Size')
# plt.grid(True)
# plt.show()
##########################################################
