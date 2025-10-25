import uuid
from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

#лучше не использовать относительные импорты
#from src.database import Base
from ..database import Base

#модель таблицы пользователя все поля понятны
class UserModel(Base):
    __tablename__ = 'user'

    id: Mapped[uuid.UUID] = mapped_column(
        UUID, primary_key=True, index=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    hashed_password: Mapped[str]
    fio: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=True)
    is_verified: Mapped[bool] = mapped_column(default=False)
    is_superuser: Mapped[bool] = mapped_column(default=False)

#модель для записи сессий пользователя с внешним ключом user_id и удалением типа CASCADE
#наверное для отслеживания посещений
class RefreshSessionModel(Base):
    __tablename__ = 'refresh_session'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    refresh_token: Mapped[uuid.UUID] = mapped_column(UUID, index=True)
    expires_in: Mapped[int]
    created_at: Mapped[datetime] = mapped_column(sa.TIMESTAMP(timezone=True),
                                                 server_default=func.now())
    user_id: Mapped[uuid.UUID] = mapped_column(UUID, sa.ForeignKey(
        "user.id", ondelete="CASCADE"))
