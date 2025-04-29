import mysql.connector


def create_mysql_connection(host, user_name, user_pass, db_name):
    try:
        # Replace the placeholders with your actual database credentials
        conn = mysql.connector.connect(
            host=host,
            user=user_name,
            password=user_pass,
            database=db_name
        )
        print("Connection to MySQL database successful!")
        return conn
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None


def execute_query(conn, query):
    """
    this function it will connected to DB and fetch the details based on query
    """
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    except mysql.connector.Error as e:
        print(f"Error executing query: {e}")
