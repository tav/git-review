# No Copyright (-) 2010 The Ampify Authors. This file is under the
# Public Domain license that can be found in the root LICENSE file.

import sys

from os.path import dirname, join as join_path, realpath

GITREVIEW_ROOT = dirname(dirname(realpath(__file__)))
THIRD_PARTY_LIBS_PATH = join_path(GITREVIEW_ROOT, 'lib')

if THIRD_PARTY_LIBS_PATH not in sys.path:
    sys.path.insert(0, THIRD_PARTY_LIBS_PATH)
