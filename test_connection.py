
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from config import DB_CONFIG


def test_mysql_connection():
    engine = None

    try:
        connection_url = URL.create(
            drivername="mysql+mysqlconnector",
            username=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            host=DB_CONFIG["host"],
            database=DB_CONFIG["database"]
        )

        engine = create_engine(connection_url)

        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT DATABASE(), VERSION()")
            )

            database_name, mysql_version = result.fetchone()

            print("MySQL connection successful!")
            print(f"Database: {database_name}")
            print(f"MySQL Version: {mysql_version}")

    except Exception as error:
        print("MySQL connection failed.")
        print(f"Error: {error}")

    finally:
        if engine is not None:
            engine.dispose()


if __name__ == "__main__":
    test_mysql_connection()
