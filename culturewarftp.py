import streamlit as st

# Show title and description.
st.title("The Culture War for the Planet")
st.header('Comparative analysis of r/collapse, r/preppers, r/itcouldhappenhere, and r/climate')
st.divider()

st.info("Still Under Construction!")

# RESEARCH MOTIVATIONS
st.header("Research Motivations:")
st.subheader("What's going on on with r/Collapse?")

st.markdown("In our worsening climate catastrophe, I've noticed the growth of a particular doomerist subreddit - r/collapse - and, perhaps more notably, the spread of its doomer rhetoric to other, less-controversial climate related subreddits, like r/preppers, r/itcouldhappenhere, and r/climate.")

st.markdown("The r/Collapse subreddit is filled with people deriving a number of narratives about the eventual collapse of modern society. I'm aiming to see what these narratives *are*. finding through-lines and AI-classified* similarities between different authors' positions, and being able to map out the rhetorical 'state space' - with an eye out for any other information I can pick up.")
st.caption("_Aiming not to over-use high-compute power AI models for this, a pet project that's meant to be about saving the planet._")

# RESEARCH QUESTION
st.header("Research Question")
st.subheader("Are there places online where you're more likely to fall down a climate doomer rabbit hole? _What makes the difference?_")
st.markdown("This question has all sorts of component parts, but answering it will require a working definition of 'doomer' vs. non-doomer online spaces: I've decided to track the subreddits' **abusive language**, **optimism/pessimism**, and other metrics to be determined...")
st.markdown("And of course, I'm comparatively analyzing the four subreddits to determine the relatively 'most/least' abusive ones, but I'll also be tracking any change in rhetoric related to climate over time (dataset collects Tweets and Reddit posts from 2018).")

# DATA SOURCES + COLLECTION
st.header("Data Sources + Data Collection")
st.subheader("Where did I get this information, _and why does it help answer our questions?_")

st.markdown("1. **The Reddit Comments**")
st.markdown("I pulled 16,000 of the top comments and text posts since 2018 from r/collapse, r/preppers, r/itcouldhappenhere and r/climate, using [Praw](https://github.com/praw-dev/praw):")


st.markdown("I then compared that data with...")

st.markdown("2. [Twitter Climate Change Sentiment Dataset](https://www.kaggle.com/datasets/edqian/twitter-climate-change-sentiment-dataset/data)")
st.markdown("I compared data ")

# CHROMADB VISUALIZATION
st.header("[Current Work] Analysis - Semantic Similarity, Topic Modeling")

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