from ultralytics import YOLO


def val():
    model = YOLO('model/smoke_and_fire.pt')
    model.val(data='dataset/smoke/data.yaml',
              split='val',
              imgsz=640,
              batch=16,
              iou=0.6,
              rect=False,
              save_json=False,
              project='runs/val',
              name='exp',
              )