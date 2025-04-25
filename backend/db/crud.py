from db.models import Item
from db.session import SessionLocal

def get_items():
    db = SessionLocal()
    items = db.query(Item).all()
    db.close()
    return items

def create_item(name: str):
    db = SessionLocal()
    item = Item(name=name)
    db.add(item)
    db.commit()
    db.refresh(item)
    db.close()
    return item