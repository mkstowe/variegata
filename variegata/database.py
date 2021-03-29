import sys

import mariadb


def get_db():
    with open("../secrets.txt", "r") as f:
        lines = f.readlines()
        username = lines[0].strip()
        password = lines[1].strip()

    try:
        conn = mariadb.connect(
            user=username,
            password=password,
            host="127.0.0.1",
            port=3306,
            database="mkstrnrc_variegata_stories"
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    return conn
