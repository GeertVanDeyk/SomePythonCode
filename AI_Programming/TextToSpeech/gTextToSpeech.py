from gtts import gTTS
from pathlib import Path

def turn2Speech (text: str, targetPath:str, fileName:str,lang = 'de', tld = 'de'):
    targetPath = Path(targetPath)
    fullpath = targetPath / fileName
    tts = gTTS(text, lang=lang, tld=tld)
    tts.save(fullpath)
    return 



if __name__ == '__main__':
    
    introduction_text = '''
    Als Gregor Samsa eines Morgens aus unruhigen Träumen erwachte, fand er sich in seinem Bett zu einem ungeheuren Ungeziefer verwandelt.
    '''
    path_string = "C:/Users/gvandeyk/OneDrive - DXC Production/Downloads"
    fileName_string = "try-out.mp3"
    
    _ = turn2Speech (introduction_text, path_string,fileName_string)
    