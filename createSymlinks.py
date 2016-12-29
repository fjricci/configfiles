#!/usr/bin/env python

import os
import shutil
import sys
from optparse import OptionParser

homedir = os.environ["HOME"]
configdir = os.path.realpath(os.path.dirname(sys.argv[0]))


class LinkMaker:

  def __init__(self, suffix):
    if suffix is not "":
      suffix = "_" + suffix

    self.links = {
        ".git-completion.sh": "git/git-completion.sh",
        ".vim": "vim/vim",
        ".bashrc" + suffix: "bash/bashrc",
        ".gitconfig" + suffix: "git/gitconfig",
        ".vimrc" + suffix: "vim/vimrc",
    }

  def conf_path(self, path):
    return os.path.join(configdir, path)

  def home_path(self, path):
    return os.path.join(homedir, path)

  def create_links(self):
    for f in self.links:
      dst = self.home_path(f)
      src = self.conf_path(self.links[f])

      if os.access(dst, os.F_OK):
        print("could not link %s, skipping" % dst)
        continue

      print("linking  %s -> %s" % (dst, src))
      if not os.path.exists(os.path.dirname(dst)):
        os.makedirs(os.path.dirname(dst))
      os.symlink(src, dst)


if __name__ == "__main__":
  parser = OptionParser()
  parser.add_option(
      "-s", "--suffix", default="", help="Set config filename suffix")
  (options, args) = parser.parse_args()

  maker = LinkMaker(options.suffix)

  maker.create_links()
