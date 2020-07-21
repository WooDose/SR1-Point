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
        #print(self.framebuffer)
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
        self.clearColor = color(int(r*255),int(g*255),int(b*255))

    def glColor(self, r,g,b):
        self.drawColor = color(int(r*255),int(g*255),int(b*255))

    def point(self,x,y):
        self.framebuffer[x][y] = self.drawColor
    
    def line(self, x1, y1, x2, y2):
        dy = abs(y2 - y1)
        #print(y2,y1)
        dx = abs(x2 - x1)
        # print(x2,x1)
        # print(dx)
        steep = dy > dx

        if steep:
            x1, y1 = y1, x1
            x2, y2 = y2, x2

        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        # print(x1,x2,y1,y2)

        offset =  0 * 2 * dx
        threshold = 0.5 * 2 * dx
        y = y1

        points = []
        # print( x1,x2)
        for x in range(x1, x2 + 1):
            # print (x, y)
            if steep:
                points.append((y, x))
            else:
                points.append((x, y))
            
            #print(dy)
            offset += (dx if steep else dy) * 2
            # print(offset, threshold, y )
            if offset > threshold:
                y += 1 if y1 < y2 else -1
                threshold += 1 * 2 * dx

        for point in points:
            self.point(point[0], point[1])

    def glVertex(self, x,y): 
        xW = int(((x+1)*(self.ViewportWidth/2))+self.xNormalized)
        #print(xW)
        yW = int(((y+1)*(self.ViewportHeight/2))+self.yNormalized)
        xW = (xW - 1) if xW == self.width else xW
        yW = (yW - 1) if yW == self.height else yW
        self.point(xW, yW)

    def glLine(self, x0,y0,x1,y1):
        x0W = ((x0+1)*(self.ViewportWidth/2))+self.xNormalized
        # print(x0W)
        x0W = int(x0W)
        x1W = ((x1+1)*(self.ViewportWidth/2))+self.xNormalized
        # print(x1W)
        x1W = int(x1W)
        y0W = int(((y0+1)*(self.ViewportHeight/2))+self.yNormalized)
        y1W = int(((y1+1)*(self.ViewportHeight/2))+self.yNormalized)
        # print(x0W, x1W, y0W, y1W)
        x0W = (x0W - 1) if x0W == self.width else x0W
        x1W = (x1W - 1) if x1W == self.width else x1W
        y0W = (y0W - 1) if y0W == self.height else y0W
        y1W = (y1W - 1) if y1W == self.height else y1W
        self.line(x0W, y0W, x1W, y1W)

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
        
        #print(self.framebuffer)
        for x in range(self.height):
            for y in range(self.width):
                f.write(self.framebuffer[y][x])
        f.close()
    
    def point(self,x,y):
        self.framebuffer[x][y] = self.drawColor

##Please for the love of God don't use non-4 multiples for your dimensions unless you want to absoultely do you know what to your you know what.

bitmap = Render(80,80,80,80, 0, 0)
# for x in range(20, 30):
#     for y in range(20, 30):
#         bitmap.glVertex(x, y)
# bitmap.glVertex(0,0)
bitmap.glColor(0, 0.5, 0.75)
bitmap.glLine(-1, 0.25, 1, -0.25)
bitmap.glColor(1, 0, 0)
bitmap.glLine(1, 1, 0, 0)
bitmap.glColor(0, 1, 0)
bitmap.glLine(-1, -1, 0, 0)
bitmap.glColor(1,1,1)
bitmap.glLine(-1,0.33,0.33,-1)
bitmap.glColor(0.25, 0.37, 0.86)
bitmap.glLine(-1, 0, 1, 0)
bitmap.glColor(0.75, 0.37, 0.86)
bitmap.glLine(0, -1, 0, 1)
bitmap.glColor(0.10, 0.10, 0.50)
bitmap.glLine(0, 1, 0, -0)
bitmap.glFinish(r'woodoseline.bmp')
