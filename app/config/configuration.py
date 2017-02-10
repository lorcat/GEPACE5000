__author__ = 'Konstantin Glazyrin'

import os
from app.load import *
from app.config.keys import *


# logging related configuration
LOGGING = {
    LOGGING_LEVEL: DEBUG
}


#### Internal configuration - please do not touch
# profiles
PROFILES = {
    # profile thread priority
    PROFILE_PRIORITY: qtcore.QThread.InheritPriority,

    # profile directory - filled by application
    PROFILE_DIR: None,

    # profile configuration - filled by application
    PROFILE_START: None
}

#### Internal configuration - please do not touch
# resources configuration
RESOURCES = {
    # do not change - filled by the application
    RESOURCE_IMAGES: None,

    # path to the HTML files - filled by the application
    RESOURCE_HTML: None,

    # dict for different purpose - filled by application
    RESOURCE_DICT: {},
}

# converting obtained values to the string
CONVERTER = {
    # how to convert an int
    CONVERT_INT: "{}",
    # how to convert a float
    CONVERT_FLOAT: "{}",
    # how to convert a string
    CONVERT_STRING: "{}",
    # default float
    DEFAULT_FLOAT: -1.
}

# functional operations
def resources():
    global RESOURCES
    return RESOURCES