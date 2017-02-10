__author__ = 'Konstantin Glazyrin'

from app.load import *
# from app.common import Tester


class ThreadPool(qtcore.QThreadPool, Tester):
    # maximum number of runners
    MAX_THREADS = 5

    # timeout to wait on the runners in ms
    THREAD_TIMEOUT = 3000

    def __init__(self, parent=None):
        Tester.__init__(self)
        qtcore.QThreadPool.__init__(self, parent)

        self.setMaxThreadCount(self.MAX_THREADS)

    def tryStart(self, *args, **kwargs):
        """
        Starts a runner in a thread
        :param runner:
        :return:
        """
        self.debug("Starting a runner ({})".format(args))
        qtcore.QThreadPool.tryStart(self, *args, **kwargs)

    def cleanup(self):
        """
        Cleaning up the procedures
        :return:
        """
        self.waitForDone(self.THREAD_TIMEOUT)

class ProcessRunner(qtcore.QRunnable, Tester):
    """
    Process starting runnable
    """
    def __init__(self, cmd, *args):
        Tester.__init__(self)
        qtcore.QRunnable.__init__(self)

        # save initialization parameters
        self.cmd = cmd
        self.args = args[0]

        if not isinstance(self.args, list) and not isinstance(self.args,tuple):
            self.error("Configuration error; process arguments must be in a list or tuple ({})".format(self.args))
            self.args = []

        self.setAutoDelete(True)

    def run(self):
        """
        Starts a process
        :return:
        """
        self.debug("Starting a process ({}) with arguments ({})".format(self.cmd, self.args))
        proc = qtcore.QProcess()

        proc.startDetached(self.cmd, self.args)


class LambdaRunner(qtcore.QRunnable, Tester):
    """
    Process starting runnable
    """
    def __init__(self, func):
        Tester.__init__(self)
        qtcore.QRunnable.__init__(self)

        self.debug("Creating a lambda runner")

        # save initialization parameters
        self.func = func

        if not self.test(self.func):
            self.error("Error on LambdaRunner creation - lambda function is None")
            return

        self.setAutoDelete(True)

    def run(self):
        """
        Starts a process
        :return:
        """
        self.debug("Starting a lambda function process ({})".format(self.func))
        self.func()


THREAD_POOL = None

def getPool(parent=None):
    global THREAD_POOL
    if THREAD_POOL is None:
        THREAD_POOL = ThreadPool(parent=parent)
    return THREAD_POOL