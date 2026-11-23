# CodSoft AI Internship - Task 5
# Face Detection using OpenCV

import cv2


def face_detection():

    print("===================================")
    print("       FACE DETECTION SYSTEM")
    print("===================================")

    # Load Haar Cascade face detector
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )

    if face_cascade.empty():
        print("Error: Face detection model not loaded!")
        return

    # Select image
    image_path = input(
        "\nEnter image path: "
    ).strip().strip('"')

    # Read image
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Unable to load image!")
        return

    # Convert image to grayscale
    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    # Display results
    print("\n===================================")
    print("       DETECTION RESULTS")
    print("===================================")
    print("Total faces detected:", len(faces))

    if len(faces) > 0:
        print("Face detection successful!")
    else:
        print("No faces detected.")

    # Save output
    cv2.imwrite("output.png", image)

    print("\nOutput saved as output.png")

    # Display image
    cv2.imshow("Face Detection Result", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    face_detection()
