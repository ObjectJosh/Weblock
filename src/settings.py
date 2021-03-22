# A file to be referenced to, containing the init function for global variables

def init(path, block_size_tuple, survey_size_tuple):
    """ Initializes global variables for the program, including general constant settings

    Args:
        path(string): the general path to 'hosts' file
        block_size_tuple(tuple): a tuple of ints describing (width, height) of the main window size
        survey_size_tuple(tuple): a tuple of ints describing (width, height) of the survey window size
    """
    global hostPath
    global block_window_size
    global survey_window_size
    hostPath = path
    block_window_size = block_size_tuple
    survey_window_size = survey_size_tuple
