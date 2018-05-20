# coding=utf-8
##定义常量类
class _const(object):
    class ConstError(TypeError):pass

    def __setattr__(self,name,value):
        if self.__dict__.has_key(name):
            raise self.ConstError,"Can't redind const(%s)" % name
        self.__dict__[name]=value

        def __delattr__(self, item):
            if name in self.__dict__:
                raise self.ConstError,"Can't undind const(%s)" % name
            raise NameError,name

import sys
sys.modules[__name__]=_const()
