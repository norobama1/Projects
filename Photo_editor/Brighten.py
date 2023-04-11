from image import Image
import numpy as np

def brighten(image,factor):
    '''
    when we adjust brightness we want to scale each value by some amount
    factor is a vale>0,how much we wan to brighten the image by
    (<1= darken , >1 = brighten)
    '''
    x_pixels,y_pixels,num_channels = image.array.shape
    #making a new array 
    new_im =Image(x_pixels=x_pixels,y_pixels=y_pixels,num_channels=num_channels)
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_im.array[x,y,c] = image.array[x,y,c]*factor

    #Vectorized verison
    #new_im.array = image.array * factor
    
    return new_im

if __name__ == '__main__':
    lake = Image(filename='lake.png')
    city = Image(filename='city.png')

    #brightening
    brightened_im = brighten(lake,1.6)
    brightened_im.write_image('brightened.png')

    #Darkning
    darkened_im = brighten(lake,0.5)
    darkened_im.write_image('darkened.png')
