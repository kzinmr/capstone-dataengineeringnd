import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database(config, defaultdb="'postgres'"):
    """
    - Creates and connects to the sparkifydb
    @return: cursor and connection to sparkifydb
    """

    host, dbname, user, password, port = config["LOCAL"].values()
    # Create new database via default database.
    conn = psycopg2.connect(
        f"host={host} dbname={defaultdb} user={user} password={password}"
    )
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    _dbname = dbname[1:-1]
    cur.execute(f"drop database if exists {_dbname};")
    cur.execute(f"create database {_dbname} with encoding 'utf8'"
                " template template0;")
    conn.close()

    # Connect to the created database.
    conn = psycopg2.connect(
        "host={} dbname={} user={} password={} port={}".format(
            *config["LOCAL"].values()
        )
    )
    cur = conn.cursor()

    return cur, conn


def drop_tables(cur, conn):
    """Drop tables if any by executing DROP queries.
    DROP queries are defined in drop_table_queries.

    Args:
        cur: SQL cursor object.
        conn: DB connection object.
    Returns:
    Raises:
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """Create tables by executing CREATE queries.
    CREATE queries are defined in create_table_queries.

    Args:
        cur: SQL cursor object.
        conn: DB connection object.
    Returns:
    Raises:
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read("db.cfg")
    print("connecting to postgres...")
    cur, conn = create_database(config)

    print("DROP EXISTING TABLES...")
    drop_tables(cur, conn)
    print("CREATE TABLES...")
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
