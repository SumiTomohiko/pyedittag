# -*- coding: utf-8 -*-

from tagpy.id3v2 import FrameFactory
import tagpy

from pyedittag import edit
from pyedittag.tests import TestCase

class TestEdit(TestCase):

    def _edit(self, attribute, value):
        edit([attribute, value, self.mp3file])

    def _test(self, attribute, expected):
        FrameFactory.instance().setDefaultTextEncoding(tagpy.StringType.UTF8)

        file_ = tagpy.FileRef(self.mp3file)
        tag = file_.tag()
        assert expected == getattr(tag, attribute)

    def _do(self, attribute, value):
        self._edit(attribute, value)
        if attribute in ("track", "year"):
            value = int(value)
        self._test(attribute, value)

    def test_title(self):
        attribute = "title"
        title = u"日本語"
        self._do(attribute, title)

    def test_artist(self):
        attribute = "artist"
        artist = u"日本語"
        self._do(attribute, artist)

    def test_album(self):
        attribute = "album"
        album = u"日本語"
        self._do(attribute, album)

    def test_year(self):
        attribute = "year"
        year = "1942"
        self._do(attribute, year)

    def test_track(self):
        attribute = "track"
        track = "42"
        self._do(attribute, track)

    def test_genre(self):
        attribute = "genre"
        genre = "Anime"
        self._do(attribute, genre)

# vim: tabstop=4 shiftwidth=4 expandtab softtabstop=4
