from setuptools import find_packages, setup

setup(
    name='testlib',
    packages=find_packages(include=['testlib']),
    version='0.1.0',
    description='Test library',
    #author='AI Infra Team',
    #license='MIT',
    install_requires=[
        #'fastapi',
        #'prometheus_client',
        #'starlette==0.18.0',
        #'jaeger-client'
        ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
