# TODO ����

class BaseConfig(object):
    # TODO ��������
    # MySQL����������
    HOSTNAME = "127.0.0.1"
    # MySQL�����Ķ˿ںţ�Ĭ��3306
    PORT = 3306
    # ����MySQL���û���
    USERNAME = "root"
    # ����MySQL������
    PASSWORD = "root"
    # MySQL�ϴ��������ݿ�����
    DATABASE = "smart_eye"
    pass


class DevelopmentConfig(BaseConfig):
    # TODO ������������
    pass


class TestConfig(BaseConfig):
    # TODO ���Ի�������
    pass


class ProductionConfig(BaseConfig):
    # TODO ������������
    pass
