# Sentiment Classifier

**Author**: Joseph Hangarter
**Version**: 1.0.0

## Overview
## 12-30-2019
* Identify a dataset suitable for sentiment classification.
    * There are pre-prepared data-sets available that have sentiments included, are split into a training set and a testing set, and have a perfectly even distribution. For this lab, please find and prepare your own even if it is not perfect.
* Access it either externally or from within your repository as appropriate.
* Based on the shape of your data, determine an appropriate spread for your positive[2], neutral[1], and negative[0] sentiments and add a column associating them with the appropriate reviews.
* Identify and normalize any issues in your dataset.
* Do the preprocessing work utilizing Keras and Tensorflow taking a One-Hot Vector approach.
* In your readme, discuss the data set you choose, the distribution of your sentiments, your training/testing split, and the preprocessing methods you choose.

## 12-31-2019
* Utilizing a One-Hot Vector approach, create a Model that utilizes a Neural Network and has:
    * input layer
    * output layer
    * at least 2 Dropout/Dense layer pairs
    * Play with your activations to achieve the accuracy you would like, but discuss which ones you selected in your readme.
* Train your Model
* Test your model with the validation set you put aside yesterday.
* Save your trained Model as Json to be used again.

## Getting Started
* run `pipenv shell`

## Architecture
* `Jupyter Notebook`
* `Pandas`
* `Numpy`
* `matplotlib`
* `tensorflow`
* `keras`

## Change Log
* 12-30-2019 4:55pm - Initial commit, `food_reviews.csv`, `food_training.ipynb` added with sentiments and samples
* 12-30-2019 5:28pm - Utilized Keras and Tensorflow.
* 01-01-2020 11:38pm - Worked on model; still needs some work