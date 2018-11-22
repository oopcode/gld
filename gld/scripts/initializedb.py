from __future__ import unicode_literals
import sys

from clld.scripts.util import initializedb, Data
from clld.db.meta import DBSession
from clld.db.models import common

import gld
from gld import models


def main(args):
    data = Data()

    dataset = common.Dataset(id=gld.__name__, domain='gld.clld.org')
    DBSession.add(dataset)


def prime_cache(args):
    """If data needs to be denormalized for lookup, do that here.
    This procedure should be separate from the db initialization, because
    it will have to be run periodiucally whenever data has been updated.
    """


if __name__ == '__main__':  # pragma: no cover
    initializedb(create=main, prime_cache=prime_cache)
    sys.exit(0)
