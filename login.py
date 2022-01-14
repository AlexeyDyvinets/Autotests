import eel

eel.init("GUI")

@eel.expose
def logChrome():
    import CromeLogin
    
@eel.expose
def logFF():
    import FFLogin  
  
eel.start("main.html", size =(684, 440))
