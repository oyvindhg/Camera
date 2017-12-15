#Probably faster, for sure uglier

from enum import Enum
import cv2

class Text(Enum):
    FONT_HERSHEY_SIMPLEX = 0
    FONT_HERSHEY_PLAIN = 1
    FONT_HERSHEY_DUPLEX = 2
    FONT_HERSHEY_COMPLEX = 3
    FONT_HERSHEY_TRIPLEX = 4
    FONT_HERSHEY_COMPLEX_SMALL = 5
    FONT_HERSHEY_SCRIPT_SIMPLEX = 6
    FONT_HERSHEY_SCRIPT_COMPLEX = 7
    FONT_ITALIC = 16

class Color(Enum):
    red = (255, 0, 0)
    blue = (0, 255)


def show_labeled2(im, boxes):
    for box in boxes:
        left = round(box[2][0] - 1/2 * box[2][2])
        top = round(box[2][1] - 1/2 * box[2][3])
        width = round(box[2][2])
        height = round(box[2][3])

        if (left < 0): left = 0
        if (left + width > im.shape[0] - 1): width = im.shape[0] - 1 - left
        if (top < 0): top = 0
        if (top + height > im.shape[1] - 1): height = im.shape[1] - 1 - top

        line_thick = 2
        cv2.rectangle(im,(left,top),(left+width,top+height),(0,255,0),line_thick)
        label = box[0].decode("utf-8")

        text_scale = 0.6
        text_thick = 1
        font = Text.FONT_HERSHEY_COMPLEX.value
        text_size = cv2.getTextSize(label, font, text_scale, text_thick)

        text_width = text_size[0][0]
        text_height = text_size[0][1]
        buf = 8

        if left - 1 < 0 or top - text_height - buf < 0:
            cv2.rectangle(im, (left, top), (left + text_width, top + text_height + buf), (0, 255, 0), -1)
            cv2.putText(im, label, (left, top + text_height), font, text_scale, (0, 0, 0), text_thick)
        else:
            cv2.rectangle(im, (left - 1, top), (left + text_width, top - text_height - buf), (0, 255, 0), -1)
            cv2.putText(im, label, (left, top - buf), font, text_scale, (0, 0, 0), text_thick)

    cv2.imshow("Show",im)
    cv2.waitKey()
    cv2.destroyAllWindows()

