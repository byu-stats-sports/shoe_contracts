"""
shoecontracts - a CLI to manage NBA shoe contracts data.
"""
import os
import nba_py
__author__ = 'Chris Beckett'
__version__ = '0.0.1'
__licence__ = 'GPLv3+'

#Comment this database_url line out when running code. 
DATABASE_URL = os.getenv('BYU_NBA_DATABASE_URL')
CURRENT_SEASON = nba_py.constants.CURRENT_SEASON
