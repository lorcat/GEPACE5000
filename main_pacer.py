from app.load import *
from app.load.load_config import *

from app.starter import *
from app.custom_app import *

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
    app = CustomApplication(sys.argv)

    # update resources path
    prepare_resources()

    # update profile path
    prepare_profiles()

    # begin with the application controller - starter
    s = Starter(app)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

# @TODO: Qt has caught an exception thrown from an event handler. Throwing  exceptions from an event handler is not supported in Qt. You must  reimplement QApplication::notify() and catch all exceptions there.