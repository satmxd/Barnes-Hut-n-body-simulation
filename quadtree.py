

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mass = 1

class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w  # Distance from center to boundary - Actual width/2
        self.h = h
        self.points = []
        self.mass = 0

    def contains(self, point):
        return (point.x >= self.x-self.w and point.x < self.x + self.w and point.y >= self.y - self.h and point.y < self.y + self.h)  # Check if Rectangle contains point

    def intersects(self, range):
        return not(range.x - range.w > self.x + self.w or
                   range.x + range.w < self.x - self.w or
                   range.y - range.h > self.y + self.h or
                   range.y + range.h < self.y - self.h)
    def draw(self, canvas, depth, mass):
        canvas.create_rectangle(self.x-self.w,self.y-self.h, self.x+self.w, self.y+self.h, outline = 'white' , width = 1)
        canvas.create_text(self.x-20, self.y, text = depth, fill = 'white')
        canvas.create_text(self.x+20, self.y, text = mass, fill = 'white')


class QuadTree:
    def __init__(self, boundary, n, depth):
        self.boundary = boundary  # Rectangle
        self.capacity = n
        self.points = []
        self.subdivided = False
        self.depth = depth
        self.count = 0
        self.com_x = 0
        self.com_y = 0
        self.mass = 0
        self.parent = None

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
        self.topright = QuadTree(tr, self.capacity, self.depth+'B')
        self.topleft = QuadTree(tl, self.capacity, self.depth+'A')
        self.bottomleft = QuadTree(bl, self.capacity, self.depth+'C')
        self.bottomright = QuadTree(br, self.capacity, self.depth+'D')
        self.topright.parent = self.topleft.parent = self.bottomleft.parent = self.bottomright.parent = self
        for i in range(len(self.points)):
            self.topright.insert(self.points[i])
            self.topleft.insert(self.points[i])
            self.bottomleft.insert(self.points[i])
            self.bottomright.insert(self.points[i])
        self.subdivided = True


    def insert(self, point):
        if not self.boundary.contains(point):
            return False
        if len(self.points) < self.capacity:
            self.points.append(point)
            return True
        else:
            if not self.subdivided:
                self.subdivide()
            return (self.topright.insert(point) or
                    self.topleft.insert(point) or
                    self.bottomright.insert(point) or
                    self.bottomleft.insert(point))

    def query(self, range, found_points):
        if not self.boundary.intersects(range):
            return
        for point in self.points:
            if range.contains(point):
                found_points.append(point)

        if self.subdivided:
            self.topright.query(range, found_points)
            self.topleft.query(range, found_points)
            self.bottomright.query(range, found_points)
            self.bottomleft.query(range, found_points)
        return found_points

    # def calculate_mass(self):
    #     #self.mass = len(self.query(self.boundary, []))
    #     if self.subdivided:
    #         trm = self.topright.mass = len(self.query(self.topright.boundary, []))
    #         tlm = self.topleft.mass = len(self.query(self.topleft.boundary, []))
    #         brm = self.bottomright.mass = len(self.query(self.bottomright.boundary, []))
    #         blm = self.bottomleft.mass = len(self.query(self.bottomleft.boundary, []))
    #         self.mass = trm+tlm+brm+blm
    #     else:
    #         print(self.points)
    #         #self.mass = len(self.points)

    def __len__(self):
        mass = len(self.points)
        if self.subdivided:
            mass = len(self.topright) + len(self.topleft) + len(self.bottomright) + len(self.bottomleft)
        return mass


    def display(self, canvas):
        self.boundary.draw(canvas, self.depth, len(self))
        #print(self.depth, self.points)
        if self.subdivided:
            self.topleft.display(canvas)
            self.topright.display(canvas)
            self.bottomleft.display(canvas)
            self.bottomright.display(canvas)
            #print(f'tl: {len(self.topleft)},  tr: {len(self.topright)}, bl: {len(self.bottomleft)}, br: {len(self.bottomright)}')

