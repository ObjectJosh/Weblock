def init(path, block_size_tuple, survey_size_tuple):
    global hostPath
    global block_window_size
    global survey_window_size
    hostPath = path
    block_window_size = block_size_tuple
    survey_window_size = survey_size_tuple
