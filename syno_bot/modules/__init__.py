from syno_bot import LOGGER

def __list_all_modules():
    from os.path import dirname, basename, isfile
    import glob
    # This generates a list of modules in this folder for the * in __main__ to work.
    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    all_modules = [basename(f)[:-3] for f in mod_paths if isfile(f)
                   and f.endswith(".py")
                   and not f.endswith('__init__.py')]

    return all_modules

ALL_MODULES = sorted(__list_all_modules())
LOGGER.info("Available modules: %s", str(ALL_MODULES))

# Commonly used constants
ACTION_REPLY, ACTION_EDIT = range(2)
