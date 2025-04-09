from enum import IntEnum


class BoxType(IntEnum):
    PRIMER = 0
    GENERAL = -1
    TUBE = -1
    SEED = -2
    FLY = -3
    BACTERIUM = -4
    CELL_LINE = -5
    TISSUE = -6
    ANTIBODY = -7
    PLASMID = -8
    GLYCEROL = -9
    ENZYME = -10
    CONSUMABLE = -11
    YEAST = -12
    FUNGUS = -13
    VIRUS = -14
    PROTEIN = -15
    LIPID = -16
    WORM = -17
    SEQUENCE = -18
    ZEBRAFISH = -19
    GENE = -20
    COMPOUND = -21
