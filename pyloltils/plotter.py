import matplotlib.pyplot as plt
import cv2 as cv
from typing import Union
import numpy as np
import PIL
import torch

Imagetype = Union[
    np.ndarray, 
    torch.Tensor, 
    PIL.JpegImagePlugin.JpegImageFile, 
    PIL.PngImagePlugin.PngImageFile
    ]

def plot_image(image: Imagetype, bgr_switch:bool=False):
    if bgr_switch is True:
        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    if isinstance(image, torch.Tensor):
        image = image.permute(1,2,0)
        image = image.numpy()
    plt.imshow(image)
    plt.show()