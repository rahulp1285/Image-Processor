# Image Processor

This package will remove the exif content from the image. Metadata connected to photos is stored in a format called “Exchangeable Image File Format” or EXIF. EXIF metadata might include:

1. Latitude and longitude coordinates for the location where the photo was taken,
2. Camera settings like ISO speed, shutter speed, focal length, aperture, white balance, and lens type.
3. The make and model of the camera.
4. The date and time the photo was taken.
5. The name and build of all programs used to view or edit the photo.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependable package Pillow.

Pillow is a Python Imaging Library (PIL), which adds support for opening, manipulating, and saving images.

```bash
pip install Pillow
```

## Examples

In the files I have attached a Test.jpg which is of size 1.74Mb and processed output Image clean_Test.jpg which is of 533 Kb.

## Architecture
I have attached high level architecture diagram for this system in drawio format.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)