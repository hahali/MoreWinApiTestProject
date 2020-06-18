import os

project_path=os.path.dirname(os.path.dirname(__file__))

#获取用例配置文件的路径
case_config_path = os.path.join(project_path, 'case.config')

#获取测试用例文件的路径
case_path=os.path.join(project_path,'testData','KXliveApiCase.xlsx')

#获取日志配置文件的路径
log_path=os.path.join(project_path,'log','log.conf')

#测试报告目录
report_dir=os.path.join(project_path,'reports')

# print(case_path)
# print(case_config_path)