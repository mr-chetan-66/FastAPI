from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from DB_S7.database import get_db
from DB_S7.db_model import DbUser

router = APIRouter(
    prefix="/live",
    tags=["Live Debug"]
)

@router.get("/users")
def live_users(db: Session = Depends(get_db)):
    users = db.query(DbUser).all()

    # Convert SQLAlchemy objects → dict
    output = []
    for u in users:
        d = u.__dict__.copy()
        d.pop("_sa_instance_state", None)
        output.append(d)

    return output