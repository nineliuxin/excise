import inspect
import os
import shlex
import signal
import subprocess
import time

import allure
import pytest


@pytest.fixture(scope="class", autouse=True)
def record():
    videfile = 'videos/' + 'video_' + str(time.time()) + '.mp4'
    # cmd = shlex.split()
    print(inspect.stack())
    cmd = "E:\Download\Others\scrcpy-win64-v1.14\scrcpy --record %s" % videfile
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    yield
    p.send_signal(signal.CTRL_C_EVENT)
    # imagefile = 'images/' + "result_" + str(time.time()) + ".png"
    # instance.screenshot(imagefile)
    time.sleep(2)
    # allure.attach.file(imagefile, name='截图', attachment_type=allure.attachment_type.PNG)
    allure.attach.file(videfile, name='视频', attachment_type=allure.attachment_type.MP4)