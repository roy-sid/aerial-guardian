# The Aerial Guardian - Drone-Based Multi-Person Detection and Tracking

**Author:** Siddhant Roy
**Dataset:** VisDrone 2019 MOT Validation Set (Task 4)

## Overview

This project implements a lightweight drone-based multi-person detection and tracking pipeline. The solution is designed to address common challenges in aerial surveillance, including:

* Small person sizes in high-altitude drone footage
* Camera motion caused by drone movement
* Maintaining consistent tracking IDs across frames
* Lightweight deployment constraints (<300 MB)

The final pipeline combines:

* YOLOv8n for person detection
* SAHI for small-object detection through sliced inference
* ByteTrack for multi-object tracking
* Camera Motion Compensation (CMC) using optical flow

---

## Repository Structure

```text
.
├── preprocess.py
├── data.yaml
├── botlab_assignment.ipynb
├── botlab_sahi.ipynb
├── weights/
│   └── best.pt
├── report/
│   └── Aerial_Guardian_Report.pdf
└── sample_output/
```

### File Descriptions

* **preprocess.py** - Converts VisDrone MOT annotations into YOLOv8 format.
* **data.yaml** - YOLO dataset configuration.
* **botlab_assignment.ipynb** - Training and evaluation notebook.
* **botlab_sahi.ipynb** - Detection, tracking, SAHI, and camera motion compensation pipeline.
* **best.pt** - Fine-tuned YOLOv8n model weights.

---

## Dataset

This project uses the VisDrone 2019 MOT Validation Set.

Dataset:
https://github.com/VisDrone/VisDrone-Dataset

After downloading the dataset:

1. Place the dataset locally.
2. Run `preprocess.py` to generate YOLO labels.
3. Update `data.yaml` paths if required.

---

## Installation

```bash
pip install ultralytics==8.4.54
pip install sahi
pip install supervision
pip install opencv-python
pip install Pillow
pip install gdown
```

---

## Training

Open and run:

```text
botlab_assignment.ipynb
```

Training configuration:

* Base model: YOLOv8n
* Epochs: 30
* Batch size: 16
* Image size: 640
* Hardware: NVIDIA T4 GPU (Google Colab)

---

## Detection and Tracking

Open and run:

```text
botlab_sahi.ipynb
```

Pipeline:

```text
Frames
  ↓
YOLOv8n
  ↓
SAHI
  ↓
Camera Motion Compensation
  ↓
ByteTrack
  ↓
Tracked Output Video
```

---

## Results

| Metric                    | Value         |
| ------------------------- | ------------- |
| Model Size                | 6.2 MB        |
| Average FPS (with CMC)    | 3.41          |
| Average FPS (without CMC) | 3.86          |
| Total Frames Processed    | 464           |
| Hardware                  | NVIDIA T4 GPU |

---
## Detection + Tracking

![Tracking Result](sample_output/output_frame (2).jpg)

## Report

Detailed implementation details, design decisions, experiments, and discussion are available in:

```text
report/report_arial_guardian.pdf
```

---

## Future Improvements

* Improve handling of heavy occlusions
* Re-train using improved validation splits
* TensorRT optimization for NVIDIA Jetson deployment
* Better support for top-down drone viewpoints

```
```
