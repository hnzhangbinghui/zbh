# -*- coding= utf-8 -*-
# @Time: 2024-02-26 15:46
# @Author： Zbh

import pytest
import requests
from zbh.Interface_automation import func_get,func_post,func_read_csv,func_write_csv
from zbh.Interface_automation import api_run


result_path=r"C:\Users\zhangbinghui\PycharmProjects\zbh\Interface_automation\test_result.csv"


def test_run():
    func_write_csv.write_csv(result_path,api_run.test_api())




if __name__ == "__main__":
    pytest.main(["-vs","test_run.py"])












