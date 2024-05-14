import sqlite3


def mb_db(cpu, price_max, price_min):

    socket = cpu[8]

    con = sqlite3.connect('pcdb.db')
    cur = con.cursor()

    cur.execute(f"SELECT * FROM motherboard_parameters "
                f"WHERE (price <= {price_max}) "
                f"AND (price >= {price_min}) "
                f"AND (socket = '{socket}')")

    selection = cur.fetchall()

    return selection


def psu_db(price_max, price_min):
    con = sqlite3.connect('pcdb.db')
    cur = con.cursor()

    cur.execute(f'SELECT * FROM psu_parameters '
                f'WHERE (price <= {price_max})'
                f'AND (price >=  {price_min})')
    selection = cur.fetchall()

    return selection


def db_sel(table, price_max, price_min):
    con = sqlite3.connect('pcdb.db')
    cur = con.cursor()
    selection = None
    if table == "cpu":
        cur.execute(f'SELECT * FROM cpu_parameters '
                    f'WHERE (price <= {price_max})'
                    f'AND (price >=  {price_min})')
        selection = cur.fetchall()

    if table == "gpu":
        cur.execute(f'SELECT * FROM gpu_parametrs '
                    f'WHERE (price <= {price_max})'
                    f'AND (price >=  {price_min})')
        selection = cur.fetchall()

    if table == "psd":
        cur.execute(f'SELECT * FROM storage_parameters '
                    f'WHERE (price <= {price_max})'
                    f'AND (price >=  {price_min})')
        selection = cur.fetchall()

    if table == "ram":
        cur.execute(f'SELECT * FROM ram_parameters '
                    f'WHERE (price <= {price_max})'
                    f'AND (price >=  {price_min})')
        selection = cur.fetchall()

    return selection


def db_pc_list(pcl):
    price = pcl[0][-1] + pcl[1][-1] + pcl[2][-1] + pcl[3][-1] + pcl[4][-1] + pcl[5][-1]
    con = sqlite3.connect("pcdb.db")
    cur = con.cursor()

    cur.execute("INSERT INTO pc (cpu, gpu, motherboard, psd, ram, ps, price) "
                "VALUES (?, ?, ?, ?, ?, ?, ?)",
                (pcl[0][0], pcl[1][0], pcl[2][0], pcl[3][0], pcl[4][0], pcl[5][0], price))

    con.commit()

    return price
