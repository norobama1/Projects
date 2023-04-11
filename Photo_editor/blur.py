from image import Image
# import numpy as np

def blur(image,kernal_size):
    '''
    kernal size is the number of pixels to take into account when applying blur
    ie kernal size =3 would be neighbors to the left/right ,top/bottom and diagonals
    kernal size should always be odd number
    '''
    x_pixels,y_pixels,num_channels = image.array.shape  
    new_im =Image(x_pixels=x_pixels,y_pixels=y_pixels,num_channels=num_channels)
    neighbor_range = kernal_size//2 #how many neighbors we need to look at one side

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                total = 0
                for x_i in range(max(0,x-neighbor_range),min(x_pixels-1,x+neighbor_range)+1):
                    for y_i in range(max(0,y-neighbor_range),min(y_pixels-1,y+neighbor_range)+1):
                        total += image.array[x_i,y_i,c]
                new_im.array[x,y,c] = total/(kernal_size**2)

    return new_im

if __name__ == '__main__':
    lake = Image(filename='lake.png')
    city = Image(filename='city.png')

    #blur with kernal size 3
    blur_3 = blur(city,3)
    blur_3.write_image('blur3.png')

    #blur with kernal size 15
    blur_15 = blur(city,15)
    blur_15.write_image('blur15.png')
