import sqlalchemy as db

engine = db.create_engine('postgresql+psycopg2://postgres:123@172.31.0.2:5432/glen-db');
conn = engine.connect()
result = conn.execute("SELECT 'holaaaaa' AS msg")