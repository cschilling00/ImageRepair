import cv2 as cv
import numpy as np
import os
import glob
from os.path import isfile, join

src_img_dir = '../DamagedImages/'
target_dir = '../RepairedImages0/'

def load_all_images():
    # Enter root directory of all images
    origin_path = os.path.join(src_img_dir, '*g')
    files = glob.glob(origin_path)
    data = []
    for f1 in files:
        img = cv.imread(f1)
        data.append(img)  # store all images in data array

    # searches through subdirectories
    # for file in glob.glob(origin_path):
    #     img = cv.imread(file)
    #     data.append(img)

    file_names = []
    for filename in os.listdir(src_img_dir):
        if isfile(join(src_img_dir, filename)):
            org_image_name = os.path.splitext(filename)[0]
            file_names.append(org_image_name)
    return data, file_names


def find_grey_area(img):
    # cv.imshow(img_path, img)
    # k = cv.waitKey(0)
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    # px = hsv[3000, 2900]
    # print( px )
    low_grey = np.array([0, 0, 127])
    high_grey = np.array([0, 0, 129])
    mask = cv.inRange(hsv, low_grey, high_grey)
    # res = cv.bitwise_or(img, img, mask=mask)

    rgb_mask = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)  # change mask to a 3 channel image
    mask_out = cv.subtract(img, rgb_mask)

    mask_out_grey = cv.cvtColor(mask_out, cv.COLOR_BGR2GRAY)
    _, thresh = cv.threshold(mask_out_grey, 1, 255, cv.THRESH_BINARY)

    contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    x, y, w, h = cv.boundingRect(thresh)
    return x, y, w, h


def detect_edgeless_area(img):
    grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    edged = cv.Canny(grey, 10, 250)
    # contours, hierarchy = cv.findContours(edged, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    # cnt = contours[0]
    x, y, w, h = cv.boundingRect(edged)
    # print('x,y,w,h')
    # print(x)
    # print(y)
    # print(w)
    # print(h)
    return x, y, w, h


def find_color_stripes(img):
    grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    rho = 1  # distance resolution in pixels of the Hough grid
    theta = np.pi / 180  # angular resolution in radians of the Hough grid
    threshold = 15  # minimum number of votes (intersections in Hough grid cell)
    min_line_length = 400  # minimum number of pixels making up a line
    max_line_gap = 40  # maximum gap in pixels between connectable line segments
    line_image = np.copy(grey) * 0  # creating a blank to draw lines on
    edges = cv.Canny(grey, 10, 250)
    lines = cv.HoughLinesP(edges, rho, theta, threshold, np.array([]),
                           min_line_length, max_line_gap)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv.line(line_image, (x1, y1), (x2, y2), (255, 255, 255), 40)
    _, thresh = cv.threshold(line_image, 1, 255, cv.THRESH_BINARY_INV)
    res = cv.bitwise_and(grey, grey, mask=thresh)
    x, y, w, h = cv.boundingRect(res)
    return x, y, w, h


def extract_thumbnail(img):
    j = 2
    start = ''
    end = ''
    array = np.array(img)
    for j in img.size:
        if img.size[j] == 0xFF:
            if not start:
                if img.size[j + 1] == 0xD8:
                    start = j

                elif img.size[j + 1] == 0xD9:
                    end = j + 2

    if start and end:
        array = img[(start, end)]
        cv.imshow('img_path', array)
        k = cv.waitKey(0)



def crop_image(x, y, w, h, img):
    # cut a little from the edge to remove remaining edges
    crop = img[y + 20:y + h - 20, x + 20:x + w - 20]
    # crop = img[y:y + h, x:x + w]
    return crop


def save_image(img, file_name):
    if img.size != 0:
        cv.imwrite(os.path.join(target_dir, file_name + '.jpg'), img)


def save_original_image(img, file_name):
    if img.size != 0:
        print(target_dir)
        print(target_dir + 'unchanged')
        print(os.path.join(target_dir + 'unchanged', file_name + '.jpg'))
        cv.imwrite(os.path.join(target_dir + 'unchanged', file_name + '.jpg'), img)


def main(data, file_names):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    if not os.path.exists(target_dir + 'unchanged'):
        os.mkdir(target_dir + 'unchanged')

    global i
    for i, img in enumerate(data):
        print(file_names[i])
        x, y, w, h = find_grey_area(img)
        grey_img = crop_image(x, y, w, h, img)
        x, y, w, h = find_color_stripes(img)
        stripes_img = crop_image(x, y, w, h, img)
        # print(grey_img.size)
        # print(stripes_img.size)
        # extract_thumbnail(img)
        if grey_img.size < stripes_img.size and grey_img.size < img.size and img.size - grey_img.size > 2000000:
            save_image(grey_img, file_names[i])
        elif grey_img.size > stripes_img.size and stripes_img.size < img.size and img.size - stripes_img.size > 2000000:
            save_image(stripes_img, file_names[i])
        else:
            x, y, w, h = detect_edgeless_area(img)
            edge_img = crop_image(x, y, w, h, img)
            if edge_img.size < img.size and img.size - edge_img.size > 2000000:
                print('edge_img.size')
                print(edge_img.size)
                print(img.size)
                save_image(edge_img, file_names[i])
            else:
                print('original')
                save_original_image(img, file_names[i])
