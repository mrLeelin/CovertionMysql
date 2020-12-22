# main function
import MysqlHelper
import ExcelHelper

if __name__ == '__main__':
    #dates = MysqlHelper.get_table_by_table_name_and_uid('item', '5')
    #ExcelHelper.write_xlsx(dates)
    ExcelHelper.read_xlsx(r"C:\Users\703\Desktop\Text\1.xlsx")
