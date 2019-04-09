from src import main as app
from src.main import validate_line_coordinates_in_canvas_range


#Required config object for configuration parameters in test case methods
config = app.load_config_json()


"""
@author - Aniruddha Anikhindi
This is dedicated test case file for PyCanv util software component.
"""


def test_load_config_json():
    '''
    Positive test case to test loaded config object is not null
    :return:
    '''
    assert config is not None


def test_validate_line_coordinates_in_canvas_range_positive_horizontal_allowed_range_successful_validation():
    """
    Positive test case for allowed range with successful validation
    :return:
    """
    global config
    list_args = ['C', 20, 6]
    list_args_line = ['L', 1, 2, 6, 2]
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = validate_line_coordinates_in_canvas_range(list=list_args_line,rows=max_rows, cols=max_cols, bucket_flag=False)
    assert exec_flag is True


def test_validate_line_coordinates_in_canvas_range_negative_row_not_allowed_range_failed_validation():
    """
    Negative test case for row co-ordinates not allowed in range with failed validation
    :return:
    """
    global config
    list_args = ['C', 20, 6]
    list_args_line = ['L', 1, 2, 21, 2]
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = validate_line_coordinates_in_canvas_range(list=list_args_line,rows=max_rows, cols=max_cols, bucket_flag=False)
    assert exec_flag is False


def test_validate_line_coordinates_in_canvas_range_positive_row_allowed_boundary_condition():
    """
    Positive test case for horizontal co-ordinates allowed in range with successful validation
    :return:
    """
    global config
    list_args = ['C', 20, 6]
    list_args_line = ['L', 1, 2, 20, 2]
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = validate_line_coordinates_in_canvas_range(list=list_args_line,rows=max_rows, cols=max_cols, bucket_flag=False)
    assert exec_flag is True


def test_validate_line_coordinates_in_canvas_range_positive_vertical_allowed_range_successful_validation():
    """
    Positive test case for vertical co-ordinates allowed in range with successful validation
    :return:
    """
    global config
    list_args = ['C', 20, 6]
    list_args_line = ['L', 6, 3, 6, 4]
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = validate_line_coordinates_in_canvas_range(list=list_args_line,rows=max_rows, cols=max_cols, bucket_flag=False)
    assert exec_flag is True


def test_validate_line_coordinates_in_canvas_range_negative_col_not_allowed_range_failed_validation():
    """
    Negative test case for row co-ordinates not allowed in canvas range with failed validation
    :return:
    """
    global config
    list_args = ['C', 20, 6]
    list_args_line = ['L', 6, 3, 6, 7]
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = validate_line_coordinates_in_canvas_range(list=list_args_line,rows=max_rows, cols=max_cols, bucket_flag=False)
    assert exec_flag is False


def test_validate_line_coordinates_in_canvas_range_positive_col_allowed_boundary_condition():
    """
    Positive test case for row co-ordinates allowed in boundary range with successful validation
    :return:
    """
    global config
    list_args = ['C', 20, 6]
    list_args_line = ['L', 6, 3, 6, 6]
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = validate_line_coordinates_in_canvas_range(list=list_args_line,rows=max_rows, cols=max_cols, bucket_flag=False)
    assert exec_flag is True


def test_validate_line_coordinates_in_canvas_range_negative_zero_not_allowed_boundary_condition():
    """
    Negative test case for all 0 co-ordinates
    :return:
    """
    global config
    list_args = ['C', 20, 6]
    list_args_line = ['L', 0, 0, 0, 0]
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = validate_line_coordinates_in_canvas_range(list=list_args_line,rows=max_rows, cols=max_cols, bucket_flag=False)
    assert exec_flag is False


def test_app_config_parameters_not_null():
    '''
    Positive test case to check config paramters are working
    :return:
    '''
    global config
    assert config['APP']['SCREEN_MESSAGE'] is not None


if __name__ == '__main__':
    test_load_config_json()
    test_validate_line_coordinates_in_canvas_range_positive_horizontal_allowed_range_successful_validation()
    test_validate_line_coordinates_in_canvas_range_negative_row_not_allowed_range_failed_validation()
    test_validate_line_coordinates_in_canvas_range_positive_row_allowed_boundary_condition()
    test_validate_line_coordinates_in_canvas_range_positive_vertical_allowed_range_successful_validation()
    test_validate_line_coordinates_in_canvas_range_negative_col_not_allowed_range_failed_validation()
    test_validate_line_coordinates_in_canvas_range_positive_col_allowed_boundary_condition()
    test_validate_line_coordinates_in_canvas_range_negative_zero_not_allowed_boundary_condition()
    test_app_config_parameters_not_null()





