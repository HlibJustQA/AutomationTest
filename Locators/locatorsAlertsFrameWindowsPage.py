from selenium.webdriver.common.by import By


class LocatorsBrowserWindow:

    new_tab_button = (By.CSS_SELECTOR, "button[id='tabButton']")
    new_window_button = (By.CSS_SELECTOR, "button[id='windowButton']")

class LocatorsAlert:

    alert_button = (By.CSS_SELECTOR, "button[id='alertButton']")
    alert_confirmation_button = (By.CSS_SELECTOR, "button[id='confirmButton']")
    confirm_text = (By.CSS_SELECTOR, "span[id='confirmResult']")
    prompt_button = (By.CSS_SELECTOR, "button[id='promtButton']")
    prompt_text = (By.CSS_SELECTOR, "span[id='promptResult']")

class LocatorsFrames:

    first_frame = (By.CSS_SELECTOR, "iframe[id='frame1']")
    second_frame = (By.CSS_SELECTOR, "iframe[id='frame2']")
    frame_text = (By.CSS_SELECTOR, "h1[id='sampleHeading']")

class LocatorsNestedFrames:

    parent_frame = (By.CSS_SELECTOR, "iframe[id='frame1']")
    parent_text = (By.CSS_SELECTOR, "body")
    child_frame = (By.CSS_SELECTOR, "iframe[srcdoc='<p>Child Iframe</p>']")
    child_text = (By.CSS_SELECTOR, "p")

class LocatorsModalDialog:

    pass
