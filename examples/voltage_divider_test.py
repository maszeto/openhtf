import openhtf as htf

# Import this output mechanism as it's the specific one we want to use.
from openhtf.output.callbacks import json_factory

from openhtf.plugs import user_input
"""Using exampples directory as a playground. Plugs should be moved to openhtf.plugs if required
   to be in path and available for all users."""
from plugE36313A import plugE36313A
from plug34461A import plug34461A

@htf.plug(powerSupply=plugE36313A)
@htf.plug(dmm=plug34461A)  # Digital Multimeter
@htf.measures(htf.Measurement('voltage').with_units('V'),
              htf.Measurement('resistance').with_units('ohm'))
def test_vdivider(test, powerSupply, dmm):
    powerSupply.set_voltage(1, 2)

    test.logger.info('Running test')

    current_voltage = powerSupply.read_voltage(1)
    resistance = dmm.read_resistance()

    test.measurements['voltage'] = current_voltage
    test.measurements['resistance'] = resistance

    test.logger.info(current_voltage)

if __name__ == '__main__':
  # We instantiate our OpenHTF test with the phases we want to run as args.
  # Multiple phases would be passed as additional args, and additional
  # keyword arguments may be passed as well.  See other examples for more
  # complex uses.
  test = htf.Test(test_vdivider)

  # In order to view the result of the test, we have to output it somewhere,
  # and a local JSON file is a convenient way to do this.  Custom output
  # mechanisms can be implemented, but for now we'll just keep it simple.
  # This will always output to the same ./voltage_divider.json file, formatted
  # slightly for human readability.
  test.add_output_callbacks(
      json_factory.OutputToJSON('./{dut_id}.voltage_divider.json', indent=2))


  test.execute(test_start=user_input.prompt_for_test_start())