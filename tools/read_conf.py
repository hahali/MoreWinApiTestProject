import configparser
from tools import project_path

class ReadConfig:
    #读取配置文件
    @staticmethod
    def read_config(file_name,section,option):
        cf=configparser.ConfigParser()
        cf.read(file_name,encoding='utf-8')
        # return cf.get(section,option)
        return cf[section][option]


if __name__=='__main__':
    print(ReadConfig.read_config(project_path.case_config_path,'MODE','mode'))



