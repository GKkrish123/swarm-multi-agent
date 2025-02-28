import sqlite3

"""
This script is used to create a SQLlite database, add tables
to it, and insert mock data, all for the OpenAI Swarm demonstration
with the other Python script in this directory.

Simply run this script with the command:

python load_sql_data.py

And then you will have a database loaded and ready to use
with the agent swarm!
"""

def execute_sql_script(cursor, script_file):
    with open(script_file, 'r') as sql_file:
        sql_script = sql_file.read()
    
    statements = sql_script.split(';')
    for statement in statements:
        if statement.strip():
            cursor.execute(statement)

def main():
    conn = sqlite3.connect('rss-feed-database.db')
    cursor = conn.cursor()

    execute_sql_script(cursor, 'ai-news-complete-tables.sql')
    conn.commit()

    execute_sql_script(cursor, 'ai-news-complete-mock-data.sql')
    conn.commit()

    cursor.execute("SELECT * FROM rss_feeds")
    feeds = cursor.fetchall()
    for feed in feeds:
        print(feed)

    conn.close()

if __name__ == "__main__":
    main()