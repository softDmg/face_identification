# import sys
# from PyQt5 import QtWidgets, QtGui, QtCore
# from gui import Ui_MainWindow
# import mysql.connector
# from FaceRec import SingleFaceRecognition
# import io
# from PIL import Image
# from PyQt5.QtGui import QPixmap
# import cv2
# import numpy as np
# import face_recognition

# mysql_config = {
#     "host": "localhost",
#     "user": "my_user",
#     "password": "my_password",
#     "database": "images_db",
#     "port": 3306
# }

# def get_image_from_db(cursor, image_id):
#     query = "SELECT image FROM images_store WHERE id = %s"
#     cursor.execute(query, (image_id,))
#     result = cursor.fetchone()
#     # print(f"Query Result: {result}")  # Debug statement
#     if result:
#         return result[0]
#     return None

# class MainApp(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)

#         # Connect buttons in tab_2 to their respective functions
#         self.ui.load_image_button_2.clicked.connect(self.load_image)
#         self.ui.match_image_button_2.clicked.connect(self.match_image)

#         self.loaded_image_path = None

#     def load_image(self):
#         # Function to load an image
#         self.ui.new_image_2.clear()
#         options = QtWidgets.QFileDialog.Options()
#         fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Load Image", "", "Images (*.png *.xpm *.jpg);;All Files (*)", options=options)
#         if fileName:
#             self.loaded_image_path = fileName
#             pixmap = QtGui.QPixmap(fileName)
#             scaled_pixmap = pixmap.scaled(self.ui.original_image_2.size(), QtCore.Qt.KeepAspectRatio)
#             self.ui.original_image_2.setPixmap(scaled_pixmap)
#             self.ui.MessageLabel_2.setText("Image Loaded")

#     def match_image(self):
#         if not self.loaded_image_path:
#             self.ui.MessageLabel_2.setText("No image loaded")
#             return

#         # Connect to the database
#         try:
#             conn = mysql.connector.connect(**mysql_config)
#             cursor = conn.cursor()

#             # Perform face recognition and get the matched image ID
#             matched_image_id = SingleFaceRecognition(self.loaded_image_path, "Faces")
#             # print(f"Matched Image ID: {matched_image_id}")  # Debug statement

#             if matched_image_id:
#                 # Retrieve the matched image from the database
#                 try:
#                     image_data = get_image_from_db(cursor, matched_image_id)
#                     # print(f"Image Data: {image_data is not None}")  # Debug statement
#                     if image_data:
#                         self.display_matched_image(image_data, matched_image_id)
#                         self.ui.MessageLabel_2.setText("Match found")
#                     else:
#                         self.ui.MessageLabel_2.setText("No match found in database")
#                 except mysql.connector.Error as err:
#                     print(f"Error retrieving image: {err}")
#                     self.ui.MessageLabel_2.setText("Error retrieving image from database")
#             else:
#                 self.ui.MessageLabel_2.setText("No match found")

#         except mysql.connector.Error as err:
#             print(f"Error connecting to database: {err}")
#             self.ui.MessageLabel_2.setText("Error connecting to database")

#         finally:
#             cursor.close()
#             conn.close()

#     def display_matched_image(self, image_data, matched_name):
#         # Display the matched image in the new_image_2 label
#         image = Image.open(io.BytesIO(image_data))
#         image_np = np.array(image)

#         # Convert image to BGR (OpenCV uses BGR by default)
#         image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

#         # Detect faces in the image
#         face_locations = face_recognition.face_locations(image_bgr, model="cnn")

#         # Draw rectangles around detected faces and put the name
#         for (top, right, bottom, left) in face_locations:
#             cv2.rectangle(image_bgr, (left, top), (right, bottom), (0, 255, 0), 2)
#             cv2.putText(image_bgr, matched_name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 5)

#         # Convert back to RGB for PIL
#         image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
#         image_with_rectangles = Image.fromarray(image_rgb)

#         # Save the image with rectangles
#         image_with_rectangles.save("matched_image_with_rectangles.jpg")

#         # Display the image with rectangles in the new_image_2 label
#         pixmap = QtGui.QPixmap("matched_image_with_rectangles.jpg")
#         scaled_pixmap = pixmap.scaled(self.ui.new_image_2.size(), QtCore.Qt.KeepAspectRatio)
#         self.ui.new_image_2.setPixmap(scaled_pixmap)

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     mainWindow = MainApp()
#     mainWindow.show()
#     sys.exit(app.exec_())
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from gui import Ui_MainWindow
import mysql.connector
from FaceRec import SingleFaceRecognition
import io
from PIL import Image
from PyQt5.QtGui import QPixmap
import cv2
import numpy as np
import face_recognition

mysql_config = {
    "host": "localhost",
    "user": "my_user",
    "password": "my_password",
    "database": "images_db",
    "port": 3306
}

def get_image_from_db(cursor, image_id):
    query = "SELECT image FROM images_store WHERE id = %s"
    cursor.execute(query, (image_id,))
    result = cursor.fetchone()
    print(f"Query Result: {result}")  # Debug statement
    if result:
        return result[0]
    return None

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect buttons in tab_2 to their respective functions
        self.ui.load_image_button_2.clicked.connect(self.load_image)
        self.ui.match_image_button_2.clicked.connect(self.match_image)

        self.loaded_image_path = None

    def load_image(self):
        # Function to load an image
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Load Image", "", "Images (*.png *.xpm *.jpg);;All Files (*)", options=options)
        if fileName:
            self.loaded_image_path = fileName
            pixmap = QtGui.QPixmap(fileName)
            scaled_pixmap = pixmap.scaled(self.ui.original_image_2.size(), QtCore.Qt.KeepAspectRatio)
            self.ui.original_image_2.setPixmap(scaled_pixmap)
            self.ui.MessageLabel_2.setText("Image Loaded")

    def match_image(self):
        if not self.loaded_image_path:
            self.ui.MessageLabel_2.setText("No image loaded")
            return

        # Connect to the database
        try:
            conn = mysql.connector.connect(**mysql_config)
            cursor = conn.cursor()

            # Perform face recognition and get the matched image ID
            matched_image_id = SingleFaceRecognition(self.loaded_image_path, "Faces")
            print(f"Matched Image ID: {matched_image_id}")  # Debug statement

            if matched_image_id:
                # Retrieve the matched image from the database
                try:
                    image_data = get_image_from_db(cursor, matched_image_id)
                    print(f"Image Data: {image_data is not None}")  # Debug statement
                    if image_data:
                        self.display_matched_image(image_data, matched_image_id)
                        self.ui.MessageLabel_2.setText("Match found")
                    else:
                        self.ui.MessageLabel_2.setText("No match found in database")
                except mysql.connector.Error as err:
                    print(f"Error retrieving image: {err}")
                    self.ui.MessageLabel_2.setText("Error retrieving image from database")
            else:
                # No match found, draw rectangles with "unknown" label
                self.draw_unknown_faces(self.loaded_image_path)
                self.ui.MessageLabel_2.setText("No match found")

        except mysql.connector.Error as err:
            print(f"Error connecting to database: {err}")
            self.ui.MessageLabel_2.setText("Error connecting to database")

        finally:
            cursor.close()
            conn.close()

    def draw_unknown_faces(self, image_path):
        # Load the image
        image = Image.open(image_path)
        image_np = np.array(image)

        # Convert image to BGR (OpenCV uses BGR by default)
        image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

        # Detect faces in the image
        face_locations = face_recognition.face_locations(image_bgr, model="cnn")

        # Draw rectangles around detected faces and put the "unknown" label
        for (top, right, bottom, left) in face_locations:
            cv2.rectangle(image_bgr, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(image_bgr, "unknown", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 5)

        # Convert back to RGB for PIL
        image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
        image_with_rectangles = Image.fromarray(image_rgb)

        # Save the image with rectangles
        image_with_rectangles.save("unknown_faces.jpg")

        # Display the image with rectangles in the new_image_2 label
        pixmap = QtGui.QPixmap("unknown_faces.jpg")
        scaled_pixmap = pixmap.scaled(self.ui.new_image_2.size(), QtCore.Qt.KeepAspectRatio)
        self.ui.new_image_2.setPixmap(scaled_pixmap)

    def display_matched_image(self, image_data, matched_name):
        # Display the matched image in the new_image_2 label
        image = Image.open(io.BytesIO(image_data))
        image_np = np.array(image)

        # Convert image to BGR (OpenCV uses BGR by default)
        image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

        # Detect faces in the image
        face_locations = face_recognition.face_locations(image_bgr, model="cnn")

        # Draw rectangles around detected faces and put the name
        for (top, right, bottom, left) in face_locations:
            cv2.rectangle(image_bgr, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(image_bgr, matched_name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 5)

        # Convert back to RGB for PIL
        image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
        image_with_rectangles = Image.fromarray(image_rgb)

        # Save the image with rectangles
        image_with_rectangles.save("matched_image_with_rectangles.jpg")

        # Display the image with rectangles in the new_image_2 label
        pixmap = QtGui.QPixmap("matched_image_with_rectangles.jpg")
        scaled_pixmap = pixmap.scaled(self.ui.new_image_2.size(), QtCore.Qt.KeepAspectRatio)
        self.ui.new_image_2.setPixmap(scaled_pixmap)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainApp()
    mainWindow.show()
    sys.exit(app.exec_())