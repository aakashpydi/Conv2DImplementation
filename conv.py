import numpy as np
import torch

class Conv2D:
    # k1 = np.array([[-1,-1,-1], [0,0,0], [1,1,1]])
    # k2 = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    # k3 = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    # k4 = np.array([[-1, -1, -1, -1,-1], [-1, -1, -1, -1, -1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
    # k5 = np.array([[-1, -1, 0, 1,1], [-1, -1, 0, 1, 1], [-1, -1, 0, 1, 1], [-1, -1, 0, 1, 1], [-1, -1, 0, -1, -1]])

    def __init__(self, in_channel, o_channel, kernel_size, stride, mode):
        self.in_channel = in_channel
        self.o_channel = o_channel
        self.kernel_size = kernel_size
        self.stride = stride
        self.mode = mode
        self.k1 = np.array([[-1,-1,-1], [0,0,0], [1,1,1]])
        self.k2 = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
        self.k3 = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        self.k4 = np.array([[-1, -1, -1, -1,-1], [-1, -1, -1, -1, -1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
        self.k5 = np.array([[-1, -1, 0, 1,1], [-1, -1, 0, 1, 1], [-1, -1, 0, 1, 1], [-1, -1, 0, 1, 1], [-1, -1, 0, -1, -1]])

    def forward(self, input_image):

        input_image = input_image.numpy()
        image_width, image_height = input_image.shape[0], input_image.shape[1]
        #image_padded = input_image
        image_padded = np.zeros((input_image.shape[0]+2, input_image.shape[1]+2))
        image_padded[1:-1, 1:-1] = input_image

        #TASK 1 where we need to use KNOWN K_1, and have ONE output stream
        if self.o_channel == 1 and self.mode == 'known':
            output = np.zeros([image_width, image_height])
            operation_count = 0
            for x in range(1, image_height-1):
                for y in range(1, image_width-1):
                    if y >= 0 and y < image_width and x >= 0 and x < image_height:
                        output[y, x] = (self.k1 * image_padded[y-1:y+2, x-1:x+2]).sum()
                        operation_count += 2 * (self.k1.shape[0] * self.k1.shape[1]) #number of additions and #multiplications equals hte number of elements here
                    y += (self.stride - 1)
                x += (self.stride - 1)
            output = torch.from_numpy(output)
            return (operation_count, output)
        #TASK 2 where we need to use KNOWN K_4, K_5, and have TWO output stream
        elif self.o_channel == 2 and self.mode == 'known':
            output = np.zeros([self.o_channel, image_width, image_height])
            kernels_to_use = (self.k4, self.k5)

            operation_count = 0
            for k in range(self.o_channel):
                for x in range(2, image_height-2):
                    for y in range(2, image_width-2):
                        if y >= 0 and y < image_width and x >= 0 and x < image_height:
                            output[k, y, x] = (kernels_to_use[k] * image_padded[y-2:y+3, x-2:x+3]).sum()
                            operation_count += 2 * (kernels_to_use[k].shape[0] * kernels_to_use[k].shape[1]) #number of additions and #multiplications equals hte number of elements here
                        y += (self.stride - 1)
                    x += (self.stride - 1)
            output = torch.from_numpy(output)
            return (operation_count, output)
            #TASK 3 where we need to use KNOWN K_1, K_2, K_3, and have THREE output stream
        elif self.o_channel == 3 and self.mode == 'known':
            output = np.zeros([self.o_channel, int(image_width/self.stride), int(image_height/self.stride)])
            kernels_to_use = (self.k1, self.k2, self.k3)

            operation_count = 0
            for k in range(self.o_channel):
                for x in range(1, image_height-1):
                    for y in range(1, image_width-1):
                        if y >= 0 and y < image_width and x >= 0 and x < image_height:
                            # print "y: " + str(y) + ", \t" + "x: " + str(x)
                            temp = (kernels_to_use[k] * image_padded[y-1:y+2, x-1:x+2]).sum()
                            output[k, int(y/self.stride), int(x/self.stride)] = temp
                            operation_count += 2 * (kernels_to_use[k].shape[0] * kernels_to_use[k].shape[1]) #number of additions and #multiplications equals hte number of elements here
                        y += (self.stride - 1)
                    x += (self.stride-1)
            output = torch.from_numpy(output)
            return (operation_count, output)
            #PARTS B AND C. WE NEED TO INITALIZE A RANDOM KERNEL.
        else:
            output = np.zeros([self.o_channel, int(image_width/self.stride), int(image_height/self.stride)])

            k_to_use = np.random.random((self.kernel_size, self.kernel_size))
            k_offset_left = int(self.kernel_size/2)
            k_offset_right = int(self.kernel_size/2) + 1

            operation_count = 0
            for k in range(self.o_channel):
                for x in range(k_offset_left, image_height-k_offset_left):
                    for y in range(k_offset_left, image_width-k_offset_left):
                        if y >= 0 and y < image_width and x >= 0 and x < image_height:
                            # print "y: " + str(y) + ", \t" + "x: " + str(x)
                            output[k, int(y/self.stride), int(x/self.stride)] = (k_to_use * image_padded[y-k_offset_left:y+k_offset_right, x-k_offset_left:x+k_offset_right]).sum()
                            operation_count += 2 * (k_to_use.shape[0] * k_to_use.shape[1]) #number of additions and #multiplications equals hte number of elements here
                        y += (self.stride - 1)
                    x += (self.stride-1)
            output = torch.from_numpy(output)
            return (operation_count, output)
