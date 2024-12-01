import pandas as pd
import json
from datetime import datetime

def process_comics_csv(filename):
    # Read the CSV file
    df = pd.read_csv(filename)
    
    # Convert dates to standard format
    date_columns = ['Cover Date', 'Release Date', 'Added Date']
    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')
    
    # Create structured data for each comic
    processed_comics = []
    
    for _, row in df.iterrows():
        comic_entry = {
            'identification': {
                'coreComicId': row['Core ComicID'],
                'coreSeriesId': row['Core SeriesID'],
                'issue': row['Issue']
            },
            'dates': {
                'coverDate': row['Cover Date'].isoformat() if pd.notna(row['Cover Date']) else None,
                'releaseDate': row['Release Date'].isoformat() if pd.notna(row['Release Date']) else None,
                'addedDate': row['Added Date'].isoformat() if pd.notna(row['Added Date']) else None
            },
            'market': {
                'value': row['Value'],
                'covrPriceValue': row['CovrPrice Value'],
                'key': {
                    'isKey': row['Key'] == 'Yes',
                    'category': row['Key Category'],
                    'reason': row['Key Reason']
                }
            },
            'content': {
                'characters': row['Characters'].split('|') if pd.notna(row['Characters']) else [],
                'storyArc': row['Story Arc'],
                'crossover': row['Crossover']
            }
        }
        processed_comics.append(comic_entry)
    
    return processed_comics

# Save processed data to JSON file
def save_processed_data(processed_comics, output_filename):
    with open(output_filename, 'w') as f:
        json.dump(processed_comics, f, indent=2)

