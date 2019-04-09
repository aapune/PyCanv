from src import main as app
from src.main import process_bucket_command



#Required config object for configuration parameters in test case methods
config = app.load_config_json()


"""
@author - Aniruddha Anikhindi
This is dedicated test case file for PyCanv Bucket filling software component.
"""


def test_process_bucket_command_positive_correct_command():
    """
    Positive test case for allowed range and successful validation
    :return:
    """
    global config
    list_args = ['C', 20, 6]
    list_args_bucket = ['B', 10, 3, 'o']
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = process_bucket_command(args_list=list_args_bucket,canvas_matrix=canvas_matrix,cols=max_cols,config=config,rows=max_rows)
    assert exec_flag is True


def test_process_bucket_command_negative_incorrect_command():
    """
    Negative test case with incorrect argument
    :return:
    """
    global config
    list_args = ['C', 20, 6]
    list_args_bucket = ['U', 19, 3, 'o']
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = process_bucket_command(args_list=list_args_bucket,canvas_matrix=canvas_matrix,cols=max_cols,config=config,rows=max_rows)
    assert exec_flag is False


def test_process_bucket_command_negative_incorrect_blank_command():
    """
    Negative test case with incorrect blank argument
    :return:
    """
    global config
    list_args = ['C', 20, 6]
    list_args_bucket = []
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = process_bucket_command(args_list=list_args_bucket,canvas_matrix=canvas_matrix,cols=max_cols,config=config,rows=max_rows)
    assert exec_flag is False


def test_process_bucket_command_negative_incorrect_argumnents_command():
    """
    Negative test case with incorrect arguments with additional arguments
    :return:
    """
    global config
    list_args = ['C', 20, 6]
    list_args_bucket = ['B', 10, 3, 3, 4]
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = process_bucket_command(args_list=list_args_bucket,canvas_matrix=canvas_matrix,cols=max_cols,config=config,rows=max_rows)
    assert exec_flag is False


def test_process_bucket_command_negative_incorrect_color_code_command():
    """
    Negative test case with incorrect color code input
    :return:
    """
    global config
    list_args = ['C', 20, 6]
    list_args_bucket = ['B', 10, 3, '%']
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = process_bucket_command(args_list=list_args_bucket,canvas_matrix=canvas_matrix,cols=max_cols,config=config,rows=max_rows)
    assert exec_flag is False


def test_process_bucket_command_negative_boundary_condition_min_command():
    """
    Positive test case for allowed range for successful validation
    :return:
    """
    global config
    list_args = ['C', 20, 6]
    list_args_bucket = ['B', 0, 0, 'o']
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = process_bucket_command(args_list=list_args_bucket,canvas_matrix=canvas_matrix,cols=max_cols,config=config,rows=max_rows)
    assert exec_flag is False


def test_process_bucket_command_negative_boundary_exceed_condition_max_command():
    """
    Negative test case with exceed co-ordinates range
    :return:
    """
    global config
    list_args = ['C', 20, 6]
    list_args_bucket = ['B', 21, 6, 'o']
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = process_bucket_command(args_list=list_args_bucket,canvas_matrix=canvas_matrix,cols=max_cols,config=config,rows=max_rows)
    assert exec_flag is False


def test_process_bucket_command_positive_boundary_condition_min_command():
    """
    Positive test case for allowed co-ordinates range of canvas
    :return:
    """
    global config
    list_args = ['C', 20, 6]
    list_args_bucket = ['B', 1, 1, 'o']
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = process_bucket_command(args_list=list_args_bucket,canvas_matrix=canvas_matrix,cols=max_cols,config=config,rows=max_rows)
    assert exec_flag is True


def test_process_bucket_command_negative_all_blank_param_with_spaces():
    """
    Negative test case with incorrect all blank arguments
    :return:
    """
    global config
    list_args = ['C', 20, 6]
    list_args_bucket = [' ', ' ', ' ', ' ']
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = process_bucket_command(args_list=list_args_bucket,canvas_matrix=canvas_matrix,cols=max_cols,config=config,rows=max_rows)
    assert exec_flag is False


def test_process_bucket_command_functional_check_bucketfill_outside_rectangle():
    """
    Functional test case to check bucketfilling functionality outside rectangle
    :return:
    """
    global config
    list_args = ['C', 3, 4]
    list_args_rectangle = ['R', 2, 1, 3, 3]
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    app.process_rectangle_command(args_list=list_args_rectangle, canvas_matrix=canvas_matrix, cols=max_cols,
                                              config=config, rows=max_rows)
    list_args_bucket = ['B', 1, 1, 'o']
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = process_bucket_command(args_list=list_args_bucket,canvas_matrix=canvas_matrix,cols=max_cols,config=config,rows=max_rows)

    coord1 = canvas_matrix[1][1]
    coord2 = canvas_matrix[1][2]
    coord3 = canvas_matrix[1][3]
    coord4 = canvas_matrix[4][1]
    coord5 = canvas_matrix[4][2]
    coord6 = canvas_matrix[4][3]

    assert exec_flag is True and coord1 == coord2 == coord3 == coord4 == coord5 == coord6 == 'O'.lower()


def test_process_bucket_command_functional_check_bucketfill_inside_rectangle():
    """
    Positive test case for allowed range for successful validation
    :return:
    """
    global config
    list_args = ['C', 5, 4]
    list_args_rectangle = ['R', 2, 2, 4, 5]
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    app.process_rectangle_command(args_list=list_args_rectangle, canvas_matrix=canvas_matrix, cols=max_cols,
                                  config=config, rows=max_rows)
    list_args_bucket = ['B', 3, 3, 'v']
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = process_bucket_command(args_list=list_args_bucket, canvas_matrix=canvas_matrix, cols=max_cols,
                                           config=config, rows=max_rows)

    coord1 = canvas_matrix[2][2]
    coord2 = canvas_matrix[2][3]
    coord3 = canvas_matrix[2][4]
    coord4 = canvas_matrix[2][5]
    coord5 = canvas_matrix[3][2]
    coord6 = canvas_matrix[3][3]
    coord7 = canvas_matrix[3][4]
    coord8 = canvas_matrix[3][5]
    coord9 = canvas_matrix[4][2]
    coord10 = canvas_matrix[4][3]
    coord11 = canvas_matrix[4][4]
    coord12 = canvas_matrix[4][5]

    assert coord1 == coord2 == coord3 == coord4 == coord5 == coord6 == coord7 == coord8 == coord9 == coord10 == coord11 == coord12 == 'V'.lower()


def test_process_bucket_command_positive_functional_color_code_fill_V():
    """
    Functional test case to check bucketfilling with V color code
    :return: boolean
    """
    global config
    list_args = ['C', 2, 2]
    list_args_bucket = ['B', 1, 1, 'v']
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = process_bucket_command(args_list=list_args_bucket,canvas_matrix=canvas_matrix,cols=max_cols,config=config,rows=max_rows)
    assert canvas_matrix[1][1] == canvas_matrix[1][2] == canvas_matrix[2][1] == canvas_matrix[2][2] == 'V'.lower()


def test_process_bucket_command_positive_functional_color_code_fill_I():
    """
    Functional test case to check bucketfilling with I color code
    :return: boolean
    """
    global config
    list_args = ['C', 2, 2]
    list_args_bucket = ['B', 1, 1, 'i']
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = process_bucket_command(args_list=list_args_bucket,canvas_matrix=canvas_matrix,cols=max_cols,config=config,rows=max_rows)
    assert canvas_matrix[1][1] == canvas_matrix[1][2] == canvas_matrix[2][1] == canvas_matrix[2][2] == 'I'.lower()


def test_process_bucket_command_positive_functional_color_code_fill_B():
    """
    Functional test case to check bucketfilling with B color code
    :return: boolean
    """
    global config
    list_args = ['C', 2, 2]
    list_args_bucket = ['B', 1, 1, 'b']
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = process_bucket_command(args_list=list_args_bucket,canvas_matrix=canvas_matrix,cols=max_cols,config=config,rows=max_rows)
    assert canvas_matrix[1][1] == canvas_matrix[1][2] == canvas_matrix[2][1] == canvas_matrix[2][2] == 'B'.lower()


def test_process_bucket_command_positive_functional_color_code_fill_G():
    """
    Functional test case to check bucketfilling with G color code
    :return: boolean
    """
    global config
    list_args = ['C', 2, 2]
    list_args_bucket = ['B', 1, 1, 'g']
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = process_bucket_command(args_list=list_args_bucket,canvas_matrix=canvas_matrix,cols=max_cols,config=config,rows=max_rows)
    assert canvas_matrix[1][1] == canvas_matrix[1][2] == canvas_matrix[2][1] == canvas_matrix[2][2] == 'G'.lower()


def test_process_bucket_command_positive_functional_color_code_fill_Y():
    """
    Functional test case to check bucketfilling with Y color code
    :return: boolean
    """
    global config
    list_args = ['C', 2, 2]
    list_args_bucket = ['B', 1, 1, 'y']
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = process_bucket_command(args_list=list_args_bucket,canvas_matrix=canvas_matrix,cols=max_cols,config=config,rows=max_rows)
    assert canvas_matrix[1][1] == canvas_matrix[1][2] == canvas_matrix[2][1] == canvas_matrix[2][2] == 'Y'.lower()


def test_process_bucket_command_positive_functional_color_code_fill_O():
    """
    Functional test case to check bucketfilling with O color code
    :return: boolean
    """
    global config
    list_args = ['C', 2, 2]
    list_args_bucket = ['B', 1, 1, 'o']
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = process_bucket_command(args_list=list_args_bucket,canvas_matrix=canvas_matrix,cols=max_cols,config=config,rows=max_rows)
    assert canvas_matrix[1][1] == canvas_matrix[1][2] == canvas_matrix[2][1] == canvas_matrix[2][2] == 'O'.lower()


def test_process_bucket_command_positive_functional_color_code_fill_R():
    """
    Functional test case to check bucketfilling with R color code
    :return: boolean
    """
    global config
    list_args = ['C', 2, 2]
    list_args_bucket = ['B', 1, 1, 'r']
    canvas_matrix, max_rows, max_cols = app.create_canvas_matrix(args_list=list_args)
    exec_flag = process_bucket_command(args_list=list_args_bucket,canvas_matrix=canvas_matrix,cols=max_cols,config=config,rows=max_rows)
    assert canvas_matrix[1][1] == canvas_matrix[1][2] == canvas_matrix[2][1] == canvas_matrix[2][2] == 'R'.lower()


if __name__ == '__main__':
    test_process_bucket_command_positive_correct_command()
    test_process_bucket_command_negative_incorrect_command()
    test_process_bucket_command_negative_incorrect_blank_command()
    test_process_bucket_command_negative_incorrect_argumnents_command()
    test_process_bucket_command_negative_incorrect_color_code_command()
    test_process_bucket_command_negative_boundary_condition_min_command()
    test_process_bucket_command_negative_boundary_exceed_condition_max_command()
    test_process_bucket_command_positive_boundary_condition_min_command()
    test_process_bucket_command_negative_all_blank_param_with_spaces()
    test_process_bucket_command_functional_check_bucketfill_outside_rectangle()
    test_process_bucket_command_functional_check_bucketfill_inside_rectangle()
    test_process_bucket_command_positive_functional_color_code_fill_V()
    test_process_bucket_command_positive_functional_color_code_fill_I()
    test_process_bucket_command_positive_functional_color_code_fill_B()
    test_process_bucket_command_positive_functional_color_code_fill_G()
    test_process_bucket_command_positive_functional_color_code_fill_Y()
    test_process_bucket_command_positive_functional_color_code_fill_O()
    test_process_bucket_command_positive_functional_color_code_fill_R()







