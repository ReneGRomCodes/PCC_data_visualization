# Exercise 17-1 Other Languages: Modify the API call in 'python_repos.py' so it generates a chart showing the most
# popular projects in other languages. Try languages such as JavaScript, Ruby, Java, Pearl, Haskell and Go.

# COMMENT: ADDED USER INPUT TO ACCESS ALL LANGUAGES AND POSSIBILITY TO SKIP THE API CALL.


import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


# Ask the user to choose language.
prompt = ("CHOOSE LANGUAGE\n1 - Python\n2 - JavaScript\n3 - Ruby\n4 - Java\n5 - Perl\n6 - Haskell\n7 - Go\n"
          "8 - SKIP API CALL\n> ")
language_choice = int(input(prompt))

if language_choice == 1:
    language = "Python"
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
elif language_choice == 2:
    language = "JavaScript"
    url = 'https://api.github.com/search/repositories?q=language:javascript&sort=stars'
elif language_choice == 3:
    language = "Ruby"
    url = 'https://api.github.com/search/repositories?q=language:ruby&sort=stars'
elif language_choice == 4:
    language = "Java"
    url = 'https://api.github.com/search/repositories?q=language:java&sort=stars'
elif language_choice == 5:
    language = "Perl"
    url = 'https://api.github.com/search/repositories?q=language:perl&sort=stars'
elif language_choice == 6:
    language = "Haskell"
    url = 'https://api.github.com/search/repositories?q=language:haskell&sort=stars'
elif language_choice == 7:
    language = "Go"
    url = 'https://api.github.com/search/repositories?q=language:go&sort=stars'
else:
    language = False
    print("Process skipped. No data returned.")

if language:
    # Make an API call and store the responses.
    r = requests.get(url)
    print("Status code:", r.status_code)

    # Store API response in a variable.
    response_dict = r.json()
    print("Total repositories:", response_dict["total_count"])

    # Explore information about the repositories.
    repo_dicts = response_dict["items"]

    names, plot_dicts = [], []
    for repo_dict in repo_dicts:
        names.append(repo_dict["name"])

        # Get the project description, if one is available.
        description = repo_dict["description"]
        if not description:
            description = "No description provided."

        plot_dict = {
            'value': repo_dict["stargazers_count"],
            'label': description,
            'xlink': repo_dict["html_url"]
        }
        plot_dicts.append(plot_dict)

    # Make visualization.
    my_style = LS("#333366", base_style=LCS)
    my_style.title_font_size = 24
    my_style.label_font_size = 14
    my_style.major_label_font_size = 18

    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1000

    chart = pygal.Bar(my_config, style=my_style)
    chart.title = f"Most-Starred {language} Projects on GitHub"
    chart.x_labels = names

    chart.add("", plot_dicts)
    chart.render_to_file("exercise_17-1.svg")


# Exercise 17-3 Testing 'python_repos.py': In 'python_repos.py' we printed the value of status code to make sure the API
# call was successful. Write a program called 'test_python_repos.py', which uses 'unittest' to assert that the value of
# 'status_code' is 200. figure out some other assertions you can make - for example, that the number of items returned
# is expected and that the total number of repositories is greater than a certain amount.

# SOLUTION TO THIS EXERCISE IN 'TEST_PYTHON_REPOS.PY' AND 'PYTHON_REPOS.PY'.
