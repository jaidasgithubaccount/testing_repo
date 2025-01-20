import streamlit as st

# Show title and description.
st.title("The Culture War for the Planet 🌎")
st.header('Comparative analysis of Reddit forums r/collapse, r/preppers, r/itcouldhappenhere, r/climate and r/climatechange', divider="blue")

# SNEAK PEEK
left, middle, right = st.columns([0.15, 0.7, 0.15])
with middle:
  st.markdown("See [below](#analysis-topic-modeling-and-text-classification) for a sneak peek at the data collected so far!")

#TABS - 
st.header("Background:")
motives, thiscase, question, datasources = st.tabs(["Research Motivations", "What's r/Collapse?", "Research Questions", "Data Sources"])

# RESEARCH MOTIVATIONS
with motives:
  st.subheader("Modeling Climate Change and Social Conflict")
  st.markdown("There's a new burgeoning theory on the contentious politics market - that :blue-background[climate change is a potential security pressure.]")
  st.markdown("Much of the current research seeks to answer the foundational question -- :blue-background[**is there a link between climate pressures and social, political and/or economic unrest?**]")
  st.markdown("To do so, researchers have tracked key metrics in various regions, evaluating communities' **climate risks**, **conflict risks** and **other infrastructural vulnerabilities** that might contribute to the next (inter)national crisis.")
  st.markdown("My research builds on the scholarship. And I've got a hunch about one, _specific_ aspect of the connection between the climate and social conflict...")
# SOCIAL MEDIA ANALYSIS - WHY THIS?
  st.subheader("Social Media and the Climate-Conflict Connection")
  st.markdown("Foreign governments can use dashboards like Germany's [Climate-Conflict Vulnerability Index](https://climate-conflict.org/www) to help predict what resources or infastructures to invest in or fortify, and where to send humanitarian aid in the case of large-scale unrest.")
  st.markdown("But how can non-state actors -- scholars, activists, journalists, friends and family -- make sense of the socio-political effects that climate change may have on our communities?")

  st.markdown("For most of us, the climate catastrophe is personal. Hurricanes, floods, heatwaves and cold snaps have personal significance; **many of us share our stories online.** By doing so, we're influenced by our social media networks. In turn, we help shape the global conversation.")

  st.markdown("Politicians and bad-faith actors alike are listening and part of these online conversations, too: to the extent we put our votes and protests where our _twitter-fingers_ are, the rhetoric we use online mirrors world we build outside. In short, **the kinds of things we say about the climate may help determine whether our communities' attitudes of resilient cooperation will help us survive the climate catastrophe, or if anti-social infighting will tear our social fabric apart.** After all, social media sentiment analysis has proven a decent method of [ascertaining public opinion](https://doi.org/10.1016/j.dajour.2022.100073).")

# ABOUT SUBREDDITS and COLLAPSE
with thiscase:
  st.subheader("So, what's going on on with r/Collapse?")
  st.markdown("Reddit is a website that hosts various forums on specific topics - news, cat pictures, the TV show Firefly, et cetera.")
  st.markdown("Popular among them are a cluster of climate-change related forums, starting with the notorious **r/collapse**. Collapse, the subreddit for 'climate fatalists,' has been known as the quintessential 'doomer' subreddit for as long as I've known of its existence (I first stumbled onto it in 2019).")
  with st.popover("**[r/collapse disclaimer]**"):
    st.markdown("Overindulging in this sub may be detrimental to your mental health. Anxiety and depression are common reactions when studying collapse. Please remain conscious of your mental health and effects this may have on you.If you are considering suicide, please call a hotline, visit r/SuicideWatch r/SWResources, r/depression, or seek professional help. If you are seeking support please visit r/CollapseSupport. Suicidal content will be removed. Suggesting others commit suicide will result in an immediate ban.")
    st.caption("No joke.")
  st.markdown("Users in the Collapse subreddit discuss the eventual collapse of modern society:")
  st.markdown(""" 
> The world isn't dying. People are killing it. And those people have names and addresses.   
> _one anonymous user_
""")
  st.markdown("""            
> Just participating in society is making many people feel drained and pessimistic. Everyone I know reports being tired and out of sorts, as one put it, regardless of their age or their social or economic standing. Progress was supposed to make everyone thrilled all the time by giving them endless possibilities, but it seems like the opposite has happened, and if collapse is the opposite of progress then collapse is the proper term for this.    
> _another anonymous user_        
""") 
  st.markdown("In our worsening climate catastrophe, I've noticed the growth of r/collapse -- and, perhaps more notably, the spread of its doomer rhetoric to other, less-controversial climate related subreddits, like **r/preppers**, **r/itcouldhappenhere**, and **r/climate**.")
  st.markdown("I'm aiming to find through-lines and AI-classified* similarities between different users' positions, across the four subreddits. I want to map out the rhetorical 'state space' - with an eye out for any other information I can pick up, like the relative popularity of certain approaches to climate change.")
  st.caption("\*_Aiming not to over-use high-compute power AI models for this, a pet project that's meant to be about saving the planet. See the **Climate-Conscious Compuatation** page for more._")


# RESEARCH QUESTION
with question:
  st.subheader("Research Questions:")
  st.subheader("1. Is there a link between climate pressures and social, political and/or economic unrest?")
  st.subheader("2. Are there places online where you're more likely to fall down a climate doomer rabbit hole? _What makes the difference?_")
  st.markdown("This question has all sorts of component parts, but answering it will require a working definition of 'doomer' vs. non-doomer online spaces: I've decided to track the subreddits' **abusive language**, and whether the comments/posts in a subreddit see the changing climate as more of a **risk** to themsleves and others, or an **opportunity** to make money or secure power over others.")
  st.markdown("And of course, I'm comparatively analyzing the four subreddits to determine the relatively 'most/least' abusive ones, but I'll also be tracking any change in rhetoric related to climate over time (dataset collects Tweets and Reddit posts from 2018).")

with datasources:
# DATA SOURCES + COLLECTION
  st.subheader("**Where did I get this information, and why does it help answer our questions?**")
  st.markdown("1. **The Reddit Comments**")
  st.markdown("""I pulled 16,000 of the top comments and text posts of all time from r/collapse, r/preppers, r/itcouldhappenhere and r/climate, using [Praw](https://github.com/praw-dev/praw). Comments were mostly from the years after 2018, but the earliest post is from 2016.""")   
  st.markdown("_The Reddit comments are the backbone of my analysis - their text content will be analyzed for abusive language._")

  st.markdown("**In order to classify the text I'd pulled as abusive language, or to determine the attitude toward climate change (opportunity vs. risk) in the text, I relied on machine learning models that had been pre-trained on other datasets...**")

  st.markdown("2. [ClimateBERT Climate Change Sentiment Dataset](https://huggingface.co/datasets/climatebert/climate_sentiment)")
  st.markdown("_This dataset was used to train the [ClimateBERT](https://huggingface.co/climatebert/distilroberta-base-climate-sentiment) classification model for climate opportunity and risk._")

  st.markdown("3. [IndicAbusive Datasets](https://github.com/hate-alert/IndicAbusive/tree/main/Dataset)")
  st.markdown("_These were used to train various hate speech models, including the [English-Abusive-MuRIL](https://huggingface.co/Hate-speech-CNERG/english-abusive-MuRIL?text=...+%40THErealDVORAK+And+man-made+global+warming+will+never+warm+the+moon%2C+sun%2C+and+stars.+End+times+are+controlled+by+God+-+not+by+carbon) classification model I used in my research._")
st.divider()


# ANALYSIS HEADER
st.header("Analysis - Topic Modeling and Text Classification")
st.info("This work is still ongoing!")

st.markdown("I've gotten some preliminary vizualizations of the topics discussed by Redditors in the various climate-related subreddits. See this link to explore interactive graphs:")

left, middle, right = st.columns([0.3, 0.4, 0.3])
with middle:
  st.page_link("culturewar_explore.py", label="Explore the Culture War", use_container_width=True, icon="🗺️")

st.markdown("""Some interesting comment topics:   
- :violet[**Homesteading and Farming**] **(6th Most Common topic):** Discussion of environmental and political collapse in the global south. Cuba and Haiti, specifically - two alleged examples of 'collapsed' states.  
- :red[**Finances**] **(3rd Most Common topic):** How to afford life under climate catastrophe. Users discuss their personal and (inter)national economies. 
- :green[**Geopolitics**] **(2nd Most Common Topic):** (Left-wing) analysis of international relations and international political economy.""")

st.markdown("But if you want to learn more about what you're looking at on that page, see **Tech Notes** below!")

# BACKEND TABS - 
st.divider()
st.header("Tech Notes:")
modeling, classification, morework = st.tabs(["Topic Modeling", "Text Classification", "Next Steps"])

# TOPIC MODELING - BERTOPIC VIZ
with modeling:
  st.subheader("Topic Modeling - setting up BERTopic")
  st.markdown("""I used [BERTopic](https://github.com/MaartenGr/BERTopic), a Python package that takes sets of documents, mines them for their topics, and analyzes an entire corpus of the documents according to those (zero-shot-) classified topics.
""")
  st.markdown("""I first had to clean my dataset (removing stopwords, cleaning up uniform formatting on some subreddits' comments, etc), and then used BERTopic to determine the 'state space' - the kinds of things that people in these climate subreddits are talking about today.
""")

  st.markdown("""The original dataset had 15807 topics; using BERTopic's reduce_topics() method, I forced the model to combine them into 20 groups. I then used a [SciKit-Learn](https://github.com/scikit-learn/scikit-learn) function to get text embeddings with English stop words removed, and re-ran the topic model with those vectorized topics. The final topic model, saved for use throughout the rest of the project, leverages these two modifications.
""")

# COMPARATIVE ANALYSIS - TEXT CLASSIFIERS
with classification:
  st.subheader("Text Classification - comparing subreddits")
  st.markdown("""I perform two 'buckets' of comparative analysis:
- **Vector Database comparative analysis:** Analyzing BERTopic topics by subreddit, with the BERTopic 'vector database' built by that Python module:
  - this will help determine whether certain topics are unique to a given climate-subreddit. (Unlikely that any of the top 10 topics in the vizualization linked above are uniqe to one subreddit, but others might be!)
- **Other Database analysis:** This is performed by augmenting a master data structure (pandas DataFrame, or .csv file) with algorithmically-derived classification, like:
	- whether the text contains abusive language
	- whether the text treats the climate as an opportunity/risk
  - psychological state of the user (optimistic vs. pessimistic, trusting vs. distrustful)
""")
  st.markdown("""There are more tweaks I want to do to the underlying BERTopic model before I can get to **vector database analysis**, so I begin with **other database analysis** below.""")
  st.markdown("""To classify the original reddit comments, I utilize HuggingFace's [transformers](https://github.com/huggingface/transformers), specifically the `pipeline` API wrapper, which simplifies the workflow tremendously. 
""")
  st.markdown("**These are the Huggingface models I'm using for my text classification:**")
  st.markdown("""
1) Classifying :blue-background[abusive language]: [Hate-speech-CNERG/english-abusive-MuRIL](https://huggingface.co/Hate-speech-CNERG/english-abusive-MuRIL)
2) Classifying :blue-background[climate opportunity/risk]: [climatebert/distilroberta-base-climate-sentiment](https://huggingface.co/climatebert/distilroberta-base-climate-sentiment)
3) Classifying social adaptivity - :blue-background[optimism vs. pessimism] and :blue-background[trust v. disgust]: [ayoubkirouane/BERT-Emotions-Classifier](https://huggingface.co/ayoubkirouane/BERT-Emotions-Classifier?text=This+is+a+basic+reddit+comment.)
""")
  st.markdown("""**I'm looking to solve the following kinds of questions:**
1. Which subreddits have the most instances of abusive language?
2. Which comments approach the climate catastrophe as an opportunity to gain a cooperative or competitive advantage? Do they tend to belong to a given subreddit rather than others?
3. How did the COVID-19 pandemic affect users' rhetoric regarding:  
a. public trust/the social contract  
b. resource hoarding (stockpiling goods)   
c. world outlook (optimism vs. pessimism, trust vs. distrust)
""")
# MORE WORK
with morework:
  st.subheader("Ongoing Work, Thoughts, Etc:")
  st.markdown("""
- Topic Modeling
	- Moving forward through time: at the end of January, I'll update the BERTopic model with a set of new comments.
  - Incorporating controversial topics: my first merge will feature half **popular**, half **controversial** textposts; aiming to get at the heart of topic disagreement within each subreddit.
- Comparative Analysis
  - Comparative topic modeling (topics by class) is preliminary visualized; analysis incoming!
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