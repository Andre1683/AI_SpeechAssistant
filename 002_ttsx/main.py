from loguru import logger
import pyttsx3
import logging
from TTS import Voice
import multiprocessing

# Unterdrücke Logausgaben der Hintergrunddienste von pyttsx3
logging.getLogger('comtypes._comobject').setLevel(logging.WARNING)

class VoiceAssistant():
    def __init__(self):
        logger.info("Initialisiere VoiceAssistant")
        
        logger.info("Initialisiere Sprachausgabe")
        self.tts = Voice()
        voices= self.tts.get_voice_keys_by_language("German")
        if len(voices) > 0:
            logger.info('Stimme {} getestet.', voices[0])
            self.tts.set_voice(voices[0])
        else:
            logger.warning("Es wurden keine Stimmen gefunden.")
        self.tts.say("Initialisierung abgeschlosse")
        logger.debug("Sprachausgabe initialisiert")
        
    def run(self):
        logger.info("VoiceAssistant Instanz wurde gestartet.")
        self.tts.say("Ich bin bereit");
        self.tts.runAndWait();
        
if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    
    va=VoiceAssistant()
    logger.info("Anwendung wurde gestartet")
    va.run()