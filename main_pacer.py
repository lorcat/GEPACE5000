from app.load import *
from app.load.load_config import *

from app.starter import *

#name of the file - used to prepare configuration
FILE = __file__

def prepare_resources():
    """
    Updates resources - images and etc. paths
    :return:
    """
    global FILE
    # path to the images
    config.RESOURCES[RESOURCE_IMAGES] = create_path(FILE, "app", "images")

    # path to the htmls
    config.RESOURCES[RESOURCE_HTML] = create_path(FILE, "app", "html")

def prepare_profiles():
    """
    Updates profile paths
    :return:
    """
    global FILE
    config.PROFILES[PROFILE_DIR] = create_path(FILE, "profiles")

def main():
    """
    Main application file
    :return:
    """
    app = qtgui.QApplication(sys.argv)

    # update resources path
    prepare_resources()

    # update profile path
    prepare_profiles()

    # begin with the application controller - starter
    s = Starter(app)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
