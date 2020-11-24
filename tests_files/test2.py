import importlib

import os

# all_files = {}
# imp_modules = []
# # all methods from imported modules
# all_methods_from_imported_modules = {}
#
# all_files["package"] = os.listdir('package')
# all_files["main_scripts"] = os.listdir('main_scripts')
#
# for key, value in enumerate(all_files, start=0):
#     print(all_files[value])
#     for file in all_files[value]:
#         if not file.startswith('__'):
#             name = file.split('.')
#             print(name)
#             plugin = f"{value}.{name[0]}"
#             imp_modules.append(importlib.import_module(plugin, "."))
#
#     # fill the dictionary with functions name as key and the actual function as value
#     for index, module in enumerate(imp_modules, start=0):
#         module_methods = dir(module)
#         for item in module_methods:
#             if not item.startswith('_'):
#                 all_methods_from_imported_modules[item] = imp_modules[index].__getattribute__(item)
# methods_array = all_methods_from_imported_modules.keys()
# print(methods_array)

# files in package directory
# files = os.listdir('package')
# # imported modules
# imp_modules = []
# # all methods from imported modules
# all_methods_from_imported_modules = {}
#
# # import all modules
# for file in files:
#     if not file.startswith('__'):
#         name = file.split('.')
#         plugin = f"package.{name[0]}"
#         imp_modules.append(importlib.import_module(plugin, "."))
#
# # fill the dictionary with functions name as key and the actual function as value
# for index, module in enumerate(imp_modules, start=0):
#     module_methods = dir(module)
#     for item in module_methods:
#         if not item.startswith('_'):
#             all_methods_from_imported_modules[item] = imp_modules[index].__getattribute__(item)


