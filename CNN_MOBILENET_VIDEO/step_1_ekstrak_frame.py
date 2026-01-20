import cv2
import os

VIDEO_DIR = "Video_BISINDO"
OUTPUT_DIR = "Citra_BISINDO"

FRAME_SKIP = 5
RESIZE = (256, 256)

os.makedirs(OUTPUT_DIR, exist_ok=True)

print(" Folder huruf:", os.listdir(VIDEO_DIR))

for label in os.listdir(VIDEO_DIR):
    label_path = os.path.join(VIDEO_DIR, label)

    if not os.path.isdir(label_path):
        continue

    video_files = [
        f for f in os.listdir(label_path)
        if f.lower().endswith(('.mp4', '.avi', '.mov', '.mkv'))
    ]
    
    if len(video_files) == 0:
        print(f"Tidak ada video di folder {label}")
        continue

    video_name = video_files[0] 
    video_path = os.path.join(label_path, video_name)

    print(f"Processing {label} → {video_name}")

    output_label_dir = os.path.join(OUTPUT_DIR, label.upper())
    os.makedirs(output_label_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Gagal membuka video {video_name}")
        continue

    frame_idx = 0
    saved = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame_idx % FRAME_SKIP == 0:
            frame = cv2.resize(frame, RESIZE)
            cv2.imwrite(
                os.path.join(output_label_dir, f"{label}_{saved:04d}.jpg"),
                frame
            )
            saved += 1

        frame_idx += 1
    cap.release()
    print(f" {label.upper()} → {saved} frame disimpan\n")
