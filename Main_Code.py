import Print_Manual as PM
import Test_functions as TF

MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]

if __name__ == '__main__':
    print("Manual of color codes:")
    PM.generate_color_map()
    print("\nExicuting Test Cases:")
    TF.Test_case()
    print('Done :)')