import math

from PIL import Image
import datetime


def gen_data(data):
    # list of binary codes
    # of given data
    new_data = []

    for i in data:
        new_data.append(format(ord(i), '08b'))
    return new_data


def mod_pix(pix, data):
    data_list = gen_data(data)
    len_data = len(data_list)
    imdata = iter(pix)

    for i in range(len_data):

        # Extracting 3 pixels at a time
        pix = [value for value in imdata.__next__()[:3] +
               imdata.__next__()[:3] +
               imdata.__next__()[:3]]

        # Pixel value should be made
        # odd for 1 and even for 0
        for j in range(0, 8):
            if data_list[i][j] == '0' and pix[j] % 2 != 0:
                pix[j] -= 1

            elif data_list[i][j] == '1' and pix[j] % 2 == 0:
                if pix[j] != 0:
                    pix[j] -= 1
                else:
                    pix[j] += 1

        # Eighth pixel of every set tells
        # whether to stop ot read further.
        # 0 means keep reading; 1 means the
        # message is over.
        if i == len_data - 1:
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


def encode_enc(new_img, data):
    w = new_img.size[0]
    (x, y) = (0, 0)

    for pixel in mod_pix(new_img.getdata(), data):

        # Putting modified pixels in the new image
        new_img.putpixel((x, y), pixel)
        if x == w - 1:
            x = 0
            y += 1
        else:
            x += 1


def encode(image, message):
    if len(message) == 0:
        raise ValueError('Data is empty')

    new_img = Image.open(image)
    encode_enc(new_img, message + get_timestamp())
    filename = image.filename.split('.')[0]
    extension = image.filename.split('.').pop()
    encoded_filename = filename + '_encoded.' + extension
    encoded_image_path = f'static/encoded_images/{encoded_filename}'
    new_img.save(encoded_image_path)
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
