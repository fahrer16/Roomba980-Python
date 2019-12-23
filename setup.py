from setuptools import find_packages, setup


setup(
    name='Roomba980-Python',
    version='1.2.4',
    license='MIT',
    description='Python program and library to control iRobot Roomba 980 ' \
    'Vacuum Cleaner for UDI ISY. Forked from project from Nick Waterton to ensure compatibility is maintained',
    author_email='fahrer@gmail.com',
    url='https://github.com/fahrer16/Roomba980-Python',
    packages=find_packages(),
    install_requires=['paho-mqtt', 'six'],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'roomba=roomba.__main__:main',
            'roomba-getpassword=roomba.getpassword:main'
        ]
    }
)
