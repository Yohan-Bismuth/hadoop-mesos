import sys
import urllib.request
# Make sure we have a way to build the Module type
Module = type(urllib.request)
import sys

class RemoteImporter:
    def __init__(self, *args):
        self.module_names = args
        
    def find_module(self, fullname, path=None):
        if fullname in self.module_names:
            self.path = "https://raw.githubusercontent.com/Yohan-Bismuth/hadoop-mesos/master/{0}.py".format(fullname)
            print(self.path)
            return self
        return None

    def load_module(self, path):
        print(self.path)
        path=self.path
        with urllib.request.urlopen(path) as stream:
            code = stream.read()
            
            compiled_code = compile(code, path, 'exec')
            module = Module(path)
            eval(compiled_code, locals=module.__dict__)
            return module
        
sys.meta_path.append(RemoteImporter('test_lib'))
