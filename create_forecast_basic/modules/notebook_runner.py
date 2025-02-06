import os
import papermill as pm

def run_notebook(notebook_path, output_dir="output_notebooks"):
    """
    הרצת מחברת Jupyter עם פרמטרים נתונים ושמירת הפלט בתיקייה נפרדת.

    notebook_path: נתיב למחברת ה-Jupyter.
    output_dir: נתיב לתיקיית הפלט (ברירת מחדל: output_notebooks).

    מחזירה True אם ההרצה הצליחה, אחרת זורקת את החריגה.
    """
    try:
        # יצירת תיקיית הפלט אם היא לא קיימת
        os.makedirs(output_dir, exist_ok=True)
        
        # יצירת נתיב למחברת הפלט
        notebook_name = os.path.basename(notebook_path).replace('.ipynb', '_output.ipynb')
        output_notebook_path = os.path.join(output_dir, notebook_name)

        # הפעלת המחברת ושמירת הפלט בתיקיית היעד
        pm.execute_notebook(
            notebook_path,  # נתיב למחברת המקורית
            output_notebook_path,  # נתיב למחברת הפלט
        )
        print(f"Notebook executed successfully: {output_notebook_path}")
        return True
    except pm.exceptions.PapermillExecutionError as pm_error:
        print(f"Error executing notebook '{notebook_path}':")
        print("Exception encountered during execution.")
        print(f"Error value: {pm_error.evalue}")
        raise  # זריקת החריגה מחדש
    except Exception as e:
        print(f"Error executing notebook '{notebook_path}': {str(e)}")
        raise  # זריקת חריגה כללית מחדש
