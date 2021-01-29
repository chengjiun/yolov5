from utils.datasets import LoadStreams
import cv2

dataset = LoadStreams('0')

for path, img, im0s, vid_cap in dataset:
    cv2.imshow('original', im0s[-1])
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

del(dataset)
