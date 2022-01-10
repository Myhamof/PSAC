#ps4 profile picture creator
from wand import image
def convert(filename):
    #open image
    with image.Image(filename=filename) as img:
        #resize the original image to 440x440:
        img.resize(440,440)
        img.save(filename=filename)
        #convert image to dds:
        img.format = 'DXT5'
        #resize image to 4 different sizes 440 x 440, 260 x 260, 128 x 128, 64 x 64:
        img.resize(440, 440)
        img.save(filename=filename.replace('.png', '440.dds'))
        img.resize(260, 260)
        img.save(filename=filename.replace('.png', '260.dds'))
        img.resize(128, 128)
        img.save(filename=filename.replace('.png', '128.dds'))
        img.resize(64, 64)
        img.save(filename=filename.replace('.png', '64.dds'))

#ask user for the image location and call the function:
convert(input('Enter image path or just drag the image here: ').replace('"', ''))