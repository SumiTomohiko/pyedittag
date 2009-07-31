# -*- coding: utf-8 -*-

from os.path import dirname, exists, join

from pyedittag import edit_mp3file, rename
from pyedittag.tests import TestCase

class TestRename(TestCase):

    def _set_attribute(self, album=None, artist=None, title=None, track=None):
        vars = ["album", "artist", "title", "track"]
        local_vars = locals()
        for var in vars:
            value = local_vars[var]
            if value is not None:
                edit_mp3file(self.mp3file, var, value)

    def _rename(self):
        rename([self.mp3file])

    def _do(self, album=None, artist=None, title=None, track=None):
        self._set_attribute(album, artist, title, track)
        self._rename()

    def _test(self, name):
        expected = join(dirname(self.mp3file), name)
        assert exists(expected)
        self.renamed_file = expected

    def test_all(self):
        self._do(u"アルバム", u"アーティスト", u"タイトル", 42)
        self._test(u"42 - アーティスト - アルバム - タイトル.mp3")

    def test_album_only(self):
        self._do(u"アルバム")
        self._test(u"00 - アルバム.mp3")

    def test_artist_only(self):
        self._do(artist=u"アーティスト")
        self._test(u"00 - アーティスト.mp3")

    def test_title_only(self):
        self._do(u"タイトル")
        self._test(u"00 - タイトル.mp3")

    def test_track_only(self):
        self._do(track=42)
        self._test(u"42.mp3")

    def test_without_album(self):
        self._do(artist=u"アーティスト", title=u"タイトル", track=42)
        self._test(u"42 - アーティスト - タイトル.mp3")

    def test_without_artist(self):
        self._do(album=u"アルバム", title=u"タイトル", track=42)
        self._test(u"42 - アルバム - タイトル.mp3")

    def test_without_title(self):
        self._do(album=u"アルバム", artist=u"アーティスト", track=42)
        self._test(u"42 - アーティスト - アルバム.mp3")

    def test_without_track(self):
        self._do(u"アルバム", u"アーティスト", u"タイトル")
        self._test(u"00 - アーティスト - アルバム - タイトル.mp3")

    def test_special_char_album(self):
        self._do(u"/", u"アーティスト", u"タイトル")
        self._test(u"00 - アーティスト - _ - タイトル.mp3")

    def test_special_char_artist(self):
        self._do(u"アルバム", u"/", u"タイトル")
        self._test(u"00 - _ - アルバム - タイトル.mp3")

    def test_special_char_title(self):
        self._do(u"アルバム", u"アーティスト", u"/")
        self._test(u"00 - アーティスト - アルバム - _.mp3")

# vim: tabstop=4 shiftwidth=4 expandtab softtabstop=4
