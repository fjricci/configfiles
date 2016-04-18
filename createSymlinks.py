#!/usr/bin/env python

import os
import shutil
import sys

homedir = os.environ["HOME"]
configdir = os.path.realpath(os.path.dirname(sys.argv[0]))

links = {
    ".bashrc"            : "bash/bashrc",
    ".git-completion.sh" : "git/git-completion.sh",
    ".gitconfig"         : "git/gitconfig",
    ".vimrc"             : "vim/vimrc",
    ".vim"               : "vim/vim",
}

def _conf_path(path):
    return os.path.join(configdir, path)

def _home_path(path):
    return os.path.join(homedir, path)

def create_links():
    for f in links:
        dst = _home_path(f)
        src = _conf_path(links[f])

        if os.access(dst, os.F_OK):
            print("could not link %s, skipping" % dst)
            continue

        print("linking  %s -> %s" % (dst, src))
        if not os.path.exists(os.path.dirname(dst)):
            os.makedirs(os.path.dirname(dst))
        os.symlink(src, dst)

if __name__ == "__main__":
    create_links()
