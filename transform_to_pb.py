# ChatGPT version

import pandas as pd
import json
projects_df = pd.read_csv('projects.csv')
with open('responses.json', 'r') as file:
    responses = json.load(file)

def clean_name(name):
    return " ".join(name.split()[:-1])

filename = {
    'voteA': 'SN',
    'voteB': 'S5',
    'voteC': 'D5',
    'voteD': 'D10',
    'voteE': 'S5R',
    'voteF': 'S5D10'
}

long_description = {
    'voteA': 'Select any number of projects',
    'voteB': 'Select 5 projects',
    'voteC': 'Distribute 5 points among projects',
    'voteD': 'Distribute 10 points among projects',
    'voteE': 'Select 5 projects and rank them',
    'voteF': 'Select 5 projects and distribute 10 points among them'
}

vote_type_pb = {
    'voteA': 'approval',
    'voteB': 'approval',
    'voteC': 'cumulative',
    'voteD': 'cumulative',
    'voteE': 'ordinal',
    'voteF': 'cumulative'
}

min_length = {
    'voteA': 1,
    'voteB': 5,
    'voteC': 1,
    'voteD': 1,
    'voteE': 1,
    'voteF': 1
}

max_length = {
    'voteA': 24,
    'voteB': 5,
    'voteC': 5,
    'voteD': 10,
    'voteE': 5,
    'voteF': 5
}

def generate_pb_content(vote_type, responses, projects_df):
    # META section
    meta_section = [
        "META",
        "key;value",
        f"description;Qualtrics Zurich PB Experiment 2023, {filename[vote_type]} format",
        "comment;Data from Yang et al. (2024), https://arxiv.org/abs/2310.03501.",
        "country;Switzerland",
        "unit;Zurich",
        f"instance;{long_description[vote_type]}",
        f"num_projects;{len(projects_df)}",
        f"num_votes;{len(responses)}",
        "budget;60000",
        f"vote_type;{vote_type_pb[vote_type]}",
        "rule;none",
        "date_begin;2023-03-09",
        "date_end;2023-03-19",
        "language;en",
        f"min_length;{min_length[vote_type]}",
        f"max_length;{max_length[vote_type]}",
    ]
    if vote_type == 'voteD' or vote_type == 'voteF': 
        meta_section.append("max_sum_points;10")
    elif vote_type == 'voteC':
        meta_section.append("max_sum_points;5")
    
    meta_section.append('PROJECTS')
    meta_section.append('project_id;cost;name;category;district')

    # PROJECTS section
    projects_section = [
        f"{row['Id']};{row['Cost'].replace(',', '')};{clean_name(row['Name'])};{row['Category'][2:]};{row['District'][2:]}"
        for index, row in projects_df.iterrows()
    ]
    
    # VOTES section
    votes_section = ["VOTES"]
    vote_format = {
            'voteA': 'approval',
            'voteB': 'approval',
            'voteC': 'cumulative',
            'voteD': 'cumulative',
            'voteE': 'ordinal',
            'voteF': 'cumulative'
        }[vote_type]
    if vote_format == 'approval' or vote_format == 'ordinal':
        votes_section.append("voter_id;vote")
    else:
        votes_section.append("voter_id;vote;points")
    votes_section[-1] += ";topic_preference_transport;topic_preference_culture;topic_preference_nature;district_preference;time_taken_seconds;format_easiness;format_expressiveness;format_rank"
    for response in responses:
        vote_data = response["Inputs"][vote_type]
        if vote_format == 'approval':
            approved = [str(index + 1) for index, approval in enumerate(vote_data) if approval == 1]
            votes_section.append(f'{response["id"]};{",".join(approved)}')
        elif vote_format == 'ordinal':
            ranked_projects = [str(index + 1) for index, points in enumerate(vote_data) if points > 0]
            ranked_projects.sort(key=lambda x: vote_data[int(x) - 1], reverse=True)
            votes_section.append(f'{response["id"]};{",".join(ranked_projects)}')
        elif vote_type == 'voteF':
            # special handling for selection
            vote_data_E = response["Inputs"]['voteE']
            selected = [index for index, points in enumerate(vote_data_E) if points > 0]
            points = [str(vote_data[index]) for index in selected]
            selected_strs = [str(index + 1) for index in selected]
            votes_section.append(f'{response["id"]};{",".join(selected_strs)};{",".join(points)}')
        elif vote_format == 'cumulative':
            positive = [str(index + 1) for index, points in enumerate(vote_data) if points > 0]
            points = [str(points) for points in vote_data if points > 0]
            votes_section.append(f'{response["id"]};{",".join(positive)};{",".join(points)}')
        votes_section[-1] += f";{response['Inputs']['topicPreference']['Transport']};{response['Inputs']['topicPreference']['Culture']};{response['Inputs']['topicPreference']['Nature']};{response['Inputs']['district'][2:]}"
        letter = vote_type[-1]
        votes_section[-1] += f";{round(float(response['Inputs']['voteTiming'][letter]))};{response['Inputs']['voteNumClicks'][letter]};{response['Inputs']['voteDifficulty'][letter]};{response['Inputs']['voteExpressiveness'][letter]};{response['Inputs']['voteFormatRanking'][letter]}"

    # Combine all sections
    return '\n'.join(meta_section + projects_section + votes_section + [''])

# List of vote types to create .pb files for
vote_types = ['voteA', 'voteB', 'voteC', 'voteD', 'voteE', 'voteF']

for vote_type in vote_types:
    content = generate_pb_content(vote_type, responses, projects_df)
    with open(f'qualtrics_zurich_2023_{filename[vote_type]}.pb', 'w') as file:
        file.write(content)

