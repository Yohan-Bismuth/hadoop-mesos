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
            self.path = "https://github.com/Yohan-Bismuth/hadoop-mesos/blob/master/{0}.py".format(lib)
            return self
        return None

    def load_module(self, path):
        with urllib.request.urlopen(path) as stream:
            code = stream.read()
            
            compiled_code = compile(code, url, 'exec')
            module = Module(parts)
            eval(compiled_code, locals=module.__dict__)
            return module
        
sys.meta_path.append(GitHubImporter('test_lib'))
