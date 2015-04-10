from PIL import Image
import numpy as np

rgb2yiq = np.array([[0.299,    0.587,      0.114],
                     [0.595716, -0.274453,  -0.321263],
                     [0.211456, -0.522591,  0.311135]])

yiq2rgb = np.array([[1,        0.9563,     0.6210],
                     [1,        -0.2721,    0.6474],
                     [1,        -1.1070,    1.7046]])
  
alpha = 0.0
beta = 1.0
gamma = 1.0

img = Image.open("bird02.jpg").convert("RGB")

width = img.size[0]
height = img.size[1]

print [width, height]
 
pixels = img.load()
 
for i in range(width/2):
    for j in range(height):
        rgb = np.array(pixels[i,j])
        
        yiq = np.dot(rgb2yiq, rgb[:,None])
        
        # Multiply alpha beta
        yiq[0] = np.clip(yiq[0] * alpha, 0, 255)
        yiq[1] = np.clip(yiq[1] * beta, 0, 255)
        yiq[2] = np.clip(yiq[2] * gamma, 0, 255)
        # Clipping
        
        rgb = np.dot(yiq2rgb, yiq)
                 
        pixels[i,j] = tuple(list(rgb))
 
img.save("output.png");

print "Ready!"