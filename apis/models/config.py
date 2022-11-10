import sqlite3
import pandas as pd
from flask import g

DATABASE = "database.db"


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    print("Connecting to Database")
    return db


def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


def df_to_sql(data):
    conn = get_db()
    data.to_sql("orders", conn, if_exists="append", index=False)


def sql_to_df():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT num, px, qty, order_type, order_date, symbol FROM orders")
    columns = ["num", "px", "qty", "order_type", "order_date", "symbol"]
    df = pd.DataFrame(cur.fetchall(), columns=columns)
    if df["px"].dtype != float or df["qty"].dtype != float:
        print("from object to float")
        df["px"] = df["px"].map(float)
        df["qty"] = df["qty"].map(float)
        df["order_type"] = df["order_type"].map(str)
        df["symbol"] = df["symbol"].map(str)
    df.set_index("num")
    return df
