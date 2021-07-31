import logging.config
import os
import json
import sys


'''
    @name : PyCanv
    @version : 1.0
    @author : Aniruddha Anikhindi
    
    PyCanv is fully designed and developed by Aniruddha Anikhindi
    PyCanv is a open source console based application developed in Python
    
    This application uses configuration file located at -> /config/config.json
    This application writes log file located at -> /log/pycanv.log
'''


#Matrix wehere canvas co-ordinates will be stored  - Row X Columns
canvas_matrix = None

#Number of rows of canvas
rows = None

#Number of columns in canvas
cols = None

#Error flag indicator
error_flag = False

#configuration object to map properties
config = None

#quit flag to return to execute sys.exit
quit_flag = False

#Logger configuration - logs will be written at location /logs/pycanv.log
logger_filename = os.path.dirname(os.getcwd()) + '/config/logger.config'
logging.config.fileConfig(fname=logger_filename, disable_existing_loggers=False)
logger = logging.getLogger('pycanv:main')


#Main function used for PyCan application - all commands are processed from this function
def main():
    global canvas_matrix, rows, cols, error_flag, config, quit_flag
    if config is None:
        config = load_config_json()
    if not error_flag:
        print(config['APP']['SCREEN_MESSAGE'])
    input_command = input(config['APP']['ENTER_MESSAGE'])
    logger.info('Command entered :' + input_command)
    try:
        args_list = input_command.split()
        if not args_list:
            logger.error('No arguments passed')
            print(config['APP']['NO_ARG_ERROR'])
        else:
            if str(args_list[0]).strip() == config['CANVAS']['COMMAND']:
                logger.debug("Processing start - Canvas command")
                if canvas_matrix is not None and rows is not None and cols is not None:
                    logger.debug("Canvas already exists, user re-entered canvas command")
                    input_confirmation = input(config['APP']['CANVAS_EXISTS_MESSAGE'])
                    logger.debug("User confirmation - "+str(input_confirmation))
                    if str(input_confirmation).strip() == 'Y':
                        canvas_matrix = None
                        rows = None
                        cols = None
                        logger.debug("Canvas deleted successfully, creating new canvas")
                        process_canvas_command(args_list, config)
                    else:
                        print_error_message(msg=config['APP']['CANVAS_NOT_DELETED_MSG'])
                else:
                    process_canvas_command(args_list, config)
                logger.debug("Processing end - Canvas command")
                main()
            elif str(args_list[0]).strip() == config['LINE']['COMMAND']:
                logger.debug("Processing start - Line command")
                process_line_command(args_list, canvas_matrix, cols, config, rows)
                logger.debug("Processing end - Line command")
                main()
            elif str(args_list[0]).strip() == config['RECTANGLE']['COMMAND']:
                logger.debug("Processing start - Rectangle command")
                process_rectangle_command(args_list, canvas_matrix, cols, config, rows)
                logger.debug("Processing end - Rectangle command")
                main()
            elif str(args_list[0]).strip() == config['BUCKET']['COMMAND']:
                logger.debug("Processing start - Bucket command")
                process_bucket_command(args_list, canvas_matrix, cols, config, rows)
                logger.debug("Processing end - Bucket command")
                main()
            elif str(args_list[0]).strip() == config['HELP']['COMMAND']:
                print('********************************************************')
                print(config['HELP']['MESSAGE'])
                print('********************************************************')
                main()
            elif str(args_list[0]).strip() == config['QUIT']['COMMAND']:
                quit_flag = True
                print(config['QUIT']['MESSAGE'])
                sys.exit(0)
            else:
                print_error_message(msg=config['APP']['KEY_ERROR'])
    except Exception as ex:
        print_error_message(msg=config['APP']['KEY_ERROR'])
        logger.error("Error occured in PycCanv - "+config['APP']['KEY_ERROR'])
    finally:
        if not quit_flag:
            main()
        else:
            sys.exit(0)

def validateArgs(args):
    try:
        if True:
            print("fff")
        else:
            pass
    except Exception  as e:
        print("error")


def process_canvas_command(args_list, config):
    '''
    This method is starting point of PyCanv application, which processes and creates canvas
    Canvas will be created with matrix of Rows+2 X Cols+2 parameters
    Canvas is created with extra 2 parameters reason being for boundary
    :param args_list:
    :param config:
    :return: success flag
    '''
    global canvas_matrix, rows, cols
    try:
        if str(args_list[0]).strip() == config['CANVAS']['COMMAND'] and len(args_list) == config['CANVAS']['ARG_COUNT']:
            if check_positive(args_list[1]) and check_positive(args_list[2]):
                if int(args_list[2]) <= int(config['CANVAS']['MAX_ALLOWED_ROWS']) and int(args_list[1]) <= int(config['CANVAS']['MAX_ALLOWED_COLS']):
                    canvas_matrix, max_rows, max_cols = create_canvas_matrix(args_list)
                    rows = max_rows
                    cols = max_cols
                    print_canvas(rows=max_rows, cols=max_cols, canvas_matrix=canvas_matrix)
                    return True
                else:
                    print_error_message(msg=config['CANVAS']['ERROR_MAX_ALLOWED'])
            else:
                print_error_message(msg=config['CANVAS']['NEGATIVE_NUM_ERROR'])
        else:
            print_error_message(msg=config['CANVAS']['ERROR'])
    except KeyError as ke:
        print_error_message(msg=config['APP']['NO_ARG_ERROR'])
    except Exception as ex:
        print_error_message(msg=config['CANVAS']['ERROR'])
    return False


def create_canvas_matrix(args_list):
    '''
    This method creates acanvas matrix based on input canvas command
    :param args_list:
    :return:
    '''
    max_rows = (int(args_list[2]) + 2)  # number of rows
    max_cols = (int(args_list[1]) + 2)  # number of columns
    canvas_matrix = [[' ' for i in range(max_cols)] for j in range(max_rows)]  # create matrix of rows X columns
    canvas_matrix[0][0] = canvas_matrix[max_rows - 1][max_cols - 1] = canvas_matrix[0][max_cols - 1] = canvas_matrix[max_rows - 1][
        0] = '-'  # fill end points
    for row in range(0, max_rows):
        for col in range(0, max_cols):
            if row == 0 or row == max_rows - 1:
                if canvas_matrix[row][col] == ' ':
                    canvas_matrix[row][col] = '-'
            if col == 0 or col == max_cols - 1:
                if canvas_matrix[row][col] == ' ':
                    canvas_matrix[row][col] = '|'
    return canvas_matrix, max_rows, max_cols


def load_config_json():
    '''
    This method is used to load configuration json file
    :return: config
    '''
    global config
    config_file_path = os.path.dirname(os.getcwd()) + '/config/config.json'
    with open(config_file_path) as json_file:
        config = json.load(json_file)
    return config


def process_line_command(args_list, canvas_matrix, cols, config, rows):
    '''
    This is method where line command is processed.
    Line comand is validated based on busines validations and after success line will be drawn on canvas
    If there is no canvas available then this method will throw error
    :param args_list:
    :param canvas_matrix:
    :param cols:
    :param config:
    :param rows:
    :return: success flag
    '''
    if args_list and str(args_list[0]).strip() == config['LINE']['COMMAND'] and len(args_list) == config['LINE']['ARG_COUNT']:
        if validate_line_coordinates_in_canvas_range(list=args_list,rows=rows,cols=cols, bucket_flag=False):
            if not canvas_matrix:
                print_error_message(msg=config['APP']['NO_CANVAS_ERROR'])
            else:
                create_flag = create_validate_line(args_list, canvas_matrix, False)
                if not create_flag:
                    print_error_message(msg=config['LINE']['INPUT_ERROR'])
                print_canvas(rows=rows, cols=cols, canvas_matrix=canvas_matrix)
                return True
        else:
            print_error_message(msg=config['LINE']['VAL_FAIL'])
    else:
        print_error_message(msg=config['LINE']['ERROR'])
    return False


def create_validate_line(list_lines, canvas_matrix, validate):
    '''
    This method is used as for dual purpose
    1. To validate line co-ordinates and 2. draw line co-ordinates
    :param list_lines:
    :param canvas_matrix:
    :param validate:
    :return: error flag
    '''
    flag_error = False
    if int(list_lines[2]) - int(list_lines[4]) == 0:
        if int(list_lines[1]) < int(list_lines[3]):
            if not validate:
                for lx in range(int(list_lines[1]), (int(list_lines[3]) + 1)):
                    canvas_matrix[int(list_lines[2])][lx] = 'x'
        elif int(list_lines[1]) > int(list_lines[3]):
            if not validate:
                for lx in range(int(list_lines[3]), (int(list_lines[1]) + 1)):
                    canvas_matrix[int(list_lines[2])][lx] = 'x'
        else:
            flag_error = True
    elif int(list_lines[1]) - int(list_lines[3]) == 0:
        if int(list_lines[2]) < int(list_lines[4]):
            if not validate:
                for ly in range(int(list_lines[2]), (int(list_lines[4]) + 1)):
                    canvas_matrix[ly][int(list_lines[1])] = 'x'
        elif int(list_lines[2]) > int(list_lines[4]):
            if not validate:
                for ly in range(int(list_lines[4]), (int(list_lines[2]) + 1)):
                    canvas_matrix[ly][int(list_lines[1])] = 'x'
        else:
            flag_error = True
    else:
        flag_error = True
    return flag_error


def process_rectangle_command(args_list, canvas_matrix, cols, config, rows):
    '''
    This method processes rectangle command of application.
    It validates rectangle co-ordinates and then after successful validation resues line component methods to draw rectangle
    :param args_list:
    :param canvas_matrix:
    :param cols:
    :param config:
    :param rows:
    :return: success flag
    '''
    if args_list and str(args_list[0]).strip() == config['RECTANGLE']['COMMAND'] and len(args_list) == config['RECTANGLE']['ARG_COUNT']:
        if not canvas_matrix:
            print_error_message(msg=config['APP']['NO_CANVAS_ERROR'])
        else:
            if validate_line_coordinates_in_canvas_range(list=args_list,rows=rows,cols=cols, bucket_flag=False):
                if validate_rectangle(args_list=args_list,canvas_matrix=canvas_matrix):
                    list_1ine1 = [0, int(args_list[1]), int(args_list[2]), int(args_list[3]), int(args_list[2])]
                    create_validate_line(list_lines=list_1ine1, canvas_matrix=canvas_matrix, validate=False)
                    list_1ine2 = [0, int(args_list[3]), int(args_list[2]), int(args_list[3]), int(args_list[4])]
                    create_validate_line(list_lines=list_1ine2, canvas_matrix=canvas_matrix,validate=False)
                    list_1ine3 = [0, int(args_list[1]), int(args_list[2]), int(args_list[1]), int(args_list[4])]
                    create_validate_line(list_lines=list_1ine3, canvas_matrix=canvas_matrix,validate=False)
                    list_1ine4 = [0, int(args_list[1]), int(args_list[4]), int(args_list[3]), int(args_list[4])]
                    create_validate_line(list_lines=list_1ine4, canvas_matrix=canvas_matrix,validate=False)
                    print_canvas(rows=rows, cols=cols, canvas_matrix=canvas_matrix)
                    return True
                else:
                    print_error_message(msg=config['RECTANGLE']['INCORRECT'])
            else:
                print_error_message(msg=config['RECTANGLE']['VAL_FAIL'])
    else:
        print_error_message(msg=config['RECTANGLE']['INCORRECT'])
    return False


def validate_rectangle(args_list,canvas_matrix):
    '''
    This is helper method to validate rectangle co-ordinates in canvas
    :param args_list:
    :param canvas_matrix:
    :return: validation flag
    '''
    list_1ine1 = [0, int(args_list[1]), int(args_list[2]), int(args_list[3]), int(args_list[2])]
    error_flag_line1 = create_validate_line(list_lines=list_1ine1, canvas_matrix=canvas_matrix, validate=True)
    list_1ine2 = [0, int(args_list[3]), int(args_list[2]), int(args_list[3]), int(args_list[4])]
    error_flag_line2 = create_validate_line(list_lines=list_1ine2, canvas_matrix=canvas_matrix, validate=True)
    list_1ine3 = [0, int(args_list[1]), int(args_list[2]), int(args_list[1]), int(args_list[4])]
    error_flag_line3 = create_validate_line(list_lines=list_1ine3, canvas_matrix=canvas_matrix, validate=True)
    list_1ine4 = [0, int(args_list[1]), int(args_list[4]), int(args_list[3]), int(args_list[4])]
    error_flag_line4 = create_validate_line(list_lines=list_1ine4, canvas_matrix=canvas_matrix,validate=True)
    return error_flag_line1==False and error_flag_line2==False and error_flag_line3==False and error_flag_line4==False


def process_bucket_command(args_list, canvas_matrix, cols, config, rows):
    '''
    This method takes bukcet arguments and processes it for filling color on canvas
    It validates arguments and color code from configuration
    :param args_list:
    :param canvas_matrix:
    :param cols:
    :param config:
    :param rows:
    :return: success flag
    '''
    if args_list and str(args_list[0]).strip() == config['BUCKET']['COMMAND'] and len(args_list) == config['BUCKET']['ARG_COUNT']:
        if int(args_list[1]) > 0 and int(args_list[2]) > 0 and validate_color_code(str(args_list[3]),config):
            if not canvas_matrix:
                print_error_message(msg=config['APP']['NO_CANVAS_ERROR'])
            else:
                if validate_bucket_coordinate_in_canvas_range(list=args_list,rows=rows,cols=cols):
                    try:
                        apply_flood_fill(canvas_matrix=canvas_matrix,x=int(args_list[2]),y=int(args_list[1]),
                                         max_row=rows,max_col=cols, color_code=str(args_list[3]))
                        print_canvas(rows=rows, cols=cols, canvas_matrix=canvas_matrix)
                        return True
                    except Exception as e:
                        print(e)
                else:
                    print_error_message(msg=config['BUCKET']['VAL_FAIL'])
        else:
            print_error_message(msg=config['BUCKET']['ERROR'])
    else:
        print_error_message(msg=config['BUCKET']['ERROR'])
    return False


def apply_flood_fill(canvas_matrix, x, y, max_row, max_col, color_code):
    '''
    This method is used to apply flood fill to other connected points
    :param canvas_matrix:
    :param x:
    :param y:
    :param max_row:
    :param max_col:
    :param color_code:
    :return:
    '''
    if str(canvas_matrix[x][y]).isspace() or str(canvas_matrix[x][y]).strip() == "":
        canvas_matrix[x][y] = color_code
        if x > 0:
            apply_flood_fill(canvas_matrix, x - 1, y, max_row=max_row, max_col=max_col, color_code=color_code)
        if x < max_row:
            apply_flood_fill(canvas_matrix, x + 1, y,max_row=max_row, max_col=max_col, color_code=color_code)
        if y > 0:
            apply_flood_fill(canvas_matrix, x, y - 1,max_row=max_row, max_col=max_col, color_code=color_code)
        if y < max_col:
            apply_flood_fill(canvas_matrix, x, y + 1,max_row=max_row, max_col=max_col, color_code=color_code)


def validate_color_code(code, config):
    '''
    This method validates input color against configuration file available color codes
    :param code:
    :param config:
    :return:
    '''
    colors = config['BUCKET']['ALLOWED_COLORS'].split(',')
    if str(code).strip() in colors:
        return True
    return False

def print_canvas(rows, cols, canvas_matrix):
    '''
    This method is used to print canvas on console
    :param rows:
    :param cols:
    :param canvas_matrix:
    :return:
    '''
    for row in range(0, rows):
        line = ''
        for col in range(0, cols):
            line = line + canvas_matrix[row][col]
        print(line)


def print_error_message(msg):
    '''
    This method is used to print error messages on console
    :param msg:
    :return:
    '''
    global error_flag
    error_flag = True
    print(msg)
    print('********************************************************')


def validate_line_coordinates_in_canvas_range(list, rows, cols, bucket_flag):
    '''
    This method validates input coordinates are within range of canvas
    :param list:
    :param rows:
    :param cols:
    :param bucket_flag:
    :return:
    '''
    if check_positive(list[1]) and check_positive(list[2]) and check_positive(list[3]) and check_positive(list[4]):
        if check_cordinates_in_rectangle_range(1, 1, cols - 2, rows -2, int(list[1]), int(list[2])):
            if check_cordinates_in_rectangle_range(1, 1, cols - 2, rows -2, int(list[3]), int(list[4])):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def validate_bucket_coordinate_in_canvas_range(list, rows, cols):
    '''
    This method is used to validate input co-ordinates of bucket filling command
    :param list:
    :param rows:
    :param cols:
    :return: validation flag
    '''
    if check_positive(list[1]) and check_positive(list[2]):
        if check_cordinates_in_rectangle_range(1, 1, cols - 2, rows -2, int(list[1]), int(list[2])):
            return True
        else:
            return False
    else:
        return False


def check_cordinates_in_rectangle_range(topleftR, topleftC, rightbottomR,rightbottomC, inputR, inputC):
    '''
    This is a helper method to validate co-ordinates are withtin range of rectanlge / canvas
    :param topleftR:
    :param topleftC:
    :param rightbottomR:
    :param rightbottomC:
    :param inputR:
    :param inputC:
    :return: validation flag
    '''
    if topleftR <= inputR <= rightbottomR and topleftC <= inputC <= rightbottomC:
        return True
    else:
        return False


def check_positive(num):
    '''
    This is utility method used to check input is number with value greater than zero
    :param num:
    :return:
    '''
    return True if str(num).isdigit() and int(num) > 0 else False


if __name__ == '__main__':
   main()