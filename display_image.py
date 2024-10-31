import mysql.connector
from mysql.connector import Error
from PIL import Image
import io

mysql_config = {
    "host": "localhost",
    "user": "my_user",
    "password": "my_password",
    "database": "images_db" 
}

def get_image_from_db(cursor, image_id):
    try:
        cursor.execute("SELECT image_column FROM images_store WHERE id = %s", (image_id,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            print("Image not found.")
            return None
    except Error as e:
        print(f"Error retrieving image: {e}")
        return None

def display_image(image_data):
    if image_data is not None:
        print(image_data)
        image = Image.open(io.BytesIO(image_data))
        image.show()
    else:
        print("No image data to display.")

def main():
    image_id = 1

    conn = mysql.connector.connect(**mysql_config)
    cursor = conn.cursor()

    image_data = get_image_from_db(cursor, image_id)

    display_image(image_data)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
