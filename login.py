import eel

eel.init("GUI")

@eel.expose
def logChrome():
    import ChromeLogin
    
@eel.expose
def logFF():
    import FFLogin  
  
eel.start("main.html", size =(684, 440))
