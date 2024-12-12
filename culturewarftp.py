import streamlit as st

# Show title and description.
st.title("The Culture War for the Planet")
st.header('Comparative analysis of r/collapse, r/preppers, r/itcouldhappenhere, and r/climate')
st.divider()

st.info("Ongoing Work - visualizations are in-progress")

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

# CHROMADB VISUALIZATION
st.header("[Ongoing Work] Analysis - Semantic Similarity, Topic Modeling")

st.markdown("Yeah, you want to skip to the good stuff. I've done the Topic Modeling, but not the Comparative Analysis, so see below for a visualization of the former:")

st.html("/workspaces/testing_repo/notpages/__pycache__/fourthlook.html")



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