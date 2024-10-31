import face_recognition
import cv2
import os
import numpy as np

def SingleFaceRecognition(image_path, faces_dir):
    # Load the image to be recognized
    unknown_image = face_recognition.load_image_file(image_path)
    unknown_encoding = face_recognition.face_encodings(unknown_image)

    if not unknown_encoding:
        print("No faces found in the image.")
        return None

    unknown_encoding = unknown_encoding[0]

    # Iterate over all images in the faces directory
    for filename in os.listdir(faces_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            known_image_path = os.path.join(faces_dir, filename)
            known_image = face_recognition.load_image_file(known_image_path)
            known_encodings = face_recognition.face_encodings(known_image)

            if not known_encodings:
                print(f"No faces found in the known image: {filename}")
                continue

            known_encoding = known_encodings[0]

            # Compare the unknown face encoding with the known face encoding
            results = face_recognition.compare_faces([known_encoding], unknown_encoding)
            print(f"Comparing with {filename}: {results}")  # Debug statement

            if results[0]:
                # Return the matched image ID (assuming the filename is the ID)
                matched_image_id = os.path.splitext(filename)[0]
                print(f"Match found: {matched_image_id}")  # Debug statement
                return matched_image_id

    print("No match found.")
    return None

def WebcamFaceRecognition(faces_dir):
    video_capture = cv2.VideoCapture(0)
    known_face_encodings = []
    known_face_names = []

    # Load a sample picture and learn how to recognize it.
    for filename in os.listdir(faces_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            known_image_path = os.path.join(faces_dir, filename)
            known_image = face_recognition.load_image_file(known_image_path)
            known_encodings = face_recognition.face_encodings(known_image)

            if known_encodings:
                known_face_encodings.append(known_encodings[0])
                known_face_names.append(os.path.splitext(filename)[0])

    while True:
        ret, frame = video_capture.read()
        rgb_frame = frame[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Uncomment the following line to test WebcamFaceRecognition
    # WebcamFaceRecognition("Faces")
    SingleFaceRecognition("presidents.jpg", "Faces")