import logging

class BaseTestCase(object):
    logging.basicConfig()
    _log=logging.getLogger("jeebei")
    _log.setLevel(logging.DEBUG)

    @property
    def log(self):
        return self._log