from setuptools import setup, Extension

def ext_modules(build=False):
  if build:
    sources = ['fontconfig.pyx']
  else:
    sources = ['fontconfig.c']
  ext = [Extension('fontconfig', sources, libraries=["fontconfig"])]
  return ext

args = {}

if __name__ == '__main__':
  try:
    from Cython.Distutils import build_ext
    args.update(cmdclass={'build_ext': build_ext})
  except ImportError:
    args.update(ext_modules=ext_modules(False))
  else:
    args.update(ext_modules=ext_modules(True))
  setup(**args)
