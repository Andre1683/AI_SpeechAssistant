from loguru import logger
import sys

logger.remove()
logger.add(sys.stdout, level="INFO")

class VoiceAssistant:
    
    def __init__(self):
        logger.error("VoiceAssistant wird initialisiert.")
    def run(self):
        logger.debug("Los geht´s!")
if __name__ == "__main__":
    va=VoiceAssistant()
    va.run()
    logger.info("Gestartet.")
