# Import required libraries for handling data
import pandas as pd
import json
from datetime import datetime

# Set the specific file paths
input_csv = '/Users/gregoryd.goyins/Downloads/panel profits ii.csv'
output_json = '/Users/gregoryd.goyins/Downloads/processed_comics.json'

# Define our processing function with detailed error handling
def process_comics_csv(filename):
    try:
        # Read the CSV file, letting pandas handle any encoding issues
        df = pd.read_csv(filename, encoding='utf-8')
        print(f"Successfully loaded {len(df)} comic records")
        
        # Process the data as before, but with added error checking
        processed_comics = []
        
        for index, row in df.iterrows():
            try:
                comic_entry = {
                    'identification': {
                        'coreComicId': str(row['Core ComicID']),
                        'coreSeriesId': str(row['Core SeriesID']),
                        'issue': str(row['Issue'])
                    },
                    'dates': {
                        'coverDate': row['Cover Date'] if pd.notna(row['Cover Date']) else None,
                        'releaseDate': row['Release Date'] if pd.notna(row['Release Date']) else None,
                        'addedDate': row['Added Date'] if pd.notna(row['Added Date']) else None
                    },
                    'market': {
                        'value': float(row['Value']) if pd.notna(row['Value']) else None,
                        'covrPriceValue': float(row['CovrPrice Value']) if pd.notna(row['CovrPrice Value']) else None,
                        'key': {
                            'isKey': row['Key'] == 'Yes',
                            'category': row['Key Category'] if pd.notna(row['Key Category']) else None,
                            'reason': row['Key Reason'] if pd.notna(row['Key Reason']) else None
                        }
                    },
                    'content': {
                        'characters': row['Characters'].split('|') if pd.notna(row['Characters']) else [],
                        'storyArc': row['Story Arc'] if pd.notna(row['Story Arc']) else None,
                        'crossover': row['Crossover'] if pd.notna(row['Crossover']) else None
                    }
                }
                processed_comics.append(comic_entry)
                
                if index % 100 == 0:  # Progress indicator
                    print(f"Processed {index} comics...")
                    
            except Exception as e:
                print(f"Error processing comic at index {index}: {str(e)}")
                continue
                
        return processed_comics
        
    except Exception as e:
        print(f"Error reading CSV file: {str(e)}")
        return None

# Save the processed data with error handling
def save_processed_data(processed_comics, output_filename):
    try:
        with open(output_filename, 'w', encoding='utf-8') as f:
            json.dump(processed_comics, f, indent=2, ensure_ascii=False)
        print(f"Successfully saved processed data to {output_filename}")
    except Exception as e:
        print(f"Error saving processed data: {str(e)}")

# Execute the processing
if __name__ == "__main__":
    print("Starting comic data processing...")
    comics_data = process_comics_csv(input_csv)
    if comics_data:
        save_processed_data(comics_data, output_json)
    print("Processing complete!")
