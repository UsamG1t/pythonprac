class Sender:
    check = False
    
    @classmethod
    def report(cls):
        if not cls.check:
            cls.check = True
            print('Greetings!')
        else:
            print("Get away!")

class Asker:

    @staticmethod
    def askall(lst):
        for item in lst:
            item.report()