# What's included in this workflow demo?
1. `sdk_project_dir.zip` is the result of the first 2 cli commands
1. You will need to install the SDK and Run the scenario to generate building loads
1. The first uo_des command will generate the demo_sys_params.json file and the weather files
1. The second uo_des command will generate the contents of demo_modelica_model.zip

# Using the URBANopt CLI
Detailed instructions can be found at http://docs.urbanopt.net \
Help in the terminal for UO SDK is at `uo -h` \
Help in the terminal for GMT is at `uo_des -h`

## Install
Installation instructions for your platform can be found at https://docs.urbanopt.net/installation/installation.html

tldr for  developers:
- Install [Ruby 2.7](https://github.com/rbenv/rbenv#installing-ruby-versions)
- Install [OpenStudio 3.5](https://github.com/NREL/OpenStudio/releases/tag/v3.5.0)
- Clone the UO SDK CLI: https://github.com/urbanopt/urbanopt-cli

Perform the following steps from inside the urbanopt-cli dir:
`cd urbanopt-cli`

## Create a project folder
`uo create -p ../gmt_demo`

## Create a scenario file (csv)
`uo create -s ../gmt_demo/example_project.json`

## Run the scenario
`uo run -s ../gmt_demo/baseline_scenario.csv -f ../gmt_demo/example_project.json`

## Post-process the scenario
`uo process -d -s ../gmt_demo/baseline_scenario.csv -f ../gmt_demo/example_project.json`

Move to the GMT dir (ensure you've pulled the newest from develop branch):
`cd ../geojson-modelica-translator` \
There are aliases to these commands from inside the sdk uo cli.

## Create a system parameters file
`uo_des build-sys-param demo_sys_params.json ../gmt_demo/baseline_scenario.csv ../gmt_demo/example_project.json`

## Create a modelica model
`uo_des create-model demo_sys_params.json ../gmt_demo/example_project.json ./demo_model`
