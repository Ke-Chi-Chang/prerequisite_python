  
import cv2
import numpy as np
import matplotlib


def imread(path, channel=3, lib='cv2'):
    if lib == cv2:
        if channel == 1:
            return cv2.imread(path, cv2.IMREAD_COLOR)
        elif channel == 3:
            return cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        elif channel == 4:
            return cv2.imread(path, cv2.IMREAD_UNCHANGED)
        else:
            raise ValueError(f"Wrong channel value: {channel} | Valid: 1, 3, 4")
    else:
        raise NotImplementedError(f"Unsupported library {lib} (matplotlib, PIL)")

def imwrite(img, path, compression_ratio=None, lib='cv2'):
    '''
    cv2.IMWRITE_JPEG_QUALITY
      - For JPEG, it can be a quality from 0 to 100 (the higher is the better)
      - Default value is 95.
    cv2.IMWRITE_PNG_COMPRESSION
      - For PNG, it can be the compression level from 0 to 9
      - A higher value means a smaller size and longer compression time
    '''
    if compression_ratio:
        suffix = Path(path).suffix
        if suffix = '.jpg':
            if compression_ratio >= 0 and compression_ratio <=100:
                cv2.imwrite(path, img, [cv2.IMWRITE_JPEG_QUALITY, compression_ratio])
            else:
                raise ValueError(f"Wrong compression_ratio of {suffix}: {compression_ratio} | Valid: 0 - 100")
        elif suffix = '.png':
            if compression_ratio >= 0 and compression_ratio <10:
                cv2.imwrite(path, img, [cv2.IMWRITE_PNG_COMPRESSION, compression_ratio])
            else:
                raise ValueError(f"Wrong compression_ratio of {suffix}: {compression_ratio} | Valid: 0 - 9")
        else:
            raise ValueError(f"Wrong suffix: {suffix} | Valid: .jpg, .png")
    else:
        cv2.imwrite(path, img)