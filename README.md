# **Implementing 2D Convolution**
## Aakash Pydi
___


### **PART A**
The following two input images were used to carry out the 2d convolutions described in task A.

A Cartoon Image (1280 x 720)
![cartoon_image](cartoon.jpg)

A Checkerboard Image (1920 x 1080)
![checker_image](checker.jpg)

The output for part A is given below. The normalized output for part A is included at the end of the file.
#### Task 1
The following two images were produced using kernel_1. The checker board result indicates that kernel 1 functions as a form of horizontal edge detector.
![cartoon_task1_k1](image_output/output_images/task_1/output_cartoon_k1_task_1.png)

![checker_task1_k1](image_output/output_images/task_1/output_checker_k1_task_1.png)

#### Task 2
The following two images were produced using kernel_4.The checker board result indicates that kernel 4 also functions as a form of horizontal edge detector. We also observe that the edge detection is more pronounced in this case.
![cartoon_task2_k4](image_output/output_images/task_2/output_cartoon_k4_task_2.png)

![checker_task2_k4](image_output/output_images/task_2/output_checker_k4_task_2.png)

The following two images were produced using kernel_5. The checker board result indicates that kernel 5 functions as a form of vertical edge detector.
![cartoon_task2_k5](image_output/output_images/task_2/output_cartoon_k5_task_2.png)

![checker_task2_k5](image_output/output_images/task_2/output_checker_k5_task_2.png)

#### Task 3
Note that all the output images are smaller than the input image due to stride value being greater than 1.

The following two images were produced using kernel_1.The checker board result indicates that kernel 1 functions as a form of horizontal edge detector.
![cartoon_task3_k1](image_output/output_images/task_3/output_cartoon_k1_task_3.png)

![checker_task3_k1](image_output/output_images/task_3/output_checker_k1_task_3.png)

The following two images were produced using kernel_2. The checker board result indicates that kernel 2 functions as a form of vertical edge detector.
![cartoon_task3_k2](image_output/output_images/task_3/output_cartoon_k2_task_3.png)

![checker_task3_k2](image_output/output_images/task_3/output_checker_k2_task_3.png)

The following two images were produced using kernel_3. This kernel is supposed to be a smoothing filter.
![cartoon_task3_k3](image_output/output_images/task_3/output_cartoon_k3_task_3.png)

![checker_task3_k3](image_output/output_images/task_3/output_checker_k3_task_3.png)

---

### **PART B**
Graphs showing the time taken for convolution as a function of the i Values (where 2^i = number of output channels), for each of the input images is given below.
![part_b_1](performance/task_b/Part_B_1.png)

![part_b_1](performance/task_b/Part_B_2.png)

---

### **PART C**
Graphs showing the number of operations in the convolutions as a function of the given kernel sizes, for each of the input images is given below.
![part_c_1](performance/task_c/Part_C_1.png)

![part_c_1](performance/task_c/Part_C_2.png)

---

### **Normalized Output for PART A**
#### Task 1
The following two images were produced using kernel_1.
![cartoon_task1_k1](image_output/normalized_output_images/task_1/output_cartoon_k1_task_1.png)

![checker_task1_k1](image_output/normalized_output_images/task_1/output_checker_k1_task_1.png)

#### Task 2
The following two images were produced using kernel_4.
![cartoon_task2_k4](image_output/normalized_output_images/task_2/output_cartoon_k4_task_2.png)

![checker_task2_k4](image_output/normalized_output_images/task_2/output_checker_k4_task_2.png)

The following two images were produced using kernel_5.
![cartoon_task2_k5](image_output/normalized_output_images/task_2/output_cartoon_k5_task_2.png)

![checker_task2_k5](image_output/normalized_output_images/task_2/output_checker_k5_task_2.png)

#### Task 3
The following two images were produced using kernel_1.
![cartoon_task3_k1](image_output/normalized_output_images/task_3/output_cartoon_k1_task_3.png)

![checker_task3_k1](image_output/normalized_output_images/task_3/output_checker_k1_task_3.png)

The following two images were produced using kernel_2.
![cartoon_task3_k2](image_output/normalized_output_images/task_3/output_cartoon_k2_task_3.png)

![checker_task3_k2](image_output/normalized_output_images/task_3/output_checker_k2_task_3.png)

The following two images were produced using kernel_3.
![cartoon_task3_k3](image_output/normalized_output_images/task_3/output_cartoon_k3_task_3.png)

![checker_task3_k3](image_output/normalized_output_images/task_3/output_checker_k3_task_3.png)
