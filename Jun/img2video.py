import cv2
import numpy as np
import glob
from tqdm import tqdm
num = 4

frameSize = (384 * num, 384 * num)

out = cv2.VideoWriter('output_video.avi', cv2.VideoWriter_fourcc(*'DIVX'), 10, frameSize)


files = sorted(glob.glob('img/*.jpg'))

for filename in tqdm(files):
    img = cv2.imread(filename)
    img = img[0: 0 + 384 * num, 0: 0 + 384 * num]

    out.write(img)

out.release()