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

def read_image(image_path):
    with Image.open(image_path) as img:
        img_byte_array = io.BytesIO()
        img.save(img_byte_array, format=img.format)
        img_byte_array = img_byte_array.getvalue()
    return img_byte_array

def insert_image_to_db(cursor, image_name, image_data):
    try:
        cursor.execute("""
            INSERT INTO images_store (image_name, image_column) 
            VALUES (%s, %s)
        """, (image_name, image_data))
        print(f"Image '{image_name}' inserted into the database.")
    except Error as e:
        print(f"Error inserting image: {e}")

def main():
    image_path = "1.jpg"
    image_name = image_path.split("/")[-1]
    image_data = read_image(image_path)

    conn = mysql.connector.connect(**mysql_config)
    cursor = conn.cursor()

    insert_image_to_db(cursor, image_name, image_data)
    
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
