import psycopg2
from sql_queries import create_table_queries, drop_table_queries

def create_database():
    # connect to default database
    conn = psycopg2.connect(host="rosie.db.elephantsql.com", database="koxdgtnq", user="koxdgtnq", password="hyik6zNrT28enwS3KAMIhRtCMlG4J2Ez")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create accounts database
    #cur.execute("DROP DATABASE IF EXISTS accounts")
    #cur.execute("CREATE DATABASE accounts")

    # close connection to default database
    #conn.close()    
    
    # connect to accounts database
    #conn = psycopg2.connect(host="rosie.db.elephantsql.com", database="accounts", user="koxdgtnq", password="hyik6zNrT28enwS3KAMIhRtCMlG4J2Ez")
    #cur = conn.cursor()
    
    return cur, conn

def drop_tables(cur, conn):
    '''Drops all tables created on the database'''
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

def create_tables(cur, conn):
    '''Created tables defined on the sql_queries script: [songplays, users, songs, artists, time]'''
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

def main():
    """ Function to drop and re create sparkifydb database and all related tables.
        Usage: python create_tables.py
    """
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()

if __name__ == "__main__":
    main()

print ("done")