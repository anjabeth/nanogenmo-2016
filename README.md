# Towers in the Land of Smiling Chimeras
## a procedurally generated novel for [nanogenmo 2016](https://github.com/NaNoGenMo/2016)

This is my entry for NaNoGenMo 2016 - a procedurally generated, progressively lipogrammatic novel. That's a lot of words. 

Procedurally generated = a computer wrote this (specifically, some Markov chains trained on a bunch of Project Gutenberg mystery and crime novels wrote this, hence the old-timey tone)

Progressively lipogrammatic = a lipogram is a text that does not contain a particular letter (e.g. "A bad facade" is a lipogram in all the letters that come after "f"). Lipograms are a fun thing to play around with, and several authors have taken it to the extreme, writing entire novels that don't contain a certain letter (see Georges Perec's [La Disparition] (https://en.wikipedia.org/wiki/A_Void), translated into English as A Void, a 300-page novel that doesn't use the letter "e"). I was inspired by Mark Dunn's [Ella Minnow Pea] (https://en.wikipedia.org/wiki/Ella_Minnow_Pea), which he describes as a "progressively lipogrammatic epistolary fable". Essentially, it's the story of an island where the letters that the residents are allowed to use decrease as the novel goes on. I wanted to see if I could do something similar, and the result was Towers in the Land of Smiling Chimeras.

How it works:
* Read in a whole bunch of Project Gutenberg texts and create a Markov model from them using markovify
* Generate the text of the novel, divided into chapters. Assign each chapter a list of banned characters. 
* For each chapter, find all words that contain those banned characters. 
* Take all those words and either
--* find a synonym for them
--* misspell them to get rid of the banned characters (hooray for words like "indoostrioosli")
--* redact them entirely

The end result is a novel that doesn't make much sense, but sure is fun to look through. I intend to do more work on the misspellings in particular (I'm a linguistics nerd and think that would be fun), as well as maybe playing with the presentation of it.

## Generate your own

If you want to generate your own novel, here's what you need to do:

A quick note about Gutenberg: it doesn't play very nice with Windows, but I fixed it like [this](http://stackoverflow.com/questions/33714698/installing-bsddb3-6-1-1-in-windows-filenotfounderror-db-include-db-h)

```
pip install gutenberg #utility for stripping and formatting Project Gutenberg texts
pip install markovify #awesome, easy-to-use Markov chains
pip install wordnik #synonym API
pip install PyDictionary #more synonyms!
```
You'll also need an account with [Wordnik](https://www.wordnik.com/signup) and an API key, which you can request easily [here](http://developer.wordnik.com/) once you create an account. They only send out the emails with the keys on Mondays, but you can find your API key anytime after you've requested it on your user settings page. 

Now you're all set! You can run the script with

```
python generate_novel.py
```

The current parameters are set to generate a 50,000 word novel for NaNoGenMo, which takes a while because of the API calls. If you're just playing around, you can change NUM_CHAPTERS and SENTENCES_PER_CHAPTER to something more reasonable - I found 10 and 5 to be good for dev purposes. 

