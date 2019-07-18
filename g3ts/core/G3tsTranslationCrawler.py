import requests
import json
import ast
import re

from . import G3tsCrawler
from ..exception import TranslationNotSuccesfullException

class G3tsTranslationCrawler( G3tsCrawler ):

    TRANSLATE_PATH = 'translate_a/single'

    def __init__( self ):
        
        super().__init__()
        
        # sl query parameter

        self.sourceLanguage = None 
                
        # dt parameters
        
        self.dt = [ 'at', 
                    'bd', 
                    'ex', 
                    'ld', 
                    'md', 
                    'qca',
                    'rw',
                    'rm',
                    'ss',
                    't', 
                    'gt' ]

        # otf parameter

        self.otf = '1'

        # ssel parameter

        self.ssel = '0'

        # tsel parameter

        self.tsel = '0'
        
        # kc parameter

        self.kc = '1'

    def generateURL( self ):

        queryParams = ''

        if not self.client == None :

            queryParams = queryParams  + '&client=' + self.client

        if not self.inputEnconding == None :

            queryParams = queryParams  + '&ie=' + self.inputEnconding

        if not self.outputEnconding == None :

            queryParams = queryParams  + '&output=' + self.inputEnconding

        if not self.sourceLanguage == None :

            queryParams = queryParams  + '&sl=' + self.sourceLanguage

        if not self.translationLanguage == None :

            queryParams = queryParams  + '&tl=' + self.translationLanguage

        if not self.homeLanguage == None :

            queryParams = queryParams  + '&hl=' + self.homeLanguage

        for dt in self.dt :

            queryParams = queryParams  + '&dt=' + dt

        if not self.otf == None :

            queryParams = queryParams  + '&otf=' + self.otf

        if not self.ssel == None :

            queryParams = queryParams  + '&ssel=' + self.ssel

        if not self.tsel == None :

            queryParams = queryParams  + '&tsel=' + self.tsel

        if not self.kc == None :

            queryParams = queryParams  + '&kc=' + self.kc

        if not self.tk == None :

            queryParams = queryParams  + '&tk=' + self.tk

        if not self.query == None :

            queryParams = queryParams  + '&q=' + self.query

        queryParamsLenght = len( queryParams )

        queryParams = queryParams[ 1 : queryParamsLenght ]

        translationURL = G3tsCrawler.BASE_URL + '/' + G3tsTranslationCrawler.TRANSLATE_PATH + '?' + queryParams

        return translationURL

    def translate( self, text ):

        self.setQuery( text )

        self.generateTk()

        translationURL = self.generateURL()

        translation = requests.get( translationURL )

        if translation.status_code != 200 :
            
            raise TranslationNotSuccesfullException( 'Translation was not successfull.' )

        translation = translation.content.decode( 'utf8' )

        translation = json.loads( translation )

        return translation
