from setuptools import setup, Extension


setup(
    name='libpcalc',
    version='1.0.0',
    
    description='Evaluate Power Calculator expressions from Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',

    author='Abhishek Kumar',
    author_email='abhi.kr.2100@gmail.com',

    url='https://github.com/abhi-kr-2100/libpcalc',

    ext_modules=[Extension('_pcalc', [
        'swig-src/pcalc_wrap.cxx',
        'power-calculator/parser/parser.cpp',
        'power-calculator/token/token.cpp'
    ])],

    py_modules=['pcalc']
)
