from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np


def load_fits(images):
    x = images
    c = len(images)
    hdulist = fits.open(images[0])
    data = hdulist[0].data
    hdulist.close()
    
    for i in range(1,c):
        hdulist = fits.open(images[i])
        data += hdulist[0].data
    mean = data/c
    return mean
