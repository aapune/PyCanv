from src import main as app


#Required config object for configuration parameters in test case methods
config = app.load_config_json()


"""
@author - Aniruddha Anikhindi
This is dedicated test case file for PyCanv Canvas Creation software component.
"""

def test_create_canvas_matrix_positive_normal_arg():
    """
    Positive test case for simple canvas matrix creation core method
    :return: boolean
    """
    global config
    list_args = ['C',20,6]
    app.create_canvas_matrix(args_list=list_args)
    assert app.error_flag is False


def test_process_canvas_command_positive_boundary_max_allowed_range():
    """
    Positive test case for max boundary range of canvas
    :return: boolean
    """
    global config
    list_args = ['C',40,40]
    exec_flag = app.process_canvas_command(args_list=list_args, config=config)
    assert exec_flag is True


def test_process_canvas_command_positive_normal_argument():
    """
    Positive test case for canvas creation
    :return: boolean
    """
    global config
    list_args = ['C',20,4]
    exec_flag = app.process_canvas_command(args_list=list_args, config=config)
    assert exec_flag is True


def test_process_canvas_command_negative_all_zero_argument():
    """
    Negative test case for canvas co-ordinates - (0,0)
    :return: boolean
    """
    global config
    list_args = ['C',0,0]
    exec_flag = app.process_canvas_command(args_list=list_args, config=config)
    assert exec_flag is False


def test_process_canvas_command_negative_input_negative_numbers():
    """
    Negative test case for negative input canvas co-ordinates
    :return: boolean
    """
    global config
    list_args = ['C',-1,-2]
    exec_flag = app.process_canvas_command(args_list=list_args, config=config)
    assert exec_flag is False


def test_process_canvas_command_negative_input_all_strings():
    """
    Negative test case for invalid input string co-ordinates for canvas creation
    :return: boolean
    """
    global config
    list_args = ['C','A','B']
    exec_flag = app.process_canvas_command(args_list=list_args, config=config)
    assert exec_flag is False


def test_process_canvas_command_negative_exceed_max_allowed_range():
    """
    Negative test case for exceeding boundary range conditions for canvas
    :return: boolean
    """
    global config
    list_args = ['C',41,41]
    exec_flag = app.process_canvas_command(args_list=list_args, config=config)
    assert exec_flag is False


def test_process_canvas_command_negative_all_blank_arguments():
    """
    Negative test case for exceeding boundary range conditions for canvas
    :return: boolean
    """
    global config
    list_args = [' ',' ',' ']
    exec_flag = app.process_canvas_command(args_list=list_args, config=config)
    assert exec_flag is False


def test_process_canvas_command_negative_coordinates_blank_arguments():
    """
    Negative test case for exceeding boundary range conditions for canvas
    :return: boolean
    """
    global config
    list_args = ['C',' ',' ']
    exec_flag = app.process_canvas_command(args_list=list_args, config=config)
    assert exec_flag is False

def test_process_canvas_command_negative_no_arguments():
    """
    Negative test case for no input arguments
    :return: boolean
    """
    global config
    list_args = []
    exec_flag = app.process_canvas_command(args_list=list_args, config=config)
    assert exec_flag is False


if __name__ == '__main__':
    test_create_canvas_matrix_positive_normal_arg()
    test_process_canvas_command_positive_boundary_max_allowed_range()
    test_process_canvas_command_positive_normal_argument()
    test_process_canvas_command_negative_all_zero_argument()
    test_process_canvas_command_negative_input_negative_numbers()
    test_process_canvas_command_negative_input_all_strings()
    test_process_canvas_command_negative_exceed_max_allowed_range()
    test_process_canvas_command_negative_all_blank_arguments()
    test_process_canvas_command_negative_no_arguments()



