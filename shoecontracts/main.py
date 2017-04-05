#!/usr/bin/env python

"""The main entry point. Invoke as `shoecontracts` or `python -m shoecontracts'.
"""

from __future__ import print_function
from datetime import datetime, date
import argparse
import logging
import shoecontracts
import shoecontracts.model
import shoecontracts.core
import shoecontracts.utils
import sys


def parse_args():
    """Parse and validate command line arguments.
    """
    formatter = argparse.ArgumentDefaultsHelpFormatter
    parser = argparse.ArgumentParser(prog='shoecontracts',
                                     description='Manage shoe contracts statistics.',
                                     formatter_class=formatter)
    
    parser.add_argument('-V', '--version', action='version', 
                        version='%(prog)s {0}'.format(shoecontracts.__version__))

    dt = datetime.now()
    today = dt.strftime('%m/%d/%Y')
    parser.add_argument('-d', '--date', action='store', 
                        type=shoecontracts.utils.valid_date_range,
                        default=today,
                        help='dash separated date range '
                             'or single date')
    
    season_example = shoecontracts.CURRENT_SEASON
    parser.add_argument('-s', '--season', action='store', type=shoecontracts.utils.valid_season,
			help='dash separated year range '
			'(example: {0})'.format(season_example))

    parser.add_argument('--no-update', dest='should_update', action='store_false',
			help='only download data; do not update database')

    parser.add_argument('-v', '--verbose', action='count',
                        help='increase output verbosity')

    return parser.parse_args()


def main():
    args = parse_args()

    logging.basicConfig(level=shoecontracts.utils.log_level(args.verbose),
                        format='%(levelname)s: %(message)s')
    start, end = args.date
    shoecontracts.core.update(args.season, args.should_update)
    
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        sys.exit(e)
