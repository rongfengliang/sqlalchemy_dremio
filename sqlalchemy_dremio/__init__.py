__version__ = '3.0.2'

from sqlalchemy.dialects import registry

# Register the Flight end point
registry.register("dremio.flight", "sqlalchemy_dremio.flight", "DremioDialect_flight")
