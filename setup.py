from setuptools import find_packages
from setuptools import setup


version = '2.0.0rc2.dev0'

setup(
    name='collective.patterns.widgets',
    version=version,
    description="patternslib based plone widgets",
    long_description='%s\n%s' % (
        open("README.rst").read(),
        open("CHANGES.rst").read(),
    ),
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='plone widgets z3cform archetypes',
    author='Nathan Van Gheem',
    author_email='vangheem@gmail.com',
    url='https://github.com/syslabcom/collective.patterns.widgets',
    license='GPL',
    packages=find_packages(),
    namespace_packages=['collective', 'collective.patterns'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        # needed because we use bundles
        'Products.ResourceRegistries>=2.1',
        # nedded because users vocabulary was added here
        'plone.app.vocabularies>=2.1.12dev',
        # needed for compatibility with jQuery 1.9+
        'Products.CMFPlone>=4.3.4'
    ],
    extras_require={
        'test': [
            'plone.app.robotframework[debug]',
            'collective.patterns.widgets[archetypes, dexterity]',
            'plone.app.testing>=4.2.4',  # we need ROBOT_TEST_LEVEL
            'mock',
        ],
        'archetypes': [
            'DateTime',
            'Products.Archetypes',
            'archetypes.schemaextender',
        ],
        'dexterity': [
            'pytz',
            'plone.app.dexterity',
            'plone.app.contenttypes>=1.1b1',
            'plone.app.event>=1.2',
        ],
    },
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
