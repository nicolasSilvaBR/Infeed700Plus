from functions.sites import IsMultiSiteEnabled
from functions.database_connection import mydb

engine = mydb()
ismulti = IsMultiSiteEnabled(engine)