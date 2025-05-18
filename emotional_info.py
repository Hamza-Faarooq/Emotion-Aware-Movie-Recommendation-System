from deepface import DeepFace
import cv2

def analyze_face(image_path):
    try:
        # Convert to grayscale for FER2013 compatibility
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(image_path, gray)

        # Analyze with DeepFace
        results = DeepFace.analyze(
            img_path=image_path,
            actions=["emotion"],
            detector_backend="retinaface",
            enforce_detection=False,
            silent=True
        )
        return {
            "dominant_emotion": results[0]["dominant_emotion"],
            "emotions": results[0]["emotion"]
        }
    except Exception as e:
        print(f"Error processing image: {str(e)}")
        return {"dominant_emotion": "neutral", "emotions": {}}


DEEPFACE_TO_TEXT_MAPPING = {
    'angry': 'anger',
    'disgust': 'disgust',
    'fear': 'fear',
    'happy': 'joy',
    'sad': 'sadness',
    'surprise': 'surprise',
    'neutral': 'neutral'
}
