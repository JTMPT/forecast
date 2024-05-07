**התקנה והרצה של פרויקט תחזית ABM**

**דרישות:**

- מחשב עם Python מותקן (להורדה:[ ](https://www.python.org/)<https://www.python.org/>)
- Visual Studio Code

1\. **התקנת Python**:

- לפני התחלת השימוש, ודאו שפייתון מותקן על המחשב. ניתן להוריד את פייתון מהקישור הבא: <https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe>
- ודאו ש-Python מתווסף לנתיב המערכת.
- סרטון הדגמה להתקנה של פייתון: <https://www.youtube.com/watch?v=m9I-YpOjXVQ>

2\. **סביבת עבודה**:

- מומלץ להריץ את הקוד באמצעות סביבת הפיתוח Visual Studio Code. ניתן להוריד את התוכנה מהקישור הבא: <https://code.visualstudio.com/download>

3\. **הורדת הקוד מ-GitHub**:

- לאחר התקנת Visual Studio Code, יש להוריד את הקוד מהגיטהאב בכתובת הבאה: <https://github.com/JTMPT/forecast/tree/create_ABM_forecast_v1.7>
- סרטון הדגמה להורדה מגיטהאב: <https://www.youtube.com/watch?v=1a1NDCN8Jog>

4\. **יצירת Virtual Environment**:

- פתחו את מסוף הפקודה.
- עברו לתיקיית הפרויקט.
- צרו Virtual Environment באמצעות הפקודה: python -m venv venv
- הפעילו את Virtual Environment באמצעות: venv\Scripts\activate
- ניתן להפעיל Virtual Environment באמצעות Visual Studio Code, להסבר: <https://code.visualstudio.com/docs/python/environments>
- סרטון הדגמה ליצירת Virtual Environment באמצעות Visual Studio Code: <https://www.youtube.com/watch?v=GZbeL5AcTgw>



5\. **התקנת ספריות**:

- התקינו את הספריות מהקובץ requirements.txt באמצעות הפקודה: pip install -r requirements.txt
- אם נתקלתם בשגיאות "No module named", התקינו את הספריות החסרות ידנית.
- סרטון הדגמה להתקנת ספריות: <https://www.youtube.com/watch?v=2hojzuyddaA>

6\. **התקנת תוספים**:

- התקינו את התוספים של Python ו-Jupyter ב-Visual Studio Code.
- הסבר: <https://marketplace.visualstudio.com/items?itemName=ms-python.python>

7\. **יצירת תיקיות פלט**:

- צרו תיקיית פלט בשם forecast\_by\_version.
- בתוך תיקיית forecast\_by\_version, צרו תיקייה בשם V4.
- בתוך תיקיית V4, צרו 3 תיקיות: BASE\_YEAR, BAU, IPLAN ו-JTMT. ודאו שהן כתובות באותיות גדולות.

8\. **הגדרת נתיב תיקיית הפלט**:

- בתיקיית create\_forecast\_basic, פתחו את הקובץ background\_files/forecast\_version\_folder\_location.txt.
- ערוך את הקובץ והזן את הנתיב של תיקיית V4 שיצרתם. לדוגמה: C:\Users\username\Documents\forecast\_by\_version\V4.

9\. **הרצת הפרויקט**:

- פתחו את הקובץ run\_basic.ipynb בתיקיית create\_forecast\_basic.
- הריצו את הקוד בקובץ.

**הערות**:

- ניתן למצוא מידע נוסף על התקנה והרצה של פרויקטי Jupyter Notebooks ב-Visual Studio Code בתיעוד הרשמי: <https://code.visualstudio.com/docs/datascience/jupyter-notebooks>
- על מנת שהקוד ירוץ כמו שצריך, אין לשנות את סדר התיקיות בפרויקט תיקיית הפלט!
