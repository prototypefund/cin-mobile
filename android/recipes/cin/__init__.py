from pythonforandroid.recipe import PythonRecipe, IncludedFilesBehaviour
from pathlib import Path


class CinRecipe(PythonRecipe):
    depends = ['python3', 'setuptools']
    url = 'https://gitlab.com/ccodein/cin/cin/-/archive/main/cin-main.zip'

    site_packages_name = 'cin'
    call_hostpython_via_targetpython = False

recipe = CinRecipe()

