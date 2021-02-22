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


# the following will only be executed if this file in particular is run (in directory /part1/task1)
if __name__ == '__main__':

    # load an example image in mat file
    image_path = '../../data/example_image.mat'
    image_data = loadmat(image_path)

    # write image into a binary file
    binary_path = '../../data/image.sim'
    simple_image_write(image_data, binary_path)

    # read the binary file
    image_size, voxdims, vol = simple_image_read(binary_path)

    # plot 3 images at different z-coordinates
    z_coords = [10, 15, 20]
    figure, axis = plt.subplots(1, 3)
    for i, z_val in enumerate(z_coords):
         axis[i].imshow(vol[:, :, z_val])
         axis[i].set_title('z-coordinate = ' + str(z_val), fontsize = 9)

    figure.suptitle('Images at 3 different z-coordinates', fontsize = 12, y = 0.8)  # set the overall title
    
    # display the figures
    plt.show()
    # save the figures as png 
    plt.savefig('different_z_images.png')
    

