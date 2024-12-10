import nbformat
from nbconvert.preprocessors import ExecutePreprocessor, CellExecutionError

def run_notebook(notebook_path, params=None, save_path=None):
    """
    מריץ מחברת Jupyter ומחזיר True אם ההרצה הצליחה, או False במקרה של שגיאה.
    
    :param notebook_path: נתיב לקובץ המחברת (input)
    :param params: מילון פרמטרים לעדכון במחברת (אופציונלי)
    :param save_path: נתיב לשמירת המחברת המעודכנת (אם לא צוין, יישמר לקובץ המקורי)
    :return: True אם ההרצה הצליחה, אחרת False
    """
    try:
        # קריאת המחברת
        with open(notebook_path) as ff:
            nb_in = nbformat.read(ff, as_version=4)
        
        # עדכון פרמטרים במחברת
        if params:
            param_cell = nbformat.v4.new_code_cell(
                source="\n".join([f"{key} = {repr(value)}" for key, value in params.items()])
            )
            nb_in.cells.insert(0, param_cell)
        
        # הרצת המחברת
        ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
        ep.preprocess(nb_in)

        # # שמירת המחברת המעודכנת (אם נדרש)
        # if save_path:
        #     with open(save_path, "w") as ff:
        #         nbformat.write(nb_in, ff)
        # else:
        #     with open(notebook_path, "w") as ff:
        #         nbformat.write(nb_in, ff)
        
        return True  # הצלחה

    except CellExecutionError as e:
        # טיפול בשגיאות תא
        print(f"Error while executing the notebook: {e}")
        return False

    except Exception as e:
        # טיפול בשגיאות כלליות
        print(f"An unexpected error occurred: {e}")
        return False
