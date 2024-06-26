# SIMRE

*SimRE is a Python-based tool for automatically identifying requirements' similarity in SPL projects.

## Parameters description

* You need to enter seven parameters. These parameters are the following:
  * nameNewReq: name of the CSV file that contains the list of new requirements. 
  * nameFeatures: name of the XML or UVL file that contains the existing requirements. 
  * nameReqDescription: name of the JSON file that contains the requirements description. 
  * language: 'en' for English and 'es' for Spanish
  * listModels: array with the models. optional. The default model is 1. The models are the following:
      * 1:Model multilingual MiniLM-L12-v2
      * 2:Model multilingual distiluse-cased-v2
      * 3:Model multilingual mpnet-base-v2
      * 4:'Model word2vec
      * 5:'Model fastText 
  * threshold: optional. The default value is 0.7.
  * preprocess: optional. The values are: True to allow the pre-processing (default value), and False for without pre-processing

## Installation by pip

* Its necessary to have installed al least Python 3.8.10 and pip 23.1.2
* The tool can be used by installing the library or downloading the code.
* After download the library using pip, use the following code to download several pre-trained models and put them on caché.

```
from simre import init_models
init_models.main()

from simre import similarity
models = similarity.load_models()
```

* This process may take several minutes depending on the processor's capacity and memory. We recommend a RAM of at least of 16 GB.
* When the process finishes, you should confirm that a "fileserver" folder has been created and contains four files.

### Usage

* The method similarity_process perform the similarity process.

```
similarity.similarity_process(nameNewReq, nameFeatures, nameReqDescription, 'en',models) 
```

* In the examples folder are some files to make a test.

```
similarity.similarity_process('newRequirements.csv', 'featureModel.xml', 'descRequirements_en.json', 'en',models) 
```

* With all the parameters.

```
similarity.similarity_process('newRequirements.csv', 'featureModel.xml', 'descRequirements_en.json', 'en',models,[1,2,3],0.6,False) 
```

* The results will be provided in a CSV file ('Similarity List.csv'). 


## Installation by code

* Download the code 
* Install the required libraries. All necessary libraries are listed in the requirements.txt file. To install them, execute the following command `pip install -r ./requirements.txt`
* It is necessary to download several pre-trained models. This can be done automatically or manually. To download the models automatically, execute the following command: `python process.py init`. To download the models manually, follow these steps:

* a. Download the models of spacy for Spanish and English: `python -m spacy download es_core_news_sm` and `python -m spacy download en_core_web_sm`
* b. Download the models of fastText for Spanish and English: `cc.es.300.bin` and `cc.es.300.bin` from https://fasttext.cc/docs/en/crawl-vectors.html
* c. Download the word2vec-based models for Spanish and English: `SBW-vectors-300-min5.bin.gz` from https://crscardellino.github.io/SBWCE/  and `GoogleNews-vectors-negative300.bin.gz` from https://code.google.com/archive/p/word2vec/  
* d. At the same directory level as the src folder, create a new folder named fileserver. Place all the pre-trained models into this folder.

### Usage

* To execute the tool without optional parameters, use the following command: `python process.py nameNewReq nameFeatures nameReqDescription language`. Example:: `python process.py newRequirements.csv featureModel.xml descRequirements_en.json en`. 
* This is an example using all the parameters: `python process.py newRequirements.csv featureModel.xml descRequirements_en.json en 1,2,3,5 0.7 False`
* The results will be provided in a CSV file on the fileserver folder ('Similarity List.csv'). 
   
## Formats

*XML file:

```
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<featureModel chosenLayoutAlgorithm="4">
  <struct>
    <and mandatory="true" name="GEMA_SPL">      
      <and name="UserManagement">
        <or name="UM_Registration">
          <feature mandatory="true" name="UM_R_ByAdmin"/>
          <feature mandatory="true" name="UM_R_Anonymous"/>
        </or>              
      </and>      
    </and>
  </struct>
  <featureOrder userDefined="false"/>
</featureModel>
```

*UVL file: 

```
features
	UserManagement 
		optional
			UM_Registration 
				or
					UM_R_ByAdmin 
					UM_R_Anonymous
```

*JSON file:

```
{
  "UserManagement": { 
      "label": "User Management",
      "desc": "User Management" 
  },
  "UM_Registration": { 
      "label": "User Registration",
      "desc": "User Registration" 
  },
  
}
```
