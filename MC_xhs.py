import sys
import os
sys.path.append(os.path.abspath("mediacrawler"))  # Add MediaCrawler to Python path
from main import main  # Import MediaCrawler’s main function

def scrape_xhs_stocks():
    args = [
        "--platform", "xhs",
        "--lt", "qrcode",
        "--type", "search",
        "--save_data_option", "csv"  # Or "sqlite", "json", etc.
    ]
    main(args)  # Run MediaCrawler
    print("Scraping #美股 complete!")

if __name__ == "__main__":
    scrape_xhs_stocks()