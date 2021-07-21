# Requiremnt to do a Install of Pillow Library
# Pillow is a Python Imaging Library (PIL), which adds support for opening, manipulating, and saving images.
# pip install Pillow

#import Image from PIL
from PIL import Image

imagename= "Test.jpg"

image = Image.open(imagename)
print('Opening Image')
# below code will  strip exif data
image_data = list(image.getdata())
image_without_exif = Image.new(image.mode, image.size)
image_without_exif.putdata(image_data)

image_without_exif.save(u"clean_{}".format(imagename))


---Upload To New Bucket Using S3 Boto3---

