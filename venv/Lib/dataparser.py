# Converts MNIST Database file format into an uncompressed csv file.
# MNIST dataset has Instances and their labels stored in separate files.
# The following functions can join instances to their labels or keep them separate.
import sys, os
import idx2numpy


# Converts MNIST digit data to csv format
# This converts all instances in digit_filename to csv format and outputs a single file.
# Instances are NOT labelled. The dataset is left unsupervised.

def convertAllDigits(digit_filename, out_filename):

    ndarr = idx2numpy.convert_from_file(digit_filename)
    train_data = open(out_filename, "w+")
    train_data.write("28,28\n")  # each instance is an image compiled of a 28 * 28 pixel grid
    n = 0;
    prefix = 0
    for i in ndarr:
        if (n == 10000):
            train_data.close()
            train_data = open(dirname + str(prefix) + write_filename, "w+")
            n = 0
            prefix += 1
        for x in i:  # row
            for y in x:  # item
                train_data.write(str(y) + ",")
        train_data.write("\n")
        n += 1

# Converts MNIST digit data to csv format.
# This converts all instances in digit_filename to csv format and outputs a single file.
# Only converts the first N instances.
# The instances are not labelled.
def convertNDigits(n, digit_filename, out_filename):

    ndarr = idx2numpy.convert_from_file(digit_filename)
    train_data = open(out_filename, "w+")
    train_data.write("28,28\n")  # each instance is an image compiled of a 28 * 28 pixel grid
    c = 0;

    for i in ndarr:
        if (c == n):
            train_data.close()
            return
        for x in i:  # row
            for y in x:  # item
                train_data.write(str(y) + ",")
        train_data.write("\n")
        c += 1


# Transforms MNIST label data to the csv format.
# This function converts only the instance class labels to csv
# Only the first N labels are processed.
def convertNLabels(n, label_filename, out_filename):

    ndarr = idx2numpy.convert_from_file(label_filename)
    train_data = open(out_filename, "w+")

    c = 0;

    for i in ndarr:
        if (c == n):
            train_data.close()
            return
        train_data.write(str(i) + ",")
        c += 1

# Transforms MNIST digit data to the csv format and adds a class label to aid with training
# MNIST data set has data instances and their labels stored in separate files.
# This function joins the label to instance in a single file.
def labelDigits(n, label_filename, instance_filename, out_filename):
    dirname = os.path.dirname(os.path.dirname(__file__))
    instance_filename = dirname + instance_filename
    label_filename = dirname + label_filename
    digits = idx2numpy.convert_from_file(instance_filename)
    labels = idx2numpy.convert_from_file(label_filename)

    train_data = open(dirname + "/assets/" + out_filename, "w+")

    c = 0;
    for i in range(0, n):
        train_data.write((str(labels[i]) + ","))
        for r in digits[i]:
            for x in r:
                train_data.write(str(x) + ",")
        if (i != n - 1):
            train_data.write("\n")

    train_data.close()


# Transforms MNIST digit data into csv format and adds a class label to aid with training.
# The CSV output data is then divided into multiple files to split the data set up into manageable chunks
# of 20000 instances per file.
def labelDigitsToMultipleFiles(label_filename, instance_filename, out_filename):
    dirname = os.path.dirname(os.path.dirname(__file__))
    instance_filename = dirname + instance_filename
    label_filename = dirname + label_filename
    digits = idx2numpy.convert_from_file(instance_filename)
    labels = idx2numpy.convert_from_file(label_filename)
    n = len(labels)
    c = 0
    prefix = 0
    out_file = open(dirname + "/assets/" + str(prefix) + "_" + out_filename, "w+")
    for i in range(0, n):
        if (c == 19999):
            prefix += 1
            c = 0
            out_file.close()
            out_file = open(dirname + "/assets/" + str(prefix) + "_" + out_filename, "w+")
        out_file.write((str(labels[i]) + ","))
        for r in digits[i]:
            for x in r:
                out_file.write(str(x) + ",")
        out_file.write("\n")
        c += 1
    out_file.close()


