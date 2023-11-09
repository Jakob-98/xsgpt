# XSGPT

GPT CLI with persistence in 10 lines of code.
GPT RAG pattern with wikipedia in ~30 lines of code.

This Python package is a result of a code golfing exercise: to accomplish a task with the fewest characters or lines possible.

## Usage

```bash
PS C:\Projects\Personal\xsgpt> xsgpt
You: Hello! My name is jakob
AI: Hello, Jakob! How can I assist you today?
You: exit
PS C:\Projects\Personal\xsgpt> xsgpt
You: What is my name?
AI: Your name is Jakob.
```


RAG-pattern with wikipedia:
```bash
PS C:\Projects\Personal\xsgpt> xsgpt-wiki
You: hello                      
AI: Hello! How can I assist you today?
You: wikipedia search for Delft, the Netherlands
AI: Delft is a city and municipality in the province of South Holland, Netherlands. It is located between Rotterdam, to the southeast, and The Hague, to the northwest. Famous for its historic connections with the House of Orange-Nassau, Delft is a popular tourist destination in the Netherlands. It's also renowned for its blue pottery, or Delftware, and as the home to the painter Jan Vermeer.

Delft played a significant role in the Dutch Golden Age and is considered to be the birthplace of microbiology, thanks to the contributions of Antonie van Leeuwenhoek and Martinus Beijerinck. Moreover, it is the home of the Delft University of Technology (TU Delft).

Historically, Delft came into being beside a canal, the 'Delf', which comes from the word delven, meaning to delve or dig, and this is how it got its name. It developed into a city, from being a rural village in early Middle Ages. In 1246, Count Willem II granted Delft its city charter.       

Delft has a number of monumental buildings and canals, with bridges that connect their banks. It also has city parks, a botanical garden, and a recreational area called the "Delftse Hout," with bike, horse-riding footpaths, a lake, and other amenities.

For more details, you can visit the [Wikipedia page](https://en.wikipedia.org/wiki/Delft).
You: exit
```

## Installation

build and install:
`python setup.py bdist_wheel`
 and:
`pip install ./dist/xsgpt-{VERSION}-py3-none-any.whl`

To install using pip:

Currently unsupported, if this gets some traction, I'll add it to pypi.
<!--
```bash
pip install xsgpt -->
