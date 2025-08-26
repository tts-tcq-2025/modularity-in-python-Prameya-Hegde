import Main_Code as MC

def get_color_from_pair_number(pair_number):
  zero_based_pair_number = pair_number - 1
  major_index = zero_based_pair_number // len(MC.MINOR_COLORS)
  if major_index >= len(MC.MAJOR_COLORS):
    raise Exception('Major index out of range')
  minor_index = zero_based_pair_number % len(MC.MINOR_COLORS)
  if minor_index >= len(MC.MINOR_COLORS):
    raise Exception('Minor index out of range')
  return MC.MAJOR_COLORS[major_index], MC.MINOR_COLORS[minor_index]

def get_pair_number_from_color(major_color, minor_color):
  try:
    major_index = MC.MAJOR_COLORS.index(major_color)
  except ValueError:
    raise Exception('Major index out of range')
  try:
    minor_index = MC.MINOR_COLORS.index(minor_color)
  except ValueError:
    raise Exception('Minor index out of range')
  return major_index * len(MC.MINOR_COLORS) + minor_index + 1