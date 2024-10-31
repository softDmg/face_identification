import face_recognition
import os
import numpy as np
import cv2

def LoadEncodings(dir):
    faces = os.listdir(dir)
    images_known = []
    for x in faces:
        images_known.append(dir + "/" + x)
    known_face_encodings = []
    known_face_names = []
    for x in images_known:
        known_image = face_recognition.load_image_file(x)
        known_face_encoding = face_recognition.face_encodings(known_image, model="large")[0]
        known_face_encodings.append(known_face_encoding)
        known_face_names.append(os.path.basename(x))

    return known_face_encodings, known_face_names

def SingleFaceRecognition(image, encodings_path):
    image = face_recognition.load_image_file(image)
    face_locations = face_recognition.face_locations(image, model="cnn")
    print(len(face_locations), " faces found")
    face_encodings = face_recognition.face_encodings(image, face_locations, model="large")
    known_face_encodings, known_face_names = LoadEncodings(encodings_path)
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            # Assuming the image name is the ID in the database
            matched_image_id = int(os.path.splitext(name)[0])
            return matched_image_id
    return None

def WebcamFaceRecognition(encodings_path):
    video_capture = cv2.VideoCapture(0)
    known_face_encodings, known_face_names = LoadEncodings(encodings_path)
    print(known_face_encodings)
    while True:
        ret, frame = video_capture.read()
        face_locations = face_recognition.face_locations(frame, model="cnn")
        face_encodings = face_recognition.face_encodings(frame, face_locations, model="large")
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                # insert into mysql here
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, os.path.splitext(name)[0], (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # WebcamFaceRecognition("Faces")
    SingleFaceRecognition("presidents.jpg", "Faces")