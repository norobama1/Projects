from image import Image
# import numpy as np

def Contrast(image ,factor,mid=0.5):
    #adjust the contrast by increasing the difference from the user-defined midpoint by some amount,factor
    x_pixels,y_pixels,num_channels = image.array.shape  
    new_im =Image(x_pixels=x_pixels,y_pixels=y_pixels,num_channels=num_channels)
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_im.array[x,y,c] = (image.array[x,y,c]-mid)*factor + mid 

    #Vectorized way
    #new_im.array = (image.array - mid)*factor + mid
    return new_im

if __name__ == '__main__':
    lake = Image(filename='lake.png')
    city = Image(filename='city.png')

    #Increase Contrast
    increase_contrast = Contrast(lake,2)
    increase_contrast.write_image('increase_contrast.png')

    #Decrease Contrast
    decrease_contrast = Contrast(lake,0.5)
    decrease_contrast.write_image('decrease_contrast.png')