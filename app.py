from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)


def run_query(query_string):
    """
    Runs the query string against the database and returns only one row
    :param query_string: (String) SQL Query string
    :return: (Float/Integer) Returns result from query execution, 0 if No result is obtained
    """

    conn = psycopg2.connect(database='homework', host='localhost', user='root', password='root')
    cur = conn.cursor()
    cur.execute(query_string)
    rs = cur.fetchone()
    conn.close()

    return rs[0] or 0


@app.route("/pax/<int:segment_id>", methods=['GET'])
def get_segment_passenger_count(segment_id):
    query_string = 'SELECT COUNT(1) FROM rides r' \
                   ' JOIN route_segments rs ON rs.route_id = r.route_id' \
                   ' JOIN tickets t ON t.ride_id = r.ride_id' \
                   ' WHERE rs.segment_id = %d;' % segment_id
    count = run_query(query_string)

    results = {
        'segment_id': segment_id, 'pax': count
    }

    return jsonify(results)


@app.route("/revenue/<int:segment_id>", methods=['GET'])
def get_segment_revenue(segment_id):
    query_string = 'SELECT SUM(t.price) FROM rides r' \
                   ' JOIN route_segments rs ON rs.route_id = r.route_id' \
                   ' JOIN tickets t ON t.ride_id = r.ride_id' \
                   ' WHERE rs.segment_id = %d;' % segment_id
    revenue = run_query(query_string)

    results = {
        'segment_id': segment_id, 'revenue': float(revenue)
    }

    return jsonify(results)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
