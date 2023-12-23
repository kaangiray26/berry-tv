from selenium import webdriver

class Browser:
    def __init__(self):
        print("Starting Firefox session...")
        
        # Set up Firefox options
        self.options = webdriver.FirefoxOptions()
        self.options.set_preference("media.autoplay.default", 0)
        
        # Create Firefox webdriver
        self.driver = webdriver.Firefox(options=self.options)
        
        # Fullscreen window
        self.driver.fullscreen_window()
        
        # Install uBlock Origin
        self.driver.install_addon("libraries/uBlock0_1.54.0.firefox.signed.xpi")
        
        self.driver.get("about:blank")
    
    def get_title(self):
        return {
            "title": self.driver.execute_script("return document.title")
        }
    
    def get_address(self):
        return {
            "address": self.driver.execute_script("return document.location.href")
        }
    
    def open_address(self, address):
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