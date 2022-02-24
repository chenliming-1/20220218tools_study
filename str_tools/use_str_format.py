def format_str():
    """格式化字符串"""
    name="clm"
    print('他的名字是：%s'%name)
    #格式化，float类型
    num = 12.33
    print("这个数字是：%.6f"%num)
    #格式化元组
    t=(1,2,3,4)
    print("这个元组是：%s"%str(t))

def format_str2():
    """format格式化"""
    t1={"username":"张三"}
    t2={"num":"45"}
    t3={"username":"clm",
        "age":"55"
        }
    """"""
    #使用位置
    print("欢迎您：{0}，{1}".format("张三","好久不见"))
    #使用名称
    print("他的名字叫{}，今年{}".format(t1["username"],t2["num"]))
    #传整个字典
    print("他的名字叫{username}，今年{age}".format(**t3))
    point=(1,2)
    #格式化元组
    print("坐标位置是({0[0]},{0[1]})".format(point))
    #格式化类
    user = User("张三",59)
    print(user.show())
class User(object):
    def __init__(self,username,age):
        self.username=username
        self.age=age
    def show(self):
        return "用户名：{self.username},年龄：{self.age}".format(self=self)

    def __str__(self):
        return self.show()





if __name__=='__main__':
    format_str2()