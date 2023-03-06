# This is a sample u2py Subroutine call Python script
import u2py
import logging

#  Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#  Select statement assumes there is a UniVerse file named CUSTOMER
cmd = u2py.Command('SELECT CUSTOMER WITH FIRST.NAME = "Keith"')

logger.info("Selecting CUSTOMER records.")
#  Execute the UniVerse command
cmd.run()

#  Create UV Select List 0
uv_record_list = u2py.List(0)

#  Read the UV record list
uv_read_list = uv_record_list.readlist()

#  Convert the UV List to a Python List
order_id_list = uv_read_list.to_list()

#  Count the number of IDs in the list
order_id_list_count = len(order_id_list)

#  Log the number of records selected
logger.info(f"{order_id_list_count} records selected.")

#  Print each Record ID
for record_id in order_id_list:
    print(record_id)

