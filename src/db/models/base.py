import inflection
from sqlalchemy import MetaData, Integer
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase, declarative_mixin, mapped_column, Mapped


@declarative_mixin
class BaseModel(DeclarativeBase):
    """Base db model class."""
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)


POSTGRES_INDEXES_NAMING_CONVENTION = {
    "ix": "%(column_0_label)_idx",
    "uq": "%(table_name)_%(column_0_name)_key",
    "ck": "%(table_name)_%(constraint_name)_check",
    "fk": "%(table_name)_%(column_0_name)_fkey",
    "pk": "%(table_name)_pkey",
}

BaseModel.metadata = MetaData(naming_convention=POSTGRES_INDEXES_NAMING_CONVENTION)
