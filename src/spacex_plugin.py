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
            device.absolute("fuel", ship["fuel"])
