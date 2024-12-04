import streamlit as st

# Show title and description.
st.title("The Culture War for the Planet")
st.header('Comparative analysis of r/collapse, r/preppers, r/itcouldhappenhere, and r/climate')
st.divider()

st.header("Research Motivations:")
st.subheader("What's going on on with r/Collapse?")

st.markdown("In our worsening climate catastrophe, I've noticed the growth of a particular doomerist subreddit - r/collapse - and, perhaps more notably, the spread of its doomer rhetoric to other, less-controversial climate related subreddits, like r/preppers, r/itcouldhappenhere, and r/climate (*in order from most to least transgressive in their tactics*).")

st.markdown("The r/Collapse subreddit is filled with people deriving a number of narratives about the eventual collapse of modern society. I'm aiming to see what these narratives *are*. finding through-lines and AI-classified* similarities between different authors' positions, and being able to map out the rhetorical 'state space' - with a keen eye toward any other information I can glean.")
st.caption("*_see Climate-Conscious Computation section for more_")

st.header("Research Question")
st.subheader("")

st.header("Data Sources")
st.subheader("Where did I get this information, _and why does it help answer our questions?_")

st.markdown("1. **The Reddit Comments**")
st.markdown("I pulled 16,000 of the top comments and text posts since 2018 from r/collapse, r/preppers, r/itcouldhappenhere and r/climate, using [Praw](https://github.com/praw-dev/praw):")
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

st.markdown("I then compared that data with...")

st.markdown("2. [Twitter Climate Change Sentiment Dataset](https://www.kaggle.com/datasets/edqian/twitter-climate-change-sentiment-dataset/data)")
st.markdown("I compared data ")