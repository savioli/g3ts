import requests
import json
import re

from ..hash import Hash

class G3tsCrawler():

    BASE_URL = 'https://translate.google.com'

    def __init__( self ):

        self.tkkIsValid = False

        self.hasher = Hash()

        # Common Parameters

        # tkk query parameter

        self.tkk = None

        # client query parameter

        self.client = 'webapp'

        # hl query parameter

        self.homeLanguage = 'en-US' 
        
        # tl query parameter

        self.translationLanguage = None
        
        # tk query parameter

        self.tk = None

        # query parameter
        
        self.query = None

        # ie parameter

        self.inputEnconding = 'UTF-8'

        # oe parameter

        self.outputEnconding = 'UTF-8'

    def setHomeLanguage( self, homeLanguage ):
        
        self.homeLanguage = homeLanguage

    def setSourceLanguage( self, sourceLanguage ):
        
        self.sourceLanguage = sourceLanguage

    def setTranslationLanguage( self, translationLanguage ):
        
        self.translationLanguage = translationLanguage

    def setQuery( self, query ):
        
        self.query = query

    def getTkk( self ):

        getRequest = requests.get( G3tsCrawler.BASE_URL )

        content = getRequest.content

        result = re.findall( '[0-9]{6}[.][0-9]{9,10}', str( content ) )
        
        self.tkk = result[ len( result ) - 1 ]

    def updateTKK( self ):

        if self.tkkIsValid == False :

            self.getTkk()

    def generateTk( self ):

        self.updateTKK()

        self.tk = self.hasher.hash( self.tkk, self.query )
