
def generate_color_map():
    import Main_Code as MC
    print('Pair No. | ColorMajor | ColorMinor')
    print('-----------------------------------')
    for i, major in enumerate(MC.MAJOR_COLORS):
        for j, minor in enumerate(MC.MINOR_COLORS):
            print(i * 5 + j+1,"       ", major,"       ", minor)

def color_pair_to_string(major_color, minor_color):
  return f'{major_color} {minor_color}'