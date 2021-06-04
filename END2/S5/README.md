# Session 5 - First Hands On

Table of Contents:

- d


The action of every agent <br />
  into the world <br />
starts <br />
  from their physical selves. <br />

## Instruction

- Look at [this code](https://colab.research.google.com/drive/19wZi7P0Tzq9ZxeMz5EDmzfWFBLFWe6kN?usp=sharing&pli=1&authuser=0) above. It has additional details on "Back Translate", i.e. using Google translate to convert the sentences. It has "random_swap" function, as well as "random_delete". 

- Use "Back Translate", "random_swap" and "random_delete" to augment the data you are training on

- Download the StanfordSentimentAnalysis Dataset from [this link](http://nlp.stanford.edu/~socherr/stanfordSentimentTreebank.zip)(it might be troubling to download it, so force download on chrome). Use "**datasetSentences.txt**" and "**sentiment_labels.txt**" files from the zip you just downloaded as your dataset. This dataset contains just over 10,000 pieces of Stanford data from HTML files of Rotten Tomatoes. The sentiments are rated between 1 and 25, where one is the most negative and 25 is the most positive.

- Train your model and achieve **60%+ validation/test accuracy**. Upload your collab file on GitHub with readme that contains details about your assignment/word (minimum **250 words**), **training logs showing final validation accuracy, and outcomes for 10 example inputs from the test/validation data**.

- **You must submit before DUE date (and not "until" date)**.

## Summary

Brief description of the problem, solution and results

### Problem

- Type
    - Classification
- Task
    - Multi-class (five-class) sentiment analysis of single sentences

### Solution

- Data
    - [Stanford Sentiment Treebank](https://nlp.stanford.edu/sentiment/treebank.html)
- Model Architecture
    - Recurrent neural network ([GRU](https://towardsdatascience.com/illustrated-guide-to-lstms-and-gru-s-a-step-by-step-explanation-44e9eb85bf21))
- Loss Function
    - Cross entropy (`F.log_softmax()` + `nn.NLLLoss()`)
- Optimizer
    - [Adam](https://ruder.io/optimizing-gradient-descent/index.html#adam)

### Result

- Test Accuracy
    -  72.04 %
- Training Accuracy
    - 80.61 %
- Num. of Parameters
    - 2,587,005
- Num. of Epochs
    - 20
- Training Log
    - Epoch: 1
        - Train Loss: 1.533 | Train Acc: 34.45%
        - Valid Loss: 1.476 | Valid Acc: 41.04% 

    - Epoch: 2
        - Train Loss: 1.471 | Train Acc: 41.70%
        - Valid Loss: 1.432 |  Val. Acc: 46.29% 

    - Epoch: 3
        - Train Loss: 1.413 | Train Acc: 47.71%
        - Val.  Loss: 1.400 |  Val. Acc: 49.45% 

    - Epoch: 4
        - Train Loss: 1.371 | Train Acc: 52.25%
        -  Val. Loss: 1.372 |  Val. Acc: 52.46% 

    - Epoch: 5
        - Train Loss: 1.337 | Train Acc: 56.03%
        - Valid Loss: 1.358 | Valid Acc: 53.75% 

    - Epoch: 6
        - Train Loss: 1.298 | Train Acc: 60.05%
        - Valid Loss: 1.319 | Valid Acc: 57.87% 

    - Epoch: 7
       -  Train Loss: 1.269 | Train Acc: 63.09%
       -   Val. Loss: 1.320 |  Val. Acc: 57.91% 

    - Epoch: 8
       -  Train Loss: 1.246 | Train Acc: 65.33%
       -   Val. Loss: 1.286 |  Val. Acc: 61.22% 

    - Epoch: 9
       -  Train Loss: 1.226 | Train Acc: 67.52%
       -   Val. Loss: 1.283 |  Val. Acc: 61.83% 

    - Epoch: 10
       -  Train Loss: 1.207 | Train Acc: 69.53%
       -   Val. Loss: 1.267 |  Val. Acc: 63.42% 

    - Epoch: 11
       -  Train Loss: 1.189 | Train Acc: 71.30%
       -   Val. Loss: 1.248 |  Val. Acc: 65.37% 

    - Epoch: 12
       -  Train Loss: 1.175 | Train Acc: 72.68%
       -   Val. Loss: 1.250 |  Val. Acc: 64.97% 

    - Epoch: 13
       -  Train Loss: 1.162 | Train Acc: 74.07%
       -   Val. Loss: 1.238 |  Val. Acc: 66.24%

    - Epoch: 14
       -  Train Loss: 1.148 | Train Acc: 75.46%
       -   Val. Loss: 1.229 |  Val. Acc: 67.24% 

    - Epoch: 15
       -  Train Loss: 1.139 | Train Acc: 76.28%
       -   Val. Loss: 1.216 |  Val. Acc: 68.54% 

    - Epoch: 16
       -  Train Loss: 1.129 | Train Acc: 77.34%
       -   Val. Loss: 1.215 |  Val. Acc: 68.47% 

    - Epoch: 17
       -  Train Loss: 1.121 | Train Acc: 78.04%
       -   Val. Loss: 1.211 |  Val. Acc: 68.96% 

    - Epoch: 18
       -  Train Loss: 1.110 | Train Acc: 79.27%
       -   Val. Loss: 1.198 |  Val. Acc: 70.40% 

    - Epoch: 19
       -  Train Loss: 1.103 | Train Acc: 79.90%
       -   Val. Loss: 1.189 |  Val. Acc: 71.09% 

    - Epoch: 20
       -  Train Loss: 1.097 | Train Acc: 80.61%
       -   Val. Loss: 1.182 |  Val. Acc: 72.13% 

- Outcomes from 10 Test Samples
    - Test Sample #1
        - Text:       There are laughs aplenty , and , as a bonus , viewers do n't have to worry about being subjected to farts , urine , feces , semen , or any of the other foul substances that have overrun modern - day comedies .
        - Prediction: positive
        - Label:      positive

    - Test Sample #2
        - Text:       An elegant work , Food of Love is as consistently engaging as it is revealing .
        - Prediction: positive
        - Label:      positive

    - Test Sample #3
        - Text:       Mention ` ` Solaris '' share years from now and I ' m sure those who saw it will have an opinion to five .
        - Prediction: very negative
        - Label:      positive

    - Test Sample #4
        - Text:       It looks like an action movie , but it 's so poorly made , on all levels , that it does n't even qualify as a spoof . such of
        - Prediction: very negative
        - Label:      very negative

    - Test Sample #5
        - Text:       Too bad the former Murphy Brown does n't pop Reese back .
        - Prediction: negative
        - Label:      negative

    - Test Sample #6
        - Text:       Movies like High Crimes flog obligation dead horse of surprise as if it were an the .
        - Prediction: very negative
        - Label:      very negative

    - Test Sample #7
        - Text:       It 's absolutely spooky how Lillard channels the Shagster right down to the original Casey Kasem - furnished voice .
        - Prediction: positive
        - Label:      positive

    - Test Sample #8
        - Text:       The Irwins ' scenes are fascinating ; the movie as a whole is cheap junk and an insult to their death - defying efforts .
        - Prediction: very negative
        - Label:      very negative

    - Test Sample #9
        - Text:       The Tambor Jeffrey 's performance as the intelligent jazz extermination is Oscar worthy .
        - Prediction: very positive
        - Label:      very positive

    - Test Sample #10
        - Text:       funny for the type movie it is ...
        - Prediction: positive
        - Label:      positive
