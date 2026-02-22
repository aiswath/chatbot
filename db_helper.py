import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Root@1234",
        database="pandeyji_eatery",
        port=3306
    )


# Function to call the MySQL stored procedure and insert an order item
def insert_order_item(food_item, quantity, order_id):
    try:
        cnx = get_connection()
        cursor = cnx.cursor()

        cursor.callproc('insert_order_item', (food_item, quantity, order_id))
        cnx.commit()

        cursor.close()
        cnx.close()

        print("Order item inserted successfully!")
        return 1

    except mysql.connector.Error as err:
        print(f"Error inserting order item: {err}")
        return -1


def insert_order_tracking(order_id, status):
    cnx = get_connection()
    cursor = cnx.cursor()

    query = "INSERT INTO order_tracking (order_id, status) VALUES (%s, %s)"
    cursor.execute(query, (order_id, status))

    cnx.commit()
    cursor.close()
    cnx.close()


def get_total_order_price(order_id):
    cnx = get_connection()
    cursor = cnx.cursor()

    query = "SELECT get_total_order_price(%s)"
    cursor.execute(query, (order_id,))
    result = cursor.fetchone()[0]

    cursor.close()
    cnx.close()
    return result


def get_next_order_id():
    cnx = get_connection()
    cursor = cnx.cursor()

    cursor.execute("SELECT MAX(order_id) FROM orders")
    result = cursor.fetchone()[0]

    cursor.close()
    cnx.close()

    return 1 if result is None else result + 1


def get_order_status(order_id):
    cnx = get_connection()
    cursor = cnx.cursor()

    query = "SELECT status FROM order_tracking WHERE order_id = %s"
    cursor.execute(query, (order_id,))
    result = cursor.fetchone()

    cursor.close()
    cnx.close()

    return result[0] if result else None
