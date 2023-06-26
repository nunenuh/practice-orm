
import datetime
from sqlalchemy import DateTime
from sqlalchemy.orm import DeclarativeBase, Column, BIGINT,VARCHAR, String, Mapped, mapped_column, ForeignKey, TIMESTAMP, func, relationship

class Base(DeclarativeBase):
    pass



# CREATE TABLE IF NOT EXISTS users (
#     telegram_id INTEGER PRIMARY KEY,
#     full_name VARCHAR(255),
#     username VARCHAR(255),
#     language_code VARCHAR(255),
#     created_at TIMESTAMP default now(),
#     referrer_id BIGINT,
#     FOREIGN KEY (referrer_id) 
#         REFERENCES users(telegram_id)
#         ON DELETE SET NULL
# );

class User(Base):
    __tablename__ = 'users'
    telegram_id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    full_name: Mapped[str] = mapped_column(VARCHAR(255))
    username: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)
    language_code: Mapped[str] = mapped_column(VARCHAR(255))
    created_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, nullable=False, server_default=func.now())
    referrer_id: Mapped[int] = mapped_column(BIGINT, ForeignKey('users.telegram_id', on_delete="SET NULL"), nullable=True)
    
    referrer = relationship("User", remote_side=[telegram_id])