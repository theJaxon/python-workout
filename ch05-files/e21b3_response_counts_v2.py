def log_return_code_summary(log_file_path):
  return_code_dict = {}

  with open(log_file_path) as log_file:
    for line in log_file:
      return_code = line.split()[8]
      return_code_dict[return_code] = return_code_dict.get(return_code, 0) + 1
    return return_code_dict

print(log_return_code_summary('mini-access.log'))