from setuptools import setup

setup(
    name='augmentor_no_random',
    packages=['Augmentor'],
    version='0.2.12',
    description='Image augmentation library for Machine Learning',
    long_description='Image augmentation library for Machine Learning',
    license='MIT',
    author='Marcus D. Bloice',
    author_email='marcus.bloice@medunigraz.at',
    url='https://github.com/mdbloice/Augmentor',                            # URL to GitHub repo
    # download_url='https://github.com/mdbloice/Augmentor/tarball/0.1.1',   # Get this using git tag
    keywords=['image', 'augmentation', 'artificial', 'generation', 'machine', 'learning'],
    include_package_data=True,  # This will include all files in MANIFEST.in in the package when installing.
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'Pillow>=5.2.0',
        'tqdm>=4.9.0',
        #'future>=0.16.0',
        'numpy>=1.11.0',
        'futures>=3.2.0; python_version == "2.7"'
    ]
    # zip_safe=False # Check this later.
)
