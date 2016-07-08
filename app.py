import config
from flask import Flask, jsonify


app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)

@app.route("/pax/<segment_id>", methods=['GET'])
def get_segment_passenger_count(segment_id):
    import psycopg2
    conn = psycopg2.connect(database='homework', host='localhost', user='root', password='root')

    cur = conn.cursor()
    query_string = """SELECT COUNT(1) FROM rides r JOIN route_segments rs ON rs.route_id = r.route_id JOIN tickets t ON t.ride_id = r.ride_id WHERE rs.segment_id = %s;""" % segment_id
    cur.execute(query_string)


    rows = cur.fetchall()
    count = 0
    for row in rows:
        print(row)
        count = row[0]
    results = {
        'segment_id': segment_id, 'pax': count
    }
    conn.close()
    return jsonify(results)


@app.route("/revenue/<segment_id>", methods=['GET'])
def get_segment_revenue(segment_id):
    import psycopg2
    conn = psycopg2.connect(database='homework', host='localhost', user='root', password='root')

    cur = conn.cursor()
    query_string = """SELECT SUM(t.price) FROM rides r JOIN route_segments rs ON rs.route_id = r.route_id JOIN tickets t ON t.ride_id = r.ride_id WHERE rs.segment_id = %s;""" % segment_id
    cur.execute(query_string)

    rows = cur.fetchall()
    revenue = 0
    for row in rows:
        print(row)
        revenue = row[0]
    results = {
        'segment_id': segment_id, 'revenue': float(revenue)
    }
    conn.close()
    return jsonify(results)


if __name__ == '__main__':
    app.run()
