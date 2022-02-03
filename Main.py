import cv2 as cv
import numpy as np
import os
import glob


# load color image
def load_image():
    img_path = 'SAMSUNG SM-J710F (000014600640).jpg'
    image = cv.imread(img_path, cv.IMREAD_COLOR)


def load_all_images():
    # Enter Directory of all images

    img_dir = "../DamagedImages/"
    origin_path = os.path.join(img_dir, '*g')
    files = glob.glob(origin_path)
    data = []
    for f1 in files:
        img = cv.imread(f1)
        data.append(img)  # store all images in data array
    file_names = []
    for filename in os.listdir(img_dir):
        org_image_name = os.path.splitext(filename)[0]
        file_names.append(org_image_name)
    return data, file_names


def find_corrupt_area(img, file_name):
    target_dir = "../RepairedImages/"
    img_path = 'image_path'
    # cv.imshow(img_path, img)
    # k = cv.waitKey(0)
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    # px = hsv[530, 959]
    # print( px )
    low_grey = np.array([0, 0, 127])
    high_grey = np.array([0, 0, 129])
    mask = cv.inRange(hsv, low_grey, high_grey)
    res = cv.bitwise_or(img, img, mask=mask)
    cv.imshow(img_path, res)
    k = cv.waitKey(0)
    # cv.imshow(img_path, mask)
    # k = cv.waitKey(0)

    rgb_mask = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)  # change mask to a 3 channel image
    mask_out = cv.subtract(img, rgb_mask)
    # cv.imshow(img_path, mask_out)
    # k = cv.waitKey(0)

    mask_out_grey = cv.cvtColor(mask_out, cv.COLOR_BGR2GRAY)
    _, thresh = cv.threshold(mask_out_grey, 1, 255, cv.THRESH_BINARY)
    # cv.imshow(img_path, thresh)
    # k = cv.waitKey(0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    x, y, w, h = cv.boundingRect(cnt)
    crop = img[y:y + h, x:x + w]
    # cv.imshow(img_path, crop)
    # k = cv.waitKey(0)
    cv.imwrite(os.path.join(target_dir, file_name+'.jpg'), crop)


data, file_names = load_all_images()
for i, img in enumerate(data):
    print(file_names[i])
    find_corrupt_area(img, file_names[i])
