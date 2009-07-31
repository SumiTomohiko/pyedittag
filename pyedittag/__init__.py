# -*- coding: utf-8 -*-

from os.path import dirname, join
from optparse import OptionParser
from shutil import move

from tagpy import FileRef, StringType
from tagpy.id3v2 import FrameFactory

def init_tagpy():
    FrameFactory.instance().setDefaultTextEncoding(StringType.UTF8)

def edit_mp3file(mp3file, attribute, value):
    mp3file = FileRef(mp3file)
    tag = mp3file.tag()
    if attribute in ("track", "year"):
        value = int(value)
    setattr(tag, attribute, value)
    mp3file.save()

def edit(argv):
    parser = OptionParser(usage="usage: %prog edit album | artist | genre | track | year mp3file [mp3file...]")
    options, argv = parser.parse_args(argv)

    init_tagpy()

    attribute = argv[0]
    value = argv[1]
    for arg in argv[2:]:
        edit_mp3file(arg, attribute, value)

def rename_mp3file(mp3file):
    def replace_special_chars(s):
        special_chars = { "/": None, "\\": None }
        for key, value in special_chars.items():
            if value is None:
                value = "_"
            s = s.replace(key, value)

        return s

    tag = FileRef(mp3file).tag()

    new_name = ["%02d" % (tag.track, )]
    if tag.artist:
        new_name.append(" - %s" % (replace_special_chars(tag.artist), ))
    if tag.album:
        new_name.append(" - %s" % (replace_special_chars(tag.album), ))
    if tag.title:
        new_name.append(" - %s" % (replace_special_chars(tag.title), ))
    new_name.append(".mp3")
    new_name = join(dirname(mp3file), "".join(new_name))

    move(mp3file, new_name)

def rename(argv):
    parser = OptionParser(usage="usage: %prog rename mp3file [mp3file...]")
    options, argv = parser.parse_args(argv)

    init_tagpy()

    for arg in argv:
        rename_mp3file(arg)

def track(argv):
    parser = OptionParser(usage="usage: %prog track mp3file [mp3file...]")
    options, argv = parser.parse_args(argv)

    init_tagpy()

    for i, arg in enumerate(argv):
        edit_mp3file(arg, "track", i + 1)

def main():
    from sys import argv
    parser = OptionParser(usage="usage: %prog edit | rename | track")
    options, argv = parser.parse_args(argv[1:])

    cmd2f = { "edit": edit, "rename": rename, "track": track }
    cmd2f[argv[0]](argv[1:])

# vim: tabstop=4 shiftwidth=4 expandtab softtabstop=4
