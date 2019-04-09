from src import main as app
from src.main import process_line_command
from src.main import create_validate_line


#Required config object for configuration parameters in test case methods
config = app.load_config_json()


"""
@author - Aniruddha Anikhindi
This is dedicated test case file for PyCanv Line Creation software component.
"""


def test_process_line_command_negative_all_spaces():
    """
    Positive test case for allowed range and successful validation
    :return:
    """
    global config
    list_args = ['C', 20, 6]
    list_args_line = [' ', ' ', ' ', ' ', ' ']
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = process_line_command(args_list=list_args_line, canvas_matrix=canvas_matrix, cols=max_cols, config=config, rows=max_rows)
    assert exec_flag is False


def test_process_line_command_negative_coordinates_all_spaces():
    """
    Negative test case for al blank arguments
    :return:
    """
    global config
    list_args = ['C', 20, 6]
    list_args_line = ['L', ' ', ' ', ' ', ' ']
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = process_line_command(args_list=list_args_line, canvas_matrix=canvas_matrix, cols=max_cols, config=config, rows=max_rows)
    assert exec_flag is False



def test_process_line_command_positive_horizontal_allowed_range_successful_validation():
    """
    Positive test case for allowed horizontal range with successful validation
    :return:
    """
    global config
    list_args = ['C', 20, 6]
    list_args_line = ['L', 1, 2, 6, 2]
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = process_line_command(args_list=list_args_line, canvas_matrix=canvas_matrix, cols=max_cols,
                                     config=config, rows=max_rows)
    assert exec_flag is True


def test_process_line_command_negative_row_not_allowed_range_failed_validation():
    """
    Negative test case for row co-ordinates not allowed in range for failed validation
    :return:
    """
    global config
    list_args = ['C', 20, 6]
    list_args_line = ['L', 1, 2, 21, 2]
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = process_line_command(args_list=list_args_line, canvas_matrix=canvas_matrix, cols=max_cols,
                                     config=config, rows=max_rows)
    assert exec_flag is False


def test_process_line_command_positive_row_allowed_boundary_condition():
    """
    Positive test case for row co-ordinates allowed in range for successful validation
    :return:
    """
    global config
    list_args = ['C', 20, 6]
    list_args_line = ['L', 1, 2, 20, 2]
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = process_line_command(args_list=list_args_line, canvas_matrix=canvas_matrix, cols=max_cols,
                                     config=config, rows=max_rows)
    assert exec_flag is True


def test_process_line_command_positive_vertical_allowed_range_successful_validation():
    """
    Positive test case for vertical allowed range with successful validation
    :return:
    """
    global config
    list_args = ['C', 20, 6]
    list_args_line = ['L', 6, 3, 6, 4]
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = process_line_command(args_list=list_args_line, canvas_matrix=canvas_matrix, cols=max_cols,
                                     config=config, rows=max_rows)
    assert exec_flag is True


def test_process_line_command_negative_col_not_allowed_range_failed_validation():
    """
    Negative test case for vertical row co-ordinates not allowed in range with failed validation
    :return:
    """
    global config
    list_args = ['C', 20, 6]
    list_args_line = ['L', 6, 3, 6, 7]
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = process_line_command(args_list=list_args_line, canvas_matrix=canvas_matrix, cols=max_cols,
                                     config=config, rows=max_rows)
    assert exec_flag is False


def test_process_line_command_positive_col_allowed_boundary_condition():
    """
    Positive test case for row vertical co-ordinates allowed in range with successful validation
    :return:
    """
    global config
    list_args = ['C', 20, 6]
    list_args_line = ['L', 6, 3, 6, 6]
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = process_line_command(args_list=list_args_line, canvas_matrix=canvas_matrix, cols=max_cols,
                                     config=config, rows=max_rows)
    assert exec_flag is True


def test_create_line_positive():
    """
    Positive test case to check create line method with correct arguments
    :return:
    """
    global config
    list_args = ['C', 20, 6]
    list_args_line = ['L', 6, 3, 6, 6]
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    flag_error = create_validate_line(list_lines=list_args_line,canvas_matrix=canvas_matrix,validate=True)
    assert flag_error is False


def test_create_line_negative():
    """
    Negative test case to check create line method with incorrect arguments
    :return:
    """
    global config
    list_args = ['C', 20, 6]
    list_args_line = ['L', 6, 3, 4, 8]
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    flag_error = create_validate_line(list_lines=list_args_line,canvas_matrix=canvas_matrix,validate=True)
    assert flag_error is True


def test_process_line_command_negative_zero_not_allowed_boundary_condition():
    """
    Negative test case for all 0 co-ordinates not allowed
    :return:
    """
    global config
    list_args = ['C', 20, 6]
    list_args_line = ['L', 0, 0, 0, 0]
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = process_line_command(args_list=list_args_line, canvas_matrix=canvas_matrix, cols=max_cols,
                                     config=config, rows=max_rows)
    assert exec_flag is False


if __name__ == '__main__':
    test_process_line_command_negative_all_spaces()
    test_process_line_command_negative_coordinates_all_spaces()
    test_process_line_command_positive_horizontal_allowed_range_successful_validation()
    test_process_line_command_negative_row_not_allowed_range_failed_validation()
    test_process_line_command_positive_row_allowed_boundary_condition()
    test_process_line_command_positive_vertical_allowed_range_successful_validation()
    test_process_line_command_negative_col_not_allowed_range_failed_validation()
    test_process_line_command_positive_col_allowed_boundary_condition()
    test_create_line_positive()
    test_create_line_negative()
    test_process_line_command_negative_zero_not_allowed_boundary_condition()


