import sqlalchemy

from .config import settings

engineOracle = sqlalchemy.create_engine(settings.oracle)