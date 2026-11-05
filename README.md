# Bahraini Dishes Detection

Object detection of traditional Bahraini dishes, fine-tuned in two iterations (v1 and v2).

**Classes (10):** Aseeda, Balaleet, Bayd w Tamat, Halwa, Harees, Kabab, Luqaimat, Machboos, Samboosa, Tikka.

**🔗 Deployed Model:** <LINK>

## Project Files

```
├── app.py              # Streamlit app: upload a dish photo, get detections
├── best.pt             # Final trained model used by the app
├── notebooks/
│   ├── ver_1.ipynb     # Fine-tuning and evaluation of v1
│   └── ver_2.ipynb     # Fine-tuning and evaluation of v2
├── requirements.txt
└── README.md
```

## Dataset
- 332 collected images, uploaded and annotated in Roboflow <https://universe.roboflow.com/alfadhul-almubarak/bahraini-dishes>
- Exported in YOLO format

**Preprocessing**
- Auto-Orient: applied
- Resize: stretch to 512x512

**Augmentation** (4 outputs per training example)
- Flip: horizontal
- Rotation: between -45° and +45°
- Brightness: between -20% and +20%
- Blur: up to 0.1px
- Noise: up to 0.93% of pixels

## Models

| Model | Change | Train | Validation | Test |
|-------|--------|-------|------------|------|
| Fine-tuned v1 | Initial dataset | 960 | 52 | 33 |
| Fine-tuned v2 | Added 10 more Harees images | 980 | 53 | 34 |

## Results

### Overall (test set)

| Model | Precision | Recall | mAP50 | mAP50-95 |
|-------|-----------|--------|-------|----------|
| v1 | 0.774 | 0.676 | 0.800 | 0.585 |
| v2 | 0.867 | 0.686 | 0.839 | 0.615 |

v2 improved on all four metrics.

### Per class (mAP50)

| Class | v1 | v2 |
|-------|----|----|
| Aseeda | 0.789 | 0.863 |
| Balaleet | 0.962 | 0.995 |
| Bayd w Tamat | 0.995 | 0.995 |
| Halwa | 0.927 | 0.898 |
| Harees | 0.684 | 0.806 |
| Kabab | 0.708 | 0.608 |
| Luqaimat | 0.234 | 0.587 |
| Machboos | 0.995 | 0.995 |
| Samboosa | 0.903 | 0.807 |

Harees (the class we added images for) rose from 0.684 to 0.806.

## Most Common Errors

**v1**

| Predicted | Actual | Confidence |
|-----------|--------|------------|
| Harees | Halwa | 0.78 |
| Harees | Aseeda | 0.50 |
| Harees | Balaleet | 0.44 |
| Aseeda | Bayd w Tamat | 0.40 |

**v2**

| Predicted | Actual | Confidence |
|-----------|--------|------------|
| Harees | Samboosa | 0.74 |
| Aseeda | Harees | 0.57 |
| Aseeda | Halwa | 0.31 |
| Kabab | Harees | 0.27 |
| Machboos | Bayd w Tamat | 0.25 |


## Limitations

- The test set is small (33-34 images).
- Visually similar, porridge-like dishes (Harees, Aseeda, Halwa) are the main source of confusion.

## Next Steps

- Add more images for the weakest classes (Kabab, Luqaimat, Aseeda)
- Enlarge the test set