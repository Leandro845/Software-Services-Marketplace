# Importing the debug task from the celery_config module
from .celery_config import debug_task as dbt

# Exposing the debug task in the __all__ list
__all__ = ('dbt',)
