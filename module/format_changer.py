# Shift-JIS→utf-8
import codecs

def changer():
  # Changing file format 
  Shift_JIS_csv_path = "/content/RPA_for_Gate./data_shift_jis.csv"    
  utf8_csv_path = "/content/RPA_for_Gate./data_utf-8.csv"

  # Shift-JIS→utf-8
  file_Shift_JIS = codecs.open(Shift_JIS_csv_path, "r", "Shift_JIS")
  file_utf = codecs.open(utf8_csv_path, "w", "utf-8")
  for row in file_Shift_JIS:
      file_utf.write(row)
  file_Shift_JIS.close()
  file_utf.close()
