from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "postgresql://mishka:M1sh1k019891710@localhost:5432/app_cms"

engine = create_engine(DATABASE_URL, echo=True)


def Create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session