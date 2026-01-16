# fair2-climate

```shell
git clone --single-branch --branch package git@github.com:e-marshall/fair2-climate.git
#eventually:
#git clone git@github.com:fact-sealevel/fair2-climate.git

# Make dir for input data
mkdir -p ./data/input

# Download input data
# NOTE: Data using during dev isn't this because this doesn't include radiative forcing rcmip file
curl -sL https://zenodo.org/records/11506798/files/fair2_climate_project_data.tgz | tar -xvz 

# Make dir for output data 
mkdir -p ./data/output
```