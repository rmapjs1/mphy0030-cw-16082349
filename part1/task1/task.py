## The Task Script for Task 1

## function: low-level file reading "simple_image_read"
# reads 3D medical images

## function: file writing "simple_image_write"
# writes 3D medical images into binary files (not text or other formats)
# stores intensity values into 16-bit int
# stores voxel dimensions in 32-bit float
# note: write image size into file header
# note: use a single file to store all header info with the intensity values



# 1. Load an example image in mat file, "data/example_image.mat"
# note: image contains a 3D image volume (vol) and its voxel dimensions (voxdims)

# 2. write image into file "data/image.sim" using simple_image_write fcn

# 3. read file "data/image.sim" using simple_image_read fcn

# 4. plot 3 images at different z-coordinates