import logging

from ruxit.api.base_plugin import RemoteBasePlugin

from spacex_api import get_ships

logger = logging.getLogger(__name__)


class SpaceXPlugin(RemoteBasePlugin):
    def query(self, **kwargs) -> None:

        config = kwargs.get("config")

        ships = get_ships(config.get("url"))
        logger.info(f"Encontré {len(ships)} navios")

        group = self.topology_builder.create_group("Ships", "Ships")

        for ship in ships:
            logger.info(f"Procesando navio {ship['ship_name']}")
            device = group.create_device(ship["ship_id"], ship["ship_name"])

            # Absolute metric - Value AS IS
            device.absolute("fuel", ship["fuel"])

            for engine in ship["thrust"]:

                # Dimensions (1 Custom Metric per dimension)
                device.absolute("thrust", engine["power"], dimensions={"Motor": engine["engine"]})

            # Topology data
            device.add_endpoint(ship["ship_ip"])

            # Properties
            device.report_property("Puerto", ship.get("home_port", "Desconocido"))
            device.report_property("Activo", str(ship.get("active", True)))
            device.report_property("Construcción", str(ship.get("year_built", "Desconocido")))

            # State Timeseries
            device.state_metric("weather", ship["weather"])
