from src import main as app
from src.main import process_rectangle_command


#Required config object for configuration parameters in test case methods
config = app.load_config_json()


"""
@author - Aniruddha Anikhindi
This is dedicated test case file for PyCanv Rectangle Creation software component.
"""


def test_process_rectangle_command_positive_validation():
    """
    Positive test case for allowed rectangle range with successful validation
    :return:
    """
    global config
    list_args = ['C', 20, 6]
    list_args_line = ['R', 14, 1, 18, 3]
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = process_rectangle_command(args_list=list_args_line,canvas_matrix=canvas_matrix,cols=max_cols,config=config,rows=max_rows)
    assert exec_flag is True


def test_process_rectangle_command_negative_not_allowed_range_failed_validation():
    """
    Negative test case for rectangle row co-ordinates not allowed in range with failed validation
    :return:
    """
    global config
    list_args = ['C', 20, 6]
    list_args_line = ['R', 1, 2, 21, 2]
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = process_rectangle_command(args_list=list_args_line, canvas_matrix=canvas_matrix, cols=max_cols,
                                              config=config, rows=max_rows)
    assert exec_flag is False


def test_process_rectangle_command_positive_row_col_allowed_boundary_condition():
    """
    Positive test case for rectangle row co-ordinates allowed in range with successful validation
    :return:
    """
    global config
    list_args = ['C', 20, 6]
    list_args_line = ['R', 1, 1, 20, 6]
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = process_rectangle_command(args_list=list_args_line, canvas_matrix=canvas_matrix, cols=max_cols,
                                              config=config, rows=max_rows)
    assert exec_flag is True


def test_process_rectangle_command_negative_row_incorrect_coordinates():
    """
    Negative test case for rectangle row co-ordinates allowed in range with incorrect co-ordinates
    :return:
    """
    global config
    list_args = ['C', 20, 6]
    list_args_line = ['R', 3, 4, 14, 20]
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = process_rectangle_command(args_list=list_args_line, canvas_matrix=canvas_matrix, cols=max_cols,
                                              config=config, rows=max_rows)
    assert exec_flag is False


def test_process_rectangle_command_negative_all_zero_coordinates():
    """
    Negative test case for all rectangle 0 co-ordinates
    :return:
    """
    global config
    list_args = ['C', 20, 6]
    list_args_line = ['R', 0, 0, 0, 0]
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = process_rectangle_command(args_list=list_args_line, canvas_matrix=canvas_matrix, cols=max_cols,
                                              config=config, rows=max_rows)
    assert exec_flag is False


def test_process_rectangle_command_negative_all_negative_coordinates():
    """
    Negative test case for negative co-ordinates
    :return:
    """
    global config
    list_args = ['C', 20, 6]
    list_args_line = ['R', -1, 3, -5, -8]
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = process_rectangle_command(args_list=list_args_line, canvas_matrix=canvas_matrix, cols=max_cols,
                                              config=config, rows=max_rows)
    assert exec_flag is False


def test_process_rectangle_command_negative_spaces_in_coordinates():
    """
    Negative test case with all int arguments spaces
    :return:
    """
    global config
    list_args = ['C', 20, 6]
    list_args_line = ['R', ' ', ' ', ' ', ' ']
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = process_rectangle_command(args_list=list_args_line, canvas_matrix=canvas_matrix, cols=max_cols,
                                              config=config, rows=max_rows)
    assert exec_flag is False


def test_process_rectangle_command_negative_spaces():
    """
    Negative test case for all arguments spaces
    :return:
    """
    global config
    list_args = ['C', 20, 6]
    list_args_line = [' ', ' ', ' ', ' ', ' ']
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = process_rectangle_command(args_list=list_args_line, canvas_matrix=canvas_matrix, cols=max_cols,
                                              config=config, rows=max_rows)
    assert exec_flag is False

if __name__ == '__main__':
    test_process_rectangle_command_positive_validation()
    test_process_rectangle_command_negative_not_allowed_range_failed_validation()
    test_process_rectangle_command_positive_row_col_allowed_boundary_condition()
    test_process_rectangle_command_negative_row_incorrect_coordinates()
    test_process_rectangle_command_negative_all_zero_coordinates()
    test_process_rectangle_command_negative_all_negative_coordinates()
    test_process_rectangle_command_negative_spaces_in_coordinates()
    test_process_rectangle_command_negative_spaces()



