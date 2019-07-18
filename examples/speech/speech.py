import importlib

# Search for installed module 

g3ts = importlib.util.find_spec( 'g3ts' )

# If not installed, load from local

if g3ts is None :

    import sys, os

    sys.path.append( os.path.abspath('.') )

    from g3ts import G3tsSpeechCrawler

    from g3ts.exception import TextToSpeechNotSuccesfullException


# Create a G3ts Translation Crawler

g3ts = G3tsSpeechCrawler()

# Set translation language

g3ts.setTranslationLanguage( 'en' )

text = 'Let\'s go to work!'

path = os.path.dirname( os.path.abspath( __file__ ) )

# Text-to-Speech

try:

    speech = g3ts.speech( 'Let\'s go to work')

    speech.setName( 'normal.mp3' )

    speech.save( path )

    speech = g3ts.speech( 'Let\'s go to work', 0.3 )

    speech.setName( 'slow.mp3' )

    speech.save( path )

except TextToSpeechNotSuccesfullException as e :

    print( e )