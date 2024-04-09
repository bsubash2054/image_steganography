import math
import os

from PIL import Image
import datetime

def genData(data):
    # list of binary codes
    # of given data
    newd = []

    for i in data:
        newd.append(format(ord(i), '08b'))
    return newd


def modPix(pix, data):
    datalist = genData(data)
    lendata = len(datalist)
    imdata = iter(pix)

    for i in range(lendata):

        # Extracting 3 pixels at a time
        pix = [value for value in imdata.__next__()[:3] +
               imdata.__next__()[:3] +
               imdata.__next__()[:3]]

        # Pixel value should be made
        # odd for 1 and even for 0
        for j in range(0, 8):
            if datalist[i][j] == '0' and pix[j] % 2 != 0:
                pix[j] -= 1

            elif datalist[i][j] == '1' and pix[j] % 2 == 0:
                if pix[j] != 0:
                    pix[j] -= 1
                else:
                    pix[j] += 1

        # Eighth pixel of every set tells
        # whether to stop ot read further.
        # 0 means keep reading; 1 means thec
        # message is over.
        if i == lendata - 1:
            if pix[-1] % 2 == 0:
                if pix[-1] != 0:
                    pix[-1] -= 1
                else:
                    pix[-1] += 1

        else:
            if pix[-1] % 2 != 0:
                pix[-1] -= 1

        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]


def encode_enc(newimg, data):
    w = newimg.size[0]
    (x, y) = (0, 0)

    for pixel in modPix(newimg.getdata(), data):

        # Putting modified pixels in the new image
        newimg.putpixel((x, y), pixel)
        if x == w - 1:
            x = 0
            y += 1
        else:
            x += 1


def encode(image, message):
    if len(message) == 0:
        raise ValueError('Data is empty')

    newimg = Image.open(image)
    encode_enc(newimg, message + get_timestamp())
    filename = image.filename.split('.')[0]
    extension = image.filename.split('.').pop()
    encoded_filename = filename + '_encoded.' + extension
    encoded_image_path = f'static/encoded_images/{encoded_filename}'
    newimg.save(encoded_image_path)
    return encoded_image_path


def decode(img):
    image = Image.open(img)
    data = ''
    imgdata = iter(image.getdata())

    while True:
        pixels = [value for value in imgdata.__next__()[:3] +
                  imgdata.__next__()[:3] +
                  imgdata.__next__()[:3]]

        # string of binary data
        binstr = ''

        for i in pixels[:8]:
            if i % 2 == 0:
                binstr += '0'
            else:
                binstr += '1'

        data += chr(int(binstr, 2))
        if pixels[-1] % 2 != 0:
            return data


def get_timestamp():
     # __1712703795__
    epoch = datetime.datetime.timestamp(datetime.datetime.now())
    return f"__{math.floor(epoch)}__"
