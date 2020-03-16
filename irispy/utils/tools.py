import os
import time
import sys
import re


class Logger:
    def __getattr__(self, item):
        if item in ["remove", "add", "level"]:
            return lambda *args, **kwargs: None
        return Logger()

    def __call__(self, message: str, *args, **kwargs):
        t = time.strftime("%m-%d %H:%M:%S", time.localtime())
        sys.stdout.write(
            "\n[IrisPY] " + message.format(*args, **kwargs) + " [TIME {}]".format(t)
        )


def chunks(x, y):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(x), y):
        yield x[i:i + y]


def folder_checkup(path, create: bool = True):
    path = os.path.abspath(path)
    if not os.path.exists(path) and create:
        os.mkdir(path)
    return path


def sub_string(text: str) -> str:
    return " ".join(text.split()[1:])
