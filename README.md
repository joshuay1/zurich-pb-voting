# Designing Digital Voting Systems for Citizens

This repository contains data from the study **Designing Digital Voting Systems for Citizens: Achieving Fairness and Legitimacy in Participatory Budgeting** by Joshua C. Yang, Carina I. Hausladen, Dominik Peters, Evangelos Pournaras, Regula Hänggli Fricker, and Dirk Helbing. The paper has been submitted to the ACM _Digital Government: Research and Practice_ Journal. The latest version of the paper is available here on [arXiv](https://arxiv.org/abs/2310.03501).

## Study Overview

Participatory Budgeting (PB) is a democratic process where citizens can directly propose and vote on urban projects to decide how to allocate public funds. As PB moves to digital platforms, cities have choices in the voting input formats and aggregation rules used. This study aims to identify approaches to designing PB voting that minimise cognitive load and enhance perceived fairness and legitimacy from the citizens' perspective. 

The experiment, conducted in March 2023, involved 180 participants from ETH Zurich and the University of Zurich. It was pre-registered on the AEA ACT [Registry](https://www.socialscienceregistry.org/trials/11021) and approved by the ETH Zurich Ethics Commission (approval number: EK 2022-N-143). The study was carried out via the online platform Qualtrics in English, with all participants providing informed consent. This study was supported by the Swiss National Science Foundation (SNSF) as part of the National Research Programme NRP 77 Digital Transformation, project no. 187249.

Participants were tasked with allocating a budget of 60,000 CHF among various projects within the city of Zurich using their votes, with their payoff in the experiment linked to the outcomes of their decisions.

The design aimed to investigate two main research questions:
1. **Voting Input Formats**: Participants voted using six different formats, reflecting those used in actual PB processes, to determine their preferences and the impact of these formats on collective outcomes.
2. **Aggregation Methods and Voter Perceptions**: The study explored how perceptions of fairness and trustworthiness varied across different aggregation methods (Greedy and MES), including the effect of various explanation types on these perceptions.

For a detailed account of the experimental design, including the specific voting formats used, the creation of simulated voting outcomes, and the methodology behind gathering and analysing participant feedback on these outcomes, please refer to the 'Experimental Design' section in our paper.

## Voting Input Formats

The study used 6 voting input formats, labeled A-F in the data:

- A (SN): Select any number of projects 
- B (S5): Select 5 projects
- C (D5): Distribute 5 points across projects
- D (D10): Distribute 10 points across projects 
- E (S5R): Select and rank 5 projects
- F (S5D10): Distribute 10 points across 5 selected projects

## Aggregation Methods

The study used two aggregation methods to compute simulated voting outcomes:

- Method A: The Greedy method, which selects projects with the most votes within the budget
- Method B: The Method of Equal Shares (MES), which ensures a fair distribution of budget across voters

## Data Format

The data is provided in a JSON file, with each record representing a single participant. The fields in each record include:

- `id`: A unique participant ID.
- `duration`: The time in seconds the participant took to complete the study.
- `whoDecides`: Who decides how the budget is used in Participatory Budgeting (PB) (multiple-choice).
- `knewAboutPB`: Whether the participant knew about PB before the study (true/false).
- `Limmatstadt`: Data from the tutorial questions about the hypothetical city of Limmatstadt. This data is not used for the paper as it served as a trial for participants to familiarise themselves with the PB setting.
- `Inputs`: The participant's votes and preferences in the main PB setting, including:
  - `topicPreference`: The participant's preference for different project categories (aggregate to 100 points in total).
  - `district`: The district in Zurich the participant feels most connected to (options include Nord, Süd, Ost, West, displayed as coloured areas on a city map).
  - `howConnected`: How connected the participant feels to Zurich (5-point scale).
  - `voteA`, `voteB`, ..., `voteF`: The participant's votes in the 6 different voting input formats (labelled A-F in the data, corresponding to SN, S5, D5, D10, S5R, S5D10 in the paper; the votes in S5R are the Borda scores converted from rank positions).
  - `voteTiming`: The duration in seconds the participant spent voting in each of the voting input settings.
  - `voteNumClicks`: The number of clicks the participant had while voting in each of the voting input settings.
  - Various fields for the participant's perception of the voting input formats, including:
    - `Difficulty`: How difficult the participant found the voting input format (5-point scale).
    - `Expressiveness`: How much the voting input format described their preference (5-point scale).
    - `voteFormatRanking`: Which voting format the participant would recommend the city use, in ranking order.
    - `reasonHighestRank`: The reason the participant ranked a voting input format first (open answer).
    - `reasonLowestRank`: The reason the participant ranked a voting input format last (open answer).
    - `rankingFactorsImportance`: How important are the following factors in the participant's recommendation of voting input formats:
        - `Easiness`: "How easy it is to vote."
        - `Knowledge`: "I know how the votes are going to be calculated."
        - `Accuracy`: "The voting input accurately represents my preference."
        - `IndicatesIntensities`: "I can freely indicate the intensity of my preference."
    - `recommendedNumberOfPoints`: How many points the participant recommended using for point distribution cumulative voting inputs.
  - `howPopular`: How popular the participant thought their selections of projects would be among all the voters.
  - `factorsForDecidingVotes`: How important are the following characteristics in the participant's votes for projects:
    - `district`: The district or location of the project.
    - `topic`: The urban categories or topics of the project.
    - `cost`: The cost of the project.
    - `likelihood`: The likelihood of the project winning the budget.
- `Aggregation`: The participant's responses to the simulated voting outcomes, including:
  - `situationBucket`: Which of the two simulated voting outcome instances the participant saw (1 or 2), with situation 1 assuming that simulated voters have strong preferences for projects in their districts and topical interest, and situation 2 assuming that simulated voters vote randomly. The purpose of having two outcomes is to have a different degree of differences between aggregation methods (anonymised as method A and B) to avoid overfitting with only one situation.
  - `explanationBucket`: Which explanation type the participant saw ("mechanism", "individual", or "group").
  - `firstRating`: This is the perception rating before the explanation when participants have only seen the outcome, including `satisfaction`, `fairness`, `trustworthiness` perception of the two outcomes calculated with method A (Greedy) and B (MES) (5-point scale), and `firstRatingReasons`: The qualitative reasons behind the first rating.
  - `explanationAnswers`: The fields `preferenceAsRandomVoter` and `preferenceAsRandomVoterReason` are only visible in the _individual_ group, where the participants are asked which outcome distribution (A or B) they would choose to be realised if they were a random voter in this simulation and the reasons why.
  - `secondRating`: Participants rated `fairness`, and `trustworthiness` again after seeing the explanation, and also indicated how much they comprehend the explanation in `understanding` (5-point scale).
  - `checks`: The 3 simple questions `moreLikelyNone`, `moreLikelyAll`, `moreEqualCompensation` serve as simple tests to see whether the participants understand the implications of different aggregation methods. The correct answers should be "Method A", "Method A", and "Method B", respectively. 
- `Decision`: The participant's final vote for their preferred voting input and aggregation method. This is an incentivised vote. The participants were informed that "You will be rewarded based on how your project choices match the final outcome calculated by the most supported voting input and aggregation methods.", including:
  - `method`: The participant's decision on the aggregation method, along with reasons (open field) and the importance of factors (5-point scale).
  - `input`: The decision on the voting input format and the reason behind the decision.
- `Feedback`: Optional feedback from the participant.
- `tokenGuid`, `paymentCode`: Identifiers for payment purposes (anonymised).

## Study Materials

The repository includes:

- The data from the study (`responses.json`).
- The Qualtrics survey screens used in the study (`study_export.html`).
- The votes in pabulib `.pb` format, one file for each voting input format.

## Connected Paper on Fairness and Legitimacy

Hänggli Fricker, R., Wellings, T., Zai, F., Yang, J. C., Majumdar, S., Bernhard, L., Weil, L., Hausladen, C. I., & Pournaras, E. (2024). Exploring Legitimacy: Empirical Insights into Citizens' Perceptions within Switzerland. Submitted to Philosophical Transactions special issue “Co-Creating the Future: Participatory Cities and Digital Governance".

A segment of the data available in this repository was utilised in the paper also financed by the Swiss National Science Foundation(SNSF) as part of the National Research Programme NRP77 Digital Transformation, project no. 187249. The research delves into the notions of fairness and trustworthiness as perceived by citizens, particularly within the context of Participatory Budgeting (PB) in Switzerland. This study employed a subset of the data concerning participants' fairness and trustworthiness ratings for different voting methods, both before and after receiving explanatory information, as well as regression analyses to understand satisfaction under various voting conditions.

Please refer to the respective tables in the paper for an in-depth analysis:
- Table 4: Fairness and Trustworthiness Ratings Before and After Explanations for Greedy and ES Methods. (We utilised `fairness` and `trustworthiness` in `firstRating` and `secondRating`)
- Table 11: OLS Regression Results for Satisfaction under Different Voting Methods in Zurich. (The additional `Winning` variable was calculated using the budget participant win in the simulated outcome with their S5 vote)
- Table 12: Logistic Regression Results Predicting Incentivized Choice. (We used the difference between the rating of `satisfaction`, `fairness`, `trustworthiness` for the two aggregation methods as independent variables)

## Citation

If you use the data from this study for your research, please cite our paper as follows:

Yang, J. C., Hausladen, C. I., Peters, D., Pournaras, E., Hänggli Fricker, R., & Helbing, D. (2023). Designing Digital Voting Systems for Citizens: Achieving Fairness and Legitimacy in Participatory Budgeting. https://doi.org/10.48550/arXiv.2310.03501.

### BibTeX Entry

```bibtex
@article{10.1145/3665332,
author = {Yang, Joshua C. and Hausladen, Carina I. and Peters, Dominik and Pournaras, Evangelos and Hnggli Fricker, Regula and Helbing, Dirk},
title = {Designing Digital Voting Systems for Citizens: Achieving Fairness and Legitimacy in Participatory Budgeting},
year = {2024},
issue_date = {September 2024},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
volume = {5},
number = {3},
url = {https://doi.org/10.1145/3665332},
doi = {10.1145/3665332},
abstract = {Participatory Budgeting (PB) has evolved into a key democratic instrument for resource allocation in cities. Enabled by digital platforms, cities now have the opportunity to let citizens directly propose and vote on urban projects, using different voting input and aggregation rules. However, the choices cities make in terms of the rules of their PB have often not been informed by academic studies on voter behaviour and preferences. Therefore, this work presents the results of behavioural experiments where participants were asked to vote in a fictional PB setting. We identified approaches to designing PB voting that minimise cognitive load and enhance the perceived fairness and legitimacy of the digital process from the citizens’ perspective. In our study, participants preferred voting input formats that are more expressive (like rankings and distributing points) over simpler formats (like approval voting). Participants also indicated a desire for the budget to be fairly distributed across city districts and project categories. Participants found the Method of Equal Shares voting rule to be fairer than the conventional Greedy voting rule. These findings offer actionable insights for digital governance, contributing to the development of fairer and more transparent digital systems and collective decision-making processes for citizens.},
journal = {Digit. Gov.: Res. Pract.},
month = sep,
articleno = {26},
numpages = {30},
keywords = {Participatory budgeting, digital democracy, collective decision-making, explainable AI, trust, legitimacy}
}
