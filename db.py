from time import sleep

import psycopg2
from psycopg2 import InterfaceError, OperationalError
from psycopg2.pool import SimpleConnectionPool


class PostgresSQLConnection:
    def __init__(self, host: str, port: int, database: str, username: str, password: str,
                 pool_size: int = 2) -> None:

        self._conn_params = {'host': host, 'port': port, 'dbname': database, 'user': username, 'password': password}
        self._min_pool_size = int(pool_size)
        self._max_pool_size = self._min_pool_size * 2
        self._pool = None

        self._create_connection()

    def _create_connection(self) -> None:
        """Initialize a connection pool."""
        attempts = 3  # number of attempts to create/restore DB connection
        backoff = 5  # sec
        for i in range(1, attempts + 1):  # max 15 sec to create/restore DB connection
            try:
                self._pool = SimpleConnectionPool(self._min_pool_size, self._max_pool_size, **self._conn_params)

                result = self.execute("SHOW server_version")
                print(f"Successfully connected to DB server: v{result[0][0]}")

                return
            except psycopg2.OperationalError as e:
                if i < attempts:
                    delay = i * backoff
                    print(f"DB error: {str(e)}")  # FIXME: convert to log
                    print(f"Next attempt to connect to the DB in {delay} sec")
                    sleep(delay)

        raise Exception("PostgreSQL DB is not available")

    def get_connection(self):
        """Provide an available active connection from the pool. Otherwise, it tries to reconnect to the DB."""
        conn = self._pool.getconn()
        try:
            with conn.cursor() as curs:
                # Send keepalive request
                curs.execute("SHOW server_version")
            conn.reset()
            return conn
        except (InterfaceError, OperationalError) as e:
            print(f"Unexpected DB error: {e}")
            # Recover lost DB connection
            self._create_connection()
            return self._pool.getconn()
