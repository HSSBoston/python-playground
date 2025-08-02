

def vformat_list(in_list):
  return_str =""
  columns = 3
  col_used = 0
  row_string = ""
  for item in in_list:
    row_string = row_string + f"{item:36}"
    col_used = col_used + 1
    if col_used == columns:
      return_str = return_str + row_string + "\n"
      col_used = 0
      row_string =""
  if (len(row_string)>0):
    return_str = return_str + row_string +"\n"
  return return_str