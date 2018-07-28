# 面试题

## 为什么切片和区间会忽略最后一个元素

> 在切片和区间操作不包含区间范围的最后一个元素是Python的风格，
> 这一习惯符合Python、C和其他语言里以0作为起始下标的传统
> 这样做有几个好处

- 当只有最后一个位置信息时，我们可以快速看出切片和区间里有几个元素
- 当起止信息都可见时，我们可以快速计算出切片和区间的长度，用最后一个数减去第一个下标 (stop - start) 即可
- 这样做也让我们可以利用任意一个下标把序列分割成不重叠的两部分

## 网络题

`为什么TCP连接建立需要三次握手`
>  谢希仁著《计算机网络》

- 为了防止已经失效的连接请求报文突然又传到服务端，因而产生错误
- 为了解决网络中存在延迟的重复分组
- 这个问题的本质是, 信道不可靠, 但是通信双发需要就某个问题达成一致. 而要解决这个问题, 无论你在消息中包含什么信息, 三次通信是理论上的最小值. 所以三次握手不是TCP本身的要求, 而是为了满足"在不可靠信道上可靠地传输信息"这一需求所导致的
- TCP作为一种可靠传输控制协议，其核心思想：既要保证数据可靠传输，又要提高传输的效率，而用三次恰恰可以满足以上两方面的需求

`为什么TCP断开连接需要四次挥手`


## 一些简单的PYTHON测试题

- 编写代码, 打印1-1亿之内的偶数

```python
generator = (i for i in range(1, (10 ** 8) + 1) if i % 2 == 0)
for i in generator:
    print(i)
```

- 写一个函数, 用正则表达式清除字符串中[]和其中的内容。

```python
s = "[lol]你好，帮我把这些markup清掉，[smile]。谢谢！"
```

- 请使用python, 对下面的函数进行处理
```python
def hello(name):
    print("hello, %s" % name)
```

在函数被调用时打印耗时详情

```python
<function name: hello>
<function call begin>
hello, tom
<function call end>
[timecosts: 3.81469726562e-06s]
```

- 写一个函数, 将驼峰命名法字符串转成下划线命名字符串(需考虑各类编码中常见的命名)

```
e.g.  GetItem -> get_item
      getItem -> get_item
      doIT    -> do_IT
```

- 有一个列表：[1, 2, 3, 4...n]，n=20；请编写代码打印如下规律的输出：

```
1 [1*, 2, 3, 4, 5]
2 [1, 2*, 3, 4, 5]
3 [1, 2, 3*, 4, 5]
4 [2, 3, 4*, 5, 6]
5 [3, 4, 5*, 6, 7]
6 [4, 5, 6*, 7, 8]
...

20 [16, 17, 18, 19, 20*]
```

- 写一个程序模拟银行排队, 只有一个队伍, 一个用户进入时允许插队(进入队伍任意位置), 但要保证每次导致队伍变更, 队伍中受影响的人都收到通知

```
Customer A line up at position 11
```

```
Customer B: order changed to 12
Customer C: order changed to 13
Customer D: order changed to 14
```

- 用户系统, 存在相互关注的动作, 当进入某个人的个人主页, 需要展示其粉丝数, 关注数, 粉丝列表以及关注列表. 请简要描述解决方案, 包括db建模/数据层/业务层, 以及应对高并发/关注取关等情况的处理逻辑


- 给定一些NxN的矩阵，对于任意的路线，定义其【和】为其线路上所有节点的数字的和，计算从左上角到右下角的路线和最小值。每条路线只能从某一点到其周围（上下左右）的点，不可斜行。 例如，


```
4,6
2,8 的路线和最小值为 4-2-8 14

1,2,3
4,5,6
7,8,9 的路线和最小值为 1-2-3-6-9 21
```
程序只需输出最小和值即可（一个数字）

1. 是否了解动态语言的鸭子模型

2. 是否了解可变参数与关键字参数

3. 对函数式编程有初步了解

4. 是否知道列表生成式

5. 是否知道 lambda/decorator/slots

6. 为什么要把缺省参数设为 immutable

7. 是否知道 Mixin

8. 是否知道 WSGI 接口

9. 是否知道异步框架如 gevent/tornado

10. 是否深入了解过 Python 的 GC 和 GIL

## Django


24、django、flask、tornado框架的比较？

25、什么是wsgi？

26、django请求的生命周期？

27、列举django的内置组件？

28、列举django中间件的5个方法？以及django中间件的应用场景？

29、简述什么是FBV和CBV？

30、django的request对象是在什么时候创建的？

31、如何给CBV的程序添加装饰器？

32、列举django orm 中所有的方法（QuerySet对象的所有方法）

33、only和defer的区别？

34、select_related和prefetch_related的区别？

35、filter和exclude的区别？

36、列举django orm中三种能写sql语句的方法。

37、django orm 中如何设置读写分离？

38、F和Q的作用?

39、values和values_list的区别？

40、如何使用django orm批量创建数据？

41、django的Form和ModeForm的作用？

42、django的Form组件中，如果字段中包含choices参数，请使用两种方式实现数据源实时更新。

43、django的Model中的ForeignKey字段中的on_delete参数有什么作用？

44、django中csrf的实现机制？

45、django如何实现websocket？

46、基于django使用ajax发送post请求时，都可以使用哪种方法携带csrf token？

47、django中如何实现orm表中添加数据时创建一条日志记录。

48、django缓存如何设置？

49、django的缓存能使用redis吗？如果可以的话，如何配置？

50、django路由系统中name的作用？

51、django的模板中filter和simple_tag的区别？

52、django-debug-toolbar的作用？

53、django中如何实现单元测试？

54、解释orm中 db first 和 code first的含义？

55、django中如何根据数据库表生成model中的类？

56、使用orm和原生sql的优缺点？

57、简述MVC和MTV

58、django的contenttype组件的作用？

59、谈谈你对restfull 规范的认识？

60、接口的幂等性是什么意思？

61、什么是RPC？

62、Http和Https的区别？

63、为什么要使用django rest framework框架？

64、django rest framework框架中都有那些组件？

65、django rest framework框架中的视图都可以继承哪些类？

66、简述 django rest framework框架的认证流程。

67、django rest framework如何实现的用户访问频率控制？

## Flask

68、Flask框架的优势？

69、Flask框架依赖组件？

70、Flask蓝图的作用？

71、列举使用过的Flask第三方组件？

72、简述Flask上下文管理流程?

73、Flask中的g的作用？

74、Flask中上下文管理主要涉及到了那些相关的类？并描述类主要作用？

75、为什么要Flask把Local对象中的的值stack 维护成一个列表？

76、Flask中多app应用是怎么完成？

77、在Flask中实现WebSocket需要什么组件？

78、wtforms组件的作用？

79、Flask框架默认session处理机制？

80、解释Flask框架中的Local对象和threading.local对象的区别？

81、Flask中 blinker 是什么？

82、SQLAlchemy中的 session和scoped_session 的区别？

83、SQLAlchemy如何执行原生SQL？

84、ORM的实现原理？

85、DBUtils模块的作用？


87、SQLAchemy中如何为表设置引擎和字符编码？

88、SQLAchemy中如何设置联合唯一索引？

89、简述Tornado框架的特点。

90、简述Tornado框架中Future对象的作用？

91、Tornado框架中如何编写WebSocket程序？

92、Tornado中静态文件是如何处理的？如：
<link href="\{\{static_url("commons.css")}}" rel="stylesheet" />

93、Tornado操作MySQL使用的模块？

94、Tornado操作redis使用的模块？

95、简述Tornado框架的适用场景？

## supervisor

- supervisor的实现
- 进程管理，客户端通讯

## celery

- celery的基本使用
- celery基本架构


## gunicorn

- gunicorn实现原理及架构


## redis

- 基本使用命令
- 生态的了解
- 用到哪些数据结构如跳表等


## MySQL

- MySQL基本架构
- 性能问题如何调优，索引怎么建等
- MySQL的生态，分库分表 主从备份 主主备份等
