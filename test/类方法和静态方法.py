class People(object):
    country = "China"

    @classmethod
    def get_country(cls):
        return cls.country

    @classmethod
    def set_country(cls, new_country):
        cls.country = new_country


p1 = People()
print(p1.get_country())  # 实例对象可以调用类方法
print(People.get_country())  # 类对象可以调用类方法

People.set_country("北京")  # 使用类方法修改类属性


class People(object):
    country = "上海"

    @staticmethod
    def get_country():
        return People.country


print(People.get_country())
