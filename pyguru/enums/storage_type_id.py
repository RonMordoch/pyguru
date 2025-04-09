from enum import IntEnum


class StorageTypeId(IntEnum):
    ROOM = 1
    SHELF = 21
    CLOSET = 61
    DRAWER = 81
    CAGE = 111
    REFRIGERATOR = 120
    FREEZER = 121
    CRYO_CONTAINER = 201
    SLIDE_RACK = 251
    RACK = 322
    OTHER = 321

    # According to the API documentation, `Rack Cell` has multiple options
    RACK_CELL_181 = 181
    RACK_CELL_261 = 261
    RACK_CELL_323 = 323
