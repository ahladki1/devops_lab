import requests

token = {'Authorization': 'token'}


def get_pulls(state):
    resp = 'https://api.github.com/repos/alenaPy/devops_lab/pulls'
    resp_search = 'https://api.github.com/search/issues?q=is:pr%20label:'

    if state in ['open', 'closed']:
        resp = requests.get(resp,
                            headers=token,
                            params={'state': '{0}'.format(state),
                                    'per_page': '100'})
        return resp.json()

    if state in ['accepted', 'needs work']:
        resp = requests.get(resp_search + f'\"{state}\"\
                   %20repo:alenaPy/devops_lab&per_page=100',
                            headers=token,
                            params={'per_page': '100'})
        return resp.json()["items"]

    return requests.get(resp,
                        headers=token).json()
