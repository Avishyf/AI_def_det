from ultralytics import YOLO

if __name__ == '__main__':
    # Load a YOLOv8 model (use 'yolov8n', 'yolov8s', etc.)
    model = YOLO('yolov8m.pt')

    # Train the model
    model.train(
        data=r'C:\Users\Ronen\OneDrive\Desktop\update_dataset\data.yaml',  # Use absolute path
        epochs=60,
        imgsz=640,
        batch=16,
        name='yolov8m_Final_More',
        pretrained=True,
        # Augmentation settings
        degrees=45,        # rotation (degrees)
        flipud=0.5,         # vertical flip probability
        scale=0.5,         # image scale (resize) augmentation
        lr0=0.004,        # lower initial learning rate
    )