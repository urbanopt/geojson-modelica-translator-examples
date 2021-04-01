"""
****************************************************************************************************
:copyright (c) 2019-2021 URBANopt, Alliance for Sustainable Energy, LLC, and other contributors.

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

import os
import shutil
import unittest
from pathlib import Path

# from buildingspy.io.outputfile import Reader
from geojson_modelica_translator.geojson_modelica_translator import (
    GeoJsonModelicaTranslator
)
from geojson_modelica_translator.model_connectors.couplings import (
    Coupling,
    CouplingGraph
)
from geojson_modelica_translator.model_connectors.districts import District
from geojson_modelica_translator.model_connectors.energy_transfer_systems.ets_cold_water_stub import (
    EtsColdWaterStub
)
from geojson_modelica_translator.model_connectors.energy_transfer_systems.ets_hot_water_stub import (
    EtsHotWaterStub
)
from geojson_modelica_translator.model_connectors.load_connectors.teaser import (
    Teaser
)
from geojson_modelica_translator.modelica.modelica_runner import ModelicaRunner
from geojson_modelica_translator.system_parameters.system_parameters import (
    SystemParameters
)


class GeoJSONUrbanOptExampleFileTest(unittest.TestCase):
    def setUp(self):
        self.project_name = "geojson_8_buildings"
        self.data_dir = Path(__file__).parent.parent / "examples" / "uo_teaser_project"
        self.output_dir = Path(__file__).parent.parent / "output"
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        self.results_path = self.output_dir / self.project_name
        if self.results_path.exists():
            shutil.rmtree(self.results_path)

    def test_to_modelica_defaults(self):
        feature_json_file = self.data_dir / f"{self.project_name}.json"

        gj = GeoJsonModelicaTranslator.from_geojson(feature_json_file)
        sys_params_json_file = self.data_dir / 'geojson_8_system_params.json'
        sys_params = SystemParameters(sys_params_json_file)
        gj.set_system_parameters(sys_params)
        gj.process_loads()

        self.assertEqual(len(gj.loads), 8)

        all_couplings = []

        for geojson_load in gj.json_loads:
            teaser_load = Teaser(sys_params, geojson_load)

            hot_stub = EtsHotWaterStub(sys_params)
            cold_stub = EtsColdWaterStub(sys_params)
            all_couplings.append(Coupling(teaser_load, hot_stub))
            all_couplings.append(Coupling(teaser_load, cold_stub))

        graph = CouplingGraph(all_couplings)

        district = District(
            root_dir=self.output_dir,
            project_name=self.project_name,
            system_parameters=sys_params,
            coupling_graph=graph
        )

        district.to_modelica()

        # run a single file to make sure it simulates
        mr = ModelicaRunner()

        root_path = os.path.abspath(os.path.join(district._scaffold.districts_path.files_dir))
        exitcode = mr.run_in_docker(os.path.join(root_path, 'DistrictEnergySystem.mo'),
                                    run_path=Path(district._scaffold.project_path).resolve().parent,
                                    project_name=district._scaffold.project_name)
        self.assertEqual(0, exitcode)

    # def test_teaser_district(self):
    #     """Create full network with 8 buildings -- need to add Teaser_Indirect to GMT to make this work
    #     """
    #     feature_json_file = self.data_dir / f"{self.project_name}.json"
    #
    #     gj = GeoJsonModelicaTranslator.from_geojson(feature_json_file)
    #     sys_params_json_file = self.data_dir / 'geojson_8_system_params.json'
    #     sys_params = SystemParameters(sys_params_json_file)
    #     gj.set_system_parameters(sys_params)  # not needed right now
    #
    #     # create cooling network and plant
    #     cooling_network = Network2Pipe(sys_params)
    #     cooling_plant = CoolingPlant(sys_params)
    #
    #     # create heating network and plant
    #     heating_network = Network2Pipe(sys_params)
    #     heating_plant = HeatingPlant(sys_params)
    #
    #     # create our load/ets/stubs
    #     # store all couplings to construct the District system
    #     all_couplings = [
    #         Coupling(cooling_network, cooling_plant),
    #         Coupling(heating_network, heating_plant),
    #     ]
    #
    #     for geojson_load in gj.json_loads:
    #         time_series_load = Teaser(sys_params, geojson_load)
    #         geojson_load_id = geojson_load.feature.properties["id"]
    #
    #         cooling_indirect = CoolingIndirect(sys_params, geojson_load_id)
    #         all_couplings.append(Coupling(time_series_load, cooling_indirect))
    #         all_couplings.append(Coupling(cooling_indirect, cooling_network))
    #
    #         heating_indirect = HeatingIndirect(sys_params, geojson_load_id)
    #         all_couplings.append(Coupling(time_series_load, heating_indirect))
    #         all_couplings.append(Coupling(heating_indirect, heating_network))
    #
    #     # create the couplings and graph
    #     graph = CouplingGraph(all_couplings)
    #
    #     district = District(
    #         root_dir=self.output_dir,
    #         project_name=self.project_name,
    #         system_parameters=self.sys_params,
    #         coupling_graph=graph
    #     )
    #     district.to_modelica()
