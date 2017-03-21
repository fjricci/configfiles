#!/usr/bin/env python

import os
import shutil
import sys
from optparse import OptionParser

homedir = os.environ["HOME"]
configdir = os.path.realpath(os.path.dirname(sys.argv[0]))

class LinkMaker:

  def __init__(self, suffix):
    self.suffix = suffix
    self.links = {
        ".git-completion.sh": "git/git-completion.sh",
        ".vim": "vim/vim",
        self.append_suffix(".bashrc"): "bash/bashrc",
        self.append_suffix(".gitconfig"): "git/gitconfig",
        self.append_suffix(".vimrc"): "vim/vimrc",
        self.append_suffix(".ideavimrc"): "vim/ideavimrc",
    }

  def append_suffix(self, string):
    return string + "_" + self.suffix if self.suffix is not "" else string

  def conf_path(self, path):
    return os.path.join(configdir, path)

  def home_path(self, path):
    return os.path.join(homedir, path)

  def link_file(self, f):
    dst = self.home_path(f)
    src = self.conf_path(self.links[f])

    if os.access(dst, os.F_OK):
      print("could not link %s, skipping" % dst)
      return

    print("linking  %s -> %s" % (dst, src))
    if not os.path.exists(os.path.dirname(dst)):
      os.makedirs(os.path.dirname(dst))
    os.symlink(src, dst)

  def create_links(self, file_to_link):
    if file_to_link is not "all":
      self.link_file(file_to_link)
      return

    for f in self.links:
      self.link_file(f)


if __name__ == "__main__":
  parser = OptionParser()
  parser.add_option(
      "-f", "--file-to-link", default="all", help="File to link")
  parser.add_option(
      "-s", "--suffix", default="", help="Set config filename suffix")
  (options, args) = parser.parse_args()

  maker = LinkMaker(options.suffix)

  maker.create_links(maker.append_suffix(options.file_to_link))
