import streamlit as st

# Show title and description.
st.title("Climate-Conscious Computation")
st.header("Why I'm picky with my machine learning applications", divider="green")

st.markdown("""
Okay, so there's an elephant in this room and she's BIG.  
I do not want to harm the planet doing this pro-planet research. To be clear:
1) Neither of personal projects here produce enough compute-power to cause genuine concern. I'm working with a corpus of 16,000 reddit comments, not 100,000 novels.
2) My goal is to perform valuable research in sparse fields. In the early 2020s, there was (if you can believe it) a lack of data on the scope of alt-right radicalization worldwide; I think I'm filling a similar gap these days with my research into climate-motivated rhetoric. I'm being deliberate and I think this is worth it!

#### (Here's how) I'm mitigating any potential negative environmental externalities:   
**Using pre-trained models for my text classification.** Training models takes up far more compute time/energy than querying them (... obviously), so for the classification of Reddit comments (as abusive, etc) I used pre-trained models. These models remained reliable because their application in my project is contained within the datasets used to train the models themselves - both models include significant dicussion of climate change in their training datasets.   
""")