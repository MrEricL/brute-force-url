# brute-force-url
## Usage
Basic python code to iterate through a series of URLs to download PDF/image.
This is for when the url for some file has some numbers attached that may be hard to figure out.
For example:   
  >url.com/file1_4432432.pdf  
  >url.com/file2_<???>.pdf
  
This program will loop through testing numbers for <???> and download it in the current directory.

## Examples
**Disclaimer**: This may not be allowed.
Often times pages or pictures of a future release will be on a website, just obfuscated. You can use this to force download from a range of URLs.

## Running
Simply edit the run() function to include the url and the appropriate range.  
Then run ```python brute_force_url.py```
