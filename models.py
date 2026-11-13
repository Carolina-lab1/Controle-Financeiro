import sqlite3

def init_db(db_name='financas.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("""
        create table if not exists categorias (
            id integer primary key autoincrement,
            nome text not null,
            tipo text not null
        )
    """)

    cursor.execute("""
        create table if not exists transacoes (
            id integer primary key autoincrement,
            descricao text not null,
            valor real not null,
            data text not null,
            categoria_id integer,
            foreign key (categoria_id) references categorias(id)
        )
    """)

    cursor.execute("select count(*) from categorias")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("insert into categorias (nome, tipo) values (?, ?)", [
            ("Salário", "receita"),
            ("Alimentação", "despesa"),
            ("Moradia", "despesa"),
            ("Lazer", "despesa")
        ])

    # O commit e o close DEVEM estar fora do if, para executarem sempre!
    conn.commit()
    conn.close()

def get_all_transacoes(db_name='financas.db'):
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("""
        select t.id, t.descricao, t.valor, t.data, c.nome as categoria, c.tipo 
        from transacoes t 
        join categorias c on t.categoria_id = c.id
        order by t.data desc
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows

def add_transacoes(descricao, valor, data, categoria_id, db_name='financas.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("""
        insert into transacoes (descricao, valor, data, categoria_id)
        values (?,?,?,?)
    """, (descricao, valor, data, categoria_id))

    conn.commit()
    conn.close()

def get_categorias(db_name='financas.db'):
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("select * from categorias")
    rows = cursor.fetchall()
    conn.close()
    return rows