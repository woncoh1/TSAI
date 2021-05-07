# Session 1 - Background & Very Basics

1. What is a neural network neuron?  
A neuron in a neural network is a node representing a computation. This computation consists of two parts: linear summation and non-linear activation. A critical difference between neurons and synapse is that (after training) neuronal values are temporary, while synaptic weights are permanent. Neurons vary depending on input data, so neuronal values get refreshed as input data change. Synapses, represented by the weights with which they connect neurons in adjacent layers, are the very parameters that get trained and fitted to input data, so they do not change after training, no matter what kind of input data comes in.
2. What is the use of the learning rate?  
Learning rates are step sizes of each parameter update. Each weight update is a product of the gradient of the loss function with respect to the corresponding parameter, and the step size (range: 0 ~ 1) that dictates how much of the gradient gets added or subtracted from the old weight value. Appropriate learning rates are crucial for successful training in that too low learning rates are too slow to converge to the global minima or even let parameters get stuck in local minima, while too big learning rates prevent landing on the global-minima sweet spots and even make parameters diverge.
3. How are weights initialized?  
Weights are randomly initialized. That is, we assign values randomly sampled from a certain distribution as initial parameter values. When we initialize weights to a single, specific value (or tuples of values), we increase the distance each parameter needs to travel from the initial value to an optimal value, so training takes a lot of time to converge.
4. What is "loss" in a neural network?
5. What is the "chain rule" in gradient flow?
