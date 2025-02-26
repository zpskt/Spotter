import kagglehub

def download_smoke_fire_dataset():
    path = kagglehub.dataset_download("sayedgamal99/smoke-fire-detection-yolo")
    return path