from setuptools import setup, find_packages

def get_requirements(file_path):
    with open(file_path) as file:
        lines = file.read().splitlines()
    return [line for line in lines if line.strip() and not line.startswith('-e')]
setup(
    name='mlproject',
    version='0.1.0',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    author='Houda Aitmouch',
    author_email='aitmouchhouda4@gmail.com',
    description='A machine learning project with basic setup.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/houda-aitmouch/mlproject',
    python_requires='>=3.7',
)