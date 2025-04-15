### How does a Neural Net work?

#### Components

##### Layers
- Composed of layers of neurons. The input vector into each layer = 1 x number of neurons in previous vector. Output is 1 x number of neurons in this vector.
- the input layer is where the data is inputted. The number of neurons is equal to the dimensions of the input vector.
- All of the internal layers are called hidden layers. This is where the calculations occur.
- The final layer is called the output layer. The number of neurons in this layer is equal to the number of output classes (or 1 if is continuous instead of discrete).
- An operation called softmax which normalizes the probabilities associated with each neuron is applied and the most likely option is selected.

##### Neurons
- Each neuron keeps a weight for each input dimension of the outputted vector from the previous layer and a bias which is a constant.
- It will calculate the weight vector x output from previous layer.
- Then it will perform an activation function to learn non-linear patterns (otherwise this would just be an incredibly complex linear equation).
    - ReLU: return x > 0 ? x : 0 (Fast and popular)
    - Sigmoid: return 1 / (1 + e^-x)
    -  Tanh

#### Training Set up

- For Neural Nets, your training data should look like input vector : correct output.
- You will have a training set, a validation set (used for mid training eval), and a final test set in order to evaluate the true usefulness. The idea is that the model should never have seen the test data.

#### Phases

##### Forward Propogation
- At this phase, the input vector is passed through the neural network, each layer calculates its output and passes it along to the next layer until the final layer is hit and the net spits out its output.

##### Loss Calculation
- NOTE: Training is done in batches so that general patterns can be seen. In a second, you will see why it is too volatile to train on individual inputs.
    - For continuous prediction, typically Mean Squared Error (Sum of (correct - predicted)^2) / batch size.
    - For discrete prediction, typically Cross Entropy Loss:
        - Individual output: Loss = -1 * Sum( actual * log(predicted probability)) for each possible class.
        - For the whole Batch: Loss =  (1 / batch size) * Sum( Loss Above ) for each input vector in the batch

#### Backpropagation
- Will go deep into this over the next week or two.
- In simple terms, calculate how much each node and each individual weight contributed to error with respect to the loss using chain rule.
- Store these in the nodes themselves. This is the most complicated part and is called gradient descent.

#### Optimization
- Update the weights according to how much they contributed to the loss in the opposite direction (towards stability and convergence) in order to minimize future loss.
- There are advanced optimizers which we will cover later on.
- Only update in small increments. 
    - Too small of an increment and we can get stuck in a local minima of error rather than the global minimum and training takes longer.
    - Too large of an increment and the model can completely diverge.

#### General things to know

- Overfitting: The goal of a model is to predict on unseen data. We want it to learn patterns, not memorize the data itself. This will be seen where the prediction accuracy on the train data is extremely high and the accuracy on the test data is low. This is bad. Want to avoid.
- Batch sizes should be just large enough to be stable, anything more is a waste of training data.
- An epoch is 1 full iteration through the training dataset.
