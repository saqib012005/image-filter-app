import cv2

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

    else:
        return image