import config

conn, cursor, api = config.start()

assets = api.list_assets()

for asset in assets:
    print(f"Inserting stock {asset.name} {asset.symbol}")
    config.cursor.execute("""
        INSERT INTO stock (name, symbol, exchange, is_etf)
        VALUES (%s, %s, %s, %s)                   
    """, (asset.name, asset.symbol, asset.exchange, False))

conn.commit()