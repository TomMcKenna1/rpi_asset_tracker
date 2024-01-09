import logging

from waveshare_epd import epd3in52

from asset_tracker import ImageDrawer
from asset_tracker.assets import GSPC, BTC

logging.basicConfig(level=logging.DEBUG)

logging.info("Initialising display...")
epd = epd3in52.EPD()
epd.init()
epd.display_NUM(epd.WHITE)
epd.lut_GC()
epd.refresh()

epd.send_command(0x50)
epd.send_data(0x17)
logging.info("Display initialised.")

logging.info("Gathering latest data...")
asset = BTC()
logging.info("Data gathered.")
logging.info("Drawing image...")
image_drawer = ImageDrawer(360, 240, asset)
latest_image = image_drawer.get_image(flipped=True)
logging.info("Image completed.")
logging.info("Sending to display...")
epd.display(epd.getbuffer(latest_image))
epd.lut_GC()
epd.refresh()
logging.info("Finished, sleeping the display.")
epd.sleep()