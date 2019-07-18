import requests
import json
import re

from . import G3tsCrawler
from ..exception import TextToSpeechNotSuccesfullException
from ..utils import File

class G3tsSpeechCrawler( G3tsCrawler ):

    TEXT_TO_SPEECH_PATH = 'translate_tts'

    MINIMUM_SPEED = 0.3
    NORMAL_SPEED = 1

    def __init__( self ):
        
        super().__init__()

        # idx parameter

        self.idx = ''

        # textlen parameter

        self.textlen = None

        # prev parameter

        self.prev = 'input'

        # ttsspeed parameter

        self.ttsspeed = str( G3tsSpeechCrawler.NORMAL_SPEED )

    def setSpeed( self, speed ):
        
        if speed > G3tsSpeechCrawler.NORMAL_SPEED :

            self.ttsspeed = str( G3tsSpeechCrawler.NORMAL_SPEED )

        elif speed < G3tsSpeechCrawler.MINIMUM_SPEED :

            self.ttsspeed = str( G3tsSpeechCrawler.MINIMUM_SPEED )

        else:

            if isinstance( speed, ( int, float ) ) :

                self.ttsspeed = str( speed )

            else:

                self.ttsspeed = speed

    def generateURL( self ):
        
        queryParams = ''

        if not self.client == None :

            queryParams = queryParams  + '&client=' + self.client

        if not self.inputEnconding == None :

            queryParams = queryParams  + '&ie=' + self.inputEnconding

        if not self.outputEnconding == None :

            queryParams = queryParams  + '&oe=' + self.outputEnconding

        if not self.ttsspeed == None :

            queryParams = queryParams  + '&ttsspeed=' + self.ttsspeed

        if not self.query == None :

            queryParams = queryParams  + '&q=' + self.query

        if not self.translationLanguage == None :

            queryParams = queryParams  + '&tl=' + self.translationLanguage

        if not self.idx == None :

            queryParams = queryParams  + '&idx=' + self.idx

        if not self.textlen == None :

            queryParams = queryParams  + '&textlen=' + self.textlen

        if not self.tk == None :

            queryParams = queryParams  + '&tk=' + self.tk

        if not self.prev == None :

            queryParams = queryParams  + '&prev=' + self.prev

        queryParamsLenght = len( queryParams )

        queryParams = queryParams[ 1 : queryParamsLenght ]

        textToSpeechURL = G3tsCrawler.BASE_URL + '/' + G3tsSpeechCrawler.TEXT_TO_SPEECH_PATH + '?' + queryParams

        return textToSpeechURL

    def speech( self, text, speed = 1 ):
        
        self.setSpeed( speed )

        self.setQuery( text )
        
        self.textlen = str( len( text ) )

        self.generateTk()

        textToSpeechURL = self.generateURL()

        translation = requests.get( textToSpeechURL )

        if translation.status_code != 200 :
            
            raise TextToSpeechNotSuccesfullException( 'Text-to-Speech was not successfull.' )

        audioFile = File( translation.content )

        return audioFile

