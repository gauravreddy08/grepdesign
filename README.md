# GrepDesign

Frontend development often requires time and expertise, especially when making frequent minor changes to webpages like personal portfolios, university websites, or course pages. These changes, which might need to be made every few days or weeks, can be challenging for someone without coding experience. 

**GrepDesign** is an innovative tool designed to simplify frontend development by allowing users to make small but frequent changes without any coding knowledge.

## What is GrepDesign?

GrepDesign leverages the power of the Greptile API and Large Language Models (LLMs) to interact with your codebase, retrieve the necessary code sections for editing, and then refactor them based on your instructions. This solution is perfect for those who need to make quick adjustments to their websites but lack the coding skills to do so manually.

### How It Works

1. **Identify Changes**: GrepDesign uses the Greptile API to identify and extract relevant parts of your code that need changes based on user input.
2. **Edit with LLM**: The extracted code is passed to an LLM model (GPT-4) that refactors and edits the code according to the user's needs. 
3. **Push to GitHub**: Once the changes are made, GrepDesign automatically pushes the updates back to your GitHub repository, making the process seamless and efficient.

> LLMs may not be perfect at writing new code, but they excel at refactoring.

## Demo Levels

Here are some examples showcasing GrepDesign's capabilities:

### Level 1: Basic Edits
Watch how GrepDesign handles minor HTML and CSS changes effortlessly.

![assets/final-boss.mp4](assets/test1.mp4)

### Level 2: Personalization of Templates
See how a free portfolio template is customized by filling in personal details without any manual code edits.

![assets/final-boss.mp4](assets/test2.mp4)

### Level 3: Editing Larger Codebases
Experience GrepDesign in action as it navigates through a larger codebase, such as course pages from a USC professor, and intuitively adjusts timings and content.

![assets/final-boss.mp4](assets/test3.mp4)

### Final Boss: The Frontend Nightmare
Watch as GrepDesign tackles one of the most notorious frontend tasks: centering a div!

![assets/final-boss.mp4](assets/final-boss.mp4)

## Getting Started

To get started with GrepDesign, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/grepdesign.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your API keys:
   - **Greptile API Key**: Add your Greptile API key.
   - **OpenAI API Key**: Add your OpenAI API key.
   - **GitHub Personal Access Token (PAT)**: Add your GitHub PAT to allow the application to push changes to your repository.

4. Run the application:
   ```bash
   streamlit run app.py
   ```

Here's a refined write-up about the alternative ideas you had for using the API, which you can include in your README or project documentation:

---

## Other Ideas with the API

### Idea One: Test Generation System

Initially, I wanted to create a system that would automatically generate test cases for codebases. However, I had already implemented a similar solution in another project: [gauravreddy08/gen-test](https://github.com/gauravreddy08/gen-test). So I decided not to reimplement this concept.

### Idea Two: Automated Git Commit Message Generator

Another challenge I often face is coming up with appropriate and meaningful commit messages when pushing code changes to Git (`git commit -m "message here"`). This led to the idea of using the Greptile API to track changes made to the codebase and automatically generate commit messages based on those changes.
