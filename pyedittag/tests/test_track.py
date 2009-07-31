# -*- coding: utf-8 -*-

from os import close, unlink
from shutil import copyfile
from tempfile import mkstemp

from tagpy import FileRef

from pyedittag import track
from pyedittag.tests import TestCase

class TestTrack(TestCase):

    def _make_mp3file(self, src):
        fd, path = mkstemp(suffix=".mp3")
        close(fd)
        copyfile(src, path)
        return path

    def test_track(self):
        mp3files = [
                self._make_mp3file(self.mp3file), 
                self._make_mp3file(self.mp3file)]
        try:
            track(mp3files)

            for i, mp3file in enumerate(mp3files):
                tag = FileRef(mp3file).tag()
                assert i + 1 == tag.track
        finally:
            for mp3file in mp3files:
                unlink(mp3file)

# vim: tabstop=4 shiftwidth=4 expandtab softtabstop=4
