from libs.labelFile import *

# specify threshold for score parameter
thresh = 0.25

# specify path to testing data
testing_bbox = '/home/sk/PycharmProjects/object_tracking/12/result-test/'

# specify path to testing images - for image data
image_folder = '/home/sk/datasets/kitti/testing/image_2/'

# read every line in *test*.txt to array and return array of arrays
def read_file_to_array(filename):
    array = []
    with open(filename) as file_for_read:
        for lines in file_for_read:
            if lines != '\n':
                array.append(str(lines)[:-2].split(' '))
    return array

# created shapes for labelImg PascalVocWriter class using threshold
def shapes_creator(file, thresh):
    shapes = []
    for lines in file:
        if float(lines[15]) >= thresh:
            shape = {}
            shape['label'] = str(lines[0])
            shape['points'] = [(float(lines[4]), float(lines[5])), (float(lines[6]), float(lines[5])), (float(lines[6]), float(lines[7])), (float(lines[4]), float(lines[7]))]
            shape['difficult'] = 0
            shapes.append(shape)
    return shapes


if __name__ == '__main__':

    for files in os.listdir(testing_bbox):
        if files.endswith('.txt'):
            shapes = shapes_creator(read_file_to_array(testing_bbox + files), thresh)
            LabelFile().savePascalVocFormat('labels_test/' + str(files)[:-4] + '.xml', shapes, image_folder + str(files[:-4]) + '.png', None)
            print(str(str(files[:-4]) + '.xml has been processed'))
