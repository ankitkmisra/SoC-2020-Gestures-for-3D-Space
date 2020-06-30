# SoC 2020 - Gestures for 3D Space

This repository contains the final project and all practice programs written by me during my Summer of Code 2020 project.

## Final Project - One Shot Learning with Siamese Networks

### Project Description

My final project in SoC 2020 was based on one-shot learning for gesture recognition, using a [Siamese neural network](https://en.wikipedia.org/wiki/Siamese_neural_network). A trained Siamese network calculates the 'distance' between two inputs by applying some similarity function on the corresponding encoding vectors. I build a Siamese network, with a VGG16 convolutional base (pre-trained on ImageNet), using the triplet loss function and an Adam optimizer, with the Euclidean distance between encoding vectors as the 'distance' function. This model was trained on a static [American Sign Language dataset](https://ieee-dataport.org/open-access/static-hand-gesture-asl-dataset), with 24 gesture classes having 40 images each, and it was tested on [my own dataset of hand gestures](https://github.com/ankitkmisra/SoC-2020-Gestures-for-3D-Space/tree/master/Final%20Project%20-%20One%20Shot%20Learning/gestures_dataset_2), with 15 gesture classes having 25 images each. The classification accuracy on the test set was 89.87%. Next, a Python-3 script was written to load the model architecture from a JSON file, the model weights from an H5 file, to capture video feed from the device, preprocess each frame, and print the result of classification by the model on the screen. [Here](https://github.com/ankitkmisra/SoC-2020-Gestures-for-3D-Space/tree/master/Final%20Project%20-%20One%20Shot%20Learning/Results) is a link to screenshots of each of the 15 gestures being classified by the Python script.

Here are a few examples:

!['Yo' Gesture Classification](https://github.com/ankitkmisra/SoC-2020-Gestures-for-3D-Space/blob/master/Final%20Project%20-%20One%20Shot%20Learning/Results/yo.png)
!['Spock' Gesture Classification](https://github.com/ankitkmisra/SoC-2020-Gestures-for-3D-Space/blob/master/Final%20Project%20-%20One%20Shot%20Learning/Results/spock.png)
!['Gun' Gesture Classification](https://github.com/ankitkmisra/SoC-2020-Gestures-for-3D-Space/blob/master/Final%20Project%20-%20One%20Shot%20Learning/Results/gun.png)

### Usage

To use this project, follow these steps:
1. First, make sure you have all the required dependencies. These include:
    1. Python (3.6.9)
    2. OpenCV Python (3.2.0)
    3. NumPy (1.18.1)
    4. TensorFlow (2.2.0)
    5. Keras (2.4.3)
    
2. Clone this repository.
```
$ git clone https://github.com/ankitkmisra/SoC-2020-Gestures-for-3D-Space
```

3. Move into the `Final Project - One Shot Learning` directory.
```
$ cd 'SoC-2020-Gestures-for-3D-Space/Final Project - One Shot Learning/'
```

4. Run the Python-3 script called `main.py`.
```
$ python3 main.py
```

Obviously, you will need a webcam device to run this program.

## Things I Learned From This Project

Brief descriptions of the learning components of this project are given below:

### [OpenCV Practice](https://github.com/ankitkmisra/SoC-2020-Gestures-for-3D-Space/tree/master/OpenCV%20Practice)

This directory contains several practice programs, written in Jupyter notebooks and Python-3 scripts when I was learning to use OpenCV Python. The topics covered include various kinds of image processing, such as thresholding, blurring, affine transformations, edge detection, corner detection, feature matching, watershed segmentation, etc.

### [NumPy Practice](https://github.com/ankitkmisra/SoC-2020-Gestures-for-3D-Space/tree/master/NumPy%20Practice)

This directory contains some practice programs, written in Jupyter notebooks when I was learning NumPy, from the [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) by Jake VanderPlas.

### [Pandas Practice](https://github.com/ankitkmisra/SoC-2020-Gestures-for-3D-Space/tree/master/Pandas%20Practice)

This directory contains some practice programs, written in Jupyter notebooks when I was learning Pandas, from the [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) by Jake VanderPlas, and the [Kaggle microcourse on Pandas](https://www.kaggle.com/learn/pandas).

### [Training and Deploying Models](https://github.com/ankitkmisra/SoC-2020-Gestures-for-3D-Space/tree/master/Training%20and%20Deploying%20Models)

This directory contains some machine learning programs I wrote for practice, and also a couple of practice programs for model deployment using Flask. The resources used were [Deep Learning with Python](https://www.manning.com/books/deep-learning-with-python) by François Chollet and [Hands-On Machine Learning](https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/) by Aurélien Géron. The programs have been put in different subdirectories according to the book used.

### [Transfer Learning](https://github.com/ankitkmisra/SoC-2020-Gestures-for-3D-Space/tree/master/Transfer%20Learning)

This directory contains two Jupyter notebooks, in which I used transfer learning from the VGG16 and the ResNet50 convolutional bases respectively (pre-trained on the ImageNet dataset) to build a model for gesture recognition. The data used came from the [Fingers](https://www.kaggle.com/koryakinp/fingers) dataset on Kaggle. I learned through this experience that transfer learning really helps boost the model's performance quite a bit.

### [Learning PyTorch](https://github.com/ankitkmisra/SoC-2020-Gestures-for-3D-Space/tree/master/Learning%20PyTorch)

This directory contains a single Jupyter notebook I wrote when learning the basics of PyTorch. PyTorch was not used further in this project.