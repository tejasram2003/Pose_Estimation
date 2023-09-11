import os
import cv2
import mediapipe as mp
import argparse
import warnings

warnings.filterwarnings("ignore")

def estimate_pose(image_path, threshold=0.1):
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb)
    if results.pose_landmarks is not None:
        hip_y = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].y
        knee_y = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE].y

        difference =  knee_y - hip_y

        if difference < threshold and difference > 0:
            status = "SITTING"
        else:
            status = "STANDING"

    # Annotate the image with the status
    cv2.putText(image, status, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    #Creating a filename
    filename = os.path.basename(image_path)
    filename, _ = os.path.splitext(filename)
    directory_name = 'outputs'
    os.makedirs(directory_name, exist_ok=True)


    # Save or display the annotated image
    cv2.imwrite(os.path.join(directory_name,filename+"output.jpg"), image)
    cv2.imshow("Estimated Pose", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Estimate whether a person is sitting or standing in an image.")
    parser.add_argument("--image_path", type=str, help="Path to the input image")
    parser.add_argument("--threshold", type=float, default=0.1, help="Threshold for classifying sitting or standing")
    args = parser.parse_args()
    estimate_pose(args.image_path, args.threshold)
