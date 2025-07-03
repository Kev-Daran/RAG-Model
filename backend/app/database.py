from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("Database_URL env variable is not set. Please check your env and Docker compose file and ensure env variables are set")

engine = create_async_engine(DATABASE_URL, echo=False)


AsyncSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
)


Base=declarative_base

async def get_db():
    '''
        Dependency to get async db session, this will be used in FastAPI endpoints
    '''

    async with AsyncSessionLocal() as session:
        try:
            yield session
        except:
            await session.close()