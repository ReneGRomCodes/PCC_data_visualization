import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


def api_call():
    """Make API call and store the response in 'response_dict'."""

    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    r = requests.get(url)
    response_dict = r.json()
    return r, response_dict


def repo_explore(response_dict):
    """Explore info about repositories."""

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

    return names, plot_dicts


def repo_visualization(names, plot_dicts):
    """Plot a chart of the 30 most-starred Python projects and render them to a file."""
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
    chart.title = "Most-Starred Python Projects on GitHub"
    chart.x_labels = names

    chart.add("", plot_dicts)
    chart.render_to_file("python_repos.svg")


if __name__ == "__main__":
    r, response_dict = api_call()
    names, plot_dicts = repo_explore(response_dict)
    repo_visualization(names, plot_dicts)
