import eel

eel.init('web')

try:
    eel.start('index.html', size=(200,250), port=80)
    
except Exception as debugs:
    print(debugs)