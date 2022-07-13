from pysd.translators.vensim.vensim_file import VensimFile
from pysd.translators.xmile.xmile_file import XmileFile
from pysd.builders.stan.stan_model_builder import *


vf = VensimFile("vensim_models/Inventory.mdl")
#vf = XmileFile("vensim_models/repair.xmile")
vf.parse()

am = vf.get_abstract_model()

stan_builder = StanModelBuilder(am)
# print(stan_builder.build_function_block(["failure_count", "repair_time"], ["battle_field", "repair_shop"])) # repair
print(stan_builder.create_stan_program(["demand"], ["inventory", "backlog"]))

# for section in am.sections:
#     for element in section.elements:
#         print("*" * 10)
#         print(f"name: {element.name}")
#         print(f"length: {len(element.components)}")
#         for component in element.components:
#             print(f"type: {component.type}")
#             print(f"subtype: {component.subtype}")
#             print(f"subscript: {component.subscripts}")
#             print(component.ast)

# (
#     ArithmeticStructure(
#         operators=['*', '/'],
#         arguments=(
#             ReferenceStructure(reference='a', subscripts=None),
#             ReferenceStructure(reference='b', subscripts=None),
#             1)
#     ),
#     5
# )