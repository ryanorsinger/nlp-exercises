# Natural Language Processing

## Overview
- Formal languages are languages with formulaic grammar and syntax rules. Examples of formal languages include mathematical notation, Python, SQL, command line interface, regular expressions, and any programming language.
- Natural language are any spoken or written language that people use to communicate with one another. Natural languages are natural; they have nuance, dialects, broken syntax rules that are commonly followed, colloquialisms, idioms, and slang.
- NLP is the practice of using a formal language (like Python) to extract and identify meanin   g and sentiment from datasets composed of natural languages. 

## Methods
- Text Classification
    - Supervised learning where the set of all classes are already known/defined in advanced
- Topic Modeling
    - Unsupervised, like clustering, so the set of possible topics is unknown. The topics are definited as part of generating the topic models.

## Concepts     
- Building a corpus == collecting your 
- Normalizing text
    - make text lowercase
    - remove accents, special characters, punctuation
    - stem or lemmatize words
- Tokenization and Prep
    - Tokenize:  
    - n-grams:
    - Remove stopwords (the, and, a, an, etc...)
- POS Tagging & Chunking
    - Part of Speech Tagging
    - Chunking
- Vectorization
    - Treat each sentence as a separate document.
    - Make a list of all words from all documents.
    - Create vectors. Vectors convert text that can be used by the machine learning algorithm.
    - Example:
        ```python
        # Input:
        "It was the best of times"
        "It was the worst of times"
        "It was the age of wisdom"
        "It was the age of foolishness"
        # Output:

        Dictionary = [‘It’, ‘was’, ‘the’, ‘best’, ‘of’, ‘times’, ‘worst’, ‘age’, ‘wisdom’, ‘foolishness’]
        it_was_the_best_of_times = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0]
        it_was_the_worst_of_times = [1, 1, 1, 0, 1, 1, 1, 0, 0, 0]
        it_was_the_age_of_wisdom = [1, 1, 1, 0, 1, 0, 0, 1, 1, 0]
        it_was_the_age_of_foolishness = [1, 1, 1, 0, 1, 0, 0, 1, 0, 1]
        ```

## Features
- Bag of words
- Normalized Count Occurrence
- TF-IDF (Term Frequency - Inverse Document Frequency)
- Word Embedding
    - Representation of document vocabulary.
    - Word embeddings are vector representations of a particular word.
    - Word2Vec is one of the most popular techniques to learn word embeddings using a shallow neural network. It can be obtained using two methods (both involving neural networks) (1) Skip Gram and (2) Common Bag Of Words (CBOW).

## Vocabulary
Entities: Identify the type of entity extracted such as a person, place or organization using NamedEntity
Stemming: Reduce words to their root or stem. Running, runs, and runned, become "run".
Lemmatization: Return the base or dictionary form of a word, which is the lemma. For example 'better' becomes 'good' and 'walking' becomes 'walk'. Lemmatization trys to use context to choose the lemma (truncated form), where stemming just chops down to the root form of the word.
Tokenization: Breaking up text into linguistic units such as words or n-grams
Corpus: Set of documents, datasets, sample
Document: A single observation, like the body of an email