# brute-force-url
## Usage
Basic python code to iterate through a series of URLs to download PDF/image.
This is for when the url for some file has some numbers attached that may be hard to figure out.
For example:   
  >url.com/file1_4432432.pdf  
  >url.com/file2_<???>.pdf
  
This program will loop through testing numbers for <???> and download it in the current directory.

## Running
Simply edit the run() function to include the url and the appropriate range.  
Then run ```python brute_force_url.py```
