import math

from PIL import Image
import datetime


def gen_data(data):
    # This will hold binary codes of given data
    new_data = []

    for i in data:
        new_data.append(format(ord(i), '08b'))
    return new_data


def mod_pix(pix, data):
    data_list = gen_data(data)
    len_data = len(data_list)
    imdata = iter(pix)

    for i in range(len_data):

        # Extracting 3 pixels at a time to insert one character
        pix = [value for value in imdata.__next__()[:3] +
               imdata.__next__()[:3] +
               imdata.__next__()[:3]]

        # Pixel value should be made odd for 1 and even for 0
        for j in range(0, 8):
            if data_list[i][j] == '0' and pix[j] % 2 != 0:
                pix[j] -= 1

            elif data_list[i][j] == '1' and pix[j] % 2 == 0:
                if pix[j] != 0:
                    pix[j] -= 1
                else:
                    pix[j] += 1

        # If there is message still to be included, make the ninth value even
        # If the message is finished, make the ninth value odd indicating end of encoded message.
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
    """
    The top level function that performs encoding of message inside image.
    :param image: The image file received from the user/browser.
    :param message: The message text that is to be included inside the image.
    :return: The path of the encoded image.
    """
    # Throw error if the message is empty.
    if len(message) == 0:
        raise ValueError('Data is empty')

    # Load image in memory
    new_img = Image.open(image)

    # Main function for encoding message in image.
    # We also concatenate the current timestamp along with the message in order to be able to show
    # date and time when the message was encoded.
    encode_enc(new_img, message + get_timestamp())

    # Getting filename. Taking everything before the last dot (.)
    filename = image.filename.split('.')[0]

    # Finding the extension of the image.
    extension = image.filename.split('.').pop()

    # Providing new name to the file to be saved.
    # The naming format is: <old-name> + "_encoded".<file-extension>
    encoded_filename = filename + '_encoded.' + extension

    # This is the final path of the image where it will be saved.
    encoded_image_path = f'static/encoded_images/{encoded_filename}'

    # Saving image. After this, users can download this image from the saved path.
    new_img.save(encoded_image_path)

    # We return the path of the encoded image as response so that the frontend can prompt the
    # user to download the encoded image.
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

        # if value is even, treat it as 0
        # If value is odd, treat it as 1
        for i in pixels[:8]:
            if i % 2 == 0:
                binstr += '0'
            else:
                binstr += '1'

        data += chr(int(binstr, 2))

        # Keep on reading the pixels until the third value of third pixel (i.e. ninth value in group) is odd.
        # If this value is even, it means message has not been finished
        # If odd, this indicates the end of encoded message and hence, stop reading further.
        if pixels[-1] % 2 != 0:
            return data


def get_timestamp():
    # We append the timestamp to the message as: __1712703795__
    epoch = datetime.datetime.timestamp(datetime.datetime.now())

    # getting rid of decimal points.
    return f"__{math.floor(epoch)}__"
