import sqlite3

class SqlServer():
    def __init__(self, db_location, table_name, column_name_1, column_name_2):
        self.connection  = sqlite3.connect(db_location)
        self.cursor = self.connection.cursor()
        self.table_name = table_name
        self.column_name_1 = column_name_1
        self.column_name_2 = column_name_2

    def write_to_sql_server(self, links):
        sql_command = """INSERT INTO %s (%s, %s) VALUES (?, ?)""" \
                        % (self.table_name, self.column_name_1, self.column_name_2)
        self.cursor.executemany (sql_command, links)
        self.connection.commit()

    def create_table(self):
        sql_command = """
                CREATE TABLE %s (
                    Id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    %s	TEXT,
                    %s  TEXT
                )
                """ % (self.table_name, self.column_name_1, self.column_name_2)
        self.cursor.execute(sql_command)

    def drop_table_if_exists(self):
        sql = "DROP TABLE IF EXISTS %s" % self.table_name
        self.cursor.executescript(sql)
        self.connection.commit()