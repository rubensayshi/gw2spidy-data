import sys
import MySQLdb
import json, requests

assert MySQLdb.paramstyle == 'format'

db = None
try:
    db = MySQLdb.connect('localhost', 'root', 'root', 'gw2spidy-data')
except MySQLdb.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

def process_item(item):
    insert_item(item)


def insert_item(item):
    cursor = db.cursor()

    print item

    cursor.execute("""
    REPLACE INTO `item`
    (data_id, name, type_id, sub_type_id, max_offer_unit_price, min_sale_unit_price)
    VALUES
    (%s, %s, %s, %s, %s, %s)
    """, (item['data_id'], unicode(item['name']).encode('utf-8'), item['type_id'], item['sub_type_id'], item['max_offer_unit_price'], item['min_sale_unit_price']))
    db.commit()



def fetch_all_items():
    request = requests.get("http://www.gw2spidy.com/api/v0.9/json/all-items/all")
    data = request.json()

    return data['results']





if __name__ == "__main__":
    items = fetch_all_items()

    print "processing %d items" % (len(items))

    i = 0
    for item in items:
        process_item(item)

        i += 1

        if i % 100 == 0:
            print "."