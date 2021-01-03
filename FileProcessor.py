import os

parent_directory = ""
success_directory = ""
error_directory = ""


def isDirectory(path):
    return os.path.exists(path)


def setParentDirectory(directory_input):
    global parent_directory
    parent_directory = directory_input


def setSuccessDirectory(directory_input):
    global success_directory
    success_directory = directory_input


def setErrorDirectory(directory_input):
    global error_directory
    error_directory = directory_input


def onProcessSuccess(file):
    # save file to success directory
    # remove file from parent directory
    pass


def onProcessError(file):
    # save file to error directory
    # remove file from parent directory
    pass


def processFile(file):
    pass
