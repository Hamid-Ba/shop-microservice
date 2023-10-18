from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session

from persistence.database import get_context

payment_context = Annotated[Session, Depends(get_context)]