import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig():

    @staticmethod
    def getBaseURL():
        baseURL=config.get('common details','baseURL')
        return baseURL

    @staticmethod
    def getUsername():
        username=config.get('login data','username')
        return username

    @staticmethod
    def getPassword():
        password=config.get('login data','password')
        return password
