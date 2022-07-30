import crcmod
from datetime import datetime


crc32_func = crcmod.mkCrcFun(0x104c11db7, initCrc=0, xorOut=0xFFFFFFFF)

def findPOICoords(xloc:int , yloc: int) -> list[dict[str,float]]:
    """This function will return the 3 nearest Park coordinates. Currently not querying OSM.

    Args:
        xloc (int): The X coord
        yloc (int): The Y coord

    Returns:
        list[dict[str,float]]: list of dicts, where dicts contain key x and x coord, and key y and y coord.
    """
    return  [
        {"x": 51.370967, "y": -0.367160}, 
        {"x": 51.364901, "y": -0.354071}, 
        {"x": 51.379019, "y": -0.350626}
    ]


def findGameCoords(xloc:int , yloc: int):

    nearCoords = findPOICoords(xloc,yloc)  # replace this with osm data

    for coord in nearCoords:
        
        arcadeid = generateArcadeID(coord["x"],coord["y"])
        gametype = getGameType(arcadeid=arcadeid)
        
        getOffsets()

        #Generate circle center here


    return [
        {"x": 51.370967, "y": -0.367160, "id": 1233123, "gametype": 2}, 
        {"x": 51.364901, "y": -0.354071}, 
        {"x": 51.379019, "y": -0.350626}
    ]

def getOffsets(arcadeid: int) -> tuple[int, int,  int,  int]:
    """This function generates offsets for an arcade. The offsets will change every day.
    note that the radiusOffset is to be added to the arcade offset.

    Args:
        arcadeid (int): The id of the arcade

    Returns:
        tuple[int, int,  int,  int]: arcadeOffsetX, arcadeOffsetY, radiusOffsetX, radiusOffsetY
        These are all 5 bit numbers, in the range of -16 to 16
    """
        
    now = datetime.now()
    datestr = now.strftime("%Y%m%d") # will change daily (without repeating)
    rnd = crc32_func(str(hex(arcadeid) + datestr).encode("utf-8"))
    # This is used to generate offsets. This is hashed WITH DATE, so will be different every day.
    
    arcadeOffsetX = ((rnd >> 1) & 0b11111) - 16
    arcadeOffsetY = ((rnd >> 6) & 0b11111) - 16
    radiusOffsetX = ((rnd >> 11) & 0b11111) - 16
    radiusOffsetY = ((rnd >> 16) & 0b11111) - 16

    return arcadeOffsetX, arcadeOffsetY, radiusOffsetX, radiusOffsetY

def getGameType(arcadeid: int):
    """Generates the type of game that is playable at an arcade. it is always constant.

    Args:
        arcadeid (int): The id of the arcade
    """
    return ((arcadeid >> 19) & 0b11) 
    

def generateArcadeID(xloc:int,yloc:int) -> int: 
    """arcadeid represents the id of an arcade. There is one arcade per park, and the arcadeid is wholly 
    dependent on the x and y coordinates of the park. The arcadeid is always constant for a given park

    Args:
        xloc (int): The X Coordinate
        yloc (int): The Y

    Returns:
        int: The arcadeid
    """
    return crc32_func(str(xloc)+str(yloc).encode("utf-8"))