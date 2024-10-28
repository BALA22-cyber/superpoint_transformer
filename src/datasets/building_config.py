import numpy as np


########################################################################
#                         Download information                         #
########################################################################

# FORM_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSefhHMMvN0Uwjnj_vWQgYSvtFOtaoGFWsTIcRuBTnP09NHR7A/viewform?fbzx=5530674395784263977'

# # DALES in LAS format
# LAS_TAR_NAME = 'dales_semantic_segmentation_las.tar.gz'
# LAS_UNTAR_NAME = "dales_las"

# # DALES in PLY format
# PLY_TAR_NAME = 'dales_semantic_segmentation_ply.tar.gz'
# PLY_UNTAR_NAME = "dales_ply"

# # DALES in PLY, only version with intensity and instance labels
# OBJECTS_TAR_NAME = 'DALESObjects.tar.gz'
# OBJECTS_UNTAR_NAME = "DALESObjects"


########################################################################
#                              Data splits                             #
########################################################################

# The validation set was arbitrarily chosen as the x last train tiles:


# 'KCDC109-110_E_processed.h5', 
# 'KCDC109-110_N_processed.h5',
# 'KCDC109-110_S_processed.h5',
# 'KCDC109-110_W_processed.h5', 
# 'KCDC111-112_E_processed.h5', 
# 'KCDC111-112_N_processed.h5 ',
# 'KCDC111-112_S_processed.h5',
# 'KCDC111-112_W_processed.h5'

# B1505_NE_2
# B1505_SE_1
# B1505_SE_2
# B1509_SW
# B1520_NW
# B1520_NW_BETTER
# B1520_SW_1
# B1520_SW_2_door
# B1520_SW_2_main
# B2570_SW_left
# B2570_SW_right
# B3156_NW
# B4020_SW
TILES = {
    'train': [
        'KCDC109-110_E_processed', 
        'KCDC109-110_N_processed',
        'KCDC109-110_S_processed',
        'KCDC109-110_W_processed',
        # 'B1505_NE_2',
        # 'B1509_SE_1',
        # 'B1509_SE_2',
        # 'B1509_SW',
        # 'B1520_NW',
        # 'B1520_SW_1',
        'B1520_SW_2_door',
        'B1520_SW_2_main',
        'B2570_SW_left',
        'B2570_SW_right',
        'B3156_NW'],

    'val': [
        'KCDC111-112_E_processed', 
        'KCDC111-112_N_processed',
        # 'B4020_SW',
        'B1520_NW_BETTER'],

    'test': [
        'KCDC111-112_S_processed',
        'KCDC111-112_W_processed']}


########################################################################
#                                Labels                                #
########################################################################

# DALES_NUM_CLASSES = 8
# ID2TRAINID = np.asarray([8, 0, 1, 2, 3, 4, 5, 6, 7])
# CLASS_NAMES = [
#     'Ground',
#     'Vegetation',
#     'Cars',
#     'Trucks',
#     'Power lines',
#     'Fences',
#     'Poles',
#     'Buildings',
#     'Unknown']

# CLASS_COLORS = np.asarray([
#     [243, 214, 171],  # sunset
#     [ 70, 115,  66],  # fern green
#     [233,  50, 239],
#     [243, 238,   0],
#     [190, 153, 153],
#     [  0, 233,  11],
#     [239, 114,   0],
#     [214,   66,  54],  # vermillon
#     [  0,   8, 116]])

BUILDING_NUM_CLASSES = 3

# Mapping from original classes to new training class IDs (if remapping is necessary)
ID2TRAINID = np.asarray([
    # BUILDING_NUM_CLASSES, # 0 -> Ignored
    0,            # 1 -> Class 0 (e.g., 'Window')
    1,            # 2 -> Class 1 (e.g., 'Wall')
    2             # 3 -> Class 2 (e.g., 'Door')
])

# Class names (including void/unlabeled/ignored last)
CLASS_NAMES = [
    'Window + Door',
    'Wall',
    'Others',
    'Ignored'
]

# Class color palette (including void/unlabeled/ignored last)
CLASS_COLORS = np.asarray([
    [255, 255, 0],    # Yellow for 'Window'
    [0, 255, 0],      # Green for 'Wall'
    [0, 0, 255],      # Blue for 'Door'
    [0, 0, 0]         # Black for 'Ignored'
])

# For instance segmentation
MIN_OBJECT_SIZE = 100
# THING_CLASSES = [2, 3, 4, 5, 6, 7]
THING_CLASSES = [0,2] # things, non background classes
STUFF_CLASSES = [i for i in range(BUILDING_NUM_CLASSES) if not i in THING_CLASSES]
