from PIL import Image
import matplotlib.pyplot as plt

img=Image.open('mario.jpeg')

def photo2pixelart(image, i_size, o_size):
    img=Image.open(image)

    small_img=img.resize(i_size,Image.BILINEAR)

    res=small_img.resize(img.size, Image.NEAREST)

    filename=f'mario_{i_size[0]}x{i_size[1]}.png'
    res.save(filename)

    plt.figure(figsize=(16,10))

    plt.subplot(1,2,1)
    plt.title('Original image', size=18)
    plt.imshow(img)   
    plt.axis('off')   
    plt.subplot(1,2,2)
    plt.title(f'Pixel Art {i_size[0]}x{i_size[1]}', size=18)
    plt.imshow(res)
    plt.axis('off')
    plt.savefig('temp.png')
    plt.show()
    
photo2pixelart(image='mario.jpeg',i_size=(80,80),o_size=img.size)