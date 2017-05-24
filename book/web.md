# web相关

**wsgi**
https://lecture.silentnotes.top/python-wsgi.htm

**Python web 框架**

## [Django](django/django)

> The Web framework for perfectionists with deadlines. https://www.djangoproject.com/
> Django是一个开放源代码的Web应用框架，由Python写成。采用了MVC的软件设计模式，即模型M，视图V和控制器C。它最初是被开发来用于管理劳伦斯出版集团旗下的一些以新闻内容为主的网站的。并于2005年7月在BSD许可证下发布。这套框架是以比利时的吉普赛爵士吉他手Django Reinhardt来命名的。


## [flask](pallets/flask)

> A microframework based on Werkzeug, Jinja2 and good intentions http://flask.pocoo.org/
> Flask是一个使用Python编写的轻量级Web应用框架。基于Werkzeug WSGI工具箱和Jinja2 模板引擎。 Flask使用BSD授权。
> Flask也被称为“microframework”，因为它使用简单的核心，用extension增加其他功能。Flask没有默认使用的数据库、窗体验证工具。然而，Flask保留了扩增的弹性，可以用Flask-extension加入这些功能：ORM、窗体验证工具、文件上传、各种开放式身份验证技术。


## [tornado](tornadoweb/tornado)

> Tornado is a Python web framework and asynchronous networking library, originally developed at FriendFeed.http://www.tornadoweb.org/
> Tornado全称Tornado Web Server，是一个用Python语言写成的Web服务器兼Web应用框架，由FriendFeed公司在自己的网站FriendFeed中使用，被Facebook收购以后框架以开源软件形式开放给大众。


## [bottle](bottlepy/bottle)

> bottle.py is a fast and simple micro-framework for python web-applications. http://bottlepy.org/
> Bottle是一个非常精致的WSGI框架，它提供了 Python Web开发中需要的基本支持：URL路由，Request/Response对象封装，模板支持，与WSGI服务器集成支持。整个框架的全部代码约有 4000行，它的核心部分没有其他任何依赖，只要有Python环境就可以运行。
> Bottle适用于小型的Web开发，在应用程序规模比较小的情况下可以实现快速开发。但是由于自身功能所限，对于大型的Web程序，Bottle的功能略显不足，程序员需要手动管理模块、数据库、配置等等，与Pylons等框架相比Bottle的优势就难以体现出来了。


## [falcon](falconry/falcon)

> Falcon is a bare metal Python framework for building high-performance HTTP APIs, app backends, and higher-level frameworks. https://falcon.readthedocs.io/en/stable/
> Falcon是一个构建云API的高性能Python框架，鼓励使用REST架构风格。


## [sanic](channelcat/sanic)

> Python 3.5+ web server that's written to go fast
> sanic是一款用python3.5+写的web framework，用法和flask类似，sanic的特点是非常快

## [pyramid](Pylons/pyramid)

> Pyramid web framework https://trypyramid.com/
> Pyramid希望能够做比Flask更大和复杂的应用。因此，它的引导工具会创建一个更大的项目框架
> 跟别的框架相比，Pyramid的引导工具特别的灵活。它没有被限制在一个默认应用里;pcreate可以使用任何数量的项目模板。包括我们在上面使用starter模板创建出来的，包含SQLAlchemy和ZODB支撑的项目。在PyPi上，可以找到依赖于Google App Engine，jQuery Mobile，Jinja2 templating，modern frontend frameworks等等的模板。
