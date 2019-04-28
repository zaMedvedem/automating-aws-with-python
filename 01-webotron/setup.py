from setuptools import setup

setup(
    name='webotron-80',
    version='0.1',
    author='Yevgen Reus',
    author_email='yevgen.reus@gmail.com',
    description='Webotron 80 is a tool to deploy static websites to AWS.',
    license='GPLv3+',
    packages=['webotron'],
    url='https://github.com/zaMedvedem/automating-aws-with-python/tree/master/01-webotron',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        webotron=webotron.webotron:cli
    '''
)
