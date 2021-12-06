from setuptools import setup, Extension


pcalc_extension = Extension(
    '_pcalc',
    [
        'swig-src/pcalc_wrap.cxx',
        'power-calculator/parser/parser.cpp',
        'power-calculator/token/token.cpp'
    ],
    include_dirs=['./', './power-calculator'],
)

setup(
    name='libpcalc',
    version='1.0.0',
    
    description='Evaluate Power Calculator expressions from Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',

    author='Abhishek Kumar',
    author_email='abhi.kr.2100@gmail.com',

    url='https://github.com/abhi-kr-2100/libpcalc',

    ext_modules=[pcalc_extension],

    py_modules=['pcalc']
)
