import shoecontracts.downloader
import shoecontracts.model

def update(season,should_update=True):
    shoe_contracts = shoecontracts.downloader.fetch_shoe_contracts()

    if should_update:
        shoecontracts.model.create_tables()
        shoecontracts.model.update(shoecontracts.model.ShoeContracts, shoe_contracts)

