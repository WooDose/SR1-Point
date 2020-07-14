import struct
import pprint
def char(c):
    return struct.pack('=c', c.encode('ascii'))

def word(c):
    return struct.pack('=h', c)

def dword(c):
    return struct.pack('=l', c)

def color(r, g, b):
    return bytes([b, g, r])

class Render(object):
    def __init__(self, width, height, vpw, vph, vpx, vpy):
        self.width = width
        self.height = height
        self.framebuffer = []
        self.clearColor = color(0,0,0)
        self.glCreateWindow()
        self.glViewport(vpw, vph, vpx, vpy)
        self.drawColor = color(0,0,0)
        self.glClear()

    def glInit(self):
        pass
    
    def glCreateWindow(self):
        print(self.framebuffer)
        self.framebuffer = [
            [self.clearColor for x in range(self.width)]
             for y in range(self.height)
        ]
        #pprint.pprint(self.framebuffer)
    
    def glViewport(self, width, height, x, y):
        self.ViewportWidth = width
        self.ViewportHeight = height
        self.xNormalized = x
        self.yNormalized = y


    def glClear(self):
        self.framebuffer = [
            [self.clearColor for x in range(self.width)]
             for y in range(self.height)
        ]

    def glClearColor(self, r,g,b):
        self.clearColor = color(r,g,b)

    def glColor(self, r,g,b):
        self.drawColor = color(r,g,b)

    def point(self,x,y):
        self.framebuffer[x][y] = self.drawColor

    def glVertex(self, x,y): 
        xW = int(((x+1)*(self.ViewportWidth/2))+self.xNormalized)
        yW = int(((y+1)*(self.ViewportHeight/2))+self.yNormalized)
        self.point(xW, yW)

    def glFinish(self, filename):
        f = open(filename, 'bw')

        ## Write file header
        # Header Field
        f.write(char('B'))
        f.write(char('M'))
        # Size in Bytes
        f.write(dword(14 + 40 + (self.width * self.height * 3)))
        #Reserved
        f.write(word(0))
        f.write(word(0))
        #Offset
        f.write(dword(14 + 40))

        # Image header 
        # Bytes in Header
        f.write(dword(40))
        # Width
        f.write(dword(self.width))
        # Height
        f.write(dword(self.height))
        # Color Planes
        f.write(word(1))
        # Bits/Pixel
        f.write(word(24))
        # Pixel array compression
        f.write(dword(0))
        # Size of raw bitmap
        f.write(dword(self.width * self.height * 3))
        #Colors in palette
        f.write(dword(0))
        #Important Colors
        f.write(dword(0))
        # Unused/Reserved
        f.write(dword(0))
        f.write(dword(0))

        # Pixel data
        
        print(self.framebuffer)
        for x in range(self.height):
            for y in range(self.width):
                f.write(self.framebuffer[y][x])
        f.close()
    
    def point(self,x,y):
        self.framebuffer[x][y] = self.drawColor

##Please for the love of God don't use non-4 multiples for your dimensions unless you want to absoultely do you know what to your you know what.

bitmap = Render(80,80,80,80, 0, 0)
bitmap.glColor(0, 128, 128)
# for x in range(20, 30):
#     for y in range(20, 30):
#         bitmap.glVertex(x, y)
bitmap.glVertex(-0.5,.75) 
bitmap.glFinish(r'woodose.bmp')
