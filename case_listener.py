class caseListener:
    def method_automation(self,dict_info):
        def _deco(func):
            def __deco(*args, **kwargs):
                print('Start to get test info')
                print('classname: '+dict_info["classname"])
                print('param:'+kwargs["key"])
                try:
                    print('End to get test info')
                except Exception as e:
                    print(e, 'error')
                func(*args, **kwargs)
            return __deco
        return _deco