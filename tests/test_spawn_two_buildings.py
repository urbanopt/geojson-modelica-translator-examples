"""
****************************************************************************************************
:copyright (c) 2019-2020 URBANopt, Alliance for Sustainable Energy, LLC, and other contributors.

All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted
provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions
and the following disclaimer.

Redistributions in binary form must reproduce the above copyright notice, this list of conditions
and the following disclaimer in the documentation and/or other materials provided with the
distribution.

Neither the name of the copyright holder nor the names of its contributors may be used to endorse
or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
****************************************************************************************************
"""

import itertools
import os
import shutil
import unittest

from geojson_modelica_translator.geojson_modelica_translator import (
    GeoJsonModelicaTranslator
)
from geojson_modelica_translator.system_parameters.system_parameters import (
    SystemParameters
)


class SpawnTwoBuildingTest(unittest.TestCase):
    def setUp(self):
        self.data_dir = os.path.join(os.path.dirname(__file__), "..", "examples", "spawn_two_buildings")
        self.output_dir = os.path.join(os.path.dirname(__file__), "..", "output")
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def test_from_geojson(self):
        filename = os.path.join(self.data_dir, "spawn_geojson.json")
        gj = GeoJsonModelicaTranslator.from_geojson(filename)

        self.assertEqual(len(gj.buildings), 2)

    def test_to_modelica_defaults(self):
        project_name = "spawn_geojson"
        results_path = os.path.join(self.output_dir, project_name)
        if os.path.exists(results_path):
            shutil.rmtree(results_path)

        filename = os.path.join(self.data_dir, f"{project_name}.json")
        gj = GeoJsonModelicaTranslator.from_geojson(filename)
        filename = os.path.join(self.data_dir, 'spawn_system_params.json')
        sys_params = SystemParameters(filename)
        gj.set_system_parameters(sys_params)
        gj.to_modelica(project_name, self.output_dir)

        # setup what we are going to check
        model_names = [
            "Floor",
            "ICT",
            "Meeting",
            "Office",
            "package",
            "Restroom",
            "Storage",
        ]
        building_paths = [
            os.path.join(gj.scaffold.loads_path.files_dir, b.dirname) for b in gj.buildings
        ]
        path_checks = [f"{os.path.sep.join(r)}.mo" for r in itertools.product(building_paths, model_names)]

        for p in path_checks:
            self.assertTrue(os.path.exists(p), f"Path not found: {p}")

        # go through the generated buildings and ensure that the resources are created
        resource_names = [
            "InternalGains_Floor",
            "InternalGains_ICT",
            "InternalGains_Meeting",
            "InternalGains_Office",
            "InternalGains_Restroom",
            "InternalGains_Storage",
        ]

        for b in gj.buildings:
            for resource_name in resource_names:
                # TEASER 0.7.2 used .txt for schedule files
                path = os.path.join(gj.scaffold.loads_path.files_dir, "Resources", "Data",
                                    b.dirname, f"{resource_name}.txt")
                self.assertTrue(os.path.exists(path), f"Path not found: {path}")


# import os
# from geojson_modelica_translator.geojson_modelica_translator import GeoJsonModelicaTranslator
# from geojson_modelica_translator.system_parameters.system_parameters import SystemParameters
# from geojson_modelica_translator.model_connectors.spawn import SpawnConnector
#
#
# prj_dir = 'spawn_two_building'
#
# # load in the example geojson with a single offie building
# filename = os.path.abspath('spawn_geojson_ex2.json')
# gj = GeoJsonModelicaTranslator.from_geojson(filename)
# gj.scaffold_directory(prj_dir)  # use the GeoJson translator to scaffold out the directory
#
# # load system parameter data
# filename = os.path.abspath('spawn_system_params_ex2.json')
# sys_params = SystemParameters(filename)
#
# # now test the spawn connector (independent of the larger geojson translator
# self.spawn = SpawnConnector(sys_params)
#
# for b in gj.buildings:
#     self.spawn.add_building(b)
#
# self.spawn.to_modelica('spawn_two_building', prj_dir)
