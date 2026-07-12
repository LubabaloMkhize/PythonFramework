import configparser

config=configparser.RawConfigParser()
config.read("./Configurations/config.ini")

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

    @staticmethod
    def getInvalidUsername():
        username=config.get('invalid login data', 'username')
        return  username

    @staticmethod
    def getInvalidPassword():
        password=config.get('invalid login data','password')
        return password

    @staticmethod
    def getFirstname():
        firstname = config.get('checkout information', 'firstname')
        return firstname

    @staticmethod
    def getLastname():
        lastname = config.get('checkout information', 'lastname')
        return lastname

    @staticmethod
    def getPostalCode():
        postalcode = config.get('checkout information', 'postalcode')
        return postalcode
