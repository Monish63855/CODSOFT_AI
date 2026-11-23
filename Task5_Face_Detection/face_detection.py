# ==========================================
# CODSOFT AI INTERNSHIP
# TASK 5 - FACE DETECTION SYSTEM
# ==========================================

import cv2
import os


def face_detection():

    print("=" * 50)
    print("          FACE DETECTION SYSTEM")
    print("=" * 50)

    # Load Haar Cascade model
    cascade_path = (
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )

    face_cascade = cv2.CascadeClassifier(cascade_path)

    if face_cascade.empty():
        print("Error: Face detection model not loaded!")
        return

    # Get image path
    image_path = input("\nEnter image path: ").strip().strip('"')

    # Check image file
    if not os.path.exists(image_path):
        print("Error: Image file not found!")
        return

    # Read image
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Unable to read image!")
        return

    # Convert image into grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw rectangle around detected faces
    for index, (x, y, w, h) in enumerate(faces, start=1):

        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            3
        )

        cv2.putText(
            image,
            f"Face {index}",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    # Display results
    print("\n" + "=" * 50)
    print("             DETECTION RESULTS")
    print("=" * 50)

    print("Total Faces Detected:", len(faces))

    if len(faces) > 0:
        print("Status: Face Detection Successful!")
    else:
        print("Status: No Faces Detected!")

    # Save output image
    output_path = "output.png"

    cv2.imwrite(output_path, image)

    print("\nOutput saved successfully:", output_path)

    print("=" * 50)

    # Display detected image
    cv2.imshow("Face Detection Result", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Main program
if __name__ == "__main__":
    face_detection()
