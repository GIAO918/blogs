class MusicPlayer():
    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:  # 每一次创建对象，都会得到第一次创建对象的引用
            cls.instance = super().__new__(cls)  # 如果类属性为空，把对象的内存引用赋值给类属性
        return cls.instance

    def __init__(self):
        if MusicPlayer.init_flag == True:  # 如果执行过初始化动作，直接返回
            return
        print("我正在初始化")
        MusicPlayer.init_flag = True


p1 = MusicPlayer()
p2 = MusicPlayer()
print(p1)
print(p2)
