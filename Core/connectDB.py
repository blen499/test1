import datetime
from time import time

import psycopg2
import random

def connect():
    string = "host='localhost' port='5432' dbname='testdb' user='postgres' password='12345'"
    conn = psycopg2.connect(string)
    return conn.cursor()


def select(sql):
    cur = connect()

    cur.execute(f"""
            {sql}
    """)

    a = cur.fetchall()

    cur.close()

    return a

def update(sql):
    cur = connect()

    cur.execute(f"""
            {sql}
    """)

    cur.close()

    return True


def getRandomClient():
    query = select("select distinct first_name, last_name from famousppl where in_wiki = TRUE")

    rnd = random.randint(0,(len(query)-2))

    a = " ".join(map(str, query[rnd]))

    return a


def checkUpdateClient(str, newDate):
    arr = str.split()
    query = select(f"""select distinct updated_at from famousppl where first_name ='{arr[0]}'and last_name = '{arr[1]}'""")
    a = query[0][0].strftime("%Y-%m-%d")

    if a == newDate:
        return
    else:
        print(2)
        query = update(f"""
                        update famousppl
                            set updated_at = '{newDate}'
                                where first_name = '{arr[0]}'
                                and last_name = '{arr[1]}';
                        commit;
                        """)


