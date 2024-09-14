import sqlite3
import logging


class Database:
    def __init__(self, path_to_db: str):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        con = sqlite3.connect(self.path_to_db)
        con.row_factory = sqlite3.Row
        return con

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
            data = [dict(row) for row in data]
        if fetchone:
            data = cursor.fetchone()
            data = dict(data) if data else None
        connection.close()
        return data

    def create_table_lot(self):
        sql = """
        CREATE TABLE IF NOT EXISTS tender (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lot_id INTEGER NOT NULL,
            lot_status INTEGER NOT NULL
            );"""
        self.execute(sql, commit=True)

    def addLotData(self, lot_id: int, lot_status: int):
        sql = """INSERT INTO tender(lot_id, lot_status) VALUES(?, ?)"""
        self.execute(sql, parameters=(lot_id, lot_status), commit=True)

    def getLotData(self, lot_id: int):
        sql = """SELECT * FROM tender WHERE lot_id=?;"""
        return self.execute(sql, parameters=(lot_id,), fetchone=True)

    def getAllData(self):
        sql = """SELECT * FROM tender ORDER BY id;"""
        return self.execute(sql, fetchall=True)

    def updateLotStatus(self, lot_id: int, lot_status: int):
        sql = """UPDATE tender SET lot_status=? WHERE lot_id=?"""
        return self.execute(sql, parameters=(lot_status, lot_id), commit=True)

    def deleteLotData(self, lot_id: int):
        sql = """DELETE FROM tender WHERE lot_id=?"""
        self.execute(sql, parameters=(lot_id,), commit=True)

    def delete_all(self):
        sql = """DELETE FROM tender;"""
        try:
            self.execute(sql, commit=True)
        except Exception as e:
            logging.error(e)
            return None


def logger(statement):
    msg = f"""
    ----------------------------------------------------
    Executing:
    {statement}
    ----------------------------------------------------
    """
    logging.info(msg=msg)
