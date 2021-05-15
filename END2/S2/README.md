# Session 2 - BackProp, Embeddings and Language Models

[0. Backpropagation of Errors: Excel Spreadsheet Implementation](#excel)
[1. Parts List](#parts)
[2. Major Steps](#steps)

<a name="excel"/>

## 0. Assignment: Backpropagation of Errors in Excel Spreadsheet

(Please zoom in to read details)
![END2S2A-Backprop_Excel](https://user-images.githubusercontent.com/12987758/118140939-d1c3a300-b443-11eb-822f-1dc823f7ea63.PNG)

<a name="parts"/>

## 1. Parts List

### 1-0 Network Architecture

- Fully connected layers
- 2 neurons per layer
- 3 layers: input, hidden, output

### 1-1 Neuron

- i1, i2: input-layer neurons
- h1, h2: hidden-layer neurons (linear summation)
    - a_h1, a_h2 (out_h1, out_h2 in the screenshot image): non-linear activation (sigmoid function)
- o1, o2: output-layer neurons (linear summation)
    - a_o1, a_o2 (out_o1, out_o2 in the screenshot image): non-linear activation (sigmoid function)

### 1-2 Synaptic Weight

1. Layer 1 → 2
    - w1: i1 → h1
    - w2: i2 → h1
    - w3: i1 → h2
    - w4: i2 → h2

2. Layer 2 → 3
    - w5: a_h1 → o1
    - w6: a_h2 → o1
    - w7: a_h1 → o2
    - w8: a_h2 → o2

<a name="steps"/>

## 2. Major Steps 

The following steps repeat in a loop:

1. Forward Pass (error calculation)
    - h1 = w1 * i1 + w2 * i2
    - h2 = w3 * i1 + w4 * i2
    - a_h1 = σ(h1) = 1 / (1 + exp(-h1))
    - a_h2 = σ(h2) = 1 / (1 + exp(-h2))
    - o1 = w5 * a_h1 + w6 * a_h2
    - o2 = w7 * a_h1 + w8 * a_h2
    - a_o1 = σ(o1)
    - a_o2 = σ(o2)
    - E1 = 1/2 * (t1 - a_o1)²
    - E2 = 1/2 * (t2 - a_o2)²
    - E_Total = E1 + E2 (E_Total is abbreviated as E in the screenshot image)

2. Backward Pass (gradient calculation)

3. Parameter Optimization (weight update)
