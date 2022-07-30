import crcmod
from datetime import datetime
from math import pi, cos
crc32_func = crcmod.mkCrcFun(0x104c11db7, initCrc=0, xorOut=0xFFFFFFFF)

earthRadius = 6378137

arcadeScale = 100 / 16  # 100m
circleScale = 100 / 16


def findPOICoords(xloc: int, yloc: int) -> list[dict[str, float]]:
    """This function will return the 3 nearest Park coordinates. Currently not querying OSM.

    Args:
        xloc (int): The X coord
        yloc (int): The Y coord

    Returns:
        list[dict[str,float]]: list of dicts, where dicts contain key x and x coord, and key y and y coord.
    """
    return [
        {"x": 51.356389, "y": -0.378113},
        {"x": 51.370967, "y": -0.367160},
        {"x": 51.379019, "y": -0.350626}
    ]


def returnNearCoords(xloc: int, yloc: int):

    nearCoordsList = findPOICoords(xloc, yloc)  # replace this with osm data

    out = []
    for coords in nearCoordsList:

        arcadeid = generateArcadeID(xloc=coords["x"], yloc=coords["y"])
        gametype = getGameType(arcadeid=arcadeid)

        cxloc, cyloc = getCircleCoords(coords["x"],coords["y"])
        
        out.append({"circlelat":round(cxloc,6), "circlelong":round(cyloc,6), "poilat":xloc, "poilong":yloc, "id": arcadeid, "gametype": gametype})

    return out
    return [
        {"lat": 51.370967, "long": -0.367160, "id": 1233123, "gametype": 2},
        {"lat": 51.364901, "long": -0.354071},
        {"lat": 51.379019, "long": -0.350626}
    ]

def coordOffsetter(xloc: int,yloc:int, mox:int, moy:int) -> tuple[float, float]:
    """Will generate coordinate offsets, given x and y coords, and offsets in meters

    Args:
        xloc (int): X coord
        yloc (int): Y coord
        mox (int): meter offset x
        moy (int): meter offset y

    Returns:
        tuple[float, float]: the new x location and new y location
    """
    
    dX = mox/earthRadius  # Coordinate Offsets (Radians!)
    dY = moy/(earthRadius*cos(pi*xloc/180))

    newxloc = xloc + dY * 180/pi  # New Positions (decimal degrees)
    newyloc = yloc + dX * 180/pi
    
    return newxloc, newyloc
    

def getArcadeCoords( xloc: int, yloc: int):
    aoX, aoY, _, _ = getRawOffsets(generateArcadeID(xloc, yloc))

    meter_aoX = aoX * arcadeScale  # Offsets in meters
    meter_aoY = aoY * arcadeScale

    
    arcadexloc, arcadeyloc = coordOffsetter(xloc, yloc, meter_aoX, meter_aoY)

    
    return arcadexloc, arcadeyloc


def getCircleCoords(xloc, yloc):     # relies on arcade coord

    arcadexloc, arcadeyloc = getArcadeCoords( xloc, yloc)
    
    _, _, roX, roY = getRawOffsets(generateArcadeID(xloc, yloc))
    
    meter_roX = roX * circleScale  # Offsets in meters
    meter_roY = roY * circleScale
    circlexloc, circleyloc = coordOffsetter(arcadexloc, arcadeyloc, meter_roX, meter_roY)
    return circlexloc, circleyloc


def getRawOffsets(arcadeid: int) -> tuple[int, int,  int,  int]:
    """This function generates raw offsets for an arcade. The offsets will change every day.
    note that the radiusOffset is to be added to the arcade offset.

    Args:
        arcadeid (int): The id of the arcade

    Returns:
        tuple[int, int,  int,  int]: arcadeOffsetX, arcadeOffsetY, radiusOffsetX, radiusOffsetY
        These are all 5 bit numbers, in the range of -16 to 16
    """

    now = datetime.now()
    datestr = now.strftime("%Y%m%d")  # will change daily (without repeating)
    rnd = crc32_func(str(hex(arcadeid) + datestr + "SECRETKEY").encode("utf-8"))
    # This is used to generate offsets. This is hashed WITH DATE, so will be different every day.

    arcadeOffsetX = ((rnd >> 1) & 0b11111) - 16
    arcadeOffsetY = ((rnd >> 6) & 0b11111) - 16
    radiusOffsetX = ((rnd >> 11) & 0b11111) - 16
    radiusOffsetY = ((rnd >> 16) & 0b11111) - 16

    return arcadeOffsetX, arcadeOffsetY, radiusOffsetX, radiusOffsetY


def getGameType(arcadeid: int):
    """Generates the type of game that is playable at an arcade. it is always constant for 
    a given arcade.

    Args:
        arcadeid (int): The id of the arcade
    """
    return ((arcadeid >> 19) & 0b11)


def generateArcadeID(xloc: int, yloc: int) -> int:
    """arcadeid represents the id of an arcade. There is one arcade per park, and the arcadeid is wholly 
    dependent on the x and y coordinates of the park. The arcadeid is always constant for a given park

    Args:
        xloc (int): The X Coordinate
        yloc (int): The Y

    Returns:
        int: The arcadeid
    """
    return crc32_func((str(xloc)+str(yloc)).encode("utf-8"))
