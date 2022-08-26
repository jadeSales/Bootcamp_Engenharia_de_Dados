from sqlalchemy import create _engine
engine = create_engine('postgresql+psycopg2://user:password@hostname/database_name')
