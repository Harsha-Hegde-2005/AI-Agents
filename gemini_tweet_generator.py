#to Set the API Key Securely in Notebook
import os
os.environ["GEMINI_API_KEY"] = "your-api-key-here"


# Install required libraries (run this in a notebook or Colab)
# You only need to run these once in your environment
!pip install google-generativeai --quiet
!pip install ipywidgets --quiet

# Import necessary libraries
import google.generativeai as genai
import ipywidgets as widgets
from IPython.display import display, Markdown
import os

# Load the API key securely from environment variable
# Before running, set it using: os.environ["GEMINI_API_KEY"] = "your-api-key"
API_KEY = os.environ.get("GEMINI_API_KEY")  # Make sure it's set
if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables.")

# Configure the Gemini model
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

# ========================
# UI Components Definition
# ========================

# Input for tweet topic
topic_input = widgets.Text(
    description="Topic",
    placeholder="Enter the tweet topic",
    layout=widgets.Layout(width='400px')
)

# Dropdown for tone selection
tone_input = widgets.Dropdown(
    description="Tone",
    options=['professional', 'casual', 'motivational', 'informative'],
    layout=widgets.Layout(width='400px')
)

# Input for audience
audience_input = widgets.Text(
    description="Audience",
    placeholder="e.g. students, techies, startups",
    layout=widgets.Layout(width='400px')
)

# Input for hashtags
hashtag_input = widgets.Text(
    description="Hashtags",
    placeholder="#AI #MachineLearning",
    layout=widgets.Layout(width='400px')
)

# Submit button
submit_button = widgets.Button(
    description="Generate Tweet",
    button_style='success',
    tooltip='Click to generate tweet',
    layout=widgets.Layout(width='400px')
)

# Output area for displaying tweet
output = widgets.Output()

# ========================
# Function to Generate Tweet
# ========================
def generate_tweet(b):
    output.clear_output()
    
    # Prompt for the Gemini model
    prompt = f"""
    You are an expert content writer.
    Generate a tweet on the topic: "{topic_input.value}".
    Use a {tone_input.value} tone.
    Audience: {audience_input.value}.
    Include these hashtags: {hashtag_input.value}.
    Limit the tweet to under 250 characters.
    """
    
    # Generate and display the tweet
    with output:
        try:
            response = model.generate_content(prompt)
            tweet = response.text.strip()
            display(Markdown(f"### Generated Tweet:\n\n{tweet}"))
        except Exception as e:
            print(" Error generating tweet:", e)

# Link the button click to the function
submit_button.on_click(generate_tweet)

# Layout all widgets together
form = widgets.VBox([
    widgets.HTML(value="<h3>🤖 Tweet Generator Agent</h3>"),
    topic_input,
    tone_input,
    audience_input,
    hashtag_input,
    submit_button,
    output
])

# Display the form
display(form)
