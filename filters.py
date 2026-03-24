import cv2
import numpy as np

def apply_filter(image, filter_name):

    if filter_name == "gray":
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    elif filter_name == "cartoon":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(blur, 255,
                                      cv2.ADAPTIVE_THRESH_MEAN_C,
                                      cv2.THRESH_BINARY, 9, 9)
        color = cv2.bilateralFilter(image, 9, 250, 250)
        return cv2.bitwise_and(color, color, mask=edges)

    elif filter_name == "sketch":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        inv = cv2.bitwise_not(gray)
        blur = cv2.GaussianBlur(inv, (21, 21), 0)
        inv_blur = cv2.bitwise_not(blur)
        return cv2.divide(gray, inv_blur, scale=256.0)

    # 🆕 NEW FILTERS

    elif filter_name == "blur":
        return cv2.GaussianBlur(image, (15, 15), 0)

    elif filter_name == "sharpen":
        kernel = np.array([[0, -1, 0],
                           [-1, 5,-1],
                           [0, -1, 0]])
        return cv2.filter2D(image, -1, kernel)

    elif filter_name == "edges":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return cv2.Canny(gray, 100, 200)

    elif filter_name == "sepia":
        kernel = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])
        sepia = cv2.transform(image, kernel)
        return np.clip(sepia, 0, 255).astype(np.uint8)

    elif filter_name == "negative":
        return cv2.bitwise_not(image)

    else:
        return image
