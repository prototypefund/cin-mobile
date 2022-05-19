from pythonforandroid.recipe import PythonRecipe, IncludedFilesBehaviour
from os import environ


class CinRecipe(PythonRecipe):
    depends = ['python3', 'setuptools']
    url = 'https://gitlab.com/ccodein/cin/cin/-/archive/main/cin-main.zip'

    site_packages_name = 'cin'
    call_hostpython_via_targetpython = False


class CinDevelopRecipe(IncludedFilesBehaviour, PythonRecipe):
    depends = ['python3', 'setuptools']
    if 'CIN_PATH' in environ:
        src_filename = environ['CIN_PATH']
    call_hostpython_via_targetpython = False
    install_in_hostpython = True
    site_packages_name = 'cin'


if 'CIN_PATH' in environ:
    recipe = CinDevelopRecipe()
else:
    recipe = CinRecipe()
