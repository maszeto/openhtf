import openhtf as htf
from openhtf.util import conf
# Import this output mechanism as it's the specific one we want to use.
from openhtf.output.callbacks import json_factory
from openhtf.output.servers import station_server
from openhtf.output.web_gui import web_launcher
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
  conf.load(station_server_port='4444')
  with station_server.StationServer() as server:
    web_launcher.launch('http://localhost:4444')
    for i in range(5):
      test = htf.Test(test_vdivider)
      test.add_output_callbacks(server.publish_final_state)
      test.add_output_callbacks(
          json_factory.OutputToJSON('./{dut_id}.voltage_divider.json', indent=2))

      test.execute(test_start=user_input.prompt_for_test_start())