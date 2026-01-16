import click 
from fair2_climate.fair2_climate_project import (
    fair2_project_climate
)
import fair 

@click.command()
@click.option('--pipeline-id',
              type=str,
              required=True,
              help='Unique identifier for this instance of the module')
@click.option('--rcmip-concentration-file',
              type=str,
              #default='./rcmip/rcmip-concentrations-annual-means-v5-1-0.csv',
              show_default=True,
              help='Full path to concentration file')
@click.option('--rcmip-emissions-file',
              type=str,
              #default='./rcmip/rcmip-emissions-annual-means-v5-1-0.csv',
              show_default=True,
              help='Full path to emissions file')
@click.option('--rcmip-forcing-file',
              type=str,
              #default='./rcmip/rcmip-radiative-forcing-annual-means-v5-1-0.csv',
              show_default=True,
              help='Full path to forcing file')
@click.option('--calibration-file',
              type=str,
              #default='./parameters/calibrated_constrained_parameters.csv',
              show_default=True,
              help='Full path to the climate calibration params file')
@click.option('--species-config-file',
              type=str,
              #default='./parameters/species_configs_properties_calibration1.2.0.csv',
              show_default=True,
              help='Full path to the species configuration file')
@click.option('--volcanic-erf',
              type=str,
              #default='./parameters/volcanic_ERF_1750-2101_timebounds.csv',
              show_default=True,
              help='Full path to the Volcanic ERF timebounds file')
@click.option('--solar-erf',
              type=str,
              #default='./parameters/solar_erf_timebounds.csv',
              show_default=True,
              help='Full path to the Solar ERF timebounds file')
@click.option('--scenario',
              type=str,
              default='ssp585',
              show_default=True,
              help='SSP Emissions scenario')
@click.option('--reference-year',
              type=int,
              default=1750,
              show_default=True,
              help='Reference Year')
@click.option('--nsamps',
              type=int,
              default=500,
              show_default=True,
              help='Number of samples to create (uses replacement if nsamps > n parameters)')
@click.option('--seed',
              type=int,
              default=1234,
              show_default=True,
              help='Seed value for random number generator')
@click.option('--cyear-start',
              type=int,
              default=1850,
              show_default=True,
              help='Start year of temporal range for centering')
@click.option('--cyear-end',
              type=int,
              default=1900,
              show_default=True,
              help='End year of temporal range for centering')
@click.option('--smooth-win',
              type=int,
              default=19,
              show_default=True,
              help='Number of years to use as a smoothing window')
@click.option('--pyear-start',
              type=int,
              default=2020,
              show_default=True,
              help='Projection year start')
@click.option('--pyear-end',
              type=int,
              default=2100,
              show_default=True,
              help='Projection year end')
@click.option('--output-climate-file',
              type=str,
              required=True,
              help="Full path for climate output .nc written my module.")
@click.option('--output-gsat-file',
              type=str,
              required=True,
                help="Full path for GSAT output .nc written my module.")
@click.option('--output-oceantemp-file',
              type=str,
              required=True,
                help="Full path for Ocean Temp output .nc written my module.")
@click.option('--output-ohc-file',
              type=str,
              required=True,
                help="Full path for ocean heat content output .nc written my module.")

def main(pipeline_id,
         rcmip_emissions_file,
         rcmip_concentration_file,
         rcmip_forcing_file,
         calibration_file,
         species_config_file,
         volcanic_erf,
         solar_erf,
         scenario,
         reference_year,
         nsamps,
         seed,
         cyear_start,
         cyear_end,
         smooth_win,
         pyear_start,
         pyear_end,
         output_climate_file,
         output_gsat_file,
         output_oceantemp_file,
         output_ohc_file):
    """ Command line interface for FAIR2 climate model module
    """
    click.echo("Hello from fair2-climate!")
    message = f"fair version: {fair.__version__}"
    click.echo(message)
    fair2_project_climate(pipeline_id=pipeline_id,
                                rcmip_emissions_file=rcmip_emissions_file,
                                rcmip_concentration_file=rcmip_concentration_file,
                                rcmip_forcing_file=rcmip_forcing_file,
                                calibration_file=calibration_file,
                                species_config_file=species_config_file,
                                volcanic_erf=volcanic_erf,
                                solar_erf=solar_erf,
                                scenario=scenario,
                                reference_year=reference_year,
                                nsamps=nsamps,
                                seed=seed,
                                cyear_start=cyear_start,
                                cyear_end=cyear_end,
                                smooth_win=smooth_win,
                                pyear_start=pyear_start,
                                pyear_end=pyear_end,
                                output_climate_file=output_climate_file,
                                output_gsat_file=output_gsat_file,
                                output_oceantemp_file=output_oceantemp_file,
                                output_ohc_file=output_ohc_file)
