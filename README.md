# fair2-climate
Containerized application of the fair2 [module](https://github.com/radical-collaboration/facts/tree/development/modules/fair2) from FACTS v1. 

> [!CAUTION]
> This is a prototype. It is likely to change in breaking ways. It might delete all your data. Don't use it in production.

## Example

First, create a new directory, download the required input data and prepare for the run:

```shell
git clone --single-branch --branch package git@github.com:e-marshall/fair2-climate.git
#TODO eventually:
#git clone git@github.com:fact-sealevel/fair2-climate.git

# Make dir for input data
mkdir -p ./data/input

# Download input data
# NOTE TODO: Data using during dev isn't this because this doesn't include radiative forcing rcmip file
curl -sL https://zenodo.org/records/11506798/files/fair2_climate_project_data.tgz | tar -xvz 

# Make dir for output data 
mkdir -p ./data/output
```
Then, create a Docker image: 
(**TODO: don't need this once example can use container from container registry**)
```shell
docker build -t fair2-climate . 
```

Run the application in a conatiner based on the image:
(**TODO: fix once container image builds in CICD**)
```shell
docker run --rm \
-v ./data/input:/mnt/fair2_input_data:ro \
-v ./data/output:/mnt/fair2_output_data \
fair2-climate \
--pipeline-id my_pipeline_id \
--nsamps 50 \
--rcmip-emissions-file "/mnt/fair2_input_data/rcmip/rcmip-emissions-annual-means-v5-1-0.csv" \
--rcmip-concentration-file "/mnt/fair2_input_data/rcmip/rcmip-concentrations-annual-means-v5-1-0.csv" \
--rcmip-forcing-file "/mnt/fair2_input_data/rcmip/rcmip-radiative-forcing-annual-means-v5-1-0.csv" \
--calibration-file "/mnt/fair2_input_data/parameters/calibrated_constrained_parameters.csv" \
--species-config-file "/mnt/fair2_input_data/parameters/species_configs_properties_calibration1.2.0.csv" \
--volcanic-erf "/mnt/fair2_input_data/parameters/volcanic_ERF_1750-2101_timebounds.csv" \
--solar-erf "/mnt/fair2_input_data/parameters/solar_erf_timebounds.csv" \
--reference-year 1750 \
--seed 1234 \
--cyear-start 1850 \
--cyear-end 1900 \
--smooth-win 19 \
--pyear-start 2020 \
--pyear-end 2100 \
--output-climate-file /mnt/fair2_output_data/climate.nc \
--output-gsat-file /mnt/fair2_output_data/gsat.nc \
--output-oceantemp-file /mnt/fair2_output_data/ocean_temp.nc \
--output-ohc-file /mnt/fair2_output_data/ohc.nc
```
## Features

Several options and configurations are available when running the container:
```
Usage: fair2-climate [OPTIONS]

  Command line interface for FAIR2 climate model module

Options:
  --pipeline-id TEXT              Unique identifier for this instance of the
                                  module  [required]
  --rcmip-concentration-file TEXT
                                  Full path to concentration file
  --rcmip-emissions-file TEXT     Full path to emissions file
  --rcmip-forcing-file TEXT       Full path to forcing file
  --calibration-file TEXT         Full path to the climate calibration params
                                  file
  --species-config-file TEXT      Full path to the species configuration file
  --volcanic-erf TEXT             Full path to the Volcanic ERF timebounds
                                  file
  --solar-erf TEXT                Full path to the Solar ERF timebounds file
  --scenario TEXT                 SSP Emissions scenario  [default: ssp585]
  --reference-year INTEGER        Reference Year  [default: 1750]
  --nsamps INTEGER                Number of samples to create (uses
                                  replacement if nsamps > n parameters)
                                  [default: 500]
  --seed INTEGER                  Seed value for random number generator
                                  [default: 1234]
  --cyear-start INTEGER           Start year of temporal range for centering
                                  [default: 1850]
  --cyear-end INTEGER             End year of temporal range for centering
                                  [default: 1900]
  --smooth-win INTEGER            Number of years to use as a smoothing window
                                  [default: 19]
  --pyear-start INTEGER           Projection year start  [default: 2020]
  --pyear-end INTEGER             Projection year end  [default: 2100]
  --output-climate-file TEXT      Full path for climate output .nc written my
                                  module.  [required]
  --output-gsat-file TEXT         Full path for GSAT output .nc written my
                                  module.  [required]
  --output-oceantemp-file TEXT    Full path for Ocean Temp output .nc written
                                  my module.  [required]
  --output-ohc-file TEXT          Full path for ocean heat content output .nc
                                  written my module.  [required]
  --help                          Show this message and exit.
```

See this help documentation by running:
```shell
#(not yet)
docker run --rm ghcr.io/fact-sealevel/fair2-cliamte:latest --help
```

## Building the container locally

You can build the container with Docker by cloning the repository locally and then running

```shell
docker build -t fair2-climate:dev .
```

from the repository root.

## Support

Source code is available online at https://github.com/fact-sealevel/fair2-climate. This software is open source and available under the MIT license.

Please file issues in the issue tracker at https://github.com/fact-sealevel/fair2-climate/issues.
