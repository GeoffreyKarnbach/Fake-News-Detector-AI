# Fakenews - Detector

In this project, @obrhubr and I tried to identify fake news. 

Before being able to use the detector, you will need to train the model. To do so:
- Create an empty "models" folder in the root directory.
- Run the "train()" command in main.py.


To try it out yourself, run main.py (You will have to install some libraries, the complete list is in dependencies.txt). You will be able, once you have run the file to enter an article URL (we recommend you to use an english article, as the model will be trained with a dataset of articles in english). Once you have entered the URL:

- The program will automatically try to extract the article from the URL (Most of the time, there will still be some aditionnal information after the actual article in the file. You can always modify the input file "sample_input.txt" and change the execution mode by inputing "0" at the beginning.
- Then, with some criterias we found out during our analysis (to see it, you can check out the jupyter notebook "analysis.ipynb". The criterias used to return a base coefficient are the amount of "!", the total length of the article and the amount of names given.
- After that, a tokenizer is used to output a coefficient (1 = fake news, 0 = non fake news). For that we used tensorflow.
- Finally, the base coefficient is combined with the tokenizer, to have a combination between formal criterias and specific words (tokenizer) to decide, wether this is a fake news article or not. 

As you can imagine, those two elements are not enough to detect for sure wether this is fake news or not. It can be outplayed simply by selecting certain words and avoiding the alarm criterias. We may add a keyword extraction to do a google search to be able to search for similar sources to confirm the article. Nevertheless, for now we had about 90% sucess on the test data set with only the tokenizer. 

To conclude, the detector doesn't work very well, we tried it out on articles from the New York Times and some Fake News Websites, in 7 out of 10 cases the result were correct, but we only tried it 10 times so there is no guarantee it will work fine everywhere.
