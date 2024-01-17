class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w  # Distance from center to boundary - Actual width/2
        self.h = h

    def contains(self, point):
        contain =  (point.x >= self.x-self.w and point.x <= self.x + self.w and point.y >= self.y - self.h and point.y <= self.y + self.h)  # Check if Rectangle contains point
        return contain
    def draw(self, canvas):
        canvas.create_rectangle(self.x-self.w,self.y-self.h, self.x+self.w, self.y+self.h, outline = 'white' , width = 1)

class QuadTree:
    def __init__(self, boundary, n):
        self.boundary = boundary  # Rectangle
        self.capacity = n
        self.points = []
        self.subdivided = False

    def subdivide(self):
        x = self.boundary.x
        y = self.boundary.y
        w = self.boundary.w
        h = self.boundary.h
        # Create 4 quadrants which QuadTree divides into
        tr = Rectangle(x + w/2, y - h/2, w/2, h/2)
        tl = Rectangle(x - w/2, y - h/2, w/2, h/2)
        bl = Rectangle(x - w / 2, y + h / 2, w / 2, h / 2)
        br = Rectangle(x + w / 2, y + h / 2, w / 2, h / 2)
        # Define each quadrant as another QuadTree
        self.topright = QuadTree(tr, self.capacity)
        self.topleft = QuadTree(tl, self.capacity)
        self.bottomleft = QuadTree(bl, self.capacity)
        self.bottomright = QuadTree(br, self.capacity)
        self.subdivided = True

    def insert(self, point):
        if not self.boundary.contains(point):
            return False
        elif len(self.points) < self.capacity:
            self.points.append(point)
            return True
        elif not self.subdivided:
            self.subdivide()
            return True
        return (self.topleft.insert(point) or
                self.topright.insert(point) or
                self.bottomleft.insert(point) or
                self.bottomright.insert(point))

    def display(self, canvas):
        self.boundary.draw(canvas)
        # canvas.create_rectangle(self.boundary.x-self.boundary.w,self.boundary.y-self.boundary.h, self.boundary.w*2, self.boundary.h*2, outline = 'black' , width = 2)
        if self.subdivided:
            self.topleft.display(canvas)
            self.topright.display(canvas)
            self.bottomleft.display(canvas)
            self.bottomright.display(canvas)
