import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

def run_notebook(notebook_path, params=None):
    """
    מריץ מחברת Jupyter עם או בלי פרמטרים מותאמים אישית.
    
    :param notebook_path: נתיב לקובץ המחברת (input)
    :param params: מילון פרמטרים לעדכון במחברת (אופציונלי)
    :return: מחברת מעודכנת (פורמט nbformat.NotebookNode)
    """
    # קריאת המחברת
    with open(notebook_path) as ff:
        nb_in = nbformat.read(ff, as_version=4)
    
    # עדכון פרמטרים במחברת
    if params:
        # הוספת תא פרמטרים לראש המחברת
        param_cell = nbformat.v4.new_code_cell(
            source="\n".join([f"{key} = {repr(value)}" for key, value in params.items()])
        )
        nb_in.cells.insert(0, param_cell)

    # הכנת המעבד
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    
    # הרצת המחברת
    nb_out = ep.preprocess(nb_in)
    
    return nb_in  # מחברת מעודכנת
