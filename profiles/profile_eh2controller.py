__author__ = 'Konstantin Glazyrin'

# main common libraries
from app.load import *

# specific libraries
from app.load.load_config import *

TANGO_ADDRESS = "haspp02oh1:10000/p02/gepressctrlpace5000/eh2b.01"

START = {
    # profile name
    PROFILE_NAME: "P02.2 Pressure Controller Pace5000 (EH2)",

    # HTML file for status updates
    PROFILE_HTML: "interface.html",

    # TangoDevice Address - used for checking the device availability - if device is not available or Faulty state - do not read any attribute
    PROFILE_TANGO_ADDRESS: TANGO_ADDRESS,

    # interval of time to use for polling the attributes
    PROFILE_DELAY: 500,

    # PROFILE controllers - executable to run - list of lists to run via QProcess
    # list of dicts with keys: CMD:str (must have), NICK:str (must have), ARGS:list (must have)
    # must have - must be present
    PROFILE_CONTROLLERS: [
                            {CMD:"C:\\Program Files (x86)\\Notepad++\\notepad++.exe", NICK: "Profile editor (Win)", ARGS: [__file__.replace("pyc", "py")]},
                            {CMD:"/usr/bin/gedit", NICK: "Profile editor (Linux)", ARGS: [__file__.replace("pyc", "py")]},
                            {CMD:"/usr/bin/gnome-terminal", NICK:"Command line", ARGS: []},
                            {CMD: SEPARATOR},
                            {CMD: "/usr/bin/astor", NICK: "Astor", ARGS: []},
                            {CMD: "/usr/bin/jive", NICK: "Jive", ARGS: []},
                         ],

    # list of the attributes to read
    PROFILE_ATTRLOOP: [
        # attribute to read, description to use as a tooltip, format for data representation
        {ATTR: DECOMPRESSRATE, DESC: 'DecompressRate', FORMAT: "{:6.2f}"},
        {ATTR: INLETPRESSURE, DESC: 'InletPressure', FORMAT: "{:6.0f}"},
        {ATTR: MEMBRANEPRESSURE, DESC: 'MembranePressure', FORMAT: "{:6.2f}"},
        {ATTR: OVERSHOOT, DESC: 'Overshoot'},
        {ATTR: PRESSURECONTROL, DESC: 'PressureControl'},
        {ATTR: SETPOINT, DESC: 'SetPoint', FORMAT: "{:6.2f}"},
        {ATTR: SLEWRATE, DESC: 'SlewRate', FORMAT: "{:10.2f}"},
        {ATTR: SLEWRATEMODE, DESC: 'SlewRateMode'},
        {ATTR: SOURCEEFFECTIVENESS, DESC: 'SourceEffectiveness', FORMAT: "{:03.0f}"},
    ]
}


