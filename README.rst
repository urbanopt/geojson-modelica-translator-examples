GeoJSON to Modelica Translator Examples
---------------------------------------

.. image:: https://travis-ci.org/urbanopt/geojson-modelica-translator-examples.svg?branch=develop
    :target: https://travis-ci.org/urbanopt/geojson-modelica-translator-examples

Description
-----------

This project provides examples on how to use the GeoJSON to Modelica Translator. The examples that are being
developed are shown in the matrix below with the appropriate definition of the loads, ETS model, network model,
and the district plant.

Getting Started
---------------

This project depends on the `GeoJSON to Modelica Translator`_ (GMT). The GMT will be installed when calling
:code:`pip install requirements.txt`; however, the `Modelica Buildings Library`_ (MBL) needs to be installed to build and
run the Modelica-based projects. Follow the instructions in the `GMT readme`_ on installing and configuring the MBL.

To install the dependencies run the following after checking out repository:

.. code-block:: bash

    pip install requests==2.24.0
    pip install -r requirements.txt


To run the tests in this project, run the following:

.. code-block:: bash

    py.test


If the GMT dependency is a git checkout (which is the default), then you may need to run the following command to update
the GMT dependency:

.. code-block:: bash

    pip install -U --upgrade-strategy eager -r requirements.txt


Matrix of Examples to Create
----------------------------

+-----------+---------------------+----------------+-----------+---------------+------------------------------------+-------------+
| ID        | Number of Buildings | Building Loads | ETS Model | Network Model | District Plant                     | Status      |
+-----------+---------------------+----------------+-----------+---------------+------------------------------------+-------------+
| 4GDHC - 1 | 8                   | TEASER         | N/A       | N/A           | Infinite Heating and Cooling       | Complete    |
+-----------+---------------------+----------------+-----------+---------------+------------------------------------+-------------+
| 4GDHC - 2 | 2                   | Spawn          | N/A       | N/A           | Infinite Heating and Cooling       | Complete    |
+-----------+---------------------+----------------+-----------+---------------+------------------------------------+-------------+
| 4GDHC - 3 | 8                   | TEASER         | Indirect  | None          | Infinite Heating and Cooling       | In-progress |
+-----------+---------------------+----------------+-----------+---------------+------------------------------------+-------------+
| 4GDHC - 4 | 2                   | Spawn          | Indirect  | None          | Infinite Heating and Cooling       | In-progress |
+-----------+---------------------+----------------+-----------+---------------+------------------------------------+-------------+
| 4GDHC - 5 | TBD                 | Time Series    | Indirect  | 4-Pipe        | Chiller, Cooling Tower, and Boiler | -           |
+-----------+---------------------+----------------+-----------+---------------+------------------------------------+-------------+
| 4GDHC - 6 | 8                   | Mix            | Indirect  | 4-Pipe        | Chiller, Cooling Tower, and Boiler | -           |
+-----------+---------------------+----------------+-----------+---------------+------------------------------------+-------------+


Todos
-----

* handle weather!


.. _GeoJSON to Modelica Translator: https://github.com/urbanopt/geojson-modelica-translator
.. _Modelica Buildings Library: https://github.com/lbl-srg/modelica-buildings
.. _GMT readme: https://github.com/urbanopt/geojson-modelica-translator#getting-started
