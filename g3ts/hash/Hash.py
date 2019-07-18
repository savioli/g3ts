class Hash() :
    """ This class contains logic used in py-googletrans:
        https://github.com/ssut/py-googletrans/blob/94bd300e756ee1eb0ab7e1ffe6a68c0fedfbe2ef/googletrans/gtoken.py.
    """

    def _xr( self, a, b ) :

        size_b = len( b )

        c = 0

        while c < size_b - 2 :
            
            d = b[ c + 2 ]
            
            d = ord( d[ 0 ] ) - 87 if 'a' <= d else int( d )
            
            d = ( a >> d ) if '+' == b[ c + 1 ] else a << d
            
            a = a + d & 4294967295 if '+' == b[ c ] else a ^ d

            c += 3

        return a

    def hash( self, tkk, text ) :

        a = []

        for i in text :

            val = ord( i )

            if val < 0x10000 :

                a += [ val ]

            else :

                a += [ math.floor((val - 0x10000)/0x400 + 0xD800),
                       math.floor((val - 0x10000)%0x400 + 0xDC00) ]

        b = tkk if tkk != '0' else ''
        d = b.split('.')
        b = int(d[0]) if len(d) > 1 else 0

        e = []
        g = 0
        size = len(text)

        while g < size :
        
            l = a[ g ]
        
            if l < 128 :
        
                e.append( l )
        
            else :
        
                if l < 2048 :
        
                    e.append( l >> 6 | 192 )
        
                else :
                
                    if ( l & 64512 ) == 55296 and g + 1 < size and a[ g + 1 ] & 64512 == 56320 :
        
                        g += 1
        
                        l = 65536 + ( ( l & 1023 ) << 10 ) + ( a[ g ] & 1023 )
                        
                        e.append( l >> 18 | 240 )
                        
                        e.append( l >> 12 & 63 | 128 )

                    else :

                        e.append( l >> 12 | 224 )

                    e.append( l >> 6 & 63 | 128 )

                e.append( l & 63 | 128 )

            g += 1

        a = b

        for i, value in enumerate( e ) :

            a += value

            a = self._xr( a, '+-a^+6' )

        a = self._xr( a, '+-3^+b+-f' )

        a ^= int( d[ 1 ] ) if len( d ) > 1 else 0

        if a < 0 :

            a = ( a & 2147483647 ) + 2147483648

        a %= 1000000

        return '{}.{}'.format( a, a ^ b )