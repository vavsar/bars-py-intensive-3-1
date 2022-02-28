from contextlib import contextmanager


@contextmanager
def open_file(path, mode):
    f = open(path, mode)
    counter = 0
    for line in f:
        counter += 1
    print(counter)
    yield f
    f.close()
  