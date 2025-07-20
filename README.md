# Annotation Tool (Qt-based)

A desktop application built using Qt for inspecting bottles. The tool allows manual review and annotation of rotating bottles videos captured at four distinct positions: **Lower**, **Middle**, **Top**, and **Bottom**.

---

## 🧪 Use Case

- The application can be used in numerous sectors that includes visually inspecting a video, frame-by-frame
---

## 🎯 Features

- 📁 Load multiple **Transactions** containing rotating bottle inspection videos.
- 🔍 Navigate:
  - Between **Transactions**
  - Between **Positions** (Lower, Middle, Top, Bottom)
  - Between **Frames** within a position video
- ✅ Annotate each position as:
  - `OK` – Position has no visible defect
  - `NotOK` – Position shows a visible defect
- 🗃️ Output:
  - Annotated positions are saved in folders: `outputs/annotated/OK` and `outputs/annotated/NotOK`
  - A `results.csv` is generated containing:
    - `Transaction ID`
    - `Position`
    - `Reason for rejection` (if NotOK)

---

## 🗂️ Folder Structure(Input/ Output)

- Data/
  - TXN001/
    - Bottom/
      - video.mp4
    - Lower/
    - Middle/
    - Top/
  - TXN002/
   ...
- outputs/
  - annotated/
    - OK/
    - NotOK/
  - results.csv


---

## 🚀 How to Use

1. **Launch the Qt application**
2. **Select the root `Data/` folder**
3. Use navigation buttons to:
   - Move between transactions
   - Move between positions
   - Move frame-by-frame
4. Annotate each position after review
5. Once completed, check `outputs/annotated/` and `results.csv`

---

## 🛠️ Tech Stack

- **Python**
- **PySide6**
- **OpenCV** – For video handling
- **Pandas** – For CSV generation
