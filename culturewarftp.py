import streamlit as st

# Show title and description.
st.title("The Culture War for the Planet 🌎")
st.header('Comparative analysis of r/collapse, r/preppers, r/itcouldhappenhere, and r/climate', divider="blue")

# RESEARCH MOTIVATIONS
st.header("Research Motivations:")
st.subheader("What's going on on with r/Collapse?")

st.markdown("In our worsening climate catastrophe, I've noticed the growth of a particular doomerist subreddit - r/collapse - and, perhaps more notably, the spread of its doomer rhetoric to other, less-controversial climate related subreddits, like r/preppers, r/itcouldhappenhere, and r/climate.")

st.markdown("The r/Collapse subreddit is filled with people deriving a number of narratives about the eventual collapse of modern society. I'm aiming to see what these narratives *are*. finding through-lines and AI-classified* similarities between different authors' positions, and being able to map out the rhetorical 'state space' - with an eye out for any other information I can pick up.")
st.caption("\*_Aiming not to over-use high-compute power AI models for this, a pet project that's meant to be about saving the planet. See the **Climate-Conscious Compuatation** page for more._")

# RESEARCH QUESTION
st.header("Research Question")
st.subheader("Are there places online where you're more likely to fall down a climate doomer rabbit hole? _What makes the difference?_")
st.markdown("This question has all sorts of component parts, but answering it will require a working definition of 'doomer' vs. non-doomer online spaces: I've decided to track the subreddits' **abusive language**, and whether the comments/posts in a subreddit see the changing climate as more of a **risk** to themsleves and others, or an **opportunity** to make money or secure power over others.")
st.markdown("And of course, I'm comparatively analyzing the four subreddits to determine the relatively 'most/least' abusive ones, but I'll also be tracking any change in rhetoric related to climate over time (dataset collects Tweets and Reddit posts from 2018).")

# DATA SOURCES + COLLECTION
st.header("Data Sources + Data Collection")
st.subheader("Where did I get this information, _and why does it help answer our questions?_")

st.markdown("1. **The Reddit Comments**")
st.markdown("""I pulled 16,000 of the top comments and text posts of all time from r/collapse, r/preppers, r/itcouldhappenhere and r/climate, using [Praw](https://github.com/praw-dev/praw).  
_Comments were mostly from the years after 2018, but the earliest post is from 2016. This inadvertently captures 3 presidential tenures (Trump, Biden, Trump) - the early results make me think this is relevant!_""")


st.markdown("In order to classify the text I'd pulled as abusive language, or to determine the attitude toward climate change (opportunity vs. risk) in the text, I relied on machine learning models that had been pre-trained on other datasets...")

st.markdown("2. [ClimateBERT Climate Change Sentiment Dataset](https://huggingface.co/datasets/climatebert/climate_sentiment)")
st.markdown("_This dataset was used to train the [ClimateBERT](https://huggingface.co/climatebert/distilroberta-base-climate-sentiment) classification model for climate opportunity and risk._")

st.markdown("3. [IndicAbusive Datasets](https://github.com/hate-alert/IndicAbusive/tree/main/Dataset)")
st.markdown("_These were used to train various hate speech models, including the [English-Abusive-MuRIL](https://huggingface.co/Hate-speech-CNERG/english-abusive-MuRIL?text=...+%40THErealDVORAK+And+man-made+global+warming+will+never+warm+the+moon%2C+sun%2C+and+stars.+End+times+are+controlled+by+God+-+not+by+carbon) classification model I used in my research._")

# ANALYSIS HEADER
st.header("Analysis - Semantic Similarity, Topic Modeling (Ongoing Work)")

st.markdown("I've gotten a preliminary vizualization of the topics discussed by Redditors in the various climate-related subreddits. See this link for an interactive graph:")

left, middle, right = st.columns([0.15, 0.7, 0.15])
with middle:
  st.link_button(label="Redditors' takes on the climate catastrophe", url="https://jaidasgithubaccount.github.io/data_visualizations/", icon='📊', use_container_width=True)

st.markdown("""Notable comment topics and keywords found in subreddit comments:   
- :blue[**Migration and Refugee Status**] **(Topic 12):** keywords 'Haiti', 'people', 'country'   
- :orange[**The COVID-19 Pandemic**] **(Topic 6):** keywords 'covid', 'insurance', 'virus'  
- :green[**Conservative Politics**] **(Topic 1):** keywords 'Trump', 'people', 'just'""")

st.markdown("But if you want to learn more about what you're looking at in the graph at the link above...")

# TOPIC MODELING - BERTOPIC VIZ
st.subheader("Topic Modeling - setting up BERTopic")
st.markdown("""I used [BERTopic](https://github.com/MaartenGr/BERTopic), a Python package that takes sets of documents, mines them for their topics, and analyzes an entire corpus of the documents according to those (zero-shot-) classified topics.
""")
st.markdown("""I first had to clean my dataset (removing stopwords, cleaning up uniform formatting on some subreddits' comments, etc), and then used BERTopic to determine the 'state space' - the kinds of things that people in these climate subreddits are talking about today.
""")

st.markdown("""The original dataset had 15807 topics; using BERTopic's reduce_topics() method, I forced the model to combine them into 20 groups. I then used a [SciKit-Learn](https://github.com/scikit-learn/scikit-learn) function to get text embeddings with English stop words removed, and re-ran the topic model with those vectorized topics. The final topic model, saved for use throughout the rest of the project, leverages these two modifications.
""")

# COMPARATIVE ANALYSIS - TEXT CLASSIFIERS
st.subheader("Comparative Analysis - setting up the text classifiers")
st.markdown("""There are two kinds of comparative analysis:
- Analyzing BERTopic topics by subreddit, with the BERTopic 'vector database' built by that Python module:
  - this will help determine whether certain topics are unique to a given climate-subreddit. (Unlikely that any of the top 10 topics in the vizualization linked above are uniqe to one subreddit, but others might be!)
- Other data analysis, performed by augmenting a master data structure (pandas DataFrame, or .csv file) with algorithmically-derived classification, like:
	- whether the text contains abusive language
	- whether the text treats the climate as an opportunity/risk
  - psychological state of the user (optimistic vs. pessimistic, trusting vs. distrustful)
""")

st.markdown("""I'm still chugging along on the Topics by Class analysis (there are more tweaks I want to do to the underlying BERTopic model), but have also been exploring classifiers to help with the other data analysis.
""")

st.markdown("""These are the Huggingface models I'm using for my text classification:
1) classifying abusive language: [Hate-speech-CNERG/english-abusive-MuRIL](https://huggingface.co/Hate-speech-CNERG/english-abusive-MuRIL)
2) classifying climate opportunity/risk: [climatebert/distilroberta-base-climate-sentiment](https://huggingface.co/climatebert/distilroberta-base-climate-sentiment)
3) classifying social adaptivity - optimism/pessimism and trust/disgust: [ayoubkirouane/BERT-Emotions-Classifier](https://huggingface.co/ayoubkirouane/BERT-Emotions-Classifier?text=This+is+a+basic+reddit+comment.)
""")

st.markdown("""To classify the original reddit comments, I utilize HuggingFace's [transformers](https://github.com/huggingface/transformers), specifically the `pipeline` API wrapper, which simplifies the workflow tremendously. 
""")

st.markdown(""" I'm looking to solve the following kinds of questions:
1. Which subreddits have the most instances of abusive language?
2. Which comments approach the climate catastrophe as an opportunity to gain a cooperative or competitive advantage? Do they tend to belong to a given subreddit rather than others?
3. How did the COVID-19 pandemic affect users' rhetoric regarding:  
a. public trust/the social contract  
b. resource hoarding (stockpiling goods)   
c. world outlook (optimism vs. pessimism, trust vs. distrust)
""")

# MORE WORK
st.subheader("Ongoing Work, Thoughts, Etc:")
st.markdown("""
- Topic Modeling
	- I've settled on BERTopic for the majority (almost all) of my Topic Modeling/Semantic analysis, over ChromaDB, Txtai, and Gensim. BERTopic is easier to use out of the box than Txtai or Gensim, and has the key analysis features ChromaDB lacks. Keeping an eye out for Chroma, with my climate-conscious computation in mind...
- Comparative Analysis
	- Topic Modeling by class - currently working!
	- Text Classification (comparing abusive subreddits) - augmenting my dataset with text-classification scores (abusive language and climate-attitude)
		- Currently stuck with some PyTorch bugs/weird RuntimeErrors. **Potential Fix:** get my hands dirty with the transformer models. The error I've gotten that halts my work is `RuntimeError: The size of tensor a (638) must match the size of tensor b (512) at non-singleton dimension 1`.
- Final Data Presentation
	- I'm thinking this project makes the most sense as an interactive website... easiest for me to send around to friends/family (my intended audience). 
""")

st.divider()

# SOURCES
st.header("Sources and Attributions")

st.markdown("### Python Packages:")
st.markdown("""**Python Reddit API Wrapper (PRAW)**  
            [GitHub](https://github.com/praw-dev/praw)  
            _Copyright (c) 2016, Bryce Boe_""")
st.markdown("""
```MIT License
Copyright (c) 2016, Bryce Boe
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.
```
            """)

st.markdown("""**BERTopic Topic Modeling**  
            [GitHub]()
""")

st.markdown("""
```
article{grootendorst2022bertopic, 
title={BERTopic: Neural topic modeling with a class-based TF-IDF procedure}, 
author={Grootendorst, Maarten}, 
journal={arXiv preprint arXiv:2203.05794},year={2022}}
```

""")

st.markdown("### Text Classifier Models:")
st.markdown("""**Hate-speech-CNERG/english-abusive-MuRIL**  
            [HuggingFace](https://huggingface.co/Hate-speech-CNERG/english-abusive-MuRIL?text=...+%40THErealDVORAK+And+man-made+global+warming+will+never+warm+the+moon%2C+sun%2C+and+stars.+End+times+are+controlled+by+God+-+not+by+carbon) | [Article Link](https://doi.org/10.48550/arXiv.2204.12543)   
            Published in **Data bootstrapping approaches to improve low resource abusive language detection for indic languages**, accepted at ACM HT 2022
""")
st.markdown("""```
@article{das2022data,
  title={Data Bootstrapping Approaches to Improve Low Resource Abusive Language Detection for Indic Languages},
  author={Das, Mithun and Banerjee, Somnath and Mukherjee, Animesh},
  journal={arXiv preprint arXiv:2204.12543},
  year={2022}
}
```""")
st.markdown("""**climatebert/distilroberta-base-climate-sentiment**   
            [HuggingFace](https://huggingface.co/climatebert/distilroberta-base-climate-sentiment) | _Part of working paper_
""")
st.markdown("""```
@techreport{bingler2023cheaptalk,
    title={How Cheap Talk in Climate Disclosures Relates to Climate Initiatives, Corporate Emissions, and Reputation Risk},
    author={Bingler, Julia and Kraus, Mathias and Leippold, Markus and Webersinke, Nicolas},
    type={Working paper},
    institution={Available at SSRN 3998435},
    year={2023}
}
 ```""")