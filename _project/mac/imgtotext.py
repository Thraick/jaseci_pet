from PIL import ImageGrab
import pytesseract
from jaseci.actions.live_actions import jaseci_action

@jaseci_action(act_group=["screen"], allow_remote=True)
def screenshot_to_text():
    # take screenshot
    screenshot = ImageGrab.grab()

    # convert to grayscale
    screenshot = screenshot.convert('L')

    # perform OCR
    text = pytesseract.image_to_string(screenshot)
    print(text)

    return text

# screenshot_to_text()

