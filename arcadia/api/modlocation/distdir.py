from math import radians, cos, sin, asin, sqrt, atan2, degrees

def bearingToCardinal(bearing):
    if 22.5 > bearing and bearing > 0:
        cardinal = 'N'
    elif 67.5 > bearing and bearing > 22.5:
        cardinal = 'NE'
    elif 112.5 > bearing and bearing > 67.5:
        cardinal = 'E'
    elif 157.5 > bearing and bearing > 112.5:
        cardinal = 'SE'
    elif 202.5 > bearing and bearing > 157.5:
        cardinal = 'S'
    elif 247.5 > bearing and bearing > 202.5:
        cardinal = 'SW'
    elif 292.5 > bearing and bearing > 247.5:
        cardinal = 'W'
    elif 337.5 > bearing and bearing > 292.5:
        cardinal = 'NW'
    elif bearing > 337.5:
        cardinal = 'N'
    return cardinal

def dist(lat1, long1, lat2, long2) -> int:
    """Returns distance IN METERS

    Args:
        lat1 (int): lat 1
        long1 (int): long 1
        lat2 (int): lat 2
        long2 (int): long2

    Returns:
        int: Distance in meters
    """

    R = 6372.8 

    dLat = radians(lat2 - lat1)
    dLon = radians(long2 - long1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
    c = 2*asin(sqrt(a))

    return R * c * 1000 # meters?

def direc(lat1, long1, lat2, long2):
    dLon = (long2 - long1)
    x = cos(radians(lat2)) * sin(radians(dLon))
    y = cos(radians(lat1)) * sin(radians(lat2)) - sin(radians(lat1)) * cos(radians(lat2)) * cos(radians(dLon))
    bearing = atan2(x,y)   # use atan2 to determine the quadrant
    bearing = degrees(bearing)

    return (bearing%360)

if __name__ == '__main__':
    print(dist(53.4808, 2.2426, 51.5072, 0.1276))
    print(direc(53.4808, 2.2426, 51.5072, 0.1276))