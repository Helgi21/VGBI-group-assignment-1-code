import pyodbc
from sqlalchemy import create_engine, insert
from dataclasses import dataclass
import urllib


@dataclass(frozen=True)
class ConnectionSettings:
    """Connection Settings."""
    server: str
    database: str
    username: str
    password: str
    driver: str = '{ODBC Driver 17 for SQL Server}'
    timeout: int = 30


class AzureConnection:
	def __init__(self, conn_sett: ConnectionSettings, echo: bool = False):
		params = urllib.parse.quote_plus(f"""
			Driver={conn_sett.driver};
			Server=tcp:{conn_sett.server},1433;
			Database={conn_sett.database};
			Uid={conn_sett.username};
			Pwd={conn_sett.password};
			Encrypt=yes;
			TrustServerCertificate=no;
			Connection Timeout={conn_sett.timeout};""")

		conn_str = f'mssql+pyodbc:///?odbc_connect={params}'
		self.engine = create_engine(conn_str, echo=echo)

	def connect(self) -> None:
		self.connection = self.engine.connect()

	def dispose(self) -> None:
		self.connection.close()
		self.engine.dispose()
