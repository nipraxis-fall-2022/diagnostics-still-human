""" Scan outlier metrics
"""

# Any imports you need
import numpy as np

def dvars(img):
    """ Calculate dvars metric on Nibabel image `img`

    The dvars calculation between two volumes is defined as the square root of
    (the mean of the (voxel differences squared)).

    Parameters
    ----------
    img : nibabel image

    Returns
    -------
    dvals : 1D array
        One-dimensional array with n-1 elements, where n is the number of
        volumes in `img`.
    """
    data = img.get_fdata()
    reshaped = np.reshape(data,(np.prod(img.shape[:-1]), img.shape[-1]))
    diff = np.diff(reshaped)
    dvals = np.sqrt(np.mean(diff ** 2, axis=0))
    return dvals