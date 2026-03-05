# Student Marks Data Processing and Reporting System

## RISE Internship - Python Programming
**Tamizhan Skills | Intern: Vijay**

---

## 📌 Project Overview
This project automates the process of analyzing student marks data and generating a detailed report. Instead of manually calculating totals, averages, and grades, this Python script does everything automatically.

---

## 🛠️ Tools & Libraries Used
- Python 3.13
- Pandas - Data processing
- Matplotlib - Chart generation
- CSV - Data storage

---

## 📂 Project Files
| File | Description |
|------|-------------|
| `students.csv` | Input dataset with student marks |
| `report.py` | Main Python script |
| `report_output.csv` | Generated report with grades |
| `chart.png` | Bar chart of student averages |

---

## ⚙️ How It Works
1. Loads student marks from CSV file
2. Cleans the data by removing empty rows
3. Calculates Total, Average and Grade for each student
4. Prints class summary (highest, lowest, class average)
5. Saves the report as a new CSV file
6. Generates a bar chart and saves it as PNG

---

## 📊 Grade System
| Average | Grade |
|---------|-------|
| 90 and above | A+ |
| 80 - 89 | A |
| 70 - 79 | B |
| 60 - 69 | C |
| Below 60 | F |

---

## ▶️ How to Run
```bash
pip install pandas matplotlib
python report.py
```

---

## 📈 Sample Output
- Report saved as `report_output.csv`
- Chart saved as `chart.png`