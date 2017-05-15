import sys, os, imp, tempfile, urllib.request

class RemoteImporter:
    def __init__(self, *args):
        self.module_names = args

    def find_module(self, fullname, path):
        if fullname in self.module_names:
            self.path = "https://raw.githubusercontent.com/Yohan-Bismuth/hadoop-mesos/master/{0}.py".format(fullname)
            return self
        return None

    def load_module(self, path):
        path=self.path
        code = urllib.request.urlopen(path).read().decode("utf-8")
        bn=basename(path).split('.')[0]
        fd, tmp_path = tempfile.mkstemp()
        tmp_mod = open(tmp_path, 'w')
        try:
            tmp_mod.write("mesos_scheduler = 'marathon'\n")
            tmp_mod.write(code)
            sys.path.append(os.path.dirname(tmp_path))
            sys.path.append(tmp_path)

            hadoop_mesos = imp.load_source('hadoop_mesos', tmp_path)
        finally:
            tmp_mod.close()
        return hadoop_mesos

sys.meta_path.append(RemoteImporter('hadoop_mesos'))
