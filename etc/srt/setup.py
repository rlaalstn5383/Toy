from setuptools import setup, find_packages

setup(
    name='srt-macro',
    version='0.1',
    author='Minsoo Kim',
    author_email='mskim5383@gmail.com',
    description='srt-macro',
    packages=find_packages('.'),
    include_package_data=True,
    zip_safe=False,
    scripts=['bin/srt-macro'],
    install_requires=[
        'heconvert',
        'requests',
    ],
)
