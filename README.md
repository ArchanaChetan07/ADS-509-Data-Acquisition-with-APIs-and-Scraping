# ADS-509-Data-Acquisition-with-APIs-and-Scraping

# Lyrics Scraper Project

This project focuses on **web scraping song lyrics** for two selected artists from [AZLyrics.com](https://www.azlyrics.com/). The extracted lyrics data is organized and saved into CSV format for further Natural Language Processing (NLP) and text analysis tasks.

---

## Project Overview

- **Selected Artists**:  
  - Adele  
  - Eminem  

- **Songs Scraped**: 20 songs per artist

- **Main Objectives**:
  - Web scrape lyrics using `BeautifulSoup` and `urllib`.
  - Organize and store lyrics by artist, year, and decade.
  - Save all data into a structured CSV file for future analysis.
  - Handle missing data and page errors gracefully.

---

## Technologies Used

- Python 3.x  
- BeautifulSoup (for HTML Parsing)  
- Pandas (for data manipulation and CSV export)  
- urllib (for URL requests)  
- OS & Time Libraries (for file handling and delays)

---

##  Output

- **CSV File**:  
  `lyrics_dataset.csv` containing columns:  
  - Artist  
  - Song_Title  
  - Lyrics  
  - Album_Year  
  - Decade  

---

## Notes
- Respect AZLyrics' `robots.txt` and website scraping policies.
- Sleep intervals have been added to reduce server load.

