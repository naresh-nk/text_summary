# Summarize Text
Simple Python program to parse and summarize a text from web pages. This is useful to extract valuable information from any article.

## Getting Started

Import the text_summary into you existing program or run as stand alone script.

```
	article_url = 'https://www.nytimes.com/2019/06/02/opinion/vaccines-peter-hotez.html'
	#tag = "#mw-content-text > div > p"
	tag = '#story'
	text = get_article_text(article_url, tag)
	print('\nComplete Text: \n',text)
	print('\n', 'Summary Text: ', '\n')

	top_sentences = get_top_sentences(4, text)
	for s in top_sentences:
		print(s)
```

### Prerequisites Installation

It's tested on Python 3.7.2 version. install required packages from given requirements.txt file.
```
pip install -r requirements.txt

```

## Running the tests

```
python text_summary.py

```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* [PluralSight](https://www.pluralsight.com)