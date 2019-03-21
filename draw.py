from display import *
from matrix import *

  # ====================
  # add the points for a rectagular prism whose
  # upper-left corner is (x, y, z) with width,
  # height and depth dimensions.
  # ====================
def add_box( points, x, y, z, width, height, depth ):
    # [b]ack[u]pper[l]eft
    # [f]ront[b]ottom[r]ight
    bul = [x,y,z]
    bur = [x + width, y, z]
    bbl = [x, y - height, z]
    bbr = [x + width, y - height, z]
    ful = [x,y, z-depth]
    fur = [x + width, y, z-depth]
    fbl = [x, y - height, z-depth]
    fbr = [x + width, y - height, z-depth]
    add_edge(points, bul[0], bul[1], bul[2], bur[0],bur[1],bur[2])
    add_edge(points, bur[0], bur[1], bur[2], bbr[0],bbr[1],bbr[2])
    add_edge(points, bbr[0], bbr[1], bbr[2], bbl[0],bbl[1],bbl[2])
    add_edge(points, bbl[0], bbl[1], bbl[2], bul[0],bul[1],bul[2])

    add_edge(points, bul[0], bul[1], bul[2], ful[0],ful[1],ful[2])
    add_edge(points, bur[0], bur[1], bur[2], fur[0],fur[1],fur[2])
    add_edge(points, bbr[0], bbr[1], bbr[2], fbr[0],fbr[1],fbr[2])
    add_edge(points, bbl[0], bbl[1], bbl[2], fbl[0],fbl[1],fbl[2])

    add_edge(points, ful[0], ful[1], ful[2], fur[0],fur[1],fur[2])
    add_edge(points, fur[0], fur[1], fur[2], fbr[0],fbr[1],fbr[2])
    add_edge(points, fbr[0], fbr[1], fbr[2], fbl[0],fbl[1],fbl[2])
    add_edge(points, fbl[0], fbl[1], fbl[2], ful[0],ful[1],ful[2])


def cos (angle):
    return math.cos(angle)


def sin (angle):
    return math.sin(angle)

  # ====================
  # Generates all the points along the surface
  # of a torus with center (cx, cy, cz) and
  # radii r0 and r1.
  # Returns a matrix of those points
  # ====================
def generate_torus( points, cx, cy, cz, r0, r1, step ):
    torus = []
    counter = 1
    while (counter <= step):
        phi = (float(counter)/step) * 2 * math.pi
        i = 1
        while (i <= step):
            t = (float(i)/step) * 2 * math.pi
            tr0 = r0 * cos(t)
            x = cx + ((tr0 + r1) * cos(phi))
            y = cy + (r0 * sin(t))
            z = cz + ((tr0 + r1) * -sin(phi))
            torus.append([x,y,z])
            i += 1
        counter += 1
    return torus


  # ====================
  # adds all the points for a torus with center
  # (cx, cy, cz) and radii r0, r1 to points
  # should call generate_torus to create the
  # necessary points
  # ====================
def add_torus( points, cx, cy, cz, r0, r1, step ):
    torus = generate_torus(points, cx, cy, cz, r0, r1, step)
    # print torus
    i = 0
    while (i < len(torus)):
        add_edge(points, torus[i][0], torus[i][1], torus[i][2], torus[i][0], torus[i][1], torus[i][2])
        i +=1

  # ====================
  # adds all the points for a sphere with center
  # (cx, cy, cz) and radius r to points
  # should call generate_sphere to create the
  # necessary points
  # ====================
def add_sphere( points, cx, cy, cz, r, step ):
    sphere = generate_sphere(points, cx, cy, cz, r, step)
    # print sphere
    i = 0
    while (i < len(sphere)):
        add_edge(points, sphere[i][0], sphere[i][1], sphere[i][2], sphere[i][0], sphere[i][1], sphere[i][2])
        i +=1


  # ====================
  # Generates all the points along the surface
  # of a sphere with center (cx, cy, cz) and
  # radius r.
  # Returns a matrix of those points
  # ====================
def generate_sphere( points, cx, cy, cz, r, step ):
    #print("generate sphere!!!")
    pi = math.pi
    points = []
    rotation = 0
    revolution = 0
    while (rotation < step):
        rot = rotation/float(step)
        for semicircle in range(revolution, step+1):
            circle = semicircle/float(step)
            x = cx + r * cos(pi * circle)
            y = cy + r * sin(pi * circle) * cos(2 * pi * rot)
            z = cz + r * sin(pi * circle) * sin(2 * pi * rot)
            # print (str(x))
            # print (str(y))
            # print (str(z))
            points.append([x, y, z])
        rotation +=1
    return points

def add_circle( points, cx, cy, cz, r, step ):
    x0 = r + cx
    y0 = cy
    tpi = 2*math.pi
    i = 1
    while (i <= step):
        t = float(i)/step
        x1 = r * cos(tpi * t) + cx;
        y1 = r * sin(tpi * t) + cy;
        add_edge(points, x0, y0, cz, x1, y1, cz)
        x0 = x1
        y0 = y1
        t+= step

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):

    xcoefs = generate_curve_coefs(x0, x1, x2, x3, curve_type)[0]
    ycoefs = generate_curve_coefs(y0, y1, y2, y3, curve_type)[0]

    i = 1
    while i <= step:
        t = float(i)/step
        x = t * (t * (xcoefs[0] * t + xcoefs[1]) + xcoefs[2]) + xcoefs[3]
        y = t * (t * (ycoefs[0] * t + ycoefs[1]) + ycoefs[2]) + ycoefs[3]
        #x = xcoefs[0] * t*t*t + xcoefs[1] * t*t + xcoefs[2] * t + xcoefs[3]
        #y = ycoefs[0] * t*t*t + ycoefs[1] * t*t + ycoefs[2] * t + ycoefs[3]

        add_edge(points, x0, y0, 0, x, y, 0)
        x0 = x
        y0 = y
        t+= step


def draw_lines( matrix, screen, color ):
    if len(matrix) < 2:
        print 'Need at least 2 points to draw'
        return

    point = 0
    while point < len(matrix) - 1:
        draw_line( int(matrix[point][0]),
                   int(matrix[point][1]),
                   int(matrix[point+1][0]),
                   int(matrix[point+1][1]),
                   screen, color)
        point+= 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )


def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line
