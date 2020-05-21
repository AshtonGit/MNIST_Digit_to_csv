# MNIST_Digit_to_csv
Python program that converts MNIST handwritten digit data archives into a csv format


MNIST dataset is a collection of images of handwritten digits, widely used for “classification”, “image recognition” task.
This is considered as relatively simple task, and often used for “Hello world” program in machine learning category.
It is also often used to compare algorithm performances in research.

The MNIST dataset is encoded in the IDX file format originally. This program provides functionality to convert it
into the more commonly used CSV (comma separated value) format. 

The idx2numpy library is used to make these conversions. 

**Features**

**Convert image dataset to csv**

*convertAllDigits(digit_filename, out_filename):*

Converts all instances in digit_filename to csv format, writing results to a single file.
Instances are NOT labelled. The dataset is left unsupervised.

**Convert subset of image dataset to csv**

*convertNDigits(n, digit_filename, out_filename):*

Converts the first *n* instances in digit_filename to csv format, writing results to a single file.
Instances are not labelled, the dataset is left unsupervised.

**Convert label dataset to csv**

*convertNLabels(n, label_filename, out_filename)*

Converts the first *n* instances in label_filename dataset to csv format, writing results to a single file.


**Create a supervised dataset in csv format**

*labelDigits(n, label_filename, digit_filename, out_filename)* 

Converts the first *n* digits and labels in dataset to csv and writes them to a single file.
Each newline is an  nstance. The first integer is the label followed by the digits image data.

**Create a supervised dataset in csv format split between multiple files**

*labelDigitsToMultipleFiles( label_filename, digit_filename, out_filename)*

Converts all digits and labels in dataset to csv. Digits are paired with their labels 
forming a supervised dataset. The dataset is split amongst mulitple files, each containing
max 20000 instances each.
