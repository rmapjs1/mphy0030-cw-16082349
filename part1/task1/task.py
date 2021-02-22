''' The Task Script for Part 1, Task 1:
- implementation of a low-level file reading function: simple_image_read
- implementation of a low-level file writing function: simple_image_write
'''

# import libraries
import numpy as np
from matplotlib import pyplot as plt
from scipy.io import loadmat


# function: low-level file writing --> writes 3D medical images into binary files
def simple_image_write(data, path):
    '''
    This function writes 3D medical images into binary files

    Paramters
    ----------
    - data: data from 3D medical image read in from mat file
    - path (string): filepath where the image will be saved
    '''

    # get image parameters: 3D image volume (vol) and its voxel dimensions (voxdims)
    vol = data['vol'].astype('int16')   # store intensity values into 16-bit int
    vol = vol.transpose([1, 0, 2])  # switch rows and cols
    image_size = np.asarray(np.shape(vol))  #convert into array
    voxdims = data['voxdims'][0].astype('float32')  # store into 32-bit float

    # store header info (image size, voxel dimensions) and intensity values in a dict
    image_info= {'header':
                    {
                        'image_size': image_size,
                        'voxdims': voxdims
                    },
                 'volume': vol
                }

    # write image into binary file
    with open(path, 'wb') as binary_file:
        np.save(binary_file, image_info, allow_pickle = True)


# function: low-level file reading  --> reads 3D medical images (binary)
def simple_image_read(path):
    '''
    This function reads in medical images stored as binary files

    Paramters
    ---------
    - path (string): filepath to the binary image

    Returns
    -------
    - image_size: image size (3x1 array)
    - voxdims: voxel dimensions (3x1 array)
    - vol: voxel intensity values (array)
    '''

    # read binary image file
    with open(path, 'rb') as binary_file:
        data = (np.load(binary_file, allow_pickle= True)).item()

        image_size = data['header']['image_size']
        voxdims = data['header']['voxdims']
        vol = data['volume']

    return image_size, voxdims, vol



# 1. Load an example image in mat file, "data/example_image.mat"
# note: image contains a 3D image volume (vol) and its voxel dimensions (voxdims)

# 2. write image into file "data/image.sim" using simple_image_write fcn

# 3. read file "data/image.sim" using simple_image_read fcn

# 4. plot 3 images at different z-coordinates