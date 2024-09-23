גירסא creat_forecast_ad_hoc_01
https://github.com/DavidPerelman/creat_forecast_ad_hoc/tree/creat_forecast_ad_hoc_01

**התקנה והרצה של פרויקט תחזית ad_hoc**

**דרישות:**

- מחשב עם Python מותקן (להורדה:[ ](https://www.python.org/)<https://www.python.org/>)
- Visual Studio Code

1\. **התקנת Python**:

- לפני התחלת השימוש, ודאו שפייתון מותקן על המחשב. ניתן להוריד את פייתון מהקישור הבא: <https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe>
- ודאו ש-Python מתווסף לנתיב המערכת.
- <a href="https://www.youtube.com/watch?v=m9I-YpOjXVQ" target="_blank">סרטון הדגמה להתקנה של פייתון</a>

2\. **סביבת עבודה**:

- מומלץ להריץ את הקוד באמצעות סביבת הפיתוח Visual Studio Code. ניתן להוריד את התוכנה מהקישור הבא: <https://code.visualstudio.com/download>

3\. **הורדת הקוד מ-GitHub**:

- לאחר התקנת Visual Studio Code, יש להוריד את הקוד מהגיטהאב בכתובת הבאה: <https://github.com/JTMPT/forecast/tree/main>
- <a href="https://www.youtube.com/watch?v=1a1NDCN8Jog" target="_blank">סרטון הדגמה להורדה מגיטהאב</a>

4\. **יצירת Virtual Environment**:

- פתחו את מסוף הפקודה.
- עברו לתיקיית הפרויקט.
- צרו Virtual Environment באמצעות הפקודה: python -m venv venv
- הפעילו את Virtual Environment באמצעות: venv\Scripts\activate
- ניתן להפעיל Virtual Environment באמצעות Visual Studio Code, להסבר: <https://code.visualstudio.com/docs/python/environments>
- <a href="https://www.youtube.com/watch?v=GZbeL5AcTgw" target="_blank">סרטון הדגמה ליצירת Virtual Environment באמצעות Visual Studio Code</a>

5\. **התקנת ספריות**:

- התקינו את הספריות מהקובץ requirements.txt באמצעות הפקודה: pip install -r requirements.txt
- אם נתקלתם בשגיאות "No module named", התקינו את הספריות החסרות ידנית.
- <a href="https://www.youtube.com/watch?v=2hojzuyddaA" target="_blank">סרטון הדגמה להתקנת ספריות</a>

6\. **התקנת תוספים**:

- התקינו את התוספים של Python ו-Jupyter ב-Visual Studio Code.
- <a href="https://marketplace.visualstudio.com/items?itemName=ms-python.python" target="_blank">הסבר על התקנת התוספים</a>

7\. **יצירת תיקיות פלט**:

- צרו תיקיית פלט בשם forecast_by_version.
- בתוך תיקיית forecast_by_version, צרו תיקייה בשם V4.
- בתוך תיקיית V4, צרו תיקייה בשם OVERVIEW ודאו שהיא כתובה באותיות גדולות.
- בתוך תיקיית V4, צרו תיקייה בשם SHP ודאו שהיא כתובה באותיות גדולות.
- בתוך תיקיית V4, צרו תיקייה בשם: BASE_YEAR. ודאו שהיא כתובה באותיות גדולות.

- צרו תיקיית לקוח (במיקום שונה מתיקיית forecast_by_version).
- בתוך תיקיית לקוח, צרו תיקייה בשם For_approval.
- בתוך תיקיית For_approval, צרו תיקייה בשם Reference_tabels.
- בתוך תיקיית Reference_tabels, צרו תיקייה בשם shp.
- הכניסו את השכבות הרציות לתיקיית shp.

8\. **הגדרת נתיב תיקיית הפלט**:

- בתיקיית create_forecast_ad_hoc, פתחו את הקובץ inputs_outputs.xlsx.
- ערוך את הקובץ והזן בשורה 2 בעמודה B (location) את הנתיב של תיקיית לקוח שיצרתם. לדוגמה: C:\Users\username\Documents\client.
- ערוך את הקובץ והזן בשורה 3 בעמודה B (location) את שם התרחיש (forecast_version). לדוגמה: with_project.
- ערוך את הקובץ והזן בשורה 3 בעמודה B (location) תאריך (v_date). לדוגמה: 240530.
- ערוך את הקובץ והזן בשורה 3 בעמודה B (location) את הנתיב של תיקיית לקוח שיצרתם. לדוגמה: C:\Users\username\Documents\forecast_by_version\V4\BASE_YEAR.

9\. **הרצת הפרויקט**:

- פתחו את הקובץ main.py שנמצא בתיקייה py_scripts שנמצאת בתיקייה create_forecast_ad_hoc.
- הריצו את הקוד בקובץ.

**הערות**:

- על מנת שהקוד ירוץ כמו שצריך, אין לשנות את סדר התיקיות בפרויקט תיקיית הפלט!
