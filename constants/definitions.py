import tempfile

# data collection type definitions
DATA_TYPE_POSITIONING = 0
DATA_TYPE_RANGING = 1
DATA_TYPE_MOTION_DATA = 2

# osc message indices relative to tag
OSC_TIME_INDEX_ABSOLUTE = 1
OSC_1D_RANGE_INDEX = 1
OSC_1D_VELOCITY_INDEX = 2
OSC_3D_POS_X_INDEX = 3
OSC_3D_POS_Y_INDEX = 4
OSC_3D_POS_Z_INDEX = 5
OSC_3D_VEL_X_INDEX = 6
OSC_3D_VEL_Y_INDEX = 7
OSC_3D_VEL_Z_INDEX = 8
OSC_PRESSURE_INDEX = 9
OSC_ACC_X_INDEX = 10
OSC_ACC_Y_INDEX = 11
OSC_ACC_Z_INDEX = 12
OSC_MAG_X_INDEX = 13
OSC_MAG_Y_INDEX = 14
OSC_MAG_Z_INDEX = 15
OSC_ANG_VEL_X_INDEX = 16
OSC_ANG_VEL_Y_INDEX = 17
OSC_ANG_VEL_Z_INDEX = 18
OSC_EULER_HEADING_INDEX = 19
OSC_EULER_ROLL_INDEX = 20
OSC_EULER_PITCH_INDEX = 21
OSC_QUATERNION_W_INDEX = 22
OSC_QUATERNION_X_INDEX = 23
OSC_QUATERNION_Y_INDEX = 24
OSC_QUATERNION_Z_INDEX = 25
OSC_LIN_ACC_X_INDEX = 26
OSC_LIN_ACC_Y_INDEX = 27
OSC_LIN_ACC_Z_INDEX = 28
OSC_GRAVITY_X_INDEX = 29
OSC_GRAVITY_Y_INDEX = 30
OSC_GRAVITY_Z_INDEX = 31

OSC_INDEX_DICT = {
    "Time": OSC_TIME_INDEX_ABSOLUTE,
    "1D Range": OSC_1D_RANGE_INDEX,
    "1D Velocity": OSC_1D_VELOCITY_INDEX,
    "3D Position X": OSC_3D_POS_X_INDEX,
    "3D Position Y": OSC_3D_POS_Y_INDEX,
    "3D Position Z": OSC_3D_POS_Z_INDEX,
    "3D Velocity X": OSC_3D_VEL_X_INDEX,
    "3D Velocity Y": OSC_3D_VEL_Y_INDEX,
    "3D Velocity Z": OSC_3D_VEL_Z_INDEX,
    "Pressure": OSC_PRESSURE_INDEX,
    "Acceleration X": OSC_ACC_X_INDEX,
    "Acceleration Y": OSC_ACC_Y_INDEX,
    "Acceleration Z": OSC_ACC_Z_INDEX,
    "Magnetic X": OSC_MAG_X_INDEX,
    "Magnetic Y": OSC_MAG_Y_INDEX,
    "Magnetic Z": OSC_MAG_Z_INDEX,
    "Angular Vel X": OSC_ANG_VEL_X_INDEX,
    "Angular Vel Y": OSC_ANG_VEL_Y_INDEX,
    "Angular Vel Z": OSC_ANG_VEL_Z_INDEX,
    "Euler Heading": OSC_EULER_HEADING_INDEX,
    "Euler Roll": OSC_EULER_ROLL_INDEX,
    "Euler Pitch": OSC_EULER_PITCH_INDEX,
    "Quaternion W": OSC_QUATERNION_W_INDEX,
    "Quaternion X": OSC_QUATERNION_X_INDEX,
    "Quaternion Y": OSC_QUATERNION_Y_INDEX,
    "Quaternion Z": OSC_QUATERNION_Z_INDEX,
    "Lin Acc X": OSC_LIN_ACC_X_INDEX,
    "Lin Acc Y": OSC_LIN_ACC_Y_INDEX,
    "Lin Acc Z": OSC_LIN_ACC_Z_INDEX,
    "Gravity X": OSC_GRAVITY_X_INDEX,
    "Gravity Y": OSC_GRAVITY_Y_INDEX,
    "Gravity Z": OSC_GRAVITY_Z_INDEX
}

MMAP_TEMP_FILE_NAME = tempfile.gettempdir() + "\\PSU Pozyx temporary file"
MMAP_LENGTH = 4096
MMAP_NO_NEW_DATA_FLAG = "No new mmap data"