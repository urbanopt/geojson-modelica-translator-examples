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

import shutil
from unittest import TestCase
from pathlib import Path

# from buildingspy.io.outputfile import Reader
from geojson_modelica_translator.geojson_modelica_translator import (
    GeoJsonModelicaTranslator
)

# from geojson_modelica_translator.modelica.modelica_runner import ModelicaRunner


class GeoJSONUrbanOptExampleFileTest(TestCase):
    def setUp(self):
        self.project_name = "geojson_8_buildings"
        self.data_dir = Path(__file__).parent.parent / "examples" / "uo_teaser_project"
        self.output_dir = Path(__file__).parent.parent / "output"
        if not self.output_dir.exists():
            self.output_dir.mkdir(parents=True, exist_ok=False)

        self.results_path = self.output_dir / self.project_name
        if self.results_path.exists():
            shutil.rmtree(self.results_path)

    def test_to_modelica_defaults(self):
        feature_json_file = self.data_dir / f"{self.project_name}.json"
        sys_params_json_file = self.data_dir / 'geojson_8_system_params.json'

        gmt = GeoJsonModelicaTranslator(
            feature_json_file,
            sys_params_json_file,
            self.output_dir,
            self.project_name,
        )
        gmt.to_modelica()

        # Assert a building successfully built a model
        self.assertTrue(self.results_path / "Loads" / "B6" / "building.mo")

        # mr = ModelicaRunner()

        # run a single building - no longer able to run with JModelica.
        # file_to_run = self.results_path / "Loads" / "B2" / "coupling.mo"
        # success, _ = mr.run_in_docker(
        #     file_to_run,
        #     run_path=self.output_dir,
        #     project_name=self.project_name
        # )
        # self.assertTrue(success)

        # results_path = Path(self.output_dir / f"{self.project_name}_results")
        # self.assertTrue(Path(results_path) / 'stdout.log')
        # self.assertTrue(
        #     Path(results_path) / 'geojson_8_buildings_Districts_DistrictEnergySystem.fmu'
        # )
        # self.assertTrue(
        #     Path(results_path) / 'geojson_8_buildings_Districts_DistrictEnergySystem_result.mat'
        # )

        # run the entire district - no longer able to run with JModelica.

        # file_to_run = self.results_path / "Districts" / "DistrictEnergySystem.mo"
        # success, _ = mr.run_in_docker(
        #     file_to_run,
        #     run_path=self.output_dir,
        #     project_name=self.project_name
        # )
        # self.assertTrue(success)

        # results_path = Path(self.output_dir / f"{self.project_name}_results")
        # self.assertTrue(Path(results_path) / 'stdout.log')
        # self.assertTrue(
        #     Path(results_path) / 'geojson_8_buildings_Districts_DistrictEnergySystem.fmu'
        # )
        # self.assertTrue(
        #     Path(results_path) / 'geojson_8_buildings_Districts_DistrictEnergySystem_result.mat'
        # )
