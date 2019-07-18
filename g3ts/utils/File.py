class File():

    def __init__( self, content ):

        self.content = content

    def setName( self, name ):

        self.name = name

    def save( self, path ):

        fullPath = path + '/' + self.name

        newFile = open( fullPath, 'wb' )

        newFile.write( self.content )
