import sqlite3


class MemoryDatabase:

    def __init__(self):

        self.db = sqlite3.connect(
            "memory.db",
            check_same_thread=False
        )

        self.cursor = self.db.cursor()

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS chat(

            id INTEGER PRIMARY KEY,

            user TEXT,

            ai TEXT

            )
            """
        )

        self.db.commit()

    def save(
        self,
        user,
        ai
    ):

        self.cursor.execute(

            """
            INSERT INTO chat(user,ai)

            VALUES(?,?)
            """,

            (
                user,
                ai
            )

        )

        self.db.commit()

    def get_history(self):

        self.cursor.execute(

            """
            SELECT user,ai

            FROM chat

            ORDER BY id DESC

            LIMIT 20
            """

        )

        return self.cursor.fetchall()[::-1]