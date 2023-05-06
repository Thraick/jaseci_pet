import keras_ocr
import time
from PIL import Image
import numpy as np
import pyautogui
from PIL import ImageGrab
import pytesseract
from jaseci.actions.live_actions import jaseci_action
import os


@jaseci_action(act_group=["screen"], allow_remote=True)
def screenshot_to_text():
    # take screenshot
    # screenshot = ImageGrab.grab()

    # convert to grayscale
    # screenshot = screenshot.convert('L')
    time.sleep(4)

    screenshot = pyautogui.screenshot()
    screenshot.save('screenshot.png')

    # perform OCR
    text = pytesseract.image_to_string(screenshot)
    print(text)

    # save screenshot to current directory
    # current_dir = os.getcwd()
    # screenshot_path = os.path.join(current_dir, 'screenshot.png')
    # screenshot.save(screenshot_path)
    return text


# # screenshot_to_text()


# # Take a screenshot of the full screen
# screenshot = pyautogui.screenshot()
# text = pytesseract.image_to_string(screenshot)
# print(text)
# # Save the screenshot as a file
# screenshot.save('screenshot.png')


# import matplotlib.pyplot as plt

# Load the text recognition model
# pipeline = keras_ocr.pipeline.Pipeline()
# screenshot = pyautogui.screenshot()
# prediction_groups = pipeline.recognize([screenshot])

# print(prediction_groups)




# import cv2
# import pyautogui
# import keras_ocr

# # Load the OCR model
# pipeline = keras_ocr.pipeline.Pipeline()

# # Take a screenshot
# screenshot = pyautogui.screenshot()

# # Convert the screenshot to a numpy array
# image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

# # Perform OCR on the image
# prediction_groups = pipeline.recognize([image])

# # Print the recognized text
# for predictions in prediction_groups:
#     for prediction in predictions:
#         print(prediction[0])


import easyocr
import numpy as np
import pyautogui
import cv2

# Load the OCR model
reader = easyocr.Reader(['en'])

# Take a screenshot
screenshot = pyautogui.screenshot()

# Convert the screenshot to a numpy array
image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

# Perform OCR on the image
result = reader.readtext(image)

# Print the recognized text
for res in result:
    print(res[1])
