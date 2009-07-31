# -*- coding: utf-8 -*-

from os import close, unlink
from os.path import abspath, dirname, exists, join
from shutil import copyfile
from tempfile import mkstemp

class TestCase(object):

    TEST_MP3 = join(dirname(abspath(__file__)), "test.mp3")

    def setup_method(self, method):
        fileno, path = mkstemp(suffix=".mp3")
        close(fileno)
        copyfile(self.TEST_MP3, path)
        self.mp3file = path
        self.renamed_file = ""

    def teardown_method(self, method):
        if exists(self.mp3file):
            unlink(self.mp3file)
        if exists(self.renamed_file):
            unlink(self.renamed_file)

# vim: tabstop=4 shiftwidth=4 expandtab softtabstop=4
