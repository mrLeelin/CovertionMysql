# excel helper

import pandas as pd
import datetime


def write_xlsx(dates: [dict]):
    """
    写入 xlsx 表
    :param dates:
    :return:
    """
    data_farm = __parse_dict_to_data_frame(dates)
    data_farm.to_excel(r"C:\Users\703\Desktop\Text\1.xlsx")
    pass


def read_xlsx(xlsx_path: str):
    """
    读取 xlsx 表
    :param xlsx xlsx_path:
    :return:
    """
    df = pd.read_excel(xlsx_path, engine='openpyxl')
    
    pass


def __parse_dict_to_data_frame(dates: [dict]) -> pd.DataFrame:
    """
    解析数据库读取出来的 数据转换为 data frame
    :param dates:
    :return:
    """
    result = {}
    for data in dates:
        dict_data = dict(data)
        for key in dict_data.keys():
            value = dict_data.get(key)
            array = []
            if result.__contains__(key):
                array = list(result.get(key))
                pass
            array.append(value)
            result[key] = array
            pass
        pass
    return pd.DataFrame.from_dict(result)
