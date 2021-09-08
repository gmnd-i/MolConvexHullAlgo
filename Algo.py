class Point:
    def __init__(self, X, Y):
        self.X = X;
        self.Y = Y;

def orientation(p, q, r):
    val = (q.Y - p.Y) * (r.X - q.X) -  (q.X - p.X) * (r.Y - q.Y);
    if val == 0:
        return 0; 	# colinear
    # return (val > 0)? 1: 2;     # clock or counterclock wise
    if val > 0:
        return 1;
    elif val < 0:
        return 2;

def convexHull(points):
    if len(points) < 3:
        return;
    
    hull = list();
    leftest_point = points[0];

    # find the leftest point
    for p in points:
        if p.X < leftest_point.X:
            leftest_point = p;
    # remove the leftmost point from the points list
    points.remove(leftest_point);

    hull.append(leftest_point);
    
