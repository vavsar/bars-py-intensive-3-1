from contextlib import contextmanager


@contextmanager
def open_file(path, mode):
    """
    contextmanager prints number of lines in files
    at the beginning of processing file
    """
    f = open(path, mode)
    counter = 0
    for line in f:
        counter += 1
    print(counter)
    yield f
    f.close()
  