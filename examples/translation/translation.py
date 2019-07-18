
import importlib

# Search for installed module 

g3ts = importlib.util.find_spec( 'g3ts' )

# If not installed, load from local

if g3ts is None :

    import sys, os

    sys.path.append( os.path.abspath('.') )

    from g3ts import G3tsTranslationCrawler
    from g3ts.exception import TranslationNotSuccesfullException

# Create a G3ts Translation Crawler

g3ts = G3tsTranslationCrawler()

# Set source language

g3ts.setSourceLanguage( 'en' )

# Set translation language

g3ts.setTranslationLanguage( 'pt' )

# Translate

text = 'Let\'s go to work!'

try:
    
    translation = g3ts.translate( text )

    print( translation )

except TranslationNotSuccesfullException as e :

    print( e )