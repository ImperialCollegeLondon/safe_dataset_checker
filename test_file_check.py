import sys
from safe_dataset_checker import *


loc_json = 'SAFE_locations.json'
gbif_db = 'backbone-current-simple.sqlite'

#
# check_file('Test_format_good.xlsx', locations_json=loc_json, gbif_database=gbif_db)
# sys.stderr.flush()
# sys.stdout.write('#\n# Checking file remotely and silently\n#\n')
# check_file('Test_format_good.xlsx', locations_json=loc_json, verbose=False)
#
# check_file('Test_format_bad.xlsx', locations_json=loc_json, gbif_database=gbif_db)
# sys.stderr.flush()
# sys.stdout.write('#\n# Checking file remotely and silently\n#\n')
# check_file('Test_format_bad.xlsx', locations_json=loc_json, verbose=False)


# part by part
ds = Dataset('Test_format_good.xlsx', gbif_database=gbif_db)
ds.load_summary()
ds.load_locations(locations_json=loc_json)
ds.load_taxa()
ds.load_data_worksheet(ds.dataworksheet_summaries[0])
ds.load_data_worksheet(ds.dataworksheet_summaries[1])
ds.final_checks()


ds = Dataset('Test_format_bad.xlsx', gbif_database=gbif_db)
ds.load_summary()
ds.load_locations(locations_json=loc_json)
ds.load_taxa()

