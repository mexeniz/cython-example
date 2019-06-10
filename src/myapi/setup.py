from distutils.core import Extension, setup
from Cython.Build import cythonize

# define an extension that will be cythonized and compiled
ext = [
    Extension(name='app', sources=['app.py']),
    Extension(name='vecutil', sources=['vecutil.py']),
    Extension(name='clf', sources=['clf.py'])
    ]
setup(
    name='myapi',
    ext_modules=cythonize(ext)
    )