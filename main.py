from sqlalchemy import insert

from dbconnect import AzureConnection, ConnectionSettings
from models import metadata_obj, FS_table, VN_table
from parseData import ParseData as PD

CONNECTION_SETTINGS = ConnectionSettings(
	server = "XXXXX.database.windows.net",
	database = "XXXXX",
	username = "XXXXX",
	password = "XXXXX"
)

conn = AzureConnection(CONNECTION_SETTINGS)
conn.connect()

# Drop and re-create tables
metadata_obj.drop_all(conn.engine)

metadata_obj.create_all(conn.engine)

data = PD().parse()

pop_VN = insert(VN_table).values(data["VN"])
# FS Needs each line to be individually inserted for some reason - related to size of dataset
for line in data["FS"]:
	pop_FS = insert(FS_table).values(line)
	conn.connection.execute(pop_FS)

conn.connection.execute(pop_VN)

## We stop doing the do here ##

conn.dispose()
