import time
import datetime

from schedule import repeat, every, run_pending
from ingestors import TradesIngestor

from ingestors import DaySummaryIngestor
from writes import DataWriter

if __name__ == "__main__":
    #instanciando o objeto
    day_summary_ingestor = DaySummaryIngestor(
        writer=DataWriter, 
        coins=["BTC", "ETH", "LTC"], 
        default_start_date=datetime.date(2021, 6, 1)
    )

    @repeat(every(1).seconds)
    def job():
        day_summary_ingestor.ingest() 

    while True:
        run_pending()
        time.sleep(0.5)


