# uznltk

https://pypi.org/project/uznltk <br>
https://github.com/UlugbekSalaev/uznltk

uznltk is Uzbek Natural Language ToolKit  
It is created as a python library and uploaded to [PyPI](https://pypi.org/). It is simply easy to use in your python project or other programming language projects via the API. 

## About project
The Natural Language Toolkit (NLTK) is a Python package for natural language processing.
## Quick links

- [Github](https://github.com/UlugbekSalaev/uznltk)
- [PyPI](https://pypi.org/project/uznltk/)
- [Web-UI](https://nlp.urdu.uz/?menu=uznltk)

## Demo

You can use [web interface](http://nlp.urdu.uz/?menu=uznltk).

## Features

- Corpus 
- Morphological annotated dataset
- Help function

# uznltk

 Natural Language Toolkit for Uzbek O‘zbek tili uchun NLP kutubxonasi

## Function

- Tokenization into words
- Sentence segmentation
- Stop-word identification
- Normalization of apostrophes in text
- Extraction of words with punctuation marks

## Installatoin

```bash
pip install uznltk

## Usage

Three options to run uznltk:

- pip
- API 
- Web interface

### pip installation

To install uznltk, simply run:

```code
pip install uznltk
```

After installation, use in python like following:
```yml
# import the library
from uznltk import Tagger
# create an object 
tagger = Tagger()
# call tagging method
tagger.pos_tag('Bizlar bugun maktabga bormoqchimiz.')
# output
[('Bizlar','NOUN'),('bugun', 'NOUN'), ('maktabga', 'NOUN'), ('bormoqchimiz', 'VERB'), ('.', 'PUNC')]
```

### API
API configurations: 
 - Method: `GET`
 - Response type: `string`
 - URL: `https://nlp.urdu.uz:8080/uznltk/pos_tag`
   - Parameters: `text:string`
 - Sample Request: `https://nlp.urdu.uz:8080/uznltk/pos_tag?text=Ular%20maktabga%20borayaptilar.`
 - Sample output: `[("Ular","NOUN"),("maktabga",""),("borayaptilar",""),(".","PUNC")]`

### Web-UI

The web interface created to use easily the library:
You can use web interface [here](http://nlp.urdu.uz/?page=uznltk).

![Demo image](src/uznltk/web-interface-ui.png)

### POS tag list
Tagger using following options as POS tag:<br>
    `NOUN`  Noun {Ot}<br>
    `VERB`  Verb {Fe'l}<br>
    `ADJ `  Adjective {Sifat}<br>
    `NUM `  Numeric {Son}<br>
    `ADV `  Adverb {Ravish}<br>
    `PRN `  Pronoun {Olmosh}<br>
    `CNJ `  Conjunction {Bog'lovchi}<br>
    `ADP `  Adposition {Ko'makchi}<br>
    `PRT `  Particle {Yuklama}<br>
    `INTJ`  Interjection {Undov}<br>
    `MOD `  Modal {Modal}<br>
    `IMIT`  Imitation {Taqlid}<br>
    `AUX `  Auxiliary verb {Yordamchi fe'l}<br>
    `PPN `  Proper noun {Atoqli ot}<br>
    `PUNC`  Punctuation {Tinish belgi}<br>
    `SYM `  Symbol {Belgi}<br>

### Result Explaining

The method ```pos_tag``` returns list, that an item of the list contain tuples for each token of the text with following format: ```(token, pos)```, for POS tag list, see <i>POS Tag List</i> section on above.  
#### Result from `tagger` method
`[('Bizlar','NOUN'),('bugun', 'NOUN'), ('maktabga', 'NOUN'), ('bormoqchimiz', 'VERB'), ('.', 'PUNC')]`

## Documentation

See [here](https://github.com/UlugbekSalaev/uznltk).

## Citation

```tex
@article{10.1063/5.0241461,
    author = {Salaev, Ulugbek},
    title = {UzMorphAnalyser: A morphological analysis model for the Uzbek language using inflectional endings},
    journal = {AIP Conference Proceedings},
    volume = {3244},
    number = {1},
    pages = {030058},
    year = {2024},
    month = {11},
    abstract = {As Uzbek language is agglutinative, has many morphological features which words formed by combining root and affixes. Affixes play an important role in the morphological analysis of words, by adding additional meanings and grammatical functions to words. Inflectional endings are utilized to express various morphological features within the language. This feature introduces numerous possibilities for word endings, thereby significantly expanding the word vocabulary and exacerbating issues related to data sparsity in statistical models. This paper present modeling of the morphological analysis of Uzbek words, including stemming, lemmatizing, and the extraction of morphological information while considering morpho-phonetic exceptions. Main steps of the model involve developing a complete set of word-ending with assigned morphological information, and additional datasets for morphological analysis. The proposed model was evaluated using a curated test set comprising 5.3K words. Through manual verification of stemming, lemmatizing, and morphological feature corrections carried out by linguistic specialists, it obtained a word-level accuracy of over 91\%. The developed tool based on the proposed model is available as a web-based application and an open-source Python library.},
    issn = {0094-243X},
    doi = {10.1063/5.0241461},
    url = {https://doi.org/10.1063/5.0241461},
    eprint = {https://pubs.aip.org/aip/acp/article-pdf/doi/10.1063/5.0241461/20272108/030058\_1\_5.0241461.pdf},
}
```

## Contact

For help and feedback, please feel free to contact [the author](https://github.com/UlugbekSalaev).