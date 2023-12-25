from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Browser:
    def __init__(self):
        self.item_index = 0
        self.selected = False
        print("Starting Firefox session...")
        
        # Set up Firefox options
        self.options = webdriver.FirefoxOptions()
        self.options.set_preference("media.autoplay.default", 0)
        
        # Set fullscreen approval
        self.options.set_preference("full-screen-api.approval-required", False)
        
        # Create Firefox webdriver
        self.driver = webdriver.Firefox(options=self.options)
        
        # Fullscreen window
        self.driver.fullscreen_window()
        
        # Install uBlock Origin
        self.driver.install_addon("/home/buzluk/berry-tv/libraries/uBlock0_1.54.0.firefox.signed.xpi")
        self.driver.execute_script("window.location.href = 'http://localhost:8000/connect'")
    
    def get_title(self):
        return {
            "title": self.driver.execute_script("return document.title")
        }
    
    def get_address(self):
        return {
            "address": self.driver.execute_script("return document.location.href")
        }
    
    def open_address(self, address):
        # Reset selected items
        self.item_index = 0
        self.selected = False
        
        # Open address
        self.driver.get(address)
        
        # Set up event listeners for play and pause events
        self.driver.execute_script("document.querySelector('video').onplaying = () => {fetch('http://localhost:8000/api/play')}")
        self.driver.execute_script("document.querySelector('video').onplay = () => {fetch('http://localhost:8000/api/play')}")
        self.driver.execute_script("document.querySelector('video').onpause = () => {fetch('http://localhost:8000/api/pause')}")
        self.driver.execute_script("document.querySelector('video').ontimeupdate = () => {fetch(`http://localhost:8000/api/timeupdate?currentTime=${document.querySelector('video').currentTime}&duration=${document.querySelector('video').duration}&paused=${document.querySelector('video').paused}&title=${document.title}`)}")
        duration = self.driver.execute_script("return document.querySelector('video').duration")
        return {
            "title": self.driver.title,
            "duration": duration
        }
        
    def play(self):
        self.driver.execute_script("document.querySelector('video').play()")
        
    def pause(self):
        self.driver.execute_script("document.querySelector('video').pause()")
        
    def seek(self, time):
        self.driver.execute_script(f"document.querySelector('video').currentTime = {time}")
        
    def seek_backward(self):
        self.driver.execute_script("document.querySelector('video').currentTime -= 10")
    
    def seek_forward(self):
        self.driver.execute_script("document.querySelector('video').currentTime += 10")
        
    def fullscreen(self):
        self.driver.find_element(By.TAG_NAME, "body").send_keys("f")
        
    def previous(self):
        # Go back in history
        self.driver.execute_script("window.history.back()")
        
    def next(self):
        # Press shift + n to go to next video
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.SHIFT, "n")

    def close(self):
        self.driver.quit()