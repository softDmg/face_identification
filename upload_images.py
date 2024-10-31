import os
import mysql.connector

# MySQL configuration
mysql_config = {
    "host": "localhost",
    "user": "my_user",
    "password": "my_password",
    "database": "images_db",
    "port": 3306
}

def upload_images_to_db(folder_path):
    # Connect to the database
    conn = mysql.connector.connect(**mysql_config)
    cursor = conn.cursor()

    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            file_path = os.path.join(folder_path, filename)
            image_id = os.path.splitext(filename)[0]

            # Check if the image already exists in the database
            cursor.execute("SELECT COUNT(*) FROM images_store WHERE id = %s", (image_id,))
            count = cursor.fetchone()[0]

            if count > 0:
                print(f"Image {filename} already exists in the database. Skipping.")
                continue

            # Read the image data and insert it into the database
            with open(file_path, 'rb') as file:
                image_data = file.read()
                query = "INSERT INTO images_store (id, image) VALUES (%s, %s)"
                cursor.execute(query, (image_id, image_data))
                conn.commit()
                print(f"Uploaded {filename} to database")

    # Close the database connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    folder_path = "Faces"  # Path to the folder containing images
    upload_images_to_db(folder_path)