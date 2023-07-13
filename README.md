### Windsor CLI [Google Drive Object Download]

The name sounds fancier that It really is.
This project is a small coding challenge that I did where the main purpose was to provide a CLI using Python, download a CSV file in memory and handle It to return only the selected header fields, informed using the flag `--fields field1,field2... as json.

I took the chance of refresh some concepts like decorators - that aren't used too frequently and some people like to request an example In some coding interviews`- and TDD - that I really like to do.

For run It, don't forget to update the id of the file on `./src/client_helpers/third_party_configs.py` In order to pull your file. Obviously this could be modified to be done dinamically, but how It was a coding challenge I put It like that.

To run just call `python windsor_cli --fields [your_fields,...]`

Well, that's It.
