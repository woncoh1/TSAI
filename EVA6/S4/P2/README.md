# Session 4 - Backpropagation and Architectural Basics

Table of Contents:  
[1. Instruction](#instruction)  
[2. Problem](#problem)  
[3. Solution](#solution)  
[4. Result](#result)  


<a name="instruction"/>

## Instruction

1. We have considered many many points in our last 4 lectures. Some of these we have covered directly and some indirectly. They are:
  1. How many layers,
  2. MaxPooling,
  3. 1x1 Convolutions,
  4. 3x3 Convolutions,
  5. Receptive Field,
  6. SoftMax,
  7. Learning Rate,
  8. Kernels and how do we decide the number of kernels?
  9. Batch Normalization,
  10. Image Normalization,
  11. Position of MaxPooling,
  12. Concept of Transition Layers,
  13. Position of Transition Layer,
  14. DropOut
  15. When do we introduce DropOut, or when do we know we have some overfitting
  16. The distance of MaxPooling from Prediction,
  17. The distance of Batch Normalization from Prediction,
  18. When do we stop convolutions and go ahead with a larger kernel or some other alternative (GAP, which we have not yet covered)
  19. How do we know our network is not going well, comparatively, very early
  20. Batch Size, and effects of batch size
  21. Etc (you can add more if we missed it here)

2. Refer to this code: [COLABLINK](https://colab.research.google.com/drive/1uJZvJdi5VprOQHROtJIHy0mnY2afjNlx). WRITE IT AGAIN SUCH THAT IT ACHIEVES:
    1. You can use anything from above you want. 
    2. **99.4% validation (test) accuracy**
    3. **Less than 20k parameters**
    4. **Less than 20 epochs**
    5. Have used BN, Dropout, a Fully connected layer, **have used GAP**. 
    6. To learn how to add different things we covered in this session, you can refer to this code: https://www.kaggle.com/enwei26/mnist-digits-pytorch-cnn-99 DONT COPY ARCHITECTURE, JUST LEARN HOW TO INTEGRATE THINGS LIKE DROPOUT, BATCHNORM, ETC.

<a name="problem"/>

## Problem

- Type
    - Classification
- Task
    - Handwritten digit recognition

<a name="solution"/>

## Solution

- Data
    - MNIST dataset
- Model Architecture
    - Convolution neural network
- Loss Function
    - Cross entropy (`F.log_softmax()` + `nn.NLLLoss()`)
- Optimizer
    - Stochastic gradient descent with momentum

<a name="result"/>

## Result

- Test Accuracy
    - 99.40 % (maximum test accuracy: 99.47 %)
- Num. of Parameters
    - 19,240
- Num. of Epochs
    - 19 (maximum test accuracy starting from epoch 16)

## Reference

1. [2-1 Define Model] [Benchmark architecture](https://medium.com/@ravivaishnav20/handwritten-digit-recognition-using-pytorch-get-99-5-accuracy-in-20-k-parameters-bcb0a2bdfa09)

2. [2-1 Define Model] [`view` vs `reshape` vs `clone`](https://stackoverflow.com/questions/49643225/whats-the-difference-between-reshape-and-view-in-pytorch)

3. [2-3 Instantiate Loss] [`NLLLoss` vs `CrossEntropyLoss`](https://github.com/rasbt/stat479-deep-learning-ss19/blob/master/other/pytorch-lossfunc-cheatsheet.md)
