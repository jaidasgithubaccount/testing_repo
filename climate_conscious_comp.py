import streamlit as st

# Show title and description.
st.title("Climate-Conscious Computation")
st.header("Why I'm picky with my ML applications")
st.divider()

st.markdown("""
Okay, so there's an elephant in this room and she's BIG!
	 I do not want to harm the planet doing this pro-planet research. 
To be CLEAR:
1) my particular project here will not produce enough ... energy or whatever... to cause any kind of trouble, here.
2) this research is technically a bit valuable, and it's also a sparse field. I'm being deliberate and I think this is worth it!
3) (here's how) I'm mitigating any potential negative environmental externalities:
	- using pre-trained models for my text classification.
		- training models takes up far more compute time/energy than querying them (... obviously), so for tasks that would require specialized training (like the PRAT standards-approximate classification I was going to try earlier), it'd be better (and effort-effective!) to download pre-trained models. I've used the vocabulary and config file from these other datasets here.
		- i'm going to use pre-trained models and import them in the most climate-conscious ways.
""")